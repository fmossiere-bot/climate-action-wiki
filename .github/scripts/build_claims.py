#!/usr/bin/env python3
"""
build_claims.py
Generates wiki/claims.json from the pages in wiki/myths/.

Each myth page produces one Counter Claims card in the app. The card is built
from a FIXED ALLOWLIST of section headings:

    Say this, Why it sounds right, What is actually true,
    If they push back, Also heard as, Sources

Every other section in the file is ignored. That is deliberate: it means
"## Go deeper", "## Connected topics" and anything else added later can never
leak into a card, and no one has to remember to exclude them.

Run: python3 .github/scripts/build_claims.py
Output: wiki/claims.json
"""

import json, re, sys
from pathlib import Path

WIKI_DIR    = Path(__file__).parent.parent.parent / 'wiki'
MYTHS_DIR   = WIKI_DIR / 'myths'
OUTPUT_FILE = WIKI_DIR / 'claims.json'

# Sections the card is built from. Anything else in the page is ignored.
CARD_SECTIONS = {
    'say this':            'say_this',
    'why it sounds right': 'kernel',
    'what is actually true': 'truth',
    'if they push back':   '_pushback',
    'also heard as':       '_heard_as',
    'sources':             '_sources',
}

VERDICTS = {
    'false':        {'label': 'False',              'color': 'red'},
    'mostly-false': {'label': 'Mostly false',       'color': 'orange'},
    'incomplete':   {'label': 'True but incomplete','color': 'yellow'},
    'true-but':     {'label': 'Fair point, and',    'color': 'green'},
}

CATEGORIES = [
    {'id': 'transport', 'label': 'Cars & flying',     'icon': 'directions_car'},
    {'id': 'energy',    'label': 'Energy',            'icon': 'bolt'},
    {'id': 'materials', 'label': 'Materials & waste', 'icon': 'recycling'},
    {'id': 'food',      'label': 'Food',              'icon': 'restaurant'},
    {'id': 'systemic',  'label': 'Big picture',       'icon': 'public'},
    {'id': 'ireland',   'label': 'Ireland',           'icon': 'flag'},
]
VALID_CATEGORIES = {c['id'] for c in CATEGORIES}


def parse_frontmatter(content: str) -> dict:
    """Same contract as build_snippets.py, plus quoted-list support for
    `tags` and `sources` so multi-entry values survive intact."""
    if not content.startswith('---'):
        return {}
    try:
        end = content.index('\n---', 3)
    except ValueError:
        return {}

    result = {}
    for line in content[3:end].splitlines():
        m = re.match(r'^(\w+)\s*:\s*(.*)', line)
        if not m:
            continue
        key, val = m.group(1).strip(), m.group(2).strip()
        if key in ('tags', 'sources'):
            items = re.findall(r'"([^"]*)"', val)
            if not items and val.startswith('['):
                items = [v.strip() for v in val.strip('[]').split(',') if v.strip()]
            result[key] = [i.lstrip('#') if key == 'tags' else i for i in items]
        else:
            result[key] = val.strip('"').strip("'")
    return result


def split_sections(body: str) -> dict:
    """Map '## Heading' -> its text, lowercased keys. Content before the first
    heading is discarded (that is the H1 and the verdict callout)."""
    sections, current, buf = {}, None, []
    for line in body.split('\n'):
        h = re.match(r'^##\s+(.*?)\s*$', line)
        if h:
            if current:
                sections[current] = '\n'.join(buf).strip()
            current, buf = h.group(1).strip().lower(), []
        elif current is not None:
            buf.append(line)
    if current:
        sections[current] = '\n'.join(buf).strip()
    return sections


def strip_comments(text: str) -> str:
    return re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL).strip()


def clean_prose(text: str) -> str:
    """Collapse a section body into single-paragraph prose for the card."""
    text = strip_comments(text)
    return ' '.join(l.strip() for l in text.split('\n') if l.strip())


def parse_pushback(text: str) -> list:
    """**"the comeback"** followed by the reply, repeated."""
    out = []
    for m in re.finditer(r'\*\*"(.+?)"\*\*\s*\n+(.+?)(?=\n\s*\*\*"|\Z)',
                         strip_comments(text), flags=re.DOTALL):
        reply = ' '.join(l.strip() for l in m.group(2).split('\n') if l.strip())
        if reply:
            out.append({'if': m.group(1).strip(), 'reply': reply})
    return out


