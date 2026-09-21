#!/usr/bin/env python3
"""Build the "English" section of Knowledge Notes from docs/topics/english/english-N.md.

Idempotent: run it after adding or editing any english-N.md and it rewrites
  - docs/notes.html      : the nav group, the section article, the rail pill, the overall badge
  - docs/topics/_nav.js  : the jump entry and the section entry
  - docs/topics/english-N.html : one detail page per conversation (kicker + pager rebuilt)
  - docs/topics/pocs-*.html    : only the static overall badge text (N/M), so every page agrees

Source format (docs/topics/english/english-N.md):
  # N · Tag — Title
  title_ko: …            situation: …   situation_ko: …   why: …   why_ko: …
  status: planned | done | recent | important | new | revisit      (default planned; revisit = done, come back later — jay, 2026-09-21)
  source: …   source_ko: …   raw: <file in docs/topics/raw/>   (optional; a conversation written from an
              outside text cites it at the end of both articles and links its raw copy — jay, 2026-09-21)
  done: 2026-09-18T15:08+09:00   (ISO +09:00, when status is recent/done; drives the TODAY/YESTERDAY DONE roll)
  ## Dialogue            Speaker: English line   /  > Korean line (directly under it)
  ## Techniques          1. **제목.** 설명 (Korean, quoting the English)
  ## Expressions         | english | 한국어 |

Rules (jay, 2026-09-16): numbering is chronological and append-only — no reordering by status.
Every time a Knowledge Notes item is added, one conversation is added here too; it need not relate to
the item. From #21 on, conversations target landing a developer / team-lead job abroad —
interviews, negotiation, leading a team in English — critical and concrete.
"""
import re, json, html, pathlib, glob, sys
from notes_numbering import display
shown = lambda x: display("nav-sec-english", x["n"])   # English numbers start at 1000 (jay, 2026-09-18); files stay english-N.md

ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs"
SRC = ROOT / "topics" / "english"
NOTES = ROOT / "notes.html"
NAVJS = ROOT / "topics" / "_nav.js"
TEMPLATE = ROOT / "topics" / "pocs-alchemy-app-is-a-budget.html"
SECTION_ID, NAV_ID, LABEL = "sec-english", "nav-sec-english", "Eng"   # label shortened (jay, 2026-09-18: "English to Eng"); ids unchanged
COLORS = {"planned": ("#64748b", "PLANNED"), "done": ("#22c55e", "DONE"), "recent": ("#191970", "TODAY DONE"),
          "important": ("#ef4444", "IMPORTANT"), "new": ("#eab308", "NEW"), "revisit": ("#a855f7", "REVISIT")}
E = lambda s: html.escape(s, quote=False).replace("'", "&#39;")

def inline(t):
    t = E(t); t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t); t = re.sub(r'`(.+?)`', r'<code>\1</code>', t)
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)

def parse(path):
    text = path.read_text(); lines = text.split("\n")
    m = re.match(r'# (\d+) · ([^—]+?) — (.+)$', lines[0]); assert m, path
    it = {"n": int(m.group(1)), "tag": m.group(2).strip(), "title": m.group(3).strip(), "status": "planned", "src": text}
    i = 1
    while i < len(lines) and lines[i].strip() and not lines[i].startswith("## "):
        k, _, v = lines[i].partition(":"); it[k.strip()] = v.strip(); i += 1
    sec = None; it["dialogue"] = []; it["techniques"] = []; it["expressions"] = []
    for l in lines[i:]:
        if l.startswith("## "): sec = l[3:].strip().lower(); continue
        if not l.strip(): continue
        if sec == "dialogue":
            if l.startswith("> "): it["dialogue"][-1]["ko"] = l[2:].strip()
            else:
                sp, _, en = l.partition(":"); it["dialogue"].append({"who": sp.strip(), "en": en.strip(), "ko": ""})
        elif sec == "techniques":
            it["techniques"].append(re.sub(r'^\d+\.\s*', '', l))
        elif sec == "expressions":
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            if len(cells) >= 2: it["expressions"].append(cells[:2])
    for k in ("title_ko", "situation", "situation_ko", "why", "why_ko"): assert k in it, (path, k)
    return it

