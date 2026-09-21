#!/usr/bin/env python3
"""Apply the TODAY DONE rule (jay, 2026-09-18) to docs/topics/_nav.js and docs/notes.html.

Rule: an item marked done is "TODAY DONE" (midnight blue, #191970) from the moment it is done until the first
item of the *next* day is done. A day starts at 06:00 KST ("done from the 6 a.m. today before the new day's
first one is done"), so every item carries `done` (ISO time, +09:00) and the day bucket is (done - 6h).date().
Items in the previous done-day bucket are "YESTERDAY DONE" (sky blue, #38bdf8; jay, 2026-09-18: "add the
other day done status of which name tells everything"). Older buckets, and items with no `done` time, are plain DONE.
So each new day's first done item rolls everything one step: LATELY → OTHER DAY → DONE.

REVISIT (purple, #a855f7; jay, 2026-09-21) is a done item kept for a later reminder: it is never relabelled here and counts as done.
Also syncs every rail dot in notes.html (colour + title) with _nav.js and removes duplicate rail entries.
Run by scripts/add-tech-item.py after each change; safe to run alone at any time.
"""
import json, re, pathlib, subprocess, sys, datetime
ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs"
DONE_COLOR = {"nav-sec-blockchain": "#22c55e", "nav-sec-fundamentals": "#0284c7", "nav-sec-invest": "#0284c7", "nav-sec-mindset": "#22c55e", "nav-sec-english": "#22c55e"}
LATELY = ("#191970", "TODAY DONE")
OTHER = ("#38bdf8", "YESTERDAY DONE")
STAGED = ("TODAY DONE", "YESTERDAY DONE", "RECENTLY DONE")
KST = datetime.timezone(datetime.timedelta(hours=9))
def bucket(ts):
    dt = datetime.datetime.fromisoformat(ts)
    if dt.tzinfo is None: dt = dt.replace(tzinfo=KST)
    return (dt.astimezone(KST) - datetime.timedelta(hours=6)).date()

n = ROOT / "topics" / "_nav.js"; t = n.read_text()
nav = json.loads(re.match(r'window\.__NAV__=(.*);\s*$', t, re.S).group(1))
days = sorted({bucket(x["done"]) for s in nav["sections"] for x in s["items"] if x.get("done")}, reverse=True)   # every stamp counts, REVISIT included: "today is KST 09-21" (jay, 2026-09-21) — the day an item was marked is its done day
latest = days[0] if days else None; previous = days[1] if len(days) > 1 else None
changed = []
for s in nav["sections"]:
    for x in s["items"]:
        if x["label"] in STAGED or (x["label"] == "DONE" and x.get("done")):
            b = bucket(x["done"]) if x.get("done") else None
            want = LATELY if b and b == latest else OTHER if b and b == previous else (DONE_COLOR[s["navId"]], "DONE")
            if (x["color"], x["label"]) != want: x["color"], x["label"] = want; changed.append(x["key"])
    done = sum(1 for x in s["items"] if x["label"] in ("DONE", "TODAY DONE", "YESTERDAY DONE", "REVISIT"))   # REVISIT never rolls; it counts as done (jay, 2026-09-21)
    for j in nav["jump"]:
        if j["id"] == s["navId"].replace("nav-", ""): j["done"], j["all"] = done, len(s["items"])
# REVISIT keeps its label and purple dot, but the Today / Yesterday buttons must still find it by its stamp
# (jay, 2026-09-21: "Today does not show anything" … "today is KST 09-21"): `day` = today | yesterday on the item, rendered as data-day on the dot.
for s in nav["sections"]:
    for x in s["items"]:
        b = bucket(x["done"]) if x["label"] == "REVISIT" and x.get("done") else None
        day = "today" if b and b == latest else "yesterday" if b and b == previous else None
        if day: x["day"] = day
        else: x.pop("day", None)
n.write_text("window.__NAV__=" + json.dumps(nav, ensure_ascii=False, separators=(",", ":")) + ";\n")

# notes.html: every rail dot follows _nav.js; duplicate <li> for one key are collapsed to the first
p = ROOT / "notes.html"; h = p.read_text()
seen = set(); dropped = 0
def li_fix(m):
    global dropped
    key = m.group(2)
    if key in seen: dropped += 1; return ""
    seen.add(key); return m.group(0)
h = re.sub(r'(        <li><a class="nav-link" href="[^"]*" data-key="([^"]+)">.*?</li>\n)', li_fix, h, flags=re.S)
by_key = {x["key"]: x for s in nav["sections"] for x in s["items"]}
def dot_fix(m):
    x = by_key.get(m.group(2))
    return m.group(1) + (f'<span class="nav-dot" style="background:{x["color"]};" title="{x["label"]}"' + (f' data-day="{x["day"]}"' if x.get("day") else "") + '></span>' if x else m.group(3))
