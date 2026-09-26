#!/usr/bin/env python3
"""Remove one item from Knowledge Notes (jay, 2026-09-25: "Can you merge the book items into one?").

    python3 scripts/remove-item.py --key <key> [--key <key> ...] [--apply]

Written because merging items needs a way to delete them and the repo had none — every other script
only adds or rewrites. Defaults to a DRY RUN; nothing is touched without --apply.

What it removes, per key:
  docs/topics/_nav.js          the item object
  docs/notes.html              the rail <li> (matched by data-key) and the card <li id="key">…</li>
  docs/topics/pocs-<key>.html  the detail page
  docs/topics/vocab/pocs-<key>.md   the key-expressions file

What it KEEPS, on purpose:
  docs/topics/raw/*-<key>.*    the raw layer is append-only. The source an item was written from
                               outlives the item; a merged item's sources must stay reachable.

Afterwards it runs reorder-by-status.py (which renumbers every section and calls roll-done-states.py)
and build-index.py, so numbering, counts and the index are consistent. English items are not handled
here — those are files under topics/english/ and are removed by deleting the .md and re-running
english-notes.py, which renumbers 1..N and will refuse a gap.
"""
import argparse, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent / "docs"

ap = argparse.ArgumentParser()
ap.add_argument("--key", action="append", required=True, help="item key, repeatable")
ap.add_argument("--apply", action="store_true", help="actually write; without it this is a dry run")
A = ap.parse_args()

navjs, notes = ROOT / "topics" / "_nav.js", ROOT / "notes.html"
nav_text = navjs.read_text()
nav = json.loads(re.match(r"window\.__NAV__=(.*);\s*$", nav_text, re.S).group(1))
html = notes.read_text()
lines = html.split("\n")

missing = []
for key in A.key:
    found_nav = any(x["key"] == key for sec in nav["sections"] for x in sec["items"])
    if not found_nav:
        missing.append(key)
if missing:
    sys.exit(f"remove-item: not in _nav.js: {', '.join(missing)}. Nothing was changed.")

plan = []
for key in A.key:
    # rail <li>: exactly one line carries data-key="key"
    rail = [i for i, l in enumerate(lines) if f'data-key="{key}"' in l]
    # card <li id="key"> … </li>
    starts = [i for i, l in enumerate(lines) if l.strip().startswith(f'<li id="{key}">')]
    card = None
    if len(starts) == 1:
        for j in range(starts[0] + 1, min(starts[0] + 40, len(lines))):
            if lines[j].strip() == "</li>":
                card = (starts[0], j); break
    page = ROOT / "topics" / f"pocs-{key}.html"
    vocab = ROOT / "topics" / "vocab" / f"pocs-{key}.md"
    plan.append(dict(key=key, rail=rail, card=card, page=page.exists(), vocab=vocab.exists(),
                     page_path=page, vocab_path=vocab))
    print(f"  {key}")
    print(f"    rail <li>   : {'line ' + str(rail[0] + 1) if len(rail) == 1 else '!! ' + str(len(rail)) + ' matches'}")
    print(f"    card <li>   : {'lines %d-%d' % (card[0] + 1, card[1] + 1) if card else '!! not found'}")
    print(f"    detail page : {'yes' if page.exists() else '!! missing'}")
    print(f"    vocab       : {'yes' if vocab.exists() else '(none)'}")

bad = [p["key"] for p in plan if len(p["rail"]) != 1 or not p["card"]]
if bad:
    sys.exit(f"remove-item: could not locate notes.html blocks cleanly for {', '.join(bad)}. Nothing was changed.")

if not A.apply:
    print("\nDRY RUN — nothing written. Re-run with --apply.")
    sys.exit(0)

drop = set()
for p in plan:
    drop.add(p["rail"][0]); drop.update(range(p["card"][0], p["card"][1] + 1))
notes.write_text("\n".join(l for i, l in enumerate(lines) if i not in drop))

keys = set(A.key)
for sec in nav["sections"]:
    sec["items"] = [x for x in sec["items"] if x["key"] not in keys]
navjs.write_text(re.sub(r"window\.__NAV__=.*;\s*$", "window.__NAV__=" + json.dumps(nav, ensure_ascii=False) + ";\n",
                        nav_text, flags=re.S))

for p in plan:
    if p["page"]: p["page_path"].unlink()
    if p["vocab"]: p["vocab_path"].unlink()

print(f"\nremoved {len(A.key)} item(s); raw/ files kept. Rebuilding…")
subprocess.run([sys.executable, str(HERE / "reorder-by-status.py")], check=True)
subprocess.run([sys.executable, str(HERE / "build-index.py")], check=True)
