// Rail-head progress badges (jay, 2026-09-16): the top badge is the CURRENT status in red;
// the line under it is the PREVIOUS DAY's closing status in blue (replacing the old pink
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
  if (cur) {
    cur.textContent = pct(done, all) + '% done · ' + done + '/' + all;
    cur.classList.remove('rail-note-pink');
    cur.style.color = '#ef4444'; cur.style.background = 'rgba(239,68,68,0.14)';
    cur.title = 'current';
  }
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