items = sorted((parse(pathlib.Path(p)) for p in glob.glob(str(SRC / "english-*.md"))), key=lambda x: x["n"])
assert [x["n"] for x in items] == list(range(1, len(items) + 1)), "english-N.md numbering must be 1..N without gaps"
N = len(items); DONE = sum(1 for x in items if x["status"] in ("done", "recent", "revisit"))
key = lambda x: f"english-{x['n']}"; href = lambda x: f"english-{x['n']}.html"

# ---------------- detail pages ----------------
tpl = TEMPLATE.read_text()
head = tpl[:tpl.index('<div class="solo">') + len('<div class="solo">\n')]
tail = tpl[tpl.index('  </div>\n  </main>\n</div>\n<script src="_nav.js">'):]
for idx, it in enumerate(items):
    # English and Korean in separate articles, like the PoC pages (jay, 2026-09-18: "separate english and korean
    # parts as others so that I don't read the translation first").
    dlg = "\n".join(f'<p><strong>{E(d["who"])}:</strong> {inline(d["en"])}</p>' for d in it["dialogue"])
    dlg_ko = "\n".join(f'<p><strong>{E(d["who"])}:</strong> {E(d["ko"])}</p>' for d in it["dialogue"])
    SWITCH = lambda on: f'<nav class="lang-switch" aria-label="Language"><a href="#en"{" class=\"on\"" if on == "en" else ""}>English</a><a href="#ko"{" class=\"on\"" if on == "ko" else ""}>한국어</a></nav>'
    tech = "<ol>" + "".join(f"<li>{inline(t)}</li>" for t in it["techniques"]) + "</ol>"
    # optional source layer (jay, 2026-09-21: "add the source of the item in detail"). A conversation
    # written from an outside text cites it in full at the end of both articles, and links the raw copy
    # under docs/topics/raw/ so the source can be reopened instead of re-remembered (raw/README.md).
    rawlink = f'raw/{E(it["raw"])}' if it.get("raw") else ""
    raw_span = f'<span title="raw"><a href="{rawlink}">raw</a></span>' if rawlink else ""
    def source_block(k, h):
        if not it.get(k): return ""
        tail = f' &middot; <a href="{rawlink}">raw</a>' if rawlink else ""
        return f'<h2>{h}</h2>\n<p class="meta">{inline(it[k])}{tail}</p>\n'
    expr = ('<table><thead><tr><th>Expression</th><th>뜻 · 쓰이는 자리</th></tr></thead><tbody>'
            + "".join(f"<tr><td><strong>{inline(a)}</strong></td><td>{inline(b)}</td></tr>" for a, b in it["expressions"]) + "</tbody></table>")
    prev = items[idx - 1] if idx > 0 else None; nxt = items[idx + 1] if idx + 1 < N else None
    pager = ('<div class="pager">' + (f'<a href="{href(prev)}">&larr; {shown(prev)}. {E(prev["title"])}</a>' if prev else '')
             + (f'<a href="{href(nxt)}">{shown(nxt)}. {E(nxt["title"])} &rarr;</a>' if nxt else '') + '</div>')
    page_head = head.replace(tpl[tpl.index('<title>'):tpl.index('</title>') + 8], f'<title>{E(it["title"])} — {LABEL} — Knowledge Notes</title>')
    page_tail = re.sub(r'window\.__NAV_CURRENT__="[^"]*"', f'window.__NAV_CURRENT__="{key(it)}"', tail)
    mid = f'''    <p class="crumb"><a href="../index.html">Workspace Index</a> &rsaquo; <a href="../notes.html">Knowledge Notes</a> &rsaquo; <a href="../notes.html#{SECTION_ID}">{LABEL}</a> &rsaquo; {E(it["title"])}</p>
  <header class="topic-hero">
      <p class="topic-kicker"><span class="topic-no">#{shown(it)}</span><span>{E(it["tag"])}</span>{raw_span}</p>
      <h1>{E(it["title"])}</h1>
      <p class="lead">{E(it["situation"])}</p>
      {SWITCH(None)}
    </header>
    <article id="en">
      {SWITCH("en")}
      <p class="copy-row"><button type="button" class="copy-btn" data-copy="copy-en" data-done="Copied &#10003;">Copy source</button></p>
      <script type="application/json" id="copy-en">{json.dumps(it["src"], ensure_ascii=False)}</script>
<h2>Why this conversation</h2>
<p>{inline(it["why"])}</p>
<h2>Dialogue</h2>
{dlg}
<h2>Key expressions</h2>
{expr}
{source_block("source", "Source")}      <p><a href="../notes.html#{SECTION_ID}">&larr; English</a> &middot; <a href="../notes.html?list">All Notes</a> &middot; <a href="#top">Top &uarr;</a></p>
    </article>
    <article id="ko" lang="ko">
      {SWITCH("ko")}
      <h1>{E(it["title_ko"])}</h1>
      <p class="lead">{E(it["situation_ko"])}</p>
<h2>왜 이 대화인가</h2>
<p>{E(it["why_ko"])}</p>
<h2>대화</h2>
{dlg_ko}
<h2>협업 기법 세 가지</h2>
{tech}
{source_block("source_ko", "출처")}      <p><a href="../notes.html#{SECTION_ID}">&larr; English</a> &middot; <a href="../notes.html?list">전체 노트</a> &middot; <a href="#top">맨 위 &uarr;</a></p>
    </article>
    {pager}
'''
    (ROOT / "topics" / href(it)).write_text(page_head + mid + page_tail)

