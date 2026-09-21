#!/usr/bin/env python3
"""Order Tech and Theory items by status (jay, 2026-09-18: "make the important ones have lower number than
new ones but higher than done"): REVISIT < done (DONE / YESTERDAY DONE / TODAY DONE) < IMPORTANT < NEW < PLANNED, stable
within each rank. Life is skipped (all NEW; the Health cards follow their own numbering) and English keeps its
chronological append-only numbering (jay, 2026-09-16).

Rewrites: docs/topics/_nav.js (item order + topic-no), docs/notes.html (rail <li> order, card <li> order, numbers),
and every detail page's kicker `#N` and pager. Counts do not change. Idempotent.
"""
import json, re, pathlib, subprocess, sys, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from notes_numbering import display
ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs"
RANK = {"REVISIT": -1,   # done, come back later — sits above every other done item (jay, 2026-09-21: "one more category before Done")
        "DONE": 0, "YESTERDAY DONE": 0, "TODAY DONE": 0, "RECENTLY DONE": 0, "IMPORTANT": 1, "NEW": 2, "PLANNED": 3}
SECTIONS = {"nav-sec-blockchain": "sec-blockchain", "nav-sec-fundamentals": "sec-fundamentals", "nav-sec-invest": "sec-invest", "nav-sec-mindset": "sec-mindset"}
SORTED = ("nav-sec-blockchain", "nav-sec-fundamentals", "nav-sec-invest")   # Life is numbered (from 1300) but never reordered
NEXT = {"nav-sec-blockchain": ("nav-sec-fundamentals", "sec-fundamentals"), "nav-sec-fundamentals": ("nav-sec-invest", "sec-invest"), "nav-sec-invest": ("nav-sec-english", "sec-english"), "nav-sec-mindset": ("no-results", None)}   # Life is last

n = ROOT / "topics" / "_nav.js"
nav = json.loads(re.match(r'window\.__NAV__=(.*);\s*$', n.read_text(), re.S).group(1))
s = (ROOT / "notes.html").read_text()
moved_total = 0
for navid, artid in SECTIONS.items():
    sec = next(x for x in nav["sections"] if x["navId"] == navid)
    before = [x["key"] for x in sec["items"]]
    if navid in SORTED: sec["items"].sort(key=lambda x: RANK[x["label"]])          # stable
    order = [x["key"] for x in sec["items"]]
    moved = sum(1 for a, b in zip(before, order) if a != b); moved_total += moved
    for k, x in enumerate(sec["items"], 1):
        x["text"] = f'<span class="topic-no">{display(navid, k)}</span>' + re.sub(r'^<span class="topic-no">\d+</span>', '', x["text"])
    num = {key: display(navid, k) for k, key in enumerate(order, 1)}
    # notes.html rail group: reorder + renumber the <li> blocks
    a0 = s.index(f'id="{navid}"'); a1 = s.index(f'id="{NEXT[navid][0]}"')
    navblk = s[a0:a1]
    lis = {m.group(2): m.group(1) for m in re.finditer(r'(        <li><a class="nav-link" href="[^"]*" data-key="([^"]+)">.*?</li>\n)', navblk, re.S) if m.group(2) in num}
    assert set(lis) == set(order), (navid, set(lis) ^ set(order))
    if navid in SORTED:
        first = navblk.index('        <li><a class="nav-link"'); last = navblk.rindex('</li>\n') + len('</li>\n')
        newlis = "".join(re.sub(r'<span class="topic-no">\d+</span>', f'<span class="topic-no">{num[k]}</span>', lis[k], count=1) for k in order)
        navblk = navblk[:first] + newlis + navblk[last:]
    else:   # Life: renumber each entry in place (the Health entries that follow keep their own numbers)
        for k in order: navblk = navblk.replace(lis[k], re.sub(r'<span class="topic-no">\d+</span>', f'<span class="topic-no">{num[k]}</span>', lis[k], count=1), 1)
    s = s[:a0] + navblk + s[a1:]
    # notes.html cards
    b0 = s.index(f'<article id="{artid}">'); b1 = s.index(f'<article id="{NEXT[navid][1]}">') if NEXT[navid][1] else s.index('    <p class="src">')
    cards = s[b0:b1]
    cs = {m.group(2): m.group(1) for m in re.finditer(r'(        <li id="([^"]+)">\n.*?\n        </li>\n)', cards, re.S) if m.group(2) in num}
    assert set(cs) == set(order), (artid, set(cs) ^ set(order))
    renum = lambda k: re.sub(r'(<div class="topic-head"><span class="topic-no">)\d+', lambda m: m.group(1) + str(num[k]), cs[k], count=1)
    if navid in SORTED:
        first = cards.index('        <li id="'); last = cards.rindex('        </li>\n', 0, cards.index('<!-- health-cards:start -->') if '<!-- health-cards:start -->' in cards else len(cards)) + len('        </li>\n')
        cards = cards[:first] + "".join(renum(k) for k in order) + cards[last:]
    else:
        for k in order: cards = cards.replace(cs[k], renum(k), 1)
    s = s[:b0] + cards + s[b1:]
    # detail pages: kicker + pager
    items = sec["items"]
    for idx, x in enumerate(items):
        f = ROOT / "topics" / x["href"]
        if not f.exists(): continue
        c = f.read_text()
        title = lambda y: re.sub(r'^(<span class="topic-no">\d+</span>)?(<span class="topic-tag">[^<]*</span>)?', '', y["text"])
        c2 = re.sub(r'<span class="topic-no">#\d+</span>', f'<span class="topic-no">#{display(navid, idx + 1)}</span>', c, count=1)
        prev = items[idx - 1] if idx > 0 else None; nxt = items[idx + 1] if idx + 1 < len(items) else None
        pager = '<div class="pager">' + (f'<a href="{prev["href"]}">&larr; {display(navid, idx)}. {title(prev)}</a>' if prev else '') + (f'<a href="{nxt["href"]}">{display(navid, idx + 2)}. {title(nxt)} &rarr;</a>' if nxt else '') + '</div>'
        c2 = re.sub(r'<div class="pager">.*?</div>', lambda _: pager, c2, count=1, flags=re.S)
        if c2 != c: f.write_text(c2)
    print(f"{navid}: {moved} items changed number; order now " + "".join({-1: "R", 0: "D", 1: "I", 2: "N", 3: "P"}[RANK[x["label"]]] for x in items))
(ROOT / "notes.html").write_text(s)
n.write_text("window.__NAV__=" + json.dumps(nav, ensure_ascii=False, separators=(",", ":")) + ";\n")
print(f"reorder-by-status: {moved_total} renumbered")
# rebuild docs/topics/index.json + index.md (scripts/build-index.py; jay, 2026-09-21: "Let the system hold the index")
import subprocess, sys
subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve().parent / "build-index.py")], check=True)
