#!/usr/bin/env python3
"""Render the locked Life items (jay, 2026-09-18) from docs/topics/_health.js.

One card + one rail link in docs/notes.html and one detail page docs/topics/health-N.html per tile
label in `window.__HEALTH__.tiles`, numbered 1, 2, 3 … (jay, 2026-09-18: "I want the health number start from 1 not 1000"), titled by the label (Health 1, Health 2 …). The text stays ciphertext; a card or page shows a
password field, decrypts in the browser, and the tab stays unlocked until "Lock all".
Idempotent: notes.html parts sit between <!-- health-nav --> / <!-- health-cards --> markers and the
pages are rewritten whole (stale health-N.html beyond the tile count are removed).
scripts/health-encrypt.mjs runs this after every re-encryption. Health pages are exempt from the
Key-expressions / "Where it lands in Jayverse" rules: their text is not in the repo.
"""
import json, pathlib, re, html, glob, os, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from notes_numbering import display
HN = lambda i: display("health", i + 1)   # Health numbers start at BASE['health'] (1400 → 1401 → 3001 across 2026-09-18/21)
ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs"
TOPICS = ROOT / "topics"
P = json.loads(re.match(r'window\.__HEALTH__=(.*);\s*$', (TOPICS / "_health.js").read_text(), re.S).group(1))
labels = P["tiles"]
E = html.escape
LOCKED = "&#128274; Opens with the password. The text is encrypted in the page data; nothing readable is stored on the site."

# ---------------- notes.html: rail links + cards ----------------
nav = "".join(
    f'        <li><a class="nav-link" href="topics/health-{i+1}.html" data-key="health-{i+1}"><span class="nav-dot" style="background:#94a3b8;" title="LOCKED"></span>'
    f'<span class="nav-text"><span class="topic-no">{HN(i)}</span>{E(l)}</span></a></li>\n' for i, l in enumerate(labels))
cards = "".join(f'''        <li id="health-{i+1}" class="health-item">
          <div class="topic-head"><span class="topic-no">{HN(i)}</span><span class="topic-tag">Locked</span><span class="topic-title">{E(l)}</span></div>
          <p class="topic-summary health-summary">{LOCKED}</p>
          <div class="health-slot"></div>
          <p class="topic-link"><a href="topics/health-{i+1}.html">Detail &rarr;</a> &middot; <button type="button" class="copy-btn copy-inline health-open">Open here</button> &middot; <a href="#top">Top &uarr;</a> &middot; <a href="#sec-mindset">Section top &uarr;</a></p>
        </li>
''' for i, l in enumerate(labels))
NAV = f"        <!-- health-nav:start -->\n{nav}        <!-- health-nav:end -->\n"
CARDS = f"        <!-- health-cards:start -->\n{cards}        <!-- health-cards:end -->\n"
p = ROOT / "notes.html"; s = p.read_text()
def place(s, start, end, block, region_start, region_end):
    a = s.index(region_start); b = s.index(region_end, a)
    if start in s[a:b]:
        i = s.rfind("\n", 0, s.index(start, a)) + 1          # from the start of the marker's line
        j = s.index("\n", s.index(end, i)) + 1                 # to the end of the closing marker's line
        return s[:i] + block + s[j:]
    k = s.rindex("      </ul>\n", a, b)
    return s[:k] + block + s[k:]
s = place(s, "<!-- health-nav:start -->", "<!-- health-nav:end -->", NAV, 'id="nav-sec-mindset"', 'id="no-results"')
s = place(s, "<!-- health-cards:start -->", "<!-- health-cards:end -->", CARDS, '<article id="sec-mindset">', '    <p class="src">')
p.write_text(s)