h = re.sub(r'(<a class="nav-link" href="[^"]*" data-key="([^"]+)">)(<span class="nav-dot" style="background:[^"]*;" title="[^"]*"(?: data-day="[^"]*")?></span>)', dot_fix, h)
for j in nav["jump"]:
    h = re.sub(r'(<a href="#' + j["id"] + r'"[^>]*>' + re.escape(j["label"]) + r'<b><span class="count-done">)\d+(</span><span class="count-all">/)\d+', lambda m: f'{m.group(1)}{j["done"]}{m.group(2)}{j["all"]}', h, count=1)
    h = re.sub(re.escape(j["label"]) + r' &mdash; done \(\d+\) / all \(\d+\)', f'{j["label"]} &mdash; done ({j["done"]}) / all ({j["all"]})', h, count=1)
    h = re.sub(r'(<article id="' + j["id"] + r'">.*?<span class="count-done">done \()\d+(\)</span> <span class="count-all">/ all \()\d+', lambda m: f'{m.group(1)}{j["done"]}{m.group(2)}{j["all"]}', h, count=1, flags=re.S)
# overall badge (sum of the jump pills) on notes.html and on every detail page's rail, and the index.html landing card
# (first NEW or IMPORTANT item in rail order) — both drift when a status is changed by editing _nav.js directly (jay, 2026-09-21: marking REVISIT)
td = sum(j["done"] for j in nav["jump"]); ta = sum(j["all"] for j in nav["jump"]); badge = f'{round(td * 100 / ta)}% &middot; {td}/{ta}'
BADGE = re.compile(r'(<span class="rail-note"[^>]*title="current">)[^<]*(</span>)')
h = BADGE.sub(lambda m: m.group(1) + badge + m.group(2), h, count=1)
p.write_text(h)
fixed = 0
for f in sorted((ROOT / "topics").glob("*.html")):
    c = f.read_text(); c2 = BADGE.sub(lambda m: m.group(1) + badge + m.group(2), c, count=1)
    if c2 != c: f.write_text(c2); fixed += 1
first = next((x for s_ in nav["sections"] for x in s_["items"] if x["label"] in ("NEW", "IMPORTANT")), None)
if first:
    ip = ROOT / "index.html"; t = ip.read_text()
    t, k = re.subn(r'(<a href=")[^"]*(" class="card" style="border-left: 4px solid #7c3aed;">\s*<span class="card-title">Knowledge Notes</span>\s*<span class="card-path"[^>]*>)[^<]*(</span>)',
                   lambda m: f'{m.group(1)}topics/{first["href"]}{m.group(2)}docs/topics/{first["href"]}{m.group(3)}', t, count=1)
    if k and t != ip.read_text(): ip.write_text(t); print(f"index card → topics/{first['href']} ({first['label']})")
# done date in every detail page's kicker (jay, 2026-09-21: "From now on, you should add the done date in a detail page"):
# <span title="done">YYYY-MM-DD</span> follows the stamp on the _nav.js item; removed when the item has no stamp. Health pages are locked and skipped.
DONE_SPAN = re.compile(r'<span title="done">[^<]*</span>')
dated = 0
for s_ in nav["sections"]:
    for x in s_["items"]:
        if x["label"] == "LOCKED": continue
        f = ROOT / "topics" / x["href"]
        if not f.exists(): continue
        c = f.read_text(); m = re.search(r'<p class="topic-kicker">(.*?)</p>', c, re.S)
        if not m: continue
        k = m.group(1); k2 = DONE_SPAN.sub("", k) + (f'<span title="done">done {x["done"][:10]}</span>' if x.get("done") else "")   # the word is visible, not a tooltip (jay, 2026-09-21: "Add Done data to …")
        if k2 != k: f.write_text(c[:m.start(1)] + k2 + c[m.end(1):]); dated += 1
# … and as a chip on the card head in notes.html, in the item's dot colour; removed when the stamp goes
h = p.read_text(); CHIP = re.compile(r'<span class="topic-done"[^>]*>[^<]*</span>'); chips = 0
def head_fix(m):
    global chips
    x = by_key.get(m.group(2)); inner = CHIP.sub("", m.group(3))
    if x and x.get("done"):
        ml = "6px" if 'class="topic-date"' in inner else "auto"
        inner += f'<span class="topic-done" title="done" style="flex:0 0 auto;margin-left:{ml};font-size:.66rem;line-height:1.5;color:{x["color"]};border:1px solid currentColor;border-radius:999px;padding:0 6px;font-variant-numeric:tabular-nums">done {x["done"][:10]}</span>'
    if inner != m.group(3): chips += 1
    return m.group(1) + inner + m.group(4)
h2 = re.sub(r'(<li id="([^"]+)">\s*<div class="topic-head">)(.*?)(</div>)', head_fix, h, flags=re.S)
if h2 != h: p.write_text(h2)
print(f"done-states: overall {badge}; badge rewritten on {fixed} page(s); done date written on {dated} page(s), card chips changed {chips}")
print(f"done-states: newest day {latest}, previous day {previous}; relabelled {len(changed)} item(s); duplicate rail entries dropped {dropped}")
# rebuild docs/topics/index.json + index.md (scripts/build-index.py; jay, 2026-09-21: "Let the system hold the index")
import subprocess, sys
subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve().parent / "build-index.py")], check=True)
