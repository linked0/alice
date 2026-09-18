#!/usr/bin/env python3
"""Insert or update one Blockchain & Tech (or, with --section fundamentals, Fundamentals) item in Tech Notes from two markdown files.

    python3 scripts/add-tech-item.py --key <key> --slot <N> --en <en.md> --ko <ko.md> \
        [--status new|important|planned|recent|done] [--date YYYY-MM-DD] [--type PoC] [--source chat|file]

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
import re, json, pathlib, html, argparse, datetime, glob

ap = argparse.ArgumentParser()
ap.add_argument("--key", required=True); ap.add_argument("--slot", type=int)
ap.add_argument("--en", required=True); ap.add_argument("--ko", required=True)
ap.add_argument("--status", default="new"); ap.add_argument("--date"); ap.add_argument("--type", default="PoC")
ap.add_argument("--source", default="chat", choices=["chat", "file"], help="where the subject came from: jay in chat, or the alice-tech file")
ap.add_argument("--section", default="blockchain", choices=["blockchain", "fundamentals"], help="which Tech Notes section the item belongs to")
ap.add_argument("--tag", default="Economics", help="Fundamentals only: the topic-tag chip (Math | Algorithms | Economics)")
A = ap.parse_args()
ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs"
COLORS = {"planned": ("#64748b", "PLANNED"), "done": ("#22c55e", "DONE"), "recent": ("#38bdf8", "RECENTLY DONE"),
          "important": ("#ef4444", "IMPORTANT"), "new": ("#eab308", "NEW")}
COLOR, LABEL = COLORS[A.status]
DATE = A.date or datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d")
# Section constants. Blockchain has no tag chip; Fundamentals cards carry <span class="topic-tag">Math|Algorithms|Economics</span>
# right after the number (jay, 2026-09-18: first Fundamentals item added through this script).
SECTIONS = {
    "blockchain":   dict(nav="nav-sec-blockchain",   art="sec-blockchain",   label="Blockchain & Tech", next_nav="nav-sec-fundamentals", next_art="sec-fundamentals", tag=""),
    "fundamentals": dict(nav="nav-sec-fundamentals", art="sec-fundamentals", label="Fundamentals",      next_nav="nav-sec-english",      next_art="sec-english",       tag=f'<span class="topic-tag">{A.tag}</span>'),
}
SEC = SECTIONS[A.section]; TAG = SEC["tag"]
KEY, HREF = A.key, f"pocs-{A.key}.html"
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
    slot = int(re.search(r'topic-no">(\d+)<', existing["text"]).group(1)); items[:] = [x for x in items if x["key"] != KEY]
else:
    assert A.slot, "--slot is required for a new item"; slot = A.slot
items.insert(slot - 1, {"key": KEY, "href": HREF, "color": COLOR, "label": LABEL, "text": TAG + E(TITLE)})
for k, x in enumerate(items, 1):
    x["text"] = f'<span class="topic-no">{k}</span>' + re.sub(r'^<span class="topic-no">\d+</span>', '', x["text"])
    x["n"] = str(k); x["title"] = re.sub(r'^<span class="topic-no">\d+</span>', '', x["text"])
N = len(items); DONE = sum(1 for x in items if x["label"] in ("DONE", "RECENTLY DONE"))
sec["label"] = f"{SEC['label']} ({N})"
for j in nav["jump"]:
    if j["id"] == SEC["art"]: j["all"], j["done"] = N, DONE
for x in items: x.pop("n", None); x.pop("title", None)
n.write_text("window.__NAV__=" + json.dumps(nav, ensure_ascii=False, separators=(",", ":")) + ";\n")
# convenience view used below: [key, href, color, label, n, title-html]
items = [[x["key"], x["href"], x["color"], x["label"], str(k), re.sub(r'^(<span class="topic-no">\d+</span>)?(<span class="topic-tag">[^<]*</span>)?', '', x["text"])] for k, x in enumerate(items, 1)]

# ---------------- notes.html ----------------
p = ROOT / "notes.html"; s = p.read_text()
a0 = s.index(f'id="{SEC["nav"]}"'); a1 = s.index(f'id="{SEC["next_nav"]}"')
b0 = s.index(f'<article id="{SEC["art"]}">'); b1 = s.index(f'<article id="{SEC["next_art"]}">')
nav, cards = s[a0:a1], s[b0:b1]
# drop an existing copy of this item
nav = re.sub(rf'        <li><a class="nav-link" href="#{KEY}".*?</li>\n', '', nav, flags=re.S)
cards = re.sub(rf'        <li id="{KEY}">.*?\n        </li>\n', '', cards, flags=re.S)
# renumber nav links and cards by key from the nav.js order
num = {x[0]: x[4] for x in items}
nav = re.sub(r'(data-key="([^"]+)".*?<span class="topic-no">)(\d+)(<)', lambda m: m.group(1) + num.get(m.group(2), m.group(3)) + m.group(4), nav)
cards = re.sub(r'(<li id="([^"]+)">\s*<div class="topic-head"><span class="topic-no">)(\d+)(<)', lambda m: m.group(1) + num.get(m.group(2), m.group(3)) + m.group(4), cards)
navli = (f'        <li><a class="nav-link" href="#{KEY}" data-key="{KEY}"><span class="nav-dot" style="background:{COLOR};" title="{LABEL}"></span>'
         f'<span class="nav-text"><span class="topic-no">{slot}</span>{TAG}{E(TITLE)}</span></a></li>\n')
card = f'''        <li id="{KEY}">
          <div class="topic-head"><span class="topic-no">{slot}</span>{TAG}<span class="topic-title">{E(TITLE)}</span>{DATE_SPAN}{SRC_SPAN}</div>
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
    m = re.search(rf'        <li><a class="nav-link" href="#{prev_key}".*?</li>\n', nav, re.S); assert m, prev_key
    nav = nav[:m.end()] + navli + nav[m.end():]
    i = cards.index(f'<li id="{prev_key}">'); j = cards.index('        </li>\n', i) + len('        </li>\n')
    cards = cards[:j] + card + cards[j:]
s = s[:a0] + nav + s[a1:b0] + cards + s[b1:]
s = re.sub(re.escape(SEC['label']) + r' &mdash; done \(\d+\) / all \(\d+\)', f"{SEC['label']} &mdash; done ({DONE}) / all ({N})", s, count=1)
s = re.sub(r'(<a href="#' + SEC['art'] + r'"[^>]*>' + re.escape(SEC['label']) + r'<b><span class="count-done">)\d+(</span><span class="count-all">/)\d+', lambda m: f'{m.group(1)}{DONE}{m.group(2)}{N}', s, count=1)
s = re.sub(r'(<article id="' + SEC['art'] + r'">.*?<span class="count-done">done \()\d+(\)</span> <span class="count-all">/ all \()\d+', lambda m: f'{m.group(1)}{DONE}{m.group(2)}{N}', s, count=1, flags=re.S)
# overall badge = sum of rail pills
jump = s[s.index('<div class="rail-jump">'):]; jump = jump[:jump.index('</div>')]
pills = re.findall(r'<span class="count-done">(\d+)</span><span class="count-all">/(\d+)</span>', jump)
td, ta = sum(int(a) for a, _ in pills), sum(int(b) for _, b in pills)
badge = f'{round(td * 100 / ta)}% done &middot; {td}/{ta}'
s = re.sub(r'(<span class="rail-note"[^>]*title="current">)[^<]*(</span>)', lambda m: m.group(1) + badge + m.group(2), s, count=1)
p.write_text(s)

# ---------------- detail page ----------------
tpl = (ROOT / "topics" / "pocs-alchemy-app-is-a-budget.html").read_text()
head = tpl[:tpl.index('<div class="solo">') + len('<div class="solo">\n')]
head = head.replace(tpl[tpl.index('<title>'):tpl.index('</title>') + 8], f'<title>{E(TITLE)} — Tech Notes</title>')
tail = tpl[tpl.index('  </div>\n  </main>\n</div>\n<script src="_nav.js">'):]
tail = re.sub(r'window\.__NAV_CURRENT__="[^"]*"', f'window.__NAV_CURRENT__="{KEY}"', tail)
mid = f'''    <p class="crumb"><a href="../index.html">Workspace Index</a> &rsaquo; <a href="../notes.html">Tech Notes</a> &rsaquo; {E(TITLE)}</p>
  <header class="topic-hero">
      <p class="topic-kicker"><span class="topic-no">#{slot}</span><span>{E(A.type)}</span><span title="added">{DATE}</span><span title="source">{A.source}</span></p>
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
      <p><a href="../notes.html">&larr; All Tech Notes</a> &middot; <a href="../index.html">Workspace Index</a> &middot; <a href="#top">Top &uarr;</a></p>
    </article>
    <article id="ko" lang="ko">
      <nav class="lang-switch" aria-label="Language"><a href="#en">English</a><a href="#ko" class="on">한국어</a></nav>
      <p class="copy-row"><button type="button" class="copy-btn" data-copy="copy-ko" data-done="복사됨 &#10003;">Copy 한국어</button></p>
      <script type="application/json" id="copy-ko">{json.dumps(ko_md, ensure_ascii=False)}</script>
      <h1>{E(TITLE_KO)}</h1>
      <p class="lead">{E(SUMMARY_KO)}</p>
      <p class="meta">{inline(META_KO)}</p>
{md_to_html(ko_body)}
      <p><a href="../notes.html">&larr; 전체 기술 노트</a> &middot; <a href="../index.html">워크스페이스 인덱스</a> &middot; <a href="#top">맨 위 &uarr;</a></p>
    </article>
    <div class="pager"></div>
'''
(ROOT / "topics" / HREF).write_text(head + mid + tail)

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
print(f"#{slot} {KEY} [{LABEL}, {DATE}, {A.source}] → {SEC['label']} {DONE}/{N}, overall {badge}; pages rewritten {fixed}, missing files {missing}")
