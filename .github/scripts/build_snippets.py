#!/usr/bin/env python3
"""
build_snippets.py
Generates wiki/wiki-snippets.json from all wiki .md files.

For each page it extracts:
  - slug        : URL-safe identifier derived from filename
  - filename    : path relative to wiki/ (used to build raw GitHub URL)
  - label       : page title from frontmatter
  - summary     : summary field from frontmatter (topics, keywords)
  - category    : category field from frontmatter
  - tags        : tags list from frontmatter
  - keywords    : auto-extracted from the body (bolded terms + frequent
                  non-generic long words) — a backstop signal for terms a
                  hand-written summary doesn't happen to mention (e.g. a
                  page titled/summarised around "Marine Algae" that never
                  says "kelp", even though the body is full of it).

The companion's api-proxy.php fetches this file on every query and
passes it to the LLM retriever so it can match questions against real
content — not just page titles.

Run: python3 .github/scripts/build_snippets.py
Output: wiki/wiki-snippets.json
"""

import json, re, sys, collections
from pathlib import Path

WIKI_DIR    = Path(__file__).parent.parent.parent / 'wiki'
OUTPUT_FILE = WIKI_DIR / 'wiki-snippets.json'
SKIP_FILES  = {'index.md', 'log.md', 'wiki-snippets.json'}

# Common English function words. Needed because lowering the length floor
# (below) to catch short-but-meaningful nouns like "kelp" or "peat" would
# otherwise let ordinary words like "with" or "from" through too.
STOPWORDS = {
    'this', 'that', 'these', 'those', 'with', 'from', 'have', 'has', 'had',
    'were', 'been', 'being', 'their', 'there', 'which', 'while', 'about',
    'into', 'than', 'them', 'they', 'what', 'when', 'where', 'will', 'would',
    'could', 'should', 'also', 'more', 'most', 'some', 'such', 'only', 'over',
    'each', 'other', 'even', 'just', 'like', 'much', 'many', 'both', 'still',
    'here', 'then', 'your', 'yours', 'ours', 'itself', 'himself', 'herself',
}

# Words too common across the wiki's own subject matter to be useful as a
# distinguishing keyword — matching on these tells you nothing.
GENERIC_WORDS = {
    'climate', 'carbon', 'energy', 'emissions', 'renewable', 'renewables',
    'sustainability', 'sustainable', 'environment', 'environmental',
    'action', 'actions', 'change', 'global', 'world', 'people', 'system',
    'systems', 'solution', 'solutions', 'impact', 'impacts', 'include',
    'includes', 'including', 'across', 'however', 'because', 'through',
    'important', 'significant', 'different', 'various', 'number', 'tonnes',
    'according', 'research', 'researchers', 'studies', 'study', 'roughly',
    'estimated', 'estimate', 'currently', 'without', 'between', 'often',
}

EXCLUDED_WORDS = STOPWORDS | GENERIC_WORDS
KEYWORD_LIMIT  = 12


def extract_keywords(body: str, limit: int = KEYWORD_LIMIT) -> list[str]:
    """Pull a compact set of distinctive terms out of a page body."""
    # Bolded markdown terms are usually the author's own emphasis on key
    # concepts, so they get priority over frequency-based picks.
    bold_terms = [b.strip().lower() for b in re.findall(r'\*\*([^*]{3,40})\*\*', body)]

    # Frequent, non-generic words as a fallback signal — require 3+
    # occurrences so a single incidental mention doesn't count. Floor is 4
    # characters (not the usual 5+) so short domain nouns like "kelp" or
    # "peat" aren't filtered out purely for being short.
    words = re.findall(r"[a-zA-Z][a-zA-Z\-']{3,}", body)
    freq  = collections.Counter(
        w.lower() for w in words if w.lower() not in EXCLUDED_WORDS
    )
    frequent_terms = [w for w, c in freq.most_common(limit) if c >= 3]

    seen: list[str] = []
    for term in bold_terms + frequent_terms:
        term = term.strip(' .,:;')
        if term and term not in seen:
            seen.append(term)
        if len(seen) >= limit:
            break
    return seen

def parse_frontmatter(content: str) -> dict:
    """Extract key/value pairs from YAML frontmatter block."""
    if not content.startswith('---'):
        return {}
    try:
        end = content.index('---', 3)
    except ValueError:
        return {}

    fm_text = content[3:end]
    result  = {}

    for line in fm_text.splitlines():
        # Simple key: value (handles quoted values and bare values)
        m = re.match(r'^(\w+)\s*:\s*(.*)', line)
        if not m:
            continue
        key = m.group(1).strip()
        val = m.group(2).strip().strip('"').strip("'")

        # Tags can be inline [a, b] or multi-line (we just grab inline here)
        if key == 'tags':
            tags_raw = re.findall(r'[\w#][\w\-]*', val)
            result[key] = [t.lstrip('#') for t in tags_raw if t]
        else:
            result[key] = val

    return result


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')


def build_snippets() -> list[dict]:
    snippets = []

    for md_file in sorted(WIKI_DIR.rglob('*.md')):
        if md_file.name in SKIP_FILES:
            continue

        content  = md_file.read_text(encoding='utf-8')
        fm       = parse_frontmatter(content)

        # Body only (strip frontmatter block) for keyword extraction.
        body = content
        if content.startswith('---'):
            try:
                body = content[content.index('---', 3) + 3:]
            except ValueError:
                pass

        # Relative path from wiki/ (used by api-proxy to build the raw URL)
        rel_path = md_file.relative_to(WIKI_DIR).as_posix()
        slug     = slugify(md_file.stem)
        label    = fm.get('title') or md_file.stem
        summary  = fm.get('summary', '')
        category = fm.get('category', '')
        tags     = fm.get('tags', [])
        keywords = extract_keywords(body)

        snippets.append({
            'slug':     slug,
            'filename': rel_path,
            'label':    label,
            'summary':  summary,
            'category': category,
            'tags':     tags,
            'keywords': keywords,
        })

    return snippets


if __name__ == '__main__':
    snippets = build_snippets()
    OUTPUT_FILE.write_text(
        json.dumps(snippets, ensure_ascii=False, indent=2),
        encoding='utf-8'
    )
    print(f"✅ wiki-snippets.json written — {len(snippets)} pages indexed.")
    sys.exit(0)
