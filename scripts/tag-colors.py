#!/usr/bin/env python3
"""Give the Life tag chips their own colours.

    python3 scripts/tag-colors.py [--apply]

jay, 2026-09-25: "add some unique color for the book flag."

A chip's tag is its text content, and CSS cannot select on text, so each chip also gets
data-tag="<tag>" and the colours are attribute rules. The attribute is added to every chip, not just
the Life ones, so colouring another section later is a CSS edit and nothing else.

Coloured: Book, Film, Manga and Anime, all in the SAME colour (jay: "make the film, manga, anime
have the same color as the book for the flag"). They are one family - a list of works - so one
colour marks the family rather than distinguishing its members. Work, Mind, Body and People, and
every Theory / Invest / English chip, keep the default grey.

Colours are a hue plus the same hue at low alpha, the pattern --accent-soft already uses, so they
sit on either background; a second prefers-color-scheme block lightens them for dark mode.

Idempotent.
"""
import pathlib, sys, glob, re

ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs"
APPLY = "--apply" in sys.argv

MEDIA = ("Book", "Film", "Manga", "Anime")   # 목록 카드 한 묶음 — 같은 색으로 묶는다
LIGHT_HUE, DARK_HUE = "#b45309", "#fbbf24"
LIGHT = {k: LIGHT_HUE for k in MEDIA}
DARK  = {k: DARK_HUE for k in MEDIA}

ANCHOR = '  .nav-text .topic-tag { font-size:0.6rem; padding:0 5px; margin-right:.35em; vertical-align:middle; }\n'
CSS = (ANCHOR
       + '  /* Life 태그 칩 색 (jay, 2026-09-25: "add some unique color for the book flag").\n'
       + '     칩의 텍스트가 곧 태그값인데 CSS는 텍스트로 선택할 수 없어서 data-tag 를 함께 쓴다.\n'
       + '     Book·Film·Manga·Anime 는 한 묶음이라 같은 색(jay, 2026-09-25). 나머지 칩은 기본 회색. */\n'
       + '  ' + ", ".join(f'.topic-tag[data-tag="{k}"]' for k in MEDIA) + f' {{ color:{LIGHT_HUE}; background:{LIGHT_HUE}22; }}\n'
       + '  @media (prefers-color-scheme: dark) {\n'
       + '    ' + ", ".join(f'.topic-tag[data-tag="{k}"]' for k in MEDIA) + f' {{ color:{DARK_HUE}; background:{DARK_HUE}26; }}\n'
       + '  }\n')

# chips live as plain HTML in notes.html and as JSON-escaped HTML inside _nav.js
PLAIN  = re.compile(r'<span class="topic-tag">([^<]*)</span>')
ESCAPED = re.compile(r'<span class=\\"topic-tag\\">([^<]*)</span>')

def add_attr(s):
    s, n1 = PLAIN.subn(lambda m: f'<span class="topic-tag" data-tag="{m.group(1)}">{m.group(1)}</span>', s)
    s, n2 = ESCAPED.subn(lambda m: f'<span class=\\"topic-tag\\" data-tag=\\"{m.group(1)}\\">{m.group(1)}</span>', s)
    return s, n1 + n2

chips = css = skipped = 0
targets = [ROOT / "notes.html", ROOT / "index.html", ROOT / "topics" / "_nav.js"] \
          + [pathlib.Path(f) for f in sorted(glob.glob(str(ROOT / "topics" / "*.html")))]
for p in targets:
    if not p.exists(): continue
    s = orig = p.read_text()
    s, n = add_attr(s)
    chips += n
    if ANCHOR in s and 'data-tag="Book"' not in s.split(ANCHOR)[1][:900]:
        s = s.replace(ANCHOR, CSS, 1); css += 1
    if s == orig: skipped += 1; continue
    if APPLY: p.write_text(s)

verb = "added" if APPLY else "would add"
print(f"{verb} data-tag to {chips} chip(s); {verb} the colour block to {css} file(s); {skipped} unchanged")
if not APPLY: print("(dry run — pass --apply)")
