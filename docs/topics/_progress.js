// Rail-head progress badges (jay, 2026-09-16): the top badge is the CURRENT status in red (clickable, see below);
// next to it, on the same line, is the PREVIOUS DAY's closing status in blue (jay, 2026-09-18:
// no "done" word, both badges on one line) (replacing the old pink
// "2%/day → 95% done" pace reminder). Loaded by notes.html and every topics/pocs-*.html
// after _nav.js, so all pages show the same numbers.
//
// Data: window.__NAV__.jump gives today's per-section done/all (summed here), and
// window.__NAV__.progress is the day-by-day log: [{date:"YYYY-MM-DD", done, all}, …].
// Rule when bumping counters on a new KST day: first append the previous day's closing
// numbers to `progress`, then change `jump`. The badge shows the latest entry dated before
// today; the date is kept only in the title tooltip (jay: no date in the badge text).
(function () {
  var nav = window.__NAV__; if (!nav || !nav.jump) return;
  var head = document.querySelector('.rail-head'); if (!head) return;
  var done = 0, all = 0;
  nav.jump.forEach(function (j) { done += j.done; all += j.all; });
  var pct = function (d, a) { return a ? Math.round(d * 100 / a) : 0; };
  var cur = head.querySelector('.rail-note');
  // The red badge is a button (jay, 2026-09-18: "make it clickable and make the clicking shows all the categories for
  // the buttons from Important and Today … I mean All to the status red area"). Clicking toggles body.rail-all: the
  // rail then lists every section for whichever mode button is on. The badge always reads "All · 14% · 68/472"; only the
  // tooltip and aria-pressed change (jay: one fixed shape). Kept in
  // sessionStorage so it follows you from page to page; the pages' filter re-applies on 'rail-all-change'.
  var railAll = false; try { railAll = sessionStorage.getItem('rail-all') === '1'; } catch (e) {}
  if (railAll) document.body.classList.add('rail-all');
  var paint = function () {
    if (!cur) return;
    cur.textContent = 'All · ' + pct(done, all) + '% · ' + done + '/' + all;   // one fixed shape (jay, 2026-09-18: "don't change it when being clicked")
    cur.setAttribute('aria-pressed', railAll ? 'true' : 'false');
    cur.style.boxShadow = railAll ? 'inset 0 0 0 2px #ef4444' : '';        // lit like a selected pill (jay: "have meaning of all category")
    cur.title = railAll ? 'All categories — click: back to this section only' : 'All categories — click: show every section in the rail';
  };
  if (cur) {
    cur.classList.remove('rail-note-pink');
    cur.style.color = '#ef4444'; cur.style.background = 'rgba(239,68,68,0.14)'; cur.style.cursor = 'pointer';
    cur.setAttribute('role', 'button'); cur.setAttribute('tabindex', '0');
    var toggle = function () {
      document.body.classList.toggle('rail-all', !railAll);
      try { sessionStorage.setItem('rail-all', !railAll ? '1' : '0'); } catch (e) {}
      document.dispatchEvent(new CustomEvent('rail-all-change'));   // the listener below repaints; the pages' pills listen too
    };
    document.addEventListener('rail-all-change', function () { railAll = document.body.classList.contains('rail-all'); paint(); });
    cur.addEventListener('click', toggle);
    cur.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); } });
    paint();
  }
  // Milestones (jay, 2026-09-18): 1,000 items done is the first turning point and gets a congratulation effect;
  // 2,000 is the final goal. Mirrors GOALS in scripts/notes_numbering.py. (A goal chip next to the badge was
  // removed the same day — jay: "the numbers are shown in order and we don't need this part".)
  var GOALS = [1000, 2000];
  GOALS.forEach(function (g) {
    if (done < g) return;
    var k = 'milestone-' + g; try { if (localStorage.getItem(k)) return; } catch (e) {}
    var wrap = document.createElement('div'); wrap.className = 'milestone';
    wrap.innerHTML = '<div class="milestone-card"><div class="milestone-emoji">' + (g === 1000 ? '🎉' : '🏁') + '</div><h2>' + g.toLocaleString() + ' items done</h2><p>' +
      (g === 1000 ? 'The first turning point. ' + done.toLocaleString() + ' of ' + all.toLocaleString() + ' notes are done — the goal set on 2026-09-18 is reached. Next: 2,000.' : 'The final goal set on 2026-09-18. ' + done.toLocaleString() + ' of ' + all.toLocaleString() + ' notes are done.') +
      '</p><button type="button">Thanks</button></div>';
    for (var i = 0; i < 80; i++) { var c = document.createElement('i'); c.style.cssText = 'left:' + (Math.random() * 100) + 'vw;animation-delay:' + (Math.random() * 3) + 's;animation-duration:' + (3 + Math.random() * 3) + 's;background:' + ['#ef4444', '#eab308', '#22c55e', '#38bdf8', '#191970', '#a855f7'][i % 6] + ';transform:rotate(' + (Math.random() * 360) + 'deg)'; wrap.appendChild(c); }
    var st = document.createElement('style');
    st.textContent = '.milestone{position:fixed;inset:0;z-index:9999;display:flex;align-items:center;justify-content:center;background:rgba(15,23,42,.55);overflow:hidden}' +
      '.milestone-card{position:relative;z-index:1;max-width:420px;margin:16px;padding:28px 30px;border-radius:16px;background:var(--card,#fff);color:var(--text,#0f172a);text-align:center;box-shadow:0 20px 60px rgba(0,0,0,.35)}' +
      '.milestone-card h2{margin:6px 0 10px;font-size:1.6rem}.milestone-card p{margin:0 0 18px;color:var(--text2,#475569)}.milestone-emoji{font-size:3rem}' +
      '.milestone-card button{font:inherit;padding:8px 18px;border-radius:999px;border:1px solid var(--border,#cbd5e1);background:var(--accent,#7c3aed);color:#fff;cursor:pointer}' +
      '.milestone i{position:absolute;top:-12px;width:10px;height:16px;border-radius:2px;opacity:.9;animation:milestone-fall linear infinite}' +
      '@keyframes milestone-fall{to{transform:translateY(105vh) rotate(720deg)}}';
    wrap.appendChild(st); document.body.appendChild(wrap);
    wrap.querySelector('button').addEventListener('click', function () { wrap.remove(); try { localStorage.setItem(k, new Date().toISOString().slice(0, 10)); } catch (e) {} });
  });
  var prev = head.querySelector('.rail-sub .rail-note');
  if (prev) {
    var d = new Date(), today = d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
    var log = (nav.progress || []).filter(function (e) { return e.date < today; });
    if (log.length) {
      var e = log[log.length - 1];
      prev.textContent = pct(e.done, e.all) + '% · ' + e.done + '/' + e.all;
      prev.classList.remove('rail-note-pink'); prev.style.display = 'inline-block';
      prev.title = 'closing status on ' + e.date;
    } else { prev.parentNode.hidden = true; }
  }
})();

// Status overlay loader (jay, 2026-09-21). Appended here rather than added to 776 generated pages:
// every page that shows the rail already loads this file, so this is the one place that reaches all
// of them. `document.currentScript` is this script while it runs synchronously, which gives the
// directory to resolve _status.js against — notes.html loads us as topics/_progress.js and a detail
// page as _progress.js, so a bare relative path would resolve differently on the two.
// Wrapped and silent by design: if this fails the page stays exactly as it was built.
(function () {
  try {
    var me = document.currentScript && document.currentScript.src;
    if (!me) return;
    var s = document.createElement('script');
    s.src = me.replace(/[^/]*$/, '') + '_status.js';
    s.defer = true;
    document.head.appendChild(s);
  } catch (e) { /* the built page is the fallback */ }
})();
