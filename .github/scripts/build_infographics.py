#!/usr/bin/env python3
"""
build_infographics.py
Generates wiki/infographics.json from the pages in wiki/infographics/.

Each page produces one tile in the app's infographics gallery. The tile is
built from the frontmatter plus two body sections:

    What it shows  -> caption
    Key figures    -> figures (list)

Every other section is ignored. The JSON format is documented in
docs/infographics.md so the app can be built against it.

Run: python3 .github/scripts/build_infographics.py
Output: wiki/infographics.json
"""

import json, re, sys
from pathlib import Path

WIKI_DIR    = Path(__file__).parent.parent.parent / 'wiki'
INFO_DIR    = WIKI_DIR / 'infographics'
OUTPUT_FILE = WIKI_DIR / 'infographics.json'

# Images are served straight from GitHub, the same way existing wiki pages
# embed their images, so the app needs no image hosting of its own.
RAW_BASE = 'https://raw.githubusercontent.com/fmossiere-bot/climate-action-wiki/refs/heads/main/wiki/infographics/'

# Same ids as the Counter Claims categories, plus `nature`, so the app's
# filters stay consistent between the two features.
TOPICS = [
    {'id': 'transport', 'label': 'Cars & flying',     'icon': 'directions_car'},
    {'id': 'energy',    'label': 'Energy',            'icon': 'bolt'},
    {'id': 'materials', 'label': 'Materials & waste', 'icon': 'recycling'},
    {'id': 'food',      'label': 'Food',              'icon': 'restaurant'},
    {'id': 'nature',    'label': 'Nature',            'icon': 'forest'},
    {'id': 'systemic',  'label': 'Big picture',       'icon': 'public'},
    {'id': 'ireland',   'label': 'Ireland',           'icon': 'flag'},
]
VALID_TOPICS = {t['id'] for t in TOPICS}


def parse_frontmatter(content: str) -> dict:
    """Same contract as build_claims.py, plus the block-list `related:`."""
    if not content.startswith('---'):
        return {}
    try:
        end = content.index('\n---', 3)
    except ValueError:
        return {}

    result, list_key = {}, None
    for line in content[3:end].splitlines():
        item = re.match(r'^\s+-\s+(.*)$', line)
        if item and list_key:
            result[list_key].append(item.group(1).strip().strip('"').strip("'"))
            continue
        m = re.match(r'^(\w+)\s*:\s*(.*)', line)
        if not m:
            continue
        key, val = m.group(1).strip(), m.group(2).strip()
        list_key = None
        if key in ('tags', 'sources'):
            items = re.findall(r'"([^"]*)"', val)
            if not items and val.startswith('['):
                items = [v.strip() for v in val.strip('[]').split(',') if v.strip()]
            result[key] = [i.lstrip('#') if key == 'tags' else i for i in items]
        elif key == 'related' and not val:
            result[key], list_key = [], key
        else:
            result[key] = val.strip('"').strip("'")
    return result


def split_sections(body: str) -> dict:
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
    text = strip_comments(text)
    return ' '.join(l.strip() for l in text.split('\n') if l.strip())


def parse_bullets(text: str) -> list:
    out = []
    for line in strip_comments(text).split('\n'):
        m = re.match(r'^\s*[-*+]\s+(.*)$', line)
        if m:
            out.append(m.group(1).strip())
    return out


def build():
    if not INFO_DIR.is_dir():
        print(f'No {INFO_DIR}, nothing to build.', file=sys.stderr)
        return 1

    items, warnings = [], []
    for md in sorted(INFO_DIR.glob('*.md')):
        if md.name.startswith('_'):
            continue
        text = md.read_text(encoding='utf-8')
        fm   = parse_frontmatter(text)
        body = text[text.index('\n---', 3) + 4:] if '\n---' in text else text
        sec  = split_sections(body)
        slug = md.stem

        image = fm.get('image', '')
        if not image:
            warnings.append(f'{md.name}: no image, skipped')
            continue
        if not (INFO_DIR / image).is_file():
            warnings.append(f'{md.name}: image "{image}" not found in wiki/infographics/')

        topic = fm.get('topic', '')
        if topic not in VALID_TOPICS:
            warnings.append(f'{md.name}: unknown topic "{topic}", using systemic')
            topic = 'systemic'

        for required in ('credit', 'image_alt'):
            if not fm.get(required):
                warnings.append(f'{md.name}: missing {required}')
        if not sec.get('what it shows'):
            warnings.append(f'{md.name}: missing "## What it shows"')

        items.append({
            'id':          slug,
            'title':       fm.get('title', slug),
            'caption':     clean_prose(sec.get('what it shows', '')),
            'figures':     parse_bullets(sec.get('key figures', '')),
            'image_url':   RAW_BASE + image,
            'alt':         fm.get('image_alt', ''),
            'credit':      {'name': fm.get('credit', ''), 'url': fm.get('credit_url', '')},
            'source_post': fm.get('source_post', ''),
            'data_source': fm.get('data_source', ''),
            'origin':      fm.get('origin', 'external'),
            'topic':       topic,
            'tags':        fm.get('tags', []),
            'related':     fm.get('related', []),
            'wiki':        f'infographics/{md.name}',
            'created':     fm.get('created', ''),
        })

    # Newest first, so the gallery opens on the latest additions.
    items.sort(key=lambda i: (i['created'], i['id']), reverse=True)

    out = {
        'version':      1,
        'updated':      __import__('datetime').date.today().isoformat(),
        'note':         'Generated from wiki/infographics/ by build_infographics.py. Do not edit by hand.',
        'topics':       TOPICS,
        'infographics': items,
    }
    OUTPUT_FILE.write_text(json.dumps(out, indent=2, ensure_ascii=False) + '\n',
                           encoding='utf-8')

    print(f'Wrote {len(items)} infographics to {OUTPUT_FILE}')
    for w in warnings:
        print(f'  WARNING: {w}')
    return 0


if __name__ == '__main__':
    sys.exit(build())
