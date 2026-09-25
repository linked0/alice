#!/usr/bin/env python3
"""Don't re-centre the rail when the clicked item is only partly visible.

    python3 scripts/rail-keep-partial.py [--apply]

jay, 2026-09-25: "make the left panel not scroll if the clicked thing is cut the border of the
panel because it's inconvenient to scroll unnecessarily when clicked."

The on-load guard added earlier asked "is the active item FULLY inside the rail viewport?". An item
clipped by the top or bottom edge failed that test, so the rail still slid to centre it — which is
the case jay is describing: the item is right there, readable, and the list moves anyway.

The test becomes "does the item overlap the rail viewport at all?". Centring is then reserved for
the one case it was written for: the active item is completely off-screen and would otherwise be
unfindable. 4px of slack keeps a sub-pixel sliver from counting as visible.

Only the click/load path changes. revealInRail, which runs while you scroll, keeps the stricter
test on purpose: there the active item drifts as you read, and letting it drift out entirely is the
thing that path exists to prevent.

Idempotent.
"""
import pathlib, sys, glob

ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs"
APPLY = "--apply" in sys.argv

OLD = """  // 이미 레일 안에 보이면 스크롤을 건드리지 않는다 (jay, 2026-09-25: 클릭할 때마다 목록이 깜빡인다).
  // 가운데로 끌어오는 건 항목이 레일 밖에 있을 때만. 보이는 항목을 재배치하면 목록 전체가 튄다.
  if (r.top >= c.top + 4 && r.bottom <= c.bottom - 4) return;"""
NEW = """  // 조금이라도 보이면 스크롤을 건드리지 않는다 (jay, 2026-09-25: "경계에 걸쳐 잘려 있어도 스크롤하지 마라").
  // 조건은 '완전히 보이는가'가 아니라 '겹치는가'다 — 한 줄이 반쯤 잘린 채 보이면 그것으로 충분하고,
  // 그걸 가운데로 끌어오려고 목록을 통째로 움직이면 클릭할 때마다 불필요한 스크롤이 생긴다.
  // 가운데 정렬은 항목이 레일 밖으로 완전히 나가 찾을 수 없을 때만 — 그게 이 코드가 원래 맡은 경우다.
  if (r.bottom > c.top + 4 && r.top < c.bottom - 4) return;"""

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
print(f"{verb} {patched} file(s); {skipped} already relaxed; {absent} had no on-load guard")
if not APPLY: print("(dry run — pass --apply)")
