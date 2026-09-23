// Status overlay (jay, 2026-09-21: "we can put the database only in the cloud … if there is no
// database, it's just the default page", then "go ahead" for the full version).
//
// The built pages stay the truth. When jay is signed in this reads the `status` collection — the
// changes not yet folded back into the repo — and reproduces, in the page, exactly what a rebuild
// would have done: the dot, the rank order, the number, and the counts. Nothing is written back and
// no rebuild is needed; a visitor, or jay signed out, sees the built page untouched.
//
// Why re-rank rather than just recolour: a number here is derived from status rank, so marking one
// item done changes the number of every item after it. Recolouring alone would leave the page
// internally inconsistent — a green dot beside a number that still says "planned".
//
// Everything is wrapped. Any failure (offline, blocked script, rules refusal, no database) leaves the
// page exactly as built. A visitor loads no Firebase at all: the SDK is fetched only after the "Edit"
// link in the rail foot is tapped, or on a device that has signed in before.
(function () {
  'use strict';

  var CONFIG = {
    apiKey: 'AIzaSyDS_cerGsvcrannER-irNx2Y3kGRQ3ybbk',
    authDomain: 'doubletree-498007.firebaseapp.com',
    projectId: 'doubletree-498007',
    appId: '1:179807446244:web:bfa1f0500d173c599538f1'
  };                                   // not a secret: a public identifier. The rules do the guarding.
  var OWNER = 'linked0@gmail.com';
  var SDK = 'https://www.gstatic.com/firebasejs/10.14.1/';
  var OPT_IN = 'alice-status-edit';

  // Mirrors scripts/notes_numbering.py BASE and scripts/reorder-by-status.py RANK. If either moves,
  // this moves with it — the numbers would be wrong rather than merely stale.
  var BASE = { 'nav-sec-blockchain': 1, 'nav-sec-fundamentals': 1001, 'nav-sec-invest': 1501,
               'nav-sec-mindset': 1801, 'nav-sec-english': 2001 };
  var RANK = { 'REVISIT': -1, 'DONE': 0, 'RECENTLY DONE': 0, 'YESTERDAY DONE': 0, 'TODAY DONE': 0,
               'IMPORTANT': 1, 'NEW': 2, 'PLANNED': 3, 'LOCKED': 9 };
  var SET = { planned: ['#64748b', 'PLANNED'], done: ['#22c55e', 'DONE'], recent: ['#0284c7', 'RECENTLY DONE'],
              important: ['#ef4444', 'IMPORTANT'], new: ['#eab308', 'NEW'], revisit: ['#a855f7', 'REVISIT'] };
  var CHOICES = ['done', 'revisit', 'important', 'planned'];

  var nav = window.__NAV__;
  var pending = {};                    // key -> status, the queue as this page last saw it

  function esc(k) { return (window.CSS && CSS.escape) ? CSS.escape(k) : k.replace(/"/g, '\\"'); }
  function byKey(k) { return document.querySelector('a.nav-link[data-key="' + esc(k) + '"]'); }
  function cardOf(k) { var el = document.getElementById(k); return (el && el.tagName === 'LI') ? el : null; }

  function itemForThisPage() {
    if (!nav || !nav.sections) return null;
    var file = location.pathname.split('/').pop();
    for (var i = 0; i < nav.sections.length; i++)
      for (var j = 0; j < nav.sections[i].items.length; j++)
        if (nav.sections[i].items[j].href === file) return nav.sections[i].items[j];
    return null;
  }

  // Move a list of nodes into the given order inside whatever parent they already share. Reordering
  // existing nodes rather than rebuilding the markup keeps the "current page" highlight, any handlers
  // the page attached, and anything else the built page did that this file does not know about.
  function reorder(nodes) {
    var groups = [];
    nodes.forEach(function (n) {
      if (!n) return;
      var g = null;
      for (var i = 0; i < groups.length; i++) if (groups[i].parent === n.parentNode) g = groups[i];
      if (!g) { g = { parent: n.parentNode, list: [] }; groups.push(g); }
      g.list.push(n);
    });
    groups.forEach(function (g) {
      // Only move nodes when the order actually differs. Re-appending a node that is already in place
      // still detaches and reinserts it, and across a 900-item list that reflow is visible as a flash
      // (jay, 2026-09-21: "there's some blinking" going from an Eng card to the Eng list).
      var cur = [], c = g.parent.firstElementChild;
      while (c) { if (g.list.indexOf(c) !== -1) cur.push(c); c = c.nextElementSibling; }
      var same = cur.length === g.list.length;
      if (same) for (var i = 0; i < cur.length; i++) if (cur[i] !== g.list[i]) { same = false; break; }
      if (!same) g.list.forEach(function (n) { g.parent.appendChild(n); });
    });
  }

  // Reproduce a rebuild in the DOM: apply the queue, re-rank each section, renumber, repaint.
  var last = null;                     // the totals we last asserted, for re-asserting after a repaint
  function setBadge(done, all) {
    if (!all) return;
    last = { done: done, all: all };
    if (typeof window.__RAIL_REPAINT__ === 'function') { try { window.__RAIL_REPAINT__(); } catch (e) {} }
    var badge = document.querySelector('.rail-note[title="current"]');
    if (badge) badge.textContent = 'All \u00b7 ' + Math.round(done * 100 / all) + '% \u00b7 ' + done + '/' + all;
  }
  // _progress.js repaints the badge when the all-sections toggle changes. Its listener is registered
  // first, so ours runs after it and has the last word.
  document.addEventListener('rail-all-change', function () { if (last) setBadge(last.done, last.all); });

  var touched = false;                 // has this page ever been repainted by the overlay?
  function apply() {
    if (!nav || !nav.sections) return { changed: 0, pendingCount: 0 };
    var queued = 0; for (var q in pending) if (Object.prototype.hasOwnProperty.call(pending, q)) queued++;
    // The built page already shows the truth when the queue is empty, so the cheapest correct thing
    // is to leave it alone entirely. Without this every sign-in reshuffled a list that was fine.
    if (!queued && !touched) return { changed: 0, pendingCount: 0 };
    touched = queued > 0;
    var pendingCount = 0, changed = 0;
    var totalDone = 0, totalAll = 0;

    nav.sections.forEach(function (sec) {
      var base = BASE[sec.navId];
      sec.items.forEach(function (it) {
        var s = pending[it.key];
        if (s && SET[s] && it.label !== SET[s][1]) { it.color = SET[s][0]; it.label = SET[s][1]; it.overlaid = true; }
        else it.overlaid = !!(s && SET[s] && it.overlaid);
        if (s) pendingCount++;
      });
      // stable sort by rank, exactly what reorder-by-status.py and english-notes.py do
      sec.items.forEach(function (it, i) { it._i = i; });
      sec.items.sort(function (a, b) {
        var ra = RANK[a.label], rb = RANK[b.label];
        if (ra === undefined) ra = 3; if (rb === undefined) rb = 3;
        return ra - rb || a._i - b._i;
      });

      var railNodes = [], cardNodes = [], done = 0;
      sec.items.forEach(function (it, i) {
        var shown = base === undefined ? null : base + i;
        if ((RANK[it.label] !== undefined ? RANK[it.label] : 3) <= 0) done++;
        if (shown !== null && it.text) {
          var t = it.text.replace(/(<span class="topic-no">)\d+(<\/span>)/, '$1' + shown + '$2');
          if (t !== it.text) { it.text = t; }
        }
        var a = byKey(it.key);
        if (a) {
          railNodes.push(a.parentNode && a.parentNode.tagName === 'LI' ? a.parentNode : a);
          var dot = a.querySelector('.nav-dot');
          if (dot) {
            // title must stay the bare label: the rail filters compare it exactly, so a suffix here
            // would quietly drop a queued item out of New/Today/Revisit. The ring shows "queued".
            var title = it.label;
            var ring = it.overlaid ? '2px dotted ' + it.color : '';
            if (dot.style.background !== it.color) { dot.style.background = it.color; changed++; }
            if (dot.title !== title) dot.title = title;
            if (dot.style.outline !== ring) { dot.style.outline = ring; dot.style.outlineOffset = it.overlaid ? '1px' : ''; }
          }
          var no = a.querySelector('.topic-no');
          if (no && shown !== null && no.textContent !== String(shown)) no.textContent = String(shown);
        }
        var card = cardOf(it.key);
        if (card) {
          cardNodes.push(card);
          var cno = card.querySelector('.topic-head .topic-no');
          if (cno && shown !== null && cno.textContent !== String(shown)) cno.textContent = String(shown);
        }
      });
      reorder(railNodes);
      reorder(cardNodes);
      totalDone += done; totalAll += sec.items.length;

      // nav.jump is what the rail badge reads, so update the data and let the badge repaint itself.
      // Writing the badge text here instead would be overwritten by the next repaint, which is how
      // the Eng pill came to say 3 while the badge still said 71 (jay, 2026-09-21).
      if (nav.jump) nav.jump.forEach(function (j) {
        if (j.id === sec.navId.replace('nav-', '')) { j.done = done; j.all = sec.items.length; }
      });
      // per-section counts: the jump pill on notes.html and the heading inside the article
      var pill = document.querySelector('a[data-sec="' + esc(sec.navId) + '"]');
      if (pill) {
        var pd = pill.querySelector('.count-done'), pa = pill.querySelector('.count-all');
        if (pd) pd.textContent = String(done);
        if (pa) pa.textContent = '/' + sec.items.length;
      }
      var art = document.getElementById(sec.navId.replace('nav-', ''));
      if (art) {
        var ad = art.querySelector('.count-done'), aa = art.querySelector('.count-all');
        if (ad) ad.textContent = 'done (' + done + ')';
        if (aa) aa.textContent = ' / all (' + sec.items.length + ')';
      }
    });

    // The rail-head badge. Two things write it and they are cached independently, so neither can be
    // trusted alone: _progress.js owns the text shape and repaints on click, but a browser holding
    // yesterday's copy of that file repaints from totals it captured at load and puts the old number
    // straight back (jay, 2026-09-21: "the total count doesn't change"). So: ask it to repaint from
    // the nav.jump we just updated, then assert the value ourselves regardless, and assert it again
    // after any later repaint. With both files fresh the second write is a no-op.
    setBadge(totalDone, totalAll);

    // and the number printed at the top of the item you are reading
    var cur = itemForThisPage();
    if (cur) {
      var a2 = byKey(cur.key), kick = document.querySelector('.topic-kicker .topic-no');
      if (a2 && kick) {
        var n = a2.querySelector('.topic-no');
        if (n) kick.textContent = '#' + n.textContent;
      }
    }
    return { changed: changed, pendingCount: pendingCount };
  }

  function foot() { return document.querySelector('.rail-foot'); }

  // Where the control bar goes. A detail page has a hero with the English/한국어 pills, and that is
  // where jay reads from, so the bar belongs there (jay, 2026-09-22: "how about the edit button on the
  // top part of detail page besides 한국어"). notes.html has no hero, so it keeps the rail foot.
  function heroSwitch() { return document.querySelector('.topic-hero .lang-switch'); }
  function host() { return heroSwitch() || foot(); }

  // Why the sign-in failed, in words that say what to do next. Measured 2026-09-22 with real Chrome:
  // from http://localhost:PORT the popup opens; from http://127.0.0.1:PORT and from a file:// page
  // Firebase returns the *same* auth/unauthorized-domain for two different reasons — 127.0.0.1 was
  // merely missing from the authorized list, while file:// can never work at all — the SDK requires an
  // http(s) origin. One code, two causes, which is why reading the bare code was no help. Since
  // 2026-09-22 localhost, 127.0.0.1 and jay's Tailscale address are all authorized, so the remaining
  // way to hit this is an origin nobody has added — which is what the message names.
  function explain(e) {
    var code = (e && e.code) || String(e);
    if (location.protocol === 'file:')
      return 'sign-in needs an http page — run scripts/serve.sh and open it on http://localhost:4173';
    if (code === 'auth/unauthorized-domain')
      return location.hostname + ' is not an authorized domain — add it in Firebase Auth → Settings, or use localhost / the Tailscale address';
    if (code === 'auth/popup-blocked')
      return 'the browser blocked the Google window — allow popups for this page, then try again';
    if (code === 'auth/popup-closed-by-user')
      return 'the Google window closed before sign-in finished';
    return code;
  }
  function say(msg, tone) {
    var el = document.getElementById('alice-status-msg');
    if (!el) return;
    el.textContent = msg;
    el.style.color = tone === 'bad' ? '#ef4444' : 'var(--text2, #64748b)';
  }
  function button(label, fn) {
    var b = document.createElement('button');
    b.type = 'button'; b.textContent = label;
    b.style.cssText = 'font:inherit;cursor:pointer;border:1px solid currentColor;border-radius:999px;' +
                      'padding:1px 9px;background:transparent;color:var(--text2,#64748b)';
    b.addEventListener('click', fn);
    return b;
  }

  var fb = null;
  function load() {
    if (fb) return fb;
    fb = Promise.all([
      import(SDK + 'firebase-app.js'), import(SDK + 'firebase-auth.js'), import(SDK + 'firebase-firestore.js')
    ]).then(function (m) {
      var app = m[0].initializeApp(CONFIG);
      return { auth: m[1], fs: m[2], a: m[1].getAuth(app), db: m[2].getFirestore(app) };
    });
    return fb;
  }

  function pull(k) {
    return k.fs.getDocs(k.fs.collection(k.db, 'status')).then(function (snap) {
      pending = {};
      snap.forEach(function (d) { var v = d.data() || {}; if (SET[v.status]) pending[d.id] = v.status; });
      return apply();
    });
  }

  function render(k, user) {
    var h = host(); if (!h) return;
    var bar = document.getElementById('alice-status-bar');
    if (!bar) {
      bar = document.createElement('div');
      bar.id = 'alice-status-bar';
      var inHero = h === heroSwitch();
      bar.style.cssText = 'margin-top:' + (inHero ? '10px' : '8px') + ';font-size:' + (inHero ? '.78rem' : '.72rem') +
                          ';line-height:1.9;display:flex;flex-wrap:wrap;gap:6px;align-items:center';
      h.parentNode.insertBefore(bar, h.nextSibling);
    }
    bar.textContent = '';
    var msg = document.createElement('span');
    msg.id = 'alice-status-msg';
    msg.style.cssText = 'flex:1 1 100%;color:var(--text2,#64748b)';

    if (!user) {
      bar.appendChild(button('Sign in', function () {
        say('opening Google…');
        k.auth.signInWithPopup(k.a, new k.auth.GoogleAuthProvider())
          .catch(function (e) { say(explain(e), 'bad'); });
      }));
      bar.appendChild(msg); say('sign in to change status from here');
      return;
    }
    if (user.email !== OWNER) {
      bar.appendChild(msg); say('signed in as ' + user.email + ' — not the owner', 'bad');
      return;
    }

    var item = itemForThisPage();
    if (item) CHOICES.forEach(function (s) {
      bar.appendChild(button(s, function () {
        say('saving ' + s + '…');
        k.fs.setDoc(k.fs.doc(k.db, 'status', item.key), { status: s, at: k.fs.serverTimestamp() })
          .then(function () { pending[item.key] = s; var r = apply(); say('queued ' + s + ' — ' + r.pendingCount + ' pending'); })
          .catch(function (e) { say(explain(e), 'bad'); });
      }));
    });
    // Re-reads the queue from the database and re-applies it to this page. It has nothing to do with
    // repeats (jay asked, 2026-09-23) — it is for when a status was changed on another device and this
    // tab still shows the state it loaded with. Labelled for what it reads, because "refresh" invited
    // exactly that question.
    var rb = button('re-read db', function () { say('reading…'); pull(k).then(function (r) { say(r.pendingCount + ' pending'); }); });
    rb.title = 'read the pending changes from the database again — for when you changed something on another device';
    bar.appendChild(rb);
    bar.appendChild(button('sign out', function () { k.auth.signOut(k.a); }));
    bar.appendChild(msg);
    pull(k).then(function (r) {
      say(r.pendingCount ? r.pendingCount + ' change(s) pending a rebuild — order and numbers shown live'
                         : 'signed in — no pending changes');
    }).catch(function (e) { say('overlay unavailable: ' + ((e && e.code) || e), 'bad'); });
  }

  function start() {
    load().then(function (k) {
      try { localStorage.setItem(OPT_IN, '1'); } catch (e) {}
      k.auth.onAuthStateChanged(k.a, function (user) { render(k, user); });
    }).catch(function (e) {
      say('sign-in unavailable', 'bad');
      if (window.console) console.warn('alice status overlay: SDK failed to load', e);
    });
  }

  function init() {
    if (!host()) return;
    var opted = false;
    try { opted = localStorage.getItem(OPT_IN) === '1'; } catch (e) {}
    if (opted || location.hash === '#edit') { start(); return; }
    // Two ways in, one bar. The hero pill inherits .lang-switch a, so it is the same shape as the
    // English/한국어 pills it sits next to and needs no CSS of its own in 776 generated pages.
    var sw = heroSwitch();
    if (sw) {
      var pill = document.createElement('a');
      pill.href = '#edit'; pill.textContent = 'Edit'; pill.id = 'alice-edit-pill';
      pill.addEventListener('click', function (ev) { ev.preventDefault(); pill.remove(); start(); });
      sw.appendChild(pill);
    }
    var f = foot();
    if (f) {
      f.appendChild(document.createTextNode(' · '));
      var a = document.createElement('a');
      a.href = '#edit'; a.textContent = 'Edit';
      a.addEventListener('click', function (ev) {
        ev.preventDefault();
        var p = document.getElementById('alice-edit-pill'); if (p) p.remove();
        start();
      });
      f.appendChild(a);
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
