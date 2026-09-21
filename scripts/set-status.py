#!/usr/bin/env python3
"""Change one item's status and rebuild the site (jay, 2026-09-21: "What I really want is to change
the status in the web page").

    python3 scripts/set-status.py --key english-398 --status done
    python3 scripts/set-status.py --key bok-24h-won-settlement-window --status revisit

Why a script and not a database: the status of an item already has one home, and it is different per
section. Eng keeps it in the item's own markdown (`status:` in `docs/topics/english/english-N.md`),
every other section keeps it in `docs/topics/_nav.js`, which the build scripts read. A database would
put the same fact in a second place and the two would drift — the bug that bit the duplicated landing
page on this very day. So this writes to the existing home and re-runs the existing builders; the repo
stays the single source of truth and the published site is regenerated from it.

Statuses: planned | new | important | done | recent | revisit
  recent  = done today (TODAY DONE, midnight blue; rolls to YESTERDAY DONE then DONE)
  done    = done, let roll-done-states.py decide the shade from the stamp
  revisit = done but come back to it (purple, sorts first, counts as done)
A stamp (`done:` / `"done"`) is written for done/recent/revisit and removed for the other three, because
roll-done-states.py buckets the day from that stamp.

Health items are LOCKED and refused: their text is not in the repo (docs/topics/README.md §Health).
"""
import argparse, datetime, json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
NAV = ROOT / "docs" / "topics" / "_nav.js"
KST = datetime.timezone(datetime.timedelta(hours=9))
COLORS = {"planned": ("#64748b", "PLANNED"), "done": ("#22c55e", "DONE"), "recent": ("#191970", "TODAY DONE"),
          "important": ("#ef4444", "IMPORTANT"), "new": ("#eab308", "NEW"), "revisit": ("#a855f7", "REVISIT")}
DONE_LIKE = ("done", "recent", "revisit")

def day_of(stamp):
    """The done-day a stamp falls in: the 06:00 KST boundary used by roll-done-states.py."""
    dt = datetime.datetime.fromisoformat(stamp)
    if dt.tzinfo is None: dt = dt.replace(tzinfo=KST)
    return (dt.astimezone(KST) - datetime.timedelta(hours=6)).date()

def add_pass(history, stamp):
    """Append a pass, but only when it lands on a different done-day than the last one
    (jay, 2026-09-21: a second tap in the same sitting is not a second reading).
    `history` is the list so far, oldest first; returns the new list."""
    out = [s for s in history if s]
    if out and day_of(out[-1]) == day_of(stamp):
        out[-1] = stamp                      # same day: keep one entry, move it to the later time
    else:
        out.append(stamp)
    return out

ap = argparse.ArgumentParser()
ap.add_argument("--key", required=True, help="the item key as it appears in _nav.js (Eng keys look like english-398)")
ap.add_argument("--status", required=True, choices=sorted(COLORS))
ap.add_argument("--done-at", help="ISO time with +09:00; default now (KST). Ignored for planned/new/important")
ap.add_argument("--dry-run", action="store_true")
A = ap.parse_args()

stamp = A.done_at or datetime.datetime.now(KST).strftime("%Y-%m-%dT%H:%M%z")
if len(stamp) >= 5 and stamp[-5] in "+-" and ":" not in stamp[-5:]:
    stamp = stamp[:-2] + ":" + stamp[-2:]          # +0900 -> +09:00, the form the other scripts write

nav = json.loads(re.match(r"window\.__NAV__=(.*);\s*$", NAV.read_text(), re.S).group(1))
found = [(s, x) for s in nav["sections"] for x in s["items"] if x["key"] == A.key]
if not found:
    near = [x["key"] for s in nav["sections"] for x in s["items"] if A.key.lower() in x["key"].lower()][:8]
    sys.exit(f"no item with key {A.key!r}" + (f"\ndid you mean: {', '.join(near)}" if near else ""))
sec, item = found[0]
if item["label"] == "LOCKED":
    sys.exit(f"{A.key} is a Health item and is locked; its text is not in the repo")

title = re.sub(r"<[^>]+>", "", item.get("text", ""))[:70]
print(f"{A.key}  [{sec['navId']}]  {item['label']} -> {COLORS[A.status][1]}   {title}")
if A.dry_run:
    sys.exit(0)

if sec["navId"] == "nav-sec-english":
    # Eng: the markdown is the home. english-notes.py rebuilds _nav.js from it, so editing _nav.js here
    # would be overwritten on the next run.
    md = ROOT / "docs" / "topics" / "english" / f"{A.key}.md"
    if not md.exists():
        sys.exit(f"{md} not found")
    t = md.read_text()
    t, n = re.subn(r"^status: .*$", f"status: {A.status}", t, count=1, flags=re.M)
    if not n:
        sys.exit("no 'status:' line in the header")
    if A.status in DONE_LIKE:
        m = re.search(r"^dones: (.*)$", t, re.M)
        history = [s.strip() for s in m.group(1).split(",")] if m else (
            [re.search(r"^done: (.*)$", t, re.M).group(1).strip()] if re.search(r"^done: ", t, re.M) else [])
        history = add_pass(history, stamp)
        line = "dones: " + ", ".join(history)
        if m: t = t[:m.start()] + line + t[m.end():]
        else: t = re.sub(r"^(status: .*)$", rf"\1\n{line}", t, count=1, flags=re.M)
        if re.search(r"^done: .*$", t, re.M):
            t = re.sub(r"^done: .*$", f"done: {history[-1]}", t, count=1, flags=re.M)
        else:
            t = re.sub(r"^(dones: .*)$", rf"\1\ndone: {history[-1]}", t, count=1, flags=re.M)
        print(f"   passes: {len(history)}")
    else:
        t = re.sub(r"^done: .*\n", "", t, count=1, flags=re.M)
        t = re.sub(r"^dones: .*\n", "", t, count=1, flags=re.M)
    md.write_text(t)
    builder = "english-notes.py"
else:
    item["color"], item["label"] = COLORS[A.status]
    if A.status in DONE_LIKE:
        history = add_pass(item.get("dones") or ([item["done"]] if item.get("done") else []), stamp)
        item["dones"] = history
        item["done"] = history[-1]           # `done` stays the latest, so every existing reader is untouched
        print(f"   passes: {len(history)}")
    else:
        item.pop("done", None); item.pop("dones", None); item.pop("day", None)
    NAV.write_text("window.__NAV__=" + json.dumps(nav, ensure_ascii=False, separators=(",", ":")) + ";\n")
    builder = "reorder-by-status.py"

print(f"--- {builder} ---")
subprocess.run([sys.executable, str(ROOT / "scripts" / builder)], check=True)
# reorder-by-status.py only calls roll-done-states.py when something expired from NEW, so a plain
# status change left the dots, counts, badge and card chips untouched (found 2026-09-21: the data said
# DONE while notes.html still showed PLANNED). roll is idempotent and owns all of those, so run it last.
print("--- roll-done-states.py ---")
subprocess.run([sys.executable, str(ROOT / "scripts" / "roll-done-states.py")], check=True)
