#!/usr/bin/env python3
"""Order Tech and Theory items by status (jay, 2026-09-18: "make the important ones have lower number than
new ones but higher than done"): REVISIT < done (DONE / RECENTLY DONE) < IMPORTANT < NEW < PLANNED, stable
within each rank, in every section (Life since 2026-09-21; the Health cards keep their own numbering). English is
ordered the same way by english-notes.py, which numbers by rank position while the files stay english-N.md.

Rewrites: docs/topics/_nav.js (item order + topic-no), docs/notes.html (rail <li> order, card <li> order, numbers),
and every detail page's kicker `#N` and pager. Counts do not change. Idempotent.
"""
import json, re, pathlib, subprocess, sys, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from notes_numbering import display
ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs"
RANK = {"REVISIT": -1,   # done, come back later — sits above every other done item (jay, 2026-09-21: "one more category before Done")
        "DONE": 0, "RECENTLY DONE": 0, "YESTERDAY DONE": 0, "TODAY DONE": 0, "IMPORTANT": 1, "NEW": 2, "PLANNED": 3}
SECTIONS = {"nav-sec-blockchain": "sec-blockchain", "nav-sec-fundamentals": "sec-fundamentals", "nav-sec-invest": "sec-invest", "nav-sec-mindset": "sec-mindset"}
SORTED = ("nav-sec-blockchain", "nav-sec-fundamentals", "nav-sec-invest", "nav-sec-mindset")   # Life joined on 2026-09-21 (jay: "The number should be in order for all the category"); English is ordered by english-notes.py itself
NEXT = {"nav-sec-blockchain": ("nav-sec-fundamentals", "sec-fundamentals"), "nav-sec-fundamentals": ("nav-sec-invest", "sec-invest"), "nav-sec-invest": ("nav-sec-mindset", "sec-mindset"), "nav-sec-mindset": ("nav-sec-english", "sec-english")}   # order Tech · Theory · Invest · Life · Eng (jay, 2026-09-21); Eng is last

n = ROOT / "topics" / "_nav.js"
nav = json.loads(re.match(r'window\.__NAV__=(.*);\s*$', n.read_text(), re.S).group(1))
s = (ROOT / "notes.html").read_text()
# NEW lasts two BUSINESS days (jay, 2026-09-25: "define category New as the new items during two business day based on
# Korea holiday system"; supersedes the seven-calendar-day rule of 2026-09-21). An item is NEW on the day it was added
# and through the next business day; once two or more business days have passed since `added` it rolls to PLANNED
# before ranking. Business days are Mon-Fri minus Korean public holidays — see scripts/kr_holidays.py, which refuses
# to guess about a year it has no table for. Every section except English (its statuses come from the .md files) and
# LOCKED Health cards. Items without `added` are left alone.
import datetime
import kr_holidays
TODAY = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).date()
NEW_BUSINESS_DAYS = 2
expired, uncovered = [], set()
for sec in nav["sections"]:
    if sec["navId"] == "nav-sec-english": continue
    for x in sec["items"]:
        if x["label"] != "NEW" or not x.get("added"): continue
        try:
            elapsed = kr_holidays.business_days_since(datetime.date.fromisoformat(x["added"]), TODAY)
        except ValueError as e:      # no holiday table for that year: leave the item NEW and say so loudly
            uncovered.add(str(e).split(" for ")[1].split(".")[0]); continue
        if elapsed >= NEW_BUSINESS_DAYS:
            x["label"], x["color"] = "PLANNED", "#64748b"; expired.append(x["key"])
if uncovered:
    print(f"  !! kr_holidays has no table for {', '.join(sorted(uncovered))} — those items were LEFT as NEW. "
          f"Add the year to scripts/kr_holidays.py.")
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
        first = navblk.index('        <li><a class="nav-link"'); last = navblk.rindex('</li>\n', 0, navblk.index('<!-- health-nav:start -->') if '<!-- health-nav:start -->' in navblk else len(navblk)) + len('</li>\n')   # keep the Health rail links (LOCKED, 1400…) that follow the Life items
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
        title = lambda y: re.sub(r'^(<span class="topic-no">\d+</span>)?(<span class="topic-tag"[^>]*>[^<]*</span>)?', '', y["text"])
        c2 = re.sub(r'<span class="topic-no">#\d+</span>', f'<span class="topic-no">#{display(navid, idx + 1)}</span>', c, count=1)
        prev = items[idx - 1] if idx > 0 else None; nxt = items[idx + 1] if idx + 1 < len(items) else None
        pager = '<div class="pager">' + (f'<a href="{prev["href"]}">&larr; {display(navid, idx)}. {title(prev)}</a>' if prev else '') + (f'<a href="{nxt["href"]}">{display(navid, idx + 2)}. {title(nxt)} &rarr;</a>' if nxt else '') + '</div>'
        c2 = re.sub(r'<div class="pager">.*?</div>', lambda _: pager, c2, count=1, flags=re.S)
        if c2 != c: f.write_text(c2)
    print(f"{navid}: {moved} items changed number; order now " + "".join({-1: "R", 0: "D", 1: "I", 2: "N", 3: "P"}[RANK[x["label"]]] for x in items))
(ROOT / "notes.html").write_text(s)
n.write_text("window.__NAV__=" + json.dumps(nav, ensure_ascii=False, separators=(",", ":")) + ";\n")
print(f"reorder-by-status: {moved_total} renumbered; NEW → PLANNED after {NEW_BUSINESS_DAYS} business days (KR): {len(expired)}" + (" (" + ", ".join(expired[:8]) + ("…" if len(expired) > 8 else "") + ")" if expired else ""))
if expired:   # dots, counts, badge, card chips follow _nav.js (roll never calls back here, so no loop)
    subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve().parent / "roll-done-states.py")], check=True)
# rebuild docs/topics/index.json + index.md (scripts/build-index.py; jay, 2026-09-21: "Let the system hold the index")
import subprocess, sys
subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve().parent / "build-index.py")], check=True)
