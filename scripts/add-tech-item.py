#!/usr/bin/env python3
"""Insert or update one Tech (or, with --section, Theory / Life) item in Knowledge Notes from two markdown files.

    python3 scripts/add-tech-item.py --key <key> --slot <N> --en <en.md> --ko <ko.md> \
        [--status new|important|planned|recent|done|revisit] [--date YYYY-MM-DD] [--type PoC] [--source chat|file]

Source markdown (both languages, same shape):
    # Title
    <blank>
    Summary paragraph                     -> card summary, page lead
    <blank>
    Meta paragraph                        -> page meta (status line, "for Jayverse" line)
    <blank>
    ## Why … ## How it works … ### … (tables, ordered lists, code fences, **bold**, `code`, links)

What it does (docs/, hand-maintained HTML):
    notes.html   nav entry + card at #slot, later items shift by one, section/rail counters
    topics/_nav.js  entry at #slot, renumbering, label/jump counts
    topics/pocs-<key>.html  detail page from the Alchemy page template (EN + KO, copy JSON)
    every Blockchain page: #N kicker and prev/next pager rebuilt
Rules: done items first — a new report takes the first not-done slot (pass it as --slot);
the added date (KST) shows on the card head and in the page kicker (jay, 2026-09-16).
Re-running with an existing key replaces that item in place (slot argument ignored).
"""
import re, json, pathlib, html, argparse, datetime, glob, sys, subprocess
from notes_numbering import display, position  # section bases: Tech 1, Theory 700, Life 1300 (jay, 2026-09-18)

ap = argparse.ArgumentParser()
ap.add_argument("--key", required=True); ap.add_argument("--slot", type=int, help="1-based position inside the section; the shown number is the section base + slot - 1 (Tech 1, Theory 700, Life 1300)")
ap.add_argument("--en", required=True); ap.add_argument("--ko", required=True)
ap.add_argument("--status", default="new", help="planned | done | recent (= today: TODAY DONE, midnight blue until the next day's first done item, then YESTERDAY DONE, then DONE) | important | new | revisit (= done, come back later; purple, sorts before DONE, counts as done; jay, 2026-09-21)");
ap.add_argument("--done-at", help="ISO time (+09:00) the item was done; default now (KST). Day boundary 06:00 KST — see scripts/roll-done-states.py"); ap.add_argument("--date"); ap.add_argument("--type", default="PoC")
ap.add_argument("--source", default="chat", choices=["chat", "file", "gemini"], help="where the subject came from: jay in chat, the alice-tech file, or the Gemini YouTube briefing folder (~/Documents/Gemini)")
ap.add_argument("--section", default="blockchain", choices=["blockchain", "fundamentals", "invest", "mindset"], help="which Knowledge Notes section the item belongs to")
ap.add_argument("--tag", default="Economics", help="Theory / Invest: the topic-tag chip (Theory: Math | Algorithms; Invest: Economics | Invest)")
ap.add_argument("--vocab", help="markdown table of key expressions (Expression | 뜻 · 쓰이는 자리); copied to docs/topics/vocab/<page>.md and rendered on the page (jay, 2026-09-18: every detail page carries one)")
ap.add_argument("--bin", choices=["deep", "converse", "file"], help="learning bin at capture time (learning-greed item, jay 2026-09-21): deep = moves the through line, gets the hours; converse = one interview sentence, no more; file = card + expressions, then release")
ap.add_argument("--raw", help="source file (paste, fetched text, briefing) copied once into docs/topics/raw/<date>-<key>.<ext> and linked from the kicker; never overwritten")
ap.add_argument("--sentence", help="with --bin converse: the one sentence you could say in an interview; appended to docs/topics/interview-bank.md")
A = ap.parse_args()
ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs"
COLORS = {"planned": ("#64748b", "PLANNED"), "done": ("#22c55e", "DONE"), "recent": ("#191970", "TODAY DONE"), "lately": ("#191970", "TODAY DONE"), "today": ("#191970", "TODAY DONE"),
          "important": ("#ef4444", "IMPORTANT"), "new": ("#eab308", "NEW"), "revisit": ("#a855f7", "REVISIT")}