def parse_bullets(text: str) -> list:
    out = []
    for line in strip_comments(text).split('\n'):
        m = re.match(r'^\s*[-*+]\s+(.*)$', line)
        if m:
            out.append(m.group(1).strip().strip('"'))
    return out


def parse_sources(text: str, fm_sources: list) -> list:
    """Prefer the '- Label — URL' bullets; fall back to frontmatter."""
    out = []
    for raw in parse_bullets(text) or fm_sources:
        if '—' in raw:
            label, _, url = raw.partition('—')
        elif ' http' in raw:
            i = raw.index(' http')
            label, url = raw[:i], raw[i:]
        else:
            label, url = raw, ''
        out.append({'label': label.strip(), 'url': url.strip()})
    return out


# Category is derived from the topic tags. `topic:` in frontmatter always wins
# when present, because a few claims sit in a category their tags do not imply.
TAG_CATEGORY = [
    ('transport', {'transport', 'ev', 'aviation', 'shipping'}),
    ('food',      {'food', 'agriculture'}),
    ('energy',    {'energy', 'renewables', 'energy-transition', 'buildings',
                   'energy-efficiency', 'electrification', 'phaseout'}),
    ('materials', {'circularity', 'recycle', 'plastic', 'battery', 'e-waste', 'industry'}),
    ('ireland',   {'ireland'}),
]

def derive_category(fm: dict) -> str:
    topic = fm.get('topic', '').strip()
    if topic in VALID_CATEGORIES:
        return topic
    tags = set(fm.get('tags', []))
    for cat, markers in TAG_CATEGORY:
        if tags & markers:
            return cat
    return 'systemic'


def build():
    if not MYTHS_DIR.is_dir():
        print(f'No {MYTHS_DIR}, nothing to build.', file=sys.stderr)
        return 1

    claims, warnings = [], []
    for md in sorted(MYTHS_DIR.glob('*.md')):
        if md.name.startswith('_'):
            continue
        text = md.read_text(encoding='utf-8')
        fm   = parse_frontmatter(text)
        body = text[text.index('\n---', 3) + 4:] if '\n---' in text else text
        sec  = split_sections(body)

        claim_id = fm.get('claim_id') or md.stem
        if claim_id != md.stem:
            warnings.append(f'{md.name}: claim_id "{claim_id}" != filename')

        title = fm.get('title', '')
        claim = re.sub(r'^myth:\s*', '', title, flags=re.IGNORECASE).strip()

        verdict = fm.get('verdict', 'false')
        if verdict not in VERDICTS:
            warnings.append(f'{md.name}: unknown verdict "{verdict}", using false')
            verdict = 'false'

        for required in ('say this', 'why it sounds right', 'what is actually true'):
            if not sec.get(required):
                warnings.append(f'{md.name}: missing "## {required}"')

        claims.append({
            'id':       claim_id,
            'category': derive_category(fm),
            'verdict':  verdict,
            'claim':    claim,
            'heard_as': parse_bullets(sec.get('also heard as', '')),
            'kernel':   clean_prose(sec.get('why it sounds right', '')),
            'truth':    clean_prose(sec.get('what is actually true', '')),
            'say_this': clean_prose(sec.get('say this', '')),
            'pushback': parse_pushback(sec.get('if they push back', '')),
            'sources':  parse_sources(sec.get('sources', ''), fm.get('sources', [])),
            'wiki':     '',
        })

    out = {
        'version':   1,
        'updated':   __import__('datetime').date.today().isoformat(),
        'note':      'Generated from wiki/myths/ by build_claims.py. Do not edit by hand.',
        'verdicts':  VERDICTS,
        'categories': CATEGORIES,
        'claims':    claims,
    }
    OUTPUT_FILE.write_text(json.dumps(out, indent=2, ensure_ascii=False) + '\n',
                           encoding='utf-8')

    print(f'Wrote {len(claims)} claims to {OUTPUT_FILE}')
    for w in warnings:
        print(f'  WARNING: {w}')
    return 0


if __name__ == '__main__':
    sys.exit(build())
