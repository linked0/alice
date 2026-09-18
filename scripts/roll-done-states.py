#!/usr/bin/env python3
"""Apply the TODAY DONE rule (jay, 2026-09-18) to docs/topics/_nav.js and docs/notes.html.

Rule: an item marked done is "TODAY DONE" (midnight blue, #191970) from the moment it is done until the first
item of the *next* day is done. A day starts at 06:00 KST ("done from the 6 a.m. today before the new day's
first one is done"), so every item carries `done` (ISO time, +09:00) and the day bucket is (done - 6h).date().
Items in the previous done-day bucket are "YESTERDAY DONE" (sky blue, #38bdf8; jay, 2026-09-18: "add the
other day done status of which name tells everything"). Older buckets, and items with no `done` time, are plain DONE.
So each new day's first done item rolls everything one step: LATELY → OTHER DAY → DONE.

Also syncs every rail dot in notes.html (colour + title) with _nav.js and removes duplicate rail entries.
Run by scripts/add-tech-item.py after each change; safe to run alone at any time.
"""
import json, re, pathlib, datetime
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
days = sorted({bucket(x["done"]) for s in nav["sections"] for x in s["items"] if x.get("done")}, reverse=True)
latest = days[0] if days else None; previous = days[1] if len(days) > 1 else None
changed = []
for s in nav["sections"]:
    for x in s["items"]:
        if x["label"] in STAGED or (x["label"] == "DONE" and x.get("done")):
            b = bucket(x["done"]) if x.get("done") else None
            want = LATELY if b and b == latest else OTHER if b and b == previous else (DONE_COLOR[s["navId"]], "DONE")
            if (x["color"], x["label"]) != want: x["color"], x["label"] = want; changed.append(x["key"])
    done = sum(1 for x in s["items"] if x["label"] in ("DONE", "TODAY DONE", "YESTERDAY DONE"))
    for j in nav["jump"]:
        if j["id"] == s["navId"].replace("nav-", ""): j["done"], j["all"] = done, len(s["items"])
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
    return m.group(1) + (f'<span class="nav-dot" style="background:{x["color"]};" title="{x["label"]}"></span>' if x else m.group(3))
h = re.sub(r'(<a class="nav-link" href="[^"]*" data-key="([^"]+)">)(<span class="nav-dot" style="background:[^"]*;" title="[^"]*"></span>)', dot_fix, h)
for j in nav["jump"]:
    h = re.sub(r'(<a href="#' + j["id"] + r'"[^>]*>' + re.escape(j["label"]) + r'<b><span class="count-done">)\d+(</span><span class="count-all">/)\d+', lambda m: f'{m.group(1)}{j["done"]}{m.group(2)}{j["all"]}', h, count=1)
    h = re.sub(re.escape(j["label"]) + r' &mdash; done \(\d+\) / all \(\d+\)', f'{j["label"]} &mdash; done ({j["done"]}) / all ({j["all"]})', h, count=1)
    h = re.sub(r'(<article id="' + j["id"] + r'">.*?<span class="count-done">done \()\d+(\)</span> <span class="count-all">/ all \()\d+', lambda m: f'{m.group(1)}{j["done"]}{m.group(2)}{j["all"]}', h, count=1, flags=re.S)
p.write_text(h)
print(f"done-states: newest day {latest}, previous day {previous}; relabelled {len(changed)} item(s); duplicate rail entries dropped {dropped}")