COLOR, LABEL = COLORS[A.status]
DATE = A.date or datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d")
# Section constants. Blockchain has no tag chip; Theory cards carry <span class="topic-tag">Math|Algorithms|Economics</span>
# right after the number (jay, 2026-09-18: first Theory item added through this script).
SECTIONS = {
    "blockchain":   dict(nav="nav-sec-blockchain",   art="sec-blockchain",   label="Tech", next_nav="nav-sec-fundamentals", next_art="sec-fundamentals", tag=""),
    "fundamentals": dict(nav="nav-sec-fundamentals", art="sec-fundamentals", label="Theory",         next_nav="nav-sec-invest",       next_art="sec-invest",        tag=f'<span class="topic-tag">{A.tag}</span>'),
    "invest":       dict(nav="nav-sec-invest",       art="sec-invest",       label="Invest",         next_nav="nav-sec-english",      next_art="sec-english",       tag=f'<span class="topic-tag">{A.tag}</span>'),
    "mindset":      dict(nav="nav-sec-mindset",      art="sec-mindset",      label="Life",           next_nav="no-results",           next_art=None,                tag=""),   # Life is last (jay, 2026-09-18: "Eng before Life")
}
SEC = SECTIONS[A.section]; TAG = SEC["tag"]
KEY, HREF = A.key, f"pocs-{A.key}.html"
BIN_SPAN = f'<span title="bin">{A.bin}</span>' if A.bin else ""
RAW_SPAN = ""
if A.raw:   # raw layer (docs/topics/raw/README.md): append-only copy of the source, so it can be reopened instead of re-remembered
    _src = pathlib.Path(A.raw).expanduser().resolve(); _rawdir = (ROOT / "topics" / "raw").resolve()
    if _src.parent == _rawdir: _dest = _src   # already in the raw layer (a shared file such as a morning report feeds several items): link it, copy nothing
    else:
        _dest = _rawdir / f"{DATE}-{KEY}{_src.suffix or '.txt'}"
        if not _dest.exists(): _dest.write_bytes(_src.read_bytes())
    RAW_SPAN = f'<span title="raw"><a href="raw/{_dest.name}">raw</a></span>'
E = lambda s: html.escape(s, quote=False).replace("'", "&#39;")

def inline(t):
    t = E(t); t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t); t = re.sub(r'`(.+?)`', r'<code>\1</code>', t)
    t = re.sub(r'(?<![*\w])\*(?!\*)(.+?)(?<!\*)\*(?![*\w])', r'<em>\1</em>', t)
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)

def md_to_html(md):
    out, lines, i = [], md.split("\n"), 0
    while i < len(lines):
        l = lines[i]
        if l.startswith("### "): out.append(f"<h3>{inline(l[4:])}</h3>")
        elif l.startswith("## "): out.append(f"<h2>{inline(l[3:])}</h2>")
        elif l.startswith("```"):
            j = i + 1; buf = []
            while not lines[j].startswith("```"): buf.append(lines[j]); j += 1
            out.append('<pre><code class="language-text">' + E("\n".join(buf)) + "\n</code></pre>"); i = j
        elif l.startswith("| "):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r'^\|[-| ]+\|$', lines[i]): rows.append([c.strip() for c in lines[i].strip("|").split("|")])
                i += 1
            i -= 1
            th = "".join(f"<th>{inline(c)}</th>" for c in rows[0]); tb = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
            out.append(f"<table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table>")
        elif re.match(r'^\d+\. ', l):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]): items.append(re.sub(r'^\d+\. ', '', lines[i])); i += 1
            i -= 1; out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>")
        elif l.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "): items.append(lines[i][2:]); i += 1
            i -= 1; out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
        elif l.strip(): out.append(f"<p>{inline(l)}</p>")
        i += 1
    return "\n".join(out)

def load(p):
    md = pathlib.Path(p).read_text().rstrip("\n") + "\n"; parts = md.split("\n\n")
    return md, parts[0][2:].strip(), parts[1].strip(), parts[2].strip(), "\n\n".join(parts[3:])