# ---------------- detail pages: topics/health-N.html ----------------
tpl = (TOPICS / "pocs-eat-the-same-dish-twice-tokyo.html").read_text()
head = tpl[:tpl.index('<div class="solo">') + len('<div class="solo">\n')]
tail = tpl[tpl.index('  </main>\n</div>\n<script src="_nav.js"></script>'):]
CSS = '''  /* Locked Life item (scripts/health-cards.py): ciphertext in _health.js, key from the password in the browser. */
  .health-gate { display:flex; gap:8px; align-items:center; flex-wrap:wrap; margin:8px 0 4px; }
  .health-gate input { font:inherit; padding:8px 10px; border:1px solid var(--border); border-radius:8px; background:var(--card); color:var(--text); min-width:220px; }
  .health-gate button { font:inherit; padding:8px 12px; border:1px solid var(--border); border-radius:8px; background:var(--card); color:var(--text); cursor:pointer; }
  .health-gate .msg { font-size:0.85rem; color:var(--text2); }
  .health-body h2 { margin-top:0; }
  .health-body .lang { font-size:0.78rem; color:var(--accent-2); font-weight:600; letter-spacing:.04em; margin:18px 0 4px; }
  .health-body p { margin:8px 0; }
  .health-body .health-actions { margin-top:14px; }
  .health-body .health-actions button { font:inherit; padding:6px 10px; border:1px solid var(--border); border-radius:8px; background:var(--card); color:var(--text); cursor:pointer; }
'''
NAV_PATCH = '''<script src="_health.js"></script>
<script>
// Rail for a locked item: the Life group plus the Rule links (they are not in _nav.js, so add them in memory here).
(function () {
  var d = window.__NAV__, P = window.__HEALTH__; if (!d || !P) return;
  var s = null; for (var i = 0; i < d.sections.length; i++) if (d.sections[i].navId === 'nav-sec-mindset') s = d.sections[i];
  if (!s || s.items.some(function (it) { return it.key === 'health-1'; })) return;
  var esc = function (t) { return t.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); };
  P.tiles.forEach(function (l, i) { s.items.push({ key: 'health-' + (i + 1), href: 'health-' + (i + 1) + '.html', color: '#94a3b8', label: 'LOCKED', text: '<span class="topic-no">' + (3001 + i) + '</span>' + esc(l) }); });
})();
</script>
'''
PAGE_JS = r'''<script>
(function () {
  // Locked Life item (jay, 2026-09-18). Ciphertext only; the key is derived here from the password.
  var P = window.__HEALTH__, IDX = window.__HEALTH_INDEX__, slot = document.getElementById('health-slot'), status = document.getElementById('health-status');
  if (!slot) return;
  if (!(P && window.crypto && crypto.subtle)) { slot.innerHTML = '<p class="meta">Not available in this browser.</p>'; return; }
  var gate = document.createElement('div'); gate.className = 'health-gate';
  gate.innerHTML = '<input type="password" placeholder="Password" autocomplete="off" aria-label="Password"><button type="button" class="go">Unlock</button><span class="msg"></span>';
  var input = gate.querySelector('input'), go = gate.querySelector('.go'), msg = gate.querySelector('.msg');
  var b64 = function (s) { var b = atob(s), u = new Uint8Array(b.length); for (var i = 0; i < b.length; i++) u[i] = b.charCodeAt(i); return u; };
  var esc = function (t) { return t.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); };
  var paras = function (t) { return t.split(/\n\s*\n/).map(function (x) { return '<p>' + esc(x.trim()).replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>') + '</p>'; }).join(''); };
  function showGate() { slot.innerHTML = ''; slot.appendChild(gate); status.innerHTML = '&#128274; Locked. Enter the password to read this item.'; input.focus(); }
  function render(tiles) {
    var t = tiles[IDX]; if (!t) { slot.innerHTML = '<p class="meta">No text for this item yet.</p>'; return; }
    slot.innerHTML = '<div class="health-body">' + (t.title ? '<h2>' + esc(t.title) + '</h2>' : '') + '<p class="lang">ENGLISH</p>' + paras(t.en) + '<p class="lang">한국어</p>' + paras(t.ko) +
      '<p class="health-actions"><button type="button" class="health-lockall">Lock all</button></p></div>';
    status.innerHTML = '&#128275; Unlocked for this tab.';
  }
  async function unlock(pass) {
    var enc = new TextEncoder();
    var base = await crypto.subtle.importKey('raw', enc.encode(pass), 'PBKDF2', false, ['deriveKey']);
    var key = await crypto.subtle.deriveKey({ name: 'PBKDF2', salt: b64(P.salt), iterations: P.iter, hash: 'SHA-256' }, base, { name: 'AES-GCM', length: 256 }, false, ['decrypt']);
    return JSON.parse(new TextDecoder().decode(await crypto.subtle.decrypt({ name: 'AES-GCM', iv: b64(P.iv) }, key, b64(P.ct))));
  }
  async function tryUnlock(pass, remember) {
    msg.textContent = 'Deriving key…'; go.disabled = true;
    try {
      var tiles = await unlock(pass);
      if (remember) { try { sessionStorage.setItem('life-health-pass', pass); } catch (e) {} }
      input.value = ''; render(tiles);
    } catch (e) { msg.textContent = 'Wrong password.'; if (!gate.parentNode) showGate(); }
    go.disabled = false;
  }
  go.addEventListener('click', function () { if (input.value) tryUnlock(input.value, true); });
  input.addEventListener('keydown', function (e) { if (e.key === 'Enter' && input.value) tryUnlock(input.value, true); });
  slot.addEventListener('click', function (e) { if (e.target.closest('.health-lockall')) { try { sessionStorage.removeItem('life-health-pass'); } catch (x) {} showGate(); } });
  showGate();
  var saved = null; try { saved = sessionStorage.getItem('life-health-pass'); } catch (e) {}
  if (saved) tryUnlock(saved, false);
})();
</script>
'''
n_pages = 0
for i, l in enumerate(labels):
    no = HN(i); key = f"health-{i+1}"; title = E(l)
    h = head.replace(tpl[tpl.index('<title>'):tpl.index('</title>') + 8], f'<title>{title} — Knowledge Notes</title>')
    h = h.replace('</style>', CSS + '</style>', 1)
    prev_ = f'<a href="health-{i}.html">&larr; {HN(i-1)}. {E(labels[i-1])}</a>' if i > 0 else '<a href="../notes.html#sec-mindset">&larr; Life</a>'
    next_ = f'<a href="health-{i+2}.html">{HN(i+1)}. {E(labels[i+1])} &rarr;</a>' if i + 1 < len(labels) else '<a href="../notes.html#sec-mindset">Life &rarr;</a>'
    body = f'''    <p class="crumb"><a href="../index.html">Workspace Index</a> &rsaquo; <a href="../notes.html?list">Knowledge Notes</a> &rsaquo; {title}</p>
  <header class="topic-hero">
      <p class="topic-kicker"><span class="topic-no">#{no}</span><span>Locked</span><span title="section">Life</span></p>
      <h1>{title}</h1>
      <p class="lead" id="health-status">{LOCKED}</p>
    </header>
    <article id="health-article">
      <div id="health-slot"></div>
      <p><a href="../notes.html?list">&larr; All Knowledge Notes</a> &middot; <a href="../index.html">Workspace Index</a> &middot; <a href="#top">Top &uarr;</a></p>
    </article>
    <div class="pager">{prev_}{next_}</div>
  </div>
'''
    t = tail.replace('<script src="_nav.js"></script>\n', '<script src="_nav.js"></script>\n' + NAV_PATCH, 1)
    t = re.sub(r'<script>window\.__NAV_CURRENT__="[^"]*";</script>', f'<script>window.__NAV_CURRENT__="{key}";window.__HEALTH_INDEX__={i};</script>', t, count=1)
    t = t.replace('</body>', PAGE_JS + '</body>', 1)
    (TOPICS / f"{key}.html").write_text(h + body + t); n_pages += 1
for f in glob.glob(str(TOPICS / "health-*.html")):
    m = re.search(r'health-(\d+)\.html$', f)
    if m and int(m.group(1)) > len(labels): os.remove(f); print("removed stale", os.path.basename(f))
print(f"notes.html: {len(labels)} locked Life items (1…{len(labels)}); {n_pages} detail pages topics/health-N.html")
