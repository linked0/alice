#!/usr/bin/env python3
"""Insert (or refresh) the "Key expressions" vocabulary table on Knowledge Notes detail pages.

  python3 scripts/add-vocab.py <key> [<key> ...]     # docs/topics/<key>.html  <-  docs/topics/vocab/<key>.md
  python3 scripts/add-vocab.py --all                 # every docs/topics/vocab/*.md

Rule (jay, 2026-09-18): every detail page carries the words and phrases worth learning from its
English text, with Korean meaning and where they appear. The table lives as markdown in
docs/topics/vocab/<key>.md (two columns: Expression | 뜻 · 쓰이는 자리) and is rendered at the end of
the English article ("Key expressions") and of the Korean article ("핵심 표현"). Idempotent: the
block sits between <!-- vocab:start --> and <!-- vocab:end --> and is replaced on re-run, so the
page can be regenerated and this script run again. English conversation pages already have their
own expressions table and are skipped.
"""
import argparse, html, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs" / "topics"
VOCAB = ROOT / "vocab"
E = lambda s: html.escape(s, quote=False).replace("'", "&#39;")
def inline(t):
    t = E(t); t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t); return re.sub(r'`(.+?)`', r'<code>\1</code>', t)

def rows_of(md):
    rows = []
    for l in md.splitlines():
        l = l.strip()
        if not l.startswith("|") or re.match(r'^\|[-| ]+\|$', l): continue
        cells = [c.strip() for c in l.strip("|").split("|")]
        if len(cells) < 2 or cells[0].lower() == "expression": continue
        rows.append(cells[:2])
    return rows

def block(rows, lang):
    h2, note = (("Key expressions", "Words and phrases from this page worth keeping, with the Korean meaning and the sentence they come from.")
                if lang == "en" else ("핵심 표현", "이 페이지의 영어 본문에서 배울 만한 단어와 표현, 뜻과 나온 자리."))
    tb = "".join(f"<tr><td><strong>{inline(a)}</strong></td><td>{inline(b)}</td></tr>" for a, b in rows)
    return (f'<!-- vocab:start -->\n<section class="vocab"><h2>{h2}</h2><p class="meta">{note}</p>'
            f'<div class="table-wrap" style="overflow-x:auto"><table><thead><tr><th>Expression</th><th>뜻 · 쓰이는 자리</th></tr></thead><tbody>{tb}</tbody></table></div></section>\n<!-- vocab:end -->\n')

STRIP = re.compile(r'<!-- vocab:start -->.*?<!-- vocab:end -->\n?', re.S)

def article_span(s, opener_pat):
    m = re.search(opener_pat, s)
    if not m: return None
    end = s.index("</article>", m.end())
    return m.end(), end

def insert_point(s, a0, a1, footer_marker):
    body = s[a0:a1]
    for marker in ('<p class="stub">', footer_marker, footer_marker.replace('notes.html?list', 'notes.html')):
        i = body.find(marker)
        if i >= 0: return a0 + i
    return a1

def apply(key):
    page = ROOT / f"{key}.html"; src = VOCAB / f"{key}.md"
    if key.startswith("english-"): return "skip (english page has its own expressions)"
    if not page.exists(): return f"missing page {page.name}"
    if not src.exists(): return f"missing vocab {src.name}"
    rows = rows_of(src.read_text())
    if len(rows) < 3: return f"too few rows ({len(rows)})"
    s = STRIP.sub("", page.read_text())
    en = article_span(s, r'<article id="en">|<article>(?!\s*<p class="lang-label")')
    if not en: return "no English article"
    p = insert_point(s, *en, '<p><a href="../notes.html?list">&larr; All Knowledge Notes</a>')
    s = s[:p] + block(rows, "en") + s[p:]
    ko = article_span(s, r'<article id="ko"[^>]*>|<article lang="ko">')
    if ko:
        p = insert_point(s, *ko, '<p><a href="../notes.html?list">&larr; 전체 기술 노트</a>')
        s = s[:p] + block(rows, "ko") + s[p:]
    page.write_text(s)
    return f"ok ({len(rows)} rows{'' if ko else ', en only'})"

ap = argparse.ArgumentParser(); ap.add_argument("keys", nargs="*"); ap.add_argument("--all", action="store_true")
A = ap.parse_args()
keys = A.keys or (sorted(p.stem for p in VOCAB.glob("*.md") if p.stem != "README") if A.all else [])
if not keys: ap.error("give keys or --all")
bad = 0
for k in keys:
    r = apply(k); bad += not r.startswith(("ok", "skip"))
    if not r.startswith("ok") or len(keys) == 1: print(f"{k}: {r}")
print(f"{len(keys)} pages, {bad} problems"); sys.exit(1 if bad else 0)