en_md, TITLE, SUMMARY, META, en_body = load(A.en); ko_md, TITLE_KO, SUMMARY_KO, META_KO, ko_body = load(A.ko)
# Every item closes with "Where it lands in Jayverse" (jay, 2026-09-18: all detail pages have this section).
assert "### Where it lands in Jayverse" in en_body or "## Where it lands in Jayverse" in en_body, "en.md needs a 'Where it lands in Jayverse' section"
assert "Jayverse에서의 위치" in ko_body, "ko.md needs a 'Jayverse에서의 위치' section"
WHY = re.search(r'## Why\n\n(.*?)(\n\n|$)', en_body, re.S).group(1)
HOW = " · ".join(h[4:].split(" — ")[0] for h in re.findall(r'^### .*$', en_body, re.M))
DATE_SPAN = f'<span class="topic-date" title="added" style="margin-left:auto;flex:0 0 auto;font-size:.72rem;color:var(--text2);font-variant-numeric:tabular-nums">{DATE}</span>'
SRC_SPAN = f'<span class="topic-src" title="source" style="flex:0 0 auto;margin-left:6px;font-size:.66rem;line-height:1.5;color:var(--text2);border:1px solid currentColor;border-radius:999px;padding:0 6px;opacity:.75">{A.source}</span>'

# ---------------- _nav.js first: it is the source of truth for the order ----------------
n = ROOT / "topics" / "_nav.js"; t = n.read_text()
nav = json.loads(re.match(r'window\.__NAV__=(.*);\s*$', t, re.S).group(1))
sec = next(x for x in nav["sections"] if x["navId"] == SEC["nav"])
items = sec["items"]
existing = next((x for x in items if x["key"] == KEY), None)
if existing:
    slot = position(SEC["nav"], int(re.search(r'topic-no">(\d+)<', existing["text"]).group(1))); items[:] = [x for x in items if x["key"] != KEY]
else:
    assert A.slot, "--slot is required for a new item"; slot = A.slot
new_item = {"key": KEY, "href": HREF, "color": COLOR, "label": LABEL, "text": TAG + E(TITLE)}
if LABEL == "TODAY DONE": new_item["done"] = A.done_at or datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%dT%H:%M+09:00")
elif existing and existing.get("done") and LABEL in ("DONE", "REVISIT"): new_item["done"] = existing["done"]
if LABEL == "REVISIT" and not new_item.get("done"): new_item["done"] = A.done_at or datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%dT%H:%M+09:00")   # REVISIT is done: stamp the day
items.insert(slot - 1, new_item)
for k, x in enumerate(items, 1):
    x["text"] = f'<span class="topic-no">{display(SEC["nav"], k)}</span>' + re.sub(r'^<span class="topic-no">\d+</span>', '', x["text"])
    x["n"] = str(display(SEC["nav"], k)); x["title"] = re.sub(r'^<span class="topic-no">\d+</span>', '', x["text"])
N = len(items); DONE = sum(1 for x in items if x["label"] in ("DONE", "TODAY DONE", "YESTERDAY DONE", "REVISIT"))   # REVISIT is a done item kept for a later reminder (jay, 2026-09-21)
sec["label"] = f"{SEC['label']} ({N})"
for j in nav["jump"]:
    if j["id"] == SEC["art"]: j["all"], j["done"] = N, DONE
for x in items: x.pop("n", None); x.pop("title", None)
n.write_text("window.__NAV__=" + json.dumps(nav, ensure_ascii=False, separators=(",", ":")) + ";\n")
# convenience view used below: [key, href, color, label, n, title-html]
items = [[x["key"], x["href"], x["color"], x["label"], str(display(SEC["nav"], k)), re.sub(r'^(<span class="topic-no">\d+</span>)?(<span class="topic-tag">[^<]*</span>)?', '', x["text"])] for k, x in enumerate(items, 1)]

