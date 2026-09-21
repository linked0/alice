// Status overlay (jay, 2026-09-21: "we can put the database only in the cloud … if there is no
// database, it's just the default page").
//
// The built pages are the truth. This file is an accelerator on top of them: when jay is signed in it
// reads the `status` collection — the changes not yet folded back into the repo — and repaints the
// dots, and it lets him set a new status from the item he is reading. Everything here is wrapped so
// that any failure (offline, blocked script, rules refusal, no database at all) leaves the page
// exactly as it was built. A visitor loads no Firebase at all: the SDK is only fetched after the
// "Edit" link in the rail foot is tapped, or on a device that has signed in before.
//
// The queue is drained by .github/workflows/drain-status.yml, which applies each pending change with
// scripts/set-status.py, commits, and deletes the drained documents. After a drain the overlay is
// empty and the built page is correct on its own again.
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
  var OPT_IN = 'alice-status-edit';    // per-device: this browser has signed in before
  var COLORS = {
    planned: ['#64748b', 'PLANNED'], done: ['#22c55e', 'DONE'], recent: ['#191970', 'TODAY DONE'],
    important: ['#ef4444', 'IMPORTANT'], new: ['#eab308', 'NEW'], revisit: ['#a855f7', 'REVISIT']
  };

  function itemForThisPage() {
    var nav = window.__NAV__;
    if (!nav || !nav.sections) return null;
    var file = location.pathname.split('/').pop();
    for (var i = 0; i < nav.sections.length; i++) {
      var items = nav.sections[i].items;
      for (var j = 0; j < items.length; j++) if (items[j].href === file) return items[j];
    }
    return null;                        // notes.html and the index: overlay only, no buttons
  }

  // Repaint one rail dot. The number beside it is baked into the page and only settles after a
  // drain, so the dot is marked as pending rather than pretending the change is complete.
  function paint(key, status) {
    var c = COLORS[status];
    if (!c) return;
    var dots = document.querySelectorAll('a[data-key="' + (window.CSS && CSS.escape ? CSS.escape(key) : key) + '"] .nav-dot');
    for (var i = 0; i < dots.length; i++) {
      dots[i].style.background = c[0];
      dots[i].title = c[1] + ' (pending — the number settles at the next rebuild)';
      dots[i].style.outline = '2px dotted ' + c[0];
      dots[i].style.outlineOffset = '1px';
    }
  }

  function foot() { return document.querySelector('.rail-foot'); }

  function say(msg, tone) {
    var el = document.getElementById('alice-status-msg');
    if (!el) return;
    el.textContent = msg;
    el.style.color = tone === 'bad' ? '#ef4444' : 'var(--text2, #64748b)';
  }

  var fb = null;
  function load() {                     // one lazy load of the SDK, shared by every caller
    if (fb) return fb;
    fb = Promise.all([
      import(SDK + 'firebase-app.js'),
      import(SDK + 'firebase-auth.js'),
      import(SDK + 'firebase-firestore.js')
    ]).then(function (m) {
      var app = m[0].initializeApp(CONFIG);
      return { auth: m[1], fs: m[2], a: m[1].getAuth(app), db: m[2].getFirestore(app) };
    });
    return fb;
  }

  function overlay(k) {                 // apply every pending change to the dots on this page
    return k.fs.getDocs(k.fs.collection(k.db, 'status')).then(function (snap) {
      var n = 0;
      snap.forEach(function (d) { paint(d.id, (d.data() || {}).status); n++; });
      return n;
    });
  }

  function render(k, user) {
    var f = foot();
    if (!f) return;
    var bar = document.getElementById('alice-status-bar');
    if (!bar) {
      bar = document.createElement('div');
      bar.id = 'alice-status-bar';
      bar.style.cssText = 'margin-top:8px;font-size:.72rem;line-height:1.9;display:flex;flex-wrap:wrap;gap:6px;align-items:center';
      f.parentNode.insertBefore(bar, f.nextSibling);
    }
    bar.textContent = '';
    var msg = document.createElement('span');
    msg.id = 'alice-status-msg';
    msg.style.cssText = 'flex:1 1 100%;color:var(--text2,#64748b)';

    if (!user) {
      var inBtn = button('Sign in', function () {
        say('opening Google…');
        k.auth.signInWithPopup(k.a, new k.auth.GoogleAuthProvider()).catch(function (e) {
          say(String(e && e.code || e), 'bad');
        });
      });
      bar.appendChild(inBtn); bar.appendChild(msg);
      say('sign in to change status from here');
      return;
    }
    if (user.email !== OWNER) {
      bar.appendChild(msg); say('signed in as ' + user.email + ' — not the owner', 'bad');
      return;
    }

    var item = itemForThisPage();
    if (item) {
      ['done', 'revisit', 'important', 'planned'].forEach(function (s) {
        bar.appendChild(button(s, function () {
          say('saving ' + s + '…');
          k.fs.setDoc(k.fs.doc(k.db, 'status', item.key), { status: s, at: k.fs.serverTimestamp() })
            .then(function () { paint(item.key, s); say('queued ' + s + ' — the rebuild will fold it in'); })
            .catch(function (e) { say(String(e && e.code || e), 'bad'); });
        }));
      });
    }
    bar.appendChild(button('sign out', function () { k.auth.signOut(k.a); }));
    bar.appendChild(msg);
    overlay(k).then(function (n) {
      say(item ? (n ? n + ' change(s) pending a rebuild' : 'no pending changes')
               : (n ? n + ' change(s) pending a rebuild' : 'signed in — no pending changes'));
    }).catch(function (e) { say('overlay unavailable: ' + (e && e.code || e), 'bad'); });
  }

  function button(label, fn) {
    var b = document.createElement('button');
    b.type = 'button'; b.textContent = label;
    b.style.cssText = 'font:inherit;cursor:pointer;border:1px solid currentColor;border-radius:999px;' +
                      'padding:1px 9px;background:transparent;color:var(--text2,#64748b)';
    b.addEventListener('click', fn);
    return b;
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
    var f = foot();
    if (!f) return;                     // a page without the rail: nothing to attach to, leave it alone
    var opted = false;
    try { opted = localStorage.getItem(OPT_IN) === '1'; } catch (e) {}
    if (opted || location.hash === '#edit') { start(); return; }
    // Not opted in: one small link in the same style as the rest of the foot. No SDK is fetched, so a
    // visitor pays nothing for a feature that is not theirs.
    f.appendChild(document.createTextNode(' · '));
    var a = document.createElement('a');
    a.href = '#edit'; a.textContent = 'Edit';
    a.addEventListener('click', function (ev) { ev.preventDefault(); start(); });
    f.appendChild(a);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
