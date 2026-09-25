#!/usr/bin/env python3
"""Move items to the front or back of their own status block in _nav.js, then let reorder-by-status.py
renumber everything.

    python3 scripts/move-in-status-block.py --section mindset --to end   key1 key2 …
    python3 scripts/move-in-status-block.py --section mindset --to start key1 key2 …

Why (jay, 2026-09-25: "make place book items as near as possible … I meant book, film, anime"):
numbering is driven by status — REVISIT < done < IMPORTANT < NEW < PLANNED — and that sort is stable,
so the only free variable is the order *within* a status block. Pushing a family of items to the end of
NEW and the related PLANNED ones to the front of PLANNED makes the two groups adjacent across the
status boundary, which is the closest they can get without inventing a status.

Keys given must all share one status. Dry-run unless --apply.
"""
import json, re, pathlib, argparse, subprocess, sys

ap = argparse.ArgumentParser()
ap.add_argument("--section", required=True)
ap.add_argument("--to", choices=["start", "end"], required=True)
ap.add_argument("keys", nargs="+")
ap.add_argument("--apply", action="store_true")
A = ap.parse_args()

ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs"
n = ROOT / "topics" / "_nav.js"
nav = json.loads(re.match(r'window\.__NAV__=(.*);\s*$', n.read_text(), re.S).group(1))
sec = next(x for x in nav["sections"] if x["navId"] == f"nav-sec-{A.section}")
items = sec["items"]
by_key = {x["key"]: x for x in items}
missing = [k for k in A.keys if k not in by_key]
if missing: sys.exit(f"not in section: {', '.join(missing)}")
labels = {by_key[k]["label"] for k in A.keys}
if len(labels) != 1: sys.exit(f"keys span several statuses ({', '.join(sorted(labels))}); move them separately")
label = labels.pop()

moving = [by_key[k] for k in A.keys]                       # keep the order the caller gave
rest   = [x for x in items if x["key"] not in set(A.keys)]
block  = [i for i, x in enumerate(rest) if x["label"] == label]
at = (block[0] if block else len(rest)) if A.to == "start" else ((block[-1] + 1) if block else len(rest))
sec["items"] = rest[:at] + moving + rest[at:]

print(f"{label} block, moved to {A.to}: " + ", ".join(A.keys))
for x in sec["items"]:
    if x["label"] == label:
        mark = "→" if x["key"] in set(A.keys) else " "
        print(f"  {mark} {x['key']}")

if A.apply:
    n.write_text("window.__NAV__=" + json.dumps(nav, ensure_ascii=False, separators=(",", ":")) + ";\n")
    subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve().parent / "reorder-by-status.py")], check=True)
else:
    print("\n(dry run — pass --apply)")
