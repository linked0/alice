#!/usr/bin/env python3
"""Build the left rail before the browser paints, instead of at the end of <body>.

    python3 scripts/rail-before-paint.py [--apply]

jay, 2026-09-25 (after the scroll-jump fix): "it blinks yet for the left panel".

Cause, and it is not the one the first fix addressed. On a detail page the rail container ships
EMPTY — `<nav class="rail-nav" id="nav">` holds only the "No match." paragraph — and ~975 entries
are injected by a script sitting near `</body>`, 450-odd lines later. The browser therefore paints
an empty left panel, then repaints it full. Every navigation flashes once, regardless of scroll.
notes.html does not flash because its rail is real HTML.

Fix: relocate `_nav.js`, the `__NAV_CURRENT__` assignment and the rail-building IIFE to sit
immediately after `</nav>`. Classic scripts block parsing, so the rail DOM now exists before the
rest of the document is parsed and before first paint. Nothing else moves: `_progress.js` and the
filter / scroll-spy / copy code stay where they were, because they legitimately need the whole page.

Idempotent. Pages already carrying the moved block are skipped.
"""
import pathlib, sys, glob, re

ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs" / "topics"
APPLY = "--apply" in sys.argv
NAV_CLOSE = "    </nav>\n"
MARKER = "<!-- rail built before paint -->"

moved = skipped = unmatched = 0
problems = []
for f in sorted(glob.glob(str(ROOT / "*.html"))):
    p = pathlib.Path(f); s = p.read_text()
    if MARKER in s: skipped += 1; continue

    m = re.search(r'(?P<nav><script src="_nav\.js"></script>\n)'
                  r'(?P<progress><script src="_progress\.js"></script>\n)?'
                  r'(?P<current><script>window\.__NAV_CURRENT__="[^"]*";</script>\n)?'
                  r'<script>\n'
                  r'(?P<build>\(function \(\) \{\n  var data = window\.__NAV__.*?\n\}\)\(\);\n)', s, re.S)
    if not m or NAV_CLOSE not in s:
        unmatched += 1; problems.append(p.name); continue

    # What leaves the old position: _nav.js, __NAV_CURRENT__ and the rail IIFE.
    # What stays: _progress.js, and a fresh <script> tag for the code that followed the IIFE —
    # the opening tag belonged to that block, so it has to be put back or the rest becomes text.
    progress = m.group("progress") or ""
    s2 = s[:m.start()] + progress + "<script>\n" + s[m.end():]
    block = (MARKER + "\n"
             + m.group("nav")
             + (m.group("current") or "")
             + "<script>\n" + m.group("build") + "</script>\n")
    i = s2.index(NAV_CLOSE) + len(NAV_CLOSE)
    s2 = s2[:i] + block + s2[i:]

    if APPLY: p.write_text(s2)
    moved += 1

verb = "moved" if APPLY else "would move"
print(f"{verb} the rail build on {moved} page(s); {skipped} already done; {unmatched} did not match")
if problems: print("  unmatched (left alone):", ", ".join(problems[:6]), "…" if len(problems) > 6 else "")
if not APPLY: print("(dry run — pass --apply)")