# ---------------- notes.html ----------------
p = ROOT / "notes.html"; s = p.read_text()
a0 = s.index(f'id="{SEC["nav"]}"'); a1 = s.index(f'id="{SEC["next_nav"]}"')
b0 = s.index(f'<article id="{SEC["art"]}">'); b1 = s.index(f'<article id="{SEC["next_art"]}">') if SEC["next_art"] else s.index('    <p class="src">')
nav, cards = s[a0:a1], s[b0:b1]
# drop an existing copy of this item
nav = re.sub(rf'        <li><a class="nav-link" href="[^"]*" data-key="{re.escape(KEY)}">.*?</li>\n', '', nav, flags=re.S)  # by key: hrefs carry the pocs- prefix (duplicates slipped in before 2026-09-18)
cards = re.sub(rf'        <li id="{KEY}">.*?\n        </li>\n', '', cards, flags=re.S)
# renumber nav links and cards by key from the nav.js order
num = {x[0]: x[4] for x in items}
SHOWN = display(SEC["nav"], slot)  # the number the reader sees for this slot
nav = re.sub(r'(data-key="([^"]+)".*?<span class="topic-no">)(\d+)(<)', lambda m: m.group(1) + num.get(m.group(2), m.group(3)) + m.group(4), nav)
cards = re.sub(r'(<li id="([^"]+)">\s*<div class="topic-head"><span class="topic-no">)(\d+)(<)', lambda m: m.group(1) + num.get(m.group(2), m.group(3)) + m.group(4), cards)
navli = (f'        <li><a class="nav-link" href="topics/{HREF}" data-key="{KEY}"><span class="nav-dot" style="background:{COLOR};" title="{LABEL}"></span>'
         f'<span class="nav-text"><span class="topic-no">{SHOWN}</span>{TAG}{E(TITLE)}</span></a></li>\n')
card = f'''        <li id="{KEY}">
          <div class="topic-head"><span class="topic-no">{SHOWN}</span>{TAG}<span class="topic-title">{E(TITLE)}</span>{DATE_SPAN}{SRC_SPAN}</div>
          <p class="topic-summary">{E(SUMMARY)}</p>
          <p class="topic-how"><strong>How it works</strong>{E(HOW)}</p>
          <p class="topic-why"><strong>Why</strong>{inline(WHY)}</p>
          <p class="topic-link"><a href="topics/{HREF}">Detail &rarr;</a> &middot; <a href="#top">Top &uarr;</a> &middot; <a href="#{SEC["art"]}">Section top &uarr;</a> &middot; <button type="button" class="copy-btn copy-inline" data-copy="copy-en-{KEY}" data-done="Copied &#10003;">Copy EN</button><button type="button" class="copy-btn copy-inline" data-copy="copy-ko-{KEY}" data-done="복사됨 &#10003;">Copy KO</button><script type="application/json" id="copy-en-{KEY}">{json.dumps(en_md, ensure_ascii=False)}</script><script type="application/json" id="copy-ko-{KEY}">{json.dumps(ko_md, ensure_ascii=False)}</script></p>
        </li>
'''
if slot == 1:
    nav = re.sub(r'(<ul>\n)', r'\1' + navli.replace('\\', '\\\\'), nav, count=1)
    cards = re.sub(r'(<ul class="topics">\n)', r'\1' + card.replace('\\', '\\\\'), cards, count=1)
else:
    prev_key = items[slot - 2][0]
    m = re.search(rf'        <li><a class="nav-link" href="(?:#|topics/)[^"]*" data-key="{re.escape(prev_key)}".*?</li>\n', nav, re.S); assert m, prev_key
    nav = nav[:m.end()] + navli + nav[m.end():]
    i = cards.index(f'<li id="{prev_key}">'); j = cards.index('        </li>\n', i) + len('        </li>\n')
    cards = cards[:j] + card + cards[j:]
s = s[:a0] + nav + s[a1:b0] + cards + s[b1:]
# the rail's group label carries the same count as the section label (it had drifted to 225 while the section said 236; 2026-09-18)
s = re.sub(rf'(<div class="nav-group" id="{SEC["nav"]}" data-group>\s*<p class="nav-group-label">)[^<]*(</p>)', lambda m: m.group(1) + f"{SEC['label']} ({N})" + m.group(2), s, count=1)
s = re.sub(re.escape(SEC['label']) + r' &mdash; done \(\d+\) / all \(\d+\)', f"{SEC['label']} &mdash; done ({DONE}) / all ({N})", s, count=1)
s = re.sub(r'(<a href="#' + SEC['art'] + r'"[^>]*>' + re.escape(SEC['label']) + r'<b><span class="count-done">)\d+(</span><span class="count-all">/)\d+', lambda m: f'{m.group(1)}{DONE}{m.group(2)}{N}', s, count=1)
s = re.sub(r'(<article id="' + SEC['art'] + r'">.*?<span class="count-done">done \()\d+(\)</span> <span class="count-all">/ all \()\d+', lambda m: f'{m.group(1)}{DONE}{m.group(2)}{N}', s, count=1, flags=re.S)
# overall badge = sum of rail pills
jump = s[s.index('<div class="rail-jump">'):]; jump = jump[:jump.index('</div>')]
pills = re.findall(r'<span class="count-done">(\d+)</span><span class="count-all">/(\d+)</span>', jump)
td, ta = sum(int(a) for a, _ in pills), sum(int(b) for _, b in pills)
badge = f'{round(td * 100 / ta)}% &middot; {td}/{ta}'
s = re.sub(r'(<span class="rail-note"[^>]*title="current">)[^<]*(</span>)', lambda m: m.group(1) + badge + m.group(2), s, count=1)
p.write_text(s)
# TODAY DONE rule: items done before today's 06:00 KST bucket drop to DONE; rail dots synced (scripts/roll-done-states.py)
subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve().parent / "roll-done-states.py")], check=True)

