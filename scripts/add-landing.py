#!/usr/bin/env python3
"""Insert (or refresh) the "Where it lands in Jayverse" section on Knowledge Notes detail pages.

  python3 scripts/add-landing.py <key> [<key> ...]   # docs/topics/<key>.html  <-  docs/topics/landing/<key>.md
  python3 scripts/add-landing.py --all

Rule (jay, 2026-09-18): every detail page closes its body with concrete Jayverse decisions. Pages written
with add-tech-item.py carry the section in their own markdown; this script backfills the rest from
docs/topics/landing/<key>.md, which has two lists under "## en" and "## ko". The block sits between
<!-- landing:start --> and <!-- landing:end --> and is replaced on re-run. Placement: before the
"Verified and unverified" heading when the page has one, else before the Key expressions block, the
curriculum stub, or the footer link. Pages that already have the heading outside a landing block are
left alone.
"""
import argparse, html, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs" / "topics"
SRC = ROOT / "landing"
E = lambda s: html.escape(s, quote=False).replace("'", "&#39;")
def inline(t):
    t = E(t); t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t); return re.sub(r'`(.+?)`', r'<code>\1</code>', t)

def lists(md):
    out = {}
    for lang in ("en", "ko"):
        m = re.search(rf'^## {lang}\s*\n(.*?)(?=^## |\Z)', md, re.S | re.M)
        out[lang] = [l[2:].strip() for l in m.group(1).splitlines() if l.startswith("- ")] if m else []
    return out

STRIP = re.compile(r'<!-- landing:start -->.*?<!-- landing:end -->\n?', re.S)
HEAD = {"en": "Where it lands in Jayverse", "ko": "Jayverse에서의 위치"}

def block(items, lang, level):
    lis = "".join(f"<li>{inline(x)}</li>" for x in items)
    return f'<!-- landing:start -->\n<h{level}>{HEAD[lang]}</h{level}>\n<ul>{lis}</ul>\n<!-- landing:end -->\n'

def article_span(s, opener_pat):
    m = re.search(opener_pat, s)
    if not m: return None
    return m.end(), s.index("</article>", m.end())

def insert_point(s, a0, a1, lang):
    body = s[a0:a1]
    markers = ([r'<h3>Verified and unverified</h3>'] if lang == "en" else [r'<h3>확인된 것과 미확인</h3>']) + \
              [r'<!-- vocab:start -->', r'<p class="stub">',
               r'<p><a href="\.\./notes\.html(\?list)?">&larr; (All Knowledge Notes|전체 기술 노트)</a>']
    for pat in markers:
        m = re.search(pat, body)
        if m: return a0 + m.start()
    return a1

def apply(key):
    page = ROOT / f"{key}.html"; src = SRC / f"{key}.md"
    if key.startswith("english-"): return "skip (english)"
    if not page.exists(): return f"missing page {page.name}"
    if not src.exists(): return f"missing landing {src.name}"
    L = lists(src.read_text())
    if len(L["en"]) < 2 or len(L["ko"]) < 2: return f"too few bullets (en {len(L['en'])}, ko {len(L['ko'])})"
    s = STRIP.sub("", page.read_text())
    if re.search(r'<h[23]>\s*Where it lands in Jayverse', s): return "skip (already has the section)"
    level = 2 if key.startswith(("algorithms-", "math-")) else 3
    en = article_span(s, r'<article id="en">|<article>(?!\s*<p class="lang-label")')
    if not en: return "no English article"
    p = insert_point(s, *en, "en"); s = s[:p] + block(L["en"], "en", level) + s[p:]
    ko = article_span(s, r'<article id="ko"[^>]*>|<article lang="ko">')
    if ko:
        p = insert_point(s, *ko, "ko"); s = s[:p] + block(L["ko"], "ko", level) + s[p:]
    page.write_text(s)
    return f"ok ({len(L['en'])} bullets{'' if ko else ', en only'})"

ap = argparse.ArgumentParser(); ap.add_argument("keys", nargs="*"); ap.add_argument("--all", action="store_true")
A = ap.parse_args()
keys = A.keys or (sorted(p.stem for p in SRC.glob("*.md") if p.stem != "README") if A.all else [])
if not keys: ap.error("give keys or --all")
bad = 0
for k in keys:
    r = apply(k); bad += not r.startswith(("ok", "skip"))
    if not r.startswith("ok") or len(keys) == 1: print(f"{k}: {r}")
print(f"{len(keys)} pages, {bad} problems"); sys.exit(1 if bad else 0)
