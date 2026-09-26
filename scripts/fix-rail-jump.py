#!/usr/bin/env python3
"""Stop the left rail from jumping on page load when the active item is already visible.

    python3 scripts/fix-rail-jump.py [--apply]

jay, 2026-09-25: "When clicking the item on the left panel, if the item is in the window, don't blink
the list by redrawing, because it's very cumbersome when it's blinking."

What was happening: every page ends with an IIFE that centres the rail on the active link. It ran
unconditionally, so clicking an item that was already on screen still re-centred it — the whole list
slid by half a viewport on every click. The scroll-spy path (`revealInRail`) had had the right guard
since 2026-08-27; the on-load path never got it.

The fix is that same guard: if the active link is fully inside the rail viewport, leave scrollTop
alone. Centring still happens when the item really is off-screen, which is the case the code was
written for. Idempotent — pages already carrying the guard are skipped.
"""
import pathlib, sys, glob

ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs"
APPLY = "--apply" in sys.argv

OLD = """  if (!el) return;
  var r = el.getBoundingClientRect();
  var c = nav.getBoundingClientRect();
  nav.scrollTop += (r.top - c.top) - (c.height / 2 - r.height / 2);"""
NEW = """  if (!el) return;
  var r = el.getBoundingClientRect();
  var c = nav.getBoundingClientRect();
  // 이미 레일 안에 보이면 스크롤을 건드리지 않는다 (jay, 2026-09-25: 클릭할 때마다 목록이 깜빡인다).
  // 가운데로 끌어오는 건 항목이 레일 밖에 있을 때만. 보이는 항목을 재배치하면 목록 전체가 튄다.
  if (r.top >= c.top + 4 && r.bottom <= c.bottom - 4) return;
  nav.scrollTop += (r.top - c.top) - (c.height / 2 - r.height / 2);"""

targets = [ROOT / "notes.html", ROOT / "index.html"] + [pathlib.Path(f) for f in sorted(glob.glob(str(ROOT / "topics" / "*.html")))]
patched = skipped = absent = 0
for p in targets:
    if not p.exists(): continue
    s = p.read_text()
    if NEW in s: skipped += 1; continue
    if OLD not in s: absent += 1; continue
    if APPLY: p.write_text(s.replace(OLD, NEW, 1))
    patched += 1

verb = "patched" if APPLY else "would patch"
print(f"{verb} {patched} file(s); {skipped} already had the guard; {absent} had no rail-centring block")
if not APPLY: print("(dry run — pass --apply)")