# ---------------- notes.html ----------------
s = NOTES.read_text()
# remove a previous build of the section (idempotent)
s = re.sub(rf'      <div class="nav-group" id="{NAV_ID}" data-group>.*?      </div>\n', '', s, flags=re.S)
s = re.sub(rf'    <article id="{SECTION_ID}">.*?    </article>\n', '', s, flags=re.S)
s = re.sub(rf'<a href="#{SECTION_ID}"(?: data-sec="[^"]*")? title="[^"]*">.*?</a>', '', s, flags=re.S)   # pills carry data-sec since 2026-09-18

nav_lis = "".join(
    f'        <li><a class="nav-link" href="topics/{href(x)}" data-key="{key(x)}"><span class="nav-dot" style="background:{COLORS[x["status"]][0]};" title="{COLORS[x["status"]][1]}"></span>'
    f'<span class="nav-text"><span class="topic-no">{shown(x)}</span><span class="topic-tag">{E(x["tag"])}</span>{E(x["title"])}</span></a></li>\n' for x in items)
nav_group = f'      <div class="nav-group" id="{NAV_ID}" data-group>\n        <p class="nav-group-label">{LABEL} ({N})</p>\n        <ul>\n{nav_lis}        </ul>\n      </div>\n'
anchor = '      <div class="nav-group" id="nav-sec-mindset" data-group>'   # Eng sits before Life (jay, 2026-09-18)
assert s.count(anchor) == 1; s = s.replace(anchor, nav_group + anchor)

def card(x):
    tech_titles = " · ".join(re.sub(r'\*\*(.+?)\*\*.*', r'\1', t).rstrip(".") for t in x["techniques"])
    first = x["dialogue"][0]
    return f'''        <li id="{key(x)}">
          <div class="topic-head"><span class="topic-no">{shown(x)}</span><span class="topic-tag">{E(x["tag"])}</span><span class="topic-title">{E(x["title"])}</span></div>
          <p class="topic-summary">{E(x["situation"])} <span style="opacity:.7">— {E(x["situation_ko"])}</span></p>
          <p class="topic-how"><strong>Opens with</strong>{E(first["who"])}: &ldquo;{inline(first["en"])}&rdquo; &middot; {len(x["dialogue"])} lines &middot; {E(tech_titles)}</p>
          <p class="topic-why"><strong>Why</strong>{inline(x["why"])}</p>
          <p class="topic-link"><a href="topics/{href(x)}">Detail &rarr;</a> &middot; <a href="#top">Top &uarr;</a> &middot; <a href="#{SECTION_ID}">Section top &uarr;</a></p>
        </li>
'''
article = f'''    <article id="{SECTION_ID}">
      <h1>{LABEL}</h1>
      <p class="lead">Developer conversations in English &mdash; code review, design decisions, incidents, EIP discussions, business development, ops, and one-on-ones &mdash; each line with its Korean, three collaboration techniques, and the expressions worth keeping. Numbered in the order they were written; from #21 on they are the conversations a developer and team lead needs to land a job abroad.</p>
      <p class="meta"><span class="count-done">done ({DONE})</span> <span class="count-all">/ all ({N})</span></p>
      <ul class="topics">
{"".join(card(x) for x in items)}      </ul>
    </article>
'''
anchor2 = '    <article id="sec-mindset">'
assert s.count(anchor2) == 1; s = s.replace(anchor2, article + anchor2)