# ---------------- detail page ----------------
tpl = (ROOT / "topics" / "pocs-alchemy-app-is-a-budget.html").read_text()
head = tpl[:tpl.index('<div class="solo">') + len('<div class="solo">\n')]
head = head.replace(tpl[tpl.index('<title>'):tpl.index('</title>') + 8], f'<title>{E(TITLE)} — Knowledge Notes</title>')
tail = tpl[tpl.index('  </div>\n  </main>\n</div>\n<script src="_nav.js">'):]
tail = re.sub(r'window\.__NAV_CURRENT__="[^"]*"', f'window.__NAV_CURRENT__="{KEY}"', tail)
DONE_SPAN = f'<span title="done">done {new_item["done"][:10]}</span>' if new_item.get("done") else ""   # done date in the kicker (jay, 2026-09-21); roll-done-states.py keeps it in sync afterwards
mid = f'''    <p class="crumb"><a href="../index.html">Workspace Index</a> &rsaquo; <a href="../notes.html">Knowledge Notes</a> &rsaquo; {E(TITLE)}</p>
  <header class="topic-hero">
      <p class="topic-kicker"><span class="topic-no">#{SHOWN}</span><span>{E(A.type)}</span><span title="added">{DATE}</span><span title="source">{A.source}</span>{BIN_SPAN}{RAW_SPAN}{DONE_SPAN}</p>
      <h1>{E(TITLE)}</h1>
      <p class="lead">{E(SUMMARY)}</p>
      <p class="meta">{inline(META)}</p>
      <nav class="lang-switch" aria-label="Language"><a href="#en">English</a><a href="#ko">한국어</a></nav>
    </header>
    <article id="en">
      <nav class="lang-switch" aria-label="Language"><a href="#en" class="on">English</a><a href="#ko">한국어</a></nav>
      <p class="copy-row"><button type="button" class="copy-btn" data-copy="copy-en" data-done="Copied &#10003;">Copy English</button></p>
      <script type="application/json" id="copy-en">{json.dumps(en_md, ensure_ascii=False)}</script>
{md_to_html(en_body)}
      <p><a href="../notes.html?list">&larr; All Knowledge Notes</a> &middot; <a href="../index.html">Workspace Index</a> &middot; <a href="#top">Top &uarr;</a></p>
    </article>
    <article id="ko" lang="ko">
      <nav class="lang-switch" aria-label="Language"><a href="#en">English</a><a href="#ko" class="on">한국어</a></nav>
      <p class="copy-row"><button type="button" class="copy-btn" data-copy="copy-ko" data-done="복사됨 &#10003;">Copy 한국어</button></p>
      <script type="application/json" id="copy-ko">{json.dumps(ko_md, ensure_ascii=False)}</script>
      <h1>{E(TITLE_KO)}</h1>
      <p class="lead">{E(SUMMARY_KO)}</p>
      <p class="meta">{inline(META_KO)}</p>
{md_to_html(ko_body)}
      <p><a href="../notes.html?list">&larr; 전체 기술 노트</a> &middot; <a href="../index.html">워크스페이스 인덱스</a> &middot; <a href="#top">맨 위 &uarr;</a></p>
    </article>
    <div class="pager"></div>
'''
(ROOT / "topics" / HREF).write_text(head + mid + tail)

