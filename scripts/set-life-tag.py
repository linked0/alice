#!/usr/bin/env python3
"""Set (or clear) the topic-tag chip on existing items, the way add-tech-item.py writes it for new ones.

    python3 scripts/set-life-tag.py --map tags.tsv [--apply]
    python3 scripts/set-life-tag.py --key <key> --tag Book [--apply]

tags.tsv is "<key>\t<tag>" per line; an empty tag clears the chip. Dry-run unless --apply.

Why this exists (jay, 2026-09-25: "add book or something proper flag for Life items as the Theory
items do like MATH, Algorithms"): add-tech-item.py only writes the chip when it creates or replaces
an item, and re-running it on 40-odd existing Life cards would mean rebuilding every source pair.
The chip lives in exactly three places, so setting it directly is the honest cheap path:

  docs/topics/_nav.js   item["text"], between the topic-no span and the title
  docs/notes.html       the rail <span class="nav-text">…</span>
  docs/notes.html       the card <div class="topic-head">…</div>

Detail pages render their rail from _nav.js, so they need no edit.
"""
import re, json, pathlib, argparse

ap = argparse.ArgumentParser()
ap.add_argument("--map", help="TSV file: <key>\\t<tag>")
ap.add_argument("--key"); ap.add_argument("--tag", default="")
ap.add_argument("--apply", action="store_true", help="write; without it, print what would change")
A = ap.parse_args()

ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs"
pairs = []
if A.map:
    for line in pathlib.Path(A.map).read_text().splitlines():
        if not line.strip() or line.lstrip().startswith("#"): continue
        k, _, t = line.partition("\t"); pairs.append((k.strip(), t.strip()))
if A.key: pairs.append((A.key, A.tag))
if not pairs: ap.error("give --map or --key")

CHIP = re.compile(r'<span class="topic-tag"[^>]*>[^<]*</span>')
NO   = re.compile(r'(<span class="topic-no">\d+</span>)')

nav_path = ROOT / "topics" / "_nav.js"; nav_src = nav_path.read_text()
nav = json.loads(re.match(r'window\.__NAV__=(.*);\s*$', nav_src, re.S).group(1))
by_key = {x["key"]: x for s in nav["sections"] for x in s["items"]}

notes_path = ROOT / "notes.html"; notes = notes_path.read_text()
changed, missing = [], []

for key, tag in pairs:
    item = by_key.get(key)
    if item is None: missing.append(key); continue
    chip = f'<span class="topic-tag" data-tag="{tag}">{tag}</span>' if tag else ""
    before = item["text"]
    item["text"] = NO.sub(lambda m: m.group(1) + chip, CHIP.sub("", before), count=1)
    if not NO.search(before):  # no number span (shouldn't happen) — prepend
        item["text"] = chip + CHIP.sub("", before)

    # notes.html: the rail entry and the card head both start with the same topic-no span for this key.
    hits = 0
    def sub_block(m):
        global hits
        hits += 1
        return NO.sub(lambda n: n.group(1) + chip, CHIP.sub("", m.group(0)), count=1)
    # rail: <a ... data-key="KEY"> … <span class="nav-text">…</span></a>
    notes_new = re.sub(
        r'data-key="' + re.escape(key) + r'">.*?<span class="nav-text">.*?</span></a>',
        sub_block, notes, flags=re.S)
    # card: <li id="KEY"> … <div class="topic-head">…</div>
    notes_new = re.sub(
        r'<li id="' + re.escape(key) + r'">\s*<div class="topic-head">.*?</div>',
        sub_block, notes_new, flags=re.S)
    if hits != 2: missing.append(f"{key} (matched {hits}/2 places in notes.html)")
    notes = notes_new
    changed.append((key, re.sub(r'<[^>]+>', ' ', before).strip()[:40], tag or "(cleared)"))

for k, title, tag in changed: print(f"  {tag:8s} {k:48s} {title}")
if missing: print("\nNOT FOUND / PARTIAL:"); [print("  " + m) for m in missing]
print(f"\n{len(changed)} item(s) would change." if not A.apply else f"\n{len(changed)} item(s) changed.")

if A.apply:
    nav_path.write_text("window.__NAV__=" + json.dumps(nav, ensure_ascii=False, separators=(",", ":")) + ";\n")
    notes_path.write_text(notes)
    print("wrote _nav.js and notes.html — run build-index.py if the index needs refreshing.")
