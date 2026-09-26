#!/usr/bin/env python3
"""Carry the rail's scroll position across navigation instead of centring the active item.

    python3 scripts/rail-keep-position.py [--apply]

jay, 2026-09-25: "When I click an item in the left panel, the panel is scrolled for the selected
item being centered. It's so inconvenient." … "make it not scroll" … "for that timing".

Why the previous guards could not fix this. Every guard so far asked "is the active item already
visible?" — but a click loads a NEW page, and that page's rail starts at scrollTop 0. The item you
just clicked, plainly visible a moment earlier, is off-screen by the time the guard runs, so the
guard correctly declines to fire and the centring runs. No visibility test can win, because the
state being tested was destroyed by the navigation.

So the approach changes: hand the scroll position over instead of recomputing it. The rail saves
its scrollTop to sessionStorage when you scroll it and when you click a link inside the same
section, and restores it on the next page before paint. The panel then does not move at all -
same list, same position, only the highlight changes.

Centring survives in exactly one case: a cold arrival with nothing saved (external link, new tab).
There is no previous frame to compare against, so nothing reads as movement.

Position is kept per section, and only handed over for clicks within the same section, because the
visible list differs between sections and a raw offset would be meaningless across them.

Idempotent.
"""
import pathlib, sys, glob

ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs"
APPLY = "--apply" in sys.argv

OLD = pathlib.Path("/tmp/old_iife.txt").read_text()
NEW = """(function () {
  var nav = document.querySelector('.rail-nav');
  if (!nav) return;
  var el = nav.querySelector('.nav-link.active');
  if (!el && !location.hash) {
    var dot = nav.querySelector('.nav-dot[title="IMPORTANT"]');
    el = dot && dot.closest('a');
  }
  // 레일은 페이지를 옮겨도 스크롤 위치를 그대로 물려받는다 (jay, 2026-09-25: "클릭하면 선택 항목을
  // 가운데로 맞추려고 패널이 스크롤된다 … make it not scroll, for that timing").
  // 가드로는 막을 수 없었던 이유: 클릭은 새 페이지를 띄우고 그 레일은 scrollTop=0에서 시작하므로,
  // 방금까지 보이던 항목도 여기서는 화면 밖이다. 그래서 '보이면 두기'가 아니라 '위치를 넘겨주기'로 바꾼다.
  var KEY = 'rail:pos';
  var group = el && el.closest('[data-group]');
  var sec = group ? group.id : '';
  var restored = false;
  try {
    var saved = JSON.parse(sessionStorage.getItem(KEY) || 'null');
    if (saved && saved.sec === sec && typeof saved.top === 'number') { nav.scrollTop = saved.top; restored = true; }
  } catch (e) {}
  var save = function (id) {
    try { sessionStorage.setItem(KEY, JSON.stringify({ sec: id || sec, top: nav.scrollTop })); } catch (e) {}
  };
  var timer;
  nav.addEventListener('scroll', function () { clearTimeout(timer); timer = setTimeout(save, 120); }, { passive: true });
  var links = nav.querySelectorAll('a');
  for (var i = 0; i < links.length; i++) {
    links[i].addEventListener('click', function () {
      var g = this.closest('[data-group]');
      if (g && g.id === sec) save(g.id);   // 같은 섹션 안에서의 이동일 때만 위치를 넘긴다
    });
  }
  // 클릭으로 들어온 경우(=넘겨받은 위치가 있는 경우)에는 스크롤하지 않는다.
  // 가운데 정렬은 저장된 위치가 없는 첫 진입에서만 — 비교할 직전 화면이 없으니 움직임으로 보이지 않는다.
  if (restored || !el) return;
  var r = el.getBoundingClientRect();
  var c = nav.getBoundingClientRect();
  if (r.bottom > c.top + 4 && r.top < c.bottom - 4) return;
  nav.scrollTop += (r.top - c.top) - (c.height / 2 - r.height / 2);
})();"""

targets = [ROOT / "notes.html", ROOT / "index.html"] + [pathlib.Path(f) for f in sorted(glob.glob(str(ROOT / "topics" / "*.html")))]
patched = skipped = absent = 0
for p in targets:
    if not p.exists(): continue
    s = p.read_text()
    if "var KEY = 'rail:pos';" in s: skipped += 1; continue
    if OLD not in s: absent += 1; continue
    if APPLY: p.write_text(s.replace(OLD, NEW, 1))
    patched += 1

verb = "patched" if APPLY else "would patch"
print(f"{verb} {patched} file(s); {skipped} already had it; {absent} did not match")
if not APPLY: print("(dry run — pass --apply)")