# ---------------- index card → first NEW/IMPORTANT item (jay, 2026-09-18) ----------------
# "Entering the notes goes to the detail page directly": the Knowledge Notes card on index.html opens
# the first NEW or IMPORTANT item in rail order (notes.html itself redirects the same way without a hash).
first = next((x for x in items if x[3] in ("NEW", "IMPORTANT")), None)
if first:
    ip = ROOT / "index.html"; t = ip.read_text()
    t, k = re.subn(r'(<a href=")[^"]*(" class="card" style="border-left: 4px solid #7c3aed;">\s*<span class="card-title">Knowledge Notes</span>\s*<span class="card-path"[^>]*>)[^<]*(</span>)',
                   lambda m: f'{m.group(1)}topics/{first[1]}{m.group(2)}docs/topics/{first[1]}{m.group(3)}', t, count=1)
    if k: ip.write_text(t); print(f"index card → topics/{first[1]} ({first[3]})")
    else: print("WARNING: Knowledge Notes card not found on index.html")

# ---------------- key expressions (jay, 2026-09-18) ----------------
# Every detail page ends with the words and phrases worth learning from its English text. The table
# lives in docs/topics/vocab/<page>.md; scripts/add-vocab.py renders it into both articles. Pass --vocab
# for a new item; on a re-run without --vocab the existing file is re-applied so the block survives.
import shutil
VOCAB_DIR = ROOT / "topics" / "vocab"; VOCAB_DIR.mkdir(exist_ok=True); PAGE_KEY = HREF[:-5]
if A.vocab: shutil.copyfile(A.vocab, VOCAB_DIR / f"{PAGE_KEY}.md")
if (VOCAB_DIR / f"{PAGE_KEY}.md").exists():
    subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve().parent / "add-vocab.py"), PAGE_KEY], check=True)
else:
    print(f"WARNING: no key-expressions file for {PAGE_KEY}; write docs/topics/vocab/{PAGE_KEY}.md and run scripts/add-vocab.py {PAGE_KEY}")

# ---------------- kicker + pager on every Blockchain page ----------------
fixed = missing = 0
for idx, x in enumerate(items):
    f = ROOT / "topics" / x[1]
    if not f.exists(): missing += 1; continue
    c = f.read_text()
    c2 = re.sub(r'<span class="topic-no">#\d+</span>', f'<span class="topic-no">#{x[4]}</span>', c, count=1)
    prev = items[idx - 1] if idx > 0 else None; nxt = items[idx + 1] if idx + 1 < N else None
    pager = '<div class="pager">' + (f'<a href="{prev[1]}">&larr; {prev[4]}. {prev[5]}</a>' if prev else '') + (f'<a href="{nxt[1]}">{nxt[4]}. {nxt[5]} &rarr;</a>' if nxt else '') + '</div>'
    c2 = re.sub(r'<div class="pager">.*?</div>', lambda _: pager, c2, count=1, flags=re.S)
    if c2 != c: f.write_text(c2); fixed += 1
# static overall badge on every topic page
for f in glob.glob(str(ROOT / "topics" / "*.html")):
    q = pathlib.Path(f); c = q.read_text()
    c2 = re.sub(r'(<span class="rail-note"[^>]*title="current">)[^<]*(</span>)', lambda m: m.group(1) + badge + m.group(2), c, count=1)
    if c2 != c: q.write_text(c2)
print(f"#{SHOWN} {KEY} [{LABEL}, {DATE}, {A.source}] → {SEC['label']} {DONE}/{N}, overall {badge}; pages rewritten {fixed}, missing files {missing}")

# converse bin → interview bank (learning-greed item: "the converse bin is the interview bank"; jay, 2026-09-21)
if A.bin == "converse" and A.sentence:
    bank = ROOT / "topics" / "interview-bank.md"; row = f"| {SEC['label']} {SHOWN} | [{E(TITLE)}]({HREF}) | {A.sentence.strip()} | {DATE} |\n"
    if f"]({HREF})" not in bank.read_text(): bank.write_text(bank.read_text().rstrip("\n") + "\n" + row)
# machine-readable index (docs/topics/index.json, index.md): "have I already learned this" is a search, not a memory
subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve().parent / "build-index.py")], check=True)