pill = f'<a href="#{SECTION_ID}" data-sec="{NAV_ID}" title="{LABEL} &mdash; done ({DONE}) / all ({N})">{LABEL}<b><span class="count-done">{DONE}</span><span class="count-all">/{N}</span></b></a>'
s = s.replace('<a href="#sec-mindset" data-sec="nav-sec-mindset"', pill + '<a href="#sec-mindset" data-sec="nav-sec-mindset"', 1)   # before the Life pill

# overall badge = sum of every rail pill
pills = re.findall(r'<span class="count-done">(\d+)</span><span class="count-all">/(\d+)</span>', s[s.index('<div class="rail-jump">'):s.index('</div>', s.index('<div class="rail-jump">'))])
tot_done = sum(int(a) for a, _ in pills); tot_all = sum(int(b) for _, b in pills)
badge = f'{round(tot_done * 100 / tot_all)}% &middot; {tot_done}/{tot_all}'
s, n_badge = re.subn(r'(<span class="rail-note"[^>]*title="current">)[^<]*(</span>)', lambda m: m.group(1) + badge + m.group(2), s, count=1)
assert n_badge == 1
NOTES.write_text(s)

# ---------------- _nav.js ----------------
t = NAVJS.read_text(); m = re.match(r'window\.__NAV__=(.*);\s*$', t, re.S); nav = json.loads(m.group(1))
nav["jump"] = [j for j in nav["jump"] if j["id"] != SECTION_ID]; nav["jump"].insert(next(i for i, j in enumerate(nav["jump"]) if j["id"] == "sec-mindset"), {"id": SECTION_ID, "label": LABEL, "all": N, "done": DONE})
nav["sections"] = [sec for sec in nav["sections"] if sec["navId"] != NAV_ID]; nav["sections"].insert(next(i for i, sec in enumerate(nav["sections"]) if sec["navId"] == "nav-sec-mindset"), {
    "navId": NAV_ID, "label": f"{LABEL} ({N})",
    "items": [{"key": key(x), "href": href(x), "color": COLORS[x["status"]][0], "label": COLORS[x["status"]][1],
               "text": f'<span class="topic-no">{shown(x)}</span><span class="topic-tag">{E(x["tag"])}</span>{E(x["title"])}',
               **({"done": x["done"]} if x.get("done") else {})} for x in items]})
NAVJS.write_text("window.__NAV__=" + json.dumps(nav, ensure_ascii=False, separators=(",", ":")) + ";\n")

# ---------------- static overall badge on every topic page ----------------
changed = 0
for f in glob.glob(str(ROOT / "topics" / "*.html")):
    p = pathlib.Path(f); c = p.read_text()
    c2 = re.sub(r'(<span class="rail-note"[^>]*title="current">)[^<]*(</span>)', lambda m: m.group(1) + badge + m.group(2), c, count=1)
    if c2 != c: p.write_text(c2); changed += 1

print(f"{LABEL}: {N} items ({DONE} done) → notes.html section + nav + pill; _nav.js; {N} detail pages; overall badge '{badge}' on {changed} topic pages")

# TODAY DONE / YESTERDAY DONE roll (scripts/roll-done-states.py): stamped items bucket by 06:00 KST day; rail dots synced.
import subprocess
subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve().parent / "roll-done-states.py")], check=True)
# rebuild docs/topics/index.json + index.md (scripts/build-index.py; jay, 2026-09-21: "Let the system hold the index")
import subprocess, sys
subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve().parent / "build-index.py")], check=True)
# order by status last (NEW expires after a week there; jay, 2026-09-21)
subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve().parent / "reorder-by-status.py")], check=True)
