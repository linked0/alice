#!/usr/bin/env python3
"""Apply the RECENTLY DONE rule (jay, 2026-09-23) to docs/topics/_nav.js and docs/notes.html.

Rule: an item marked done is "RECENTLY DONE" (blue, #0284c7) while its done-day is either the newest
done-day or the one before it; older buckets, and items with no `done` time, are plain DONE (#22c55e).
A day starts at 06:00 KST ("done from the 6 a.m. today before the new day's first one is done"), so every
item carries `done` (ISO time, +09:00) and the day bucket is (done - 6h).date(). Each new day's first done
item rolls everything one step: RECENTLY → RECENTLY → DONE.

Was TODAY DONE (midnight blue #191970) + YESTERDAY DONE (sky blue #38bdf8) until 2026-09-23, when jay
merged them: "too many colors are confusing so Merge Yesterday and Today as Recently". Two done-states
differing only by a day cost two hues and told the rail nothing the `done YYYY-MM-DD` chip does not.
The merged state was first drawn a deep green (#15803d) to keep recency inside the DONE hue and free blue
entirely; jay then chose blue for it after all ("How about use blue for recently except the revisit"), so
RECENTLY DONE is #0284c7 and REVISIT keeps its purple. Net effect: one blue instead of two, and DONE is
one colour in every section, since the #0284c7 Theory/Invest used for DONE moved to #22c55e on the way
through. #191970 and #38bdf8 stay unused.

REVISIT (purple, #a855f7; jay, 2026-09-21) is a done item kept for a later reminder: it is never relabelled here and counts as done.
Also syncs every rail dot in notes.html (colour + title) with _nav.js and removes duplicate rail entries.
Run by scripts/add-tech-item.py after each change; safe to run alone at any time.
"""
import json, re, pathlib, subprocess, sys, datetime
ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs"
DONE_COLOR = dict.fromkeys(("nav-sec-blockchain", "nav-sec-fundamentals", "nav-sec-invest", "nav-sec-mindset", "nav-sec-english"), "#22c55e")   # one DONE colour everywhere (jay, 2026-09-23): Theory/Invest used #0284c7, and blue is now reserved
RECENT = ("#0284c7", "RECENTLY DONE")
# One colour per label, enforced on every run (jay, 2026-09-23: "too many colors are confusing").
# Six Theory items were still #0284c7 and one Invest item #f59e0b — drift from hand edits and older
# generators, invisible in any single page but exactly what makes a palette feel noisy.
PALETTE = {"REVISIT": "#a855f7", "IMPORTANT": "#ef4444", "NEW": "#eab308", "PLANNED": "#64748b"}
STAGED = ("TODAY DONE", "YESTERDAY DONE", "RECENTLY DONE")   # old labels stay here so an existing page rolls forward on the first run
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
        if x["label"] in STAGED or x["label"] == "DONE":   # unstamped DONE items too — they kept the old per-section blue
            b = bucket(x["done"]) if x.get("done") else None
            want = RECENT if b and b in (latest, previous) else (DONE_COLOR[s["navId"]], "DONE")
            if (x["color"], x["label"]) != want: x["color"], x["label"] = want; changed.append(x["key"])
    for x in s["items"]:
        c = PALETTE.get(x["label"])
        if c and x["color"] != c: x["color"] = c; changed.append(x["key"])
    done = sum(1 for x in s["items"] if x["label"] in ("DONE", "RECENTLY DONE", "REVISIT"))   # REVISIT never rolls; it counts as done (jay, 2026-09-21)
    for j in nav["jump"]:
        if j["id"] == s["navId"].replace("nav-", ""): j["done"], j["all"] = done, len(s["items"])
# REVISIT keeps its label and purple dot, but the Recently button must still find it by its stamp
# (jay, 2026-09-21: "Today does not show anything" … "today is KST 09-21"): `day` = "recent" on the item, rendered as data-day on the dot.
for s in nav["sections"]:
    for x in s["items"]:
        b = bucket(x["done"]) if x["label"] == "REVISIT" and x.get("done") else None
        day = "recent" if b and b in (latest, previous) else None
        if day: x["day"] = day
        else: x.pop("day", None)
# Daily closing log (jay, 2026-09-22: the grey badge still read 2026-09-17). The rule used to be
# manual — "append yesterday's close, then change today's counters" — and it went five days
# unfollowed, so the badge was comparing today against a week ago. Upserting TODAY's totals on every
# run removes the rule: by the end of a day the entry holds that day's closing numbers, and tomorrow
# it is automatically "the latest entry dated before today", which is what the badge reads. A day
# with no work leaves no entry, so the badge falls back to the last day that had any — and its
# tooltip names the date, so that is visible rather than misleading.
_today = datetime.datetime.now(KST).date().isoformat()
_prog = nav.setdefault("progress", [])
_prog[:] = sorted([e for e in _prog if e.get("date") != _today] + [{"date": _today, "done": sum(j["done"] for j in nav["jump"]), "all": sum(j["all"] for j in nav["jump"])}],
                  key=lambda e: e["date"])
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
# The pass count rides on data-times only, never in `title`: the rail filters compare title exactly
# ("NEW", "REVISIT", …), so appending anything to it would silently break them for a repeated item.
def dot_fix(m):
    x = by_key.get(m.group(2))
    return m.group(1) + (f'<span class="nav-dot" style="background:{x["color"]};" title="{x["label"]}"'
                         + (f' data-day="{x["day"]}"' if x.get("day") else "")
                         + (f' data-times="{len(x["dones"])}"' if len(x.get("dones") or []) > 1 else "")
                         + '></span>' if x else m.group(3))
h = re.sub(r'(<a class="nav-link" href="[^"]*" data-key="([^"]+)">)(<span class="nav-dot" style="background:[^"]*;" title="[^"]*"(?: data-day="[^"]*")?(?: data-times="[^"]*")?></span>)', dot_fix, h)
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
