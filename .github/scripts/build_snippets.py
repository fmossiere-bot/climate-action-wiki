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

The companion's api-proxy.php fetches this file on every query and
passes it to the LLM retriever so it can match questions against real
content — not just page titles.

Run: python3 .github/scripts/build_snippets.py
Output: wiki/wiki-snippets.json
"""

import json, re, sys
from pathlib import Path

WIKI_DIR    = Path(__file__).parent.parent.parent / 'wiki'
OUTPUT_FILE = WIKI_DIR / 'wiki-snippets.json'
SKIP_FILES  = {'index.md', 'log.md', 'wiki-snippets.json'}

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

        # Relative path from wiki/ (used by api-proxy to build the raw URL)
        rel_path = md_file.relative_to(WIKI_DIR).as_posix()
        slug     = slugify(md_file.stem)
        label    = fm.get('title') or md_file.stem
        summary  = fm.get('summary', '')
        category = fm.get('category', '')
        tags     = fm.get('tags', [])

        snippets.append({
            'slug':     slug,
            'filename': rel_path,
            'label':    label,
            'summary':  summary,
            'category': category,
            'tags':     tags,
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
