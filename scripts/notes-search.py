#!/usr/bin/env python3
"""Answer "have I already learned this?" with a search instead of a memory (jay, 2026-09-21).

    python3 scripts/notes-search.py quick slots
    python3 scripts/notes-search.py --any 토큰화 tokenization
    python3 scripts/notes-search.py --section Tech --status NEW agent

Searches docs/topics/index.json (built by scripts/build-index.py): number, key, English and Korean titles,
tag, type, source, bin, English lead, related numbers and the page's key expressions. Every word must match
somewhere in the item (case-insensitive substring) unless --any is given. Run it before adding an item; if it
prints nothing, the subject is new to the site. Exit status 0 when something matched, 1 when nothing did.
"""
import json, sys, pathlib, argparse
ap = argparse.ArgumentParser()
ap.add_argument("words", nargs="+"); ap.add_argument("--any", action="store_true", help="match if any word matches (default: all)")
ap.add_argument("--section", help="Tech | Theory | Invest | Eng | Life"); ap.add_argument("--status", help="REVISIT | DONE | TODAY DONE | YESTERDAY DONE | IMPORTANT | NEW | PLANNED")
ap.add_argument("--json", action="store_true", help="print matching items as JSON")
A = ap.parse_args()
idx = json.loads((pathlib.Path(__file__).resolve().parent.parent / "docs" / "topics" / "index.json").read_text())
words = [w.lower() for w in A.words]

def haystack(i):
    parts = [str(i.get("no")), i.get("key", ""), i.get("title_en", ""), i.get("title_ko", ""), i.get("tag", ""), i.get("type", ""),
             i.get("source", ""), i.get("bin", ""), i.get("lead", ""), " ".join(i.get("related", [])), " ".join(i.get("vocab", []))]
    return " ".join(p for p in parts if p).lower()

hits = []
for i in idx["items"]:
    if A.section and i["section"].lower() != A.section.lower(): continue
    if A.status and i["status"].lower() != A.status.lower(): continue
    h = haystack(i); m = [w for w in words if w in h]
    if (A.any and m) or (not A.any and len(m) == len(words)): hits.append((len(m), i))
hits.sort(key=lambda t: (-t[0], t[1]["section"], t[1]["no"] or 0))
if A.json: print(json.dumps([i for _, i in hits], ensure_ascii=False, indent=1))
else:
    for _, i in hits:
        extra = " · ".join(x for x in (i.get("type"), i.get("date"), i.get("bin")) if x)
        print(f"{i['section']:6} {i['no']:>5}  [{i['status']}] {i['title_en']}" + (f" — {i['title_ko']}" if i.get("title_ko") else "") + f"  ({i['href']}{'; ' + extra if extra else ''})")
    print(f"-- {len(hits)} item(s) match {' '.join(A.words)!r} (index of {idx['generated']}, {idx['all']} items)" if hits else f"-- nothing matches {' '.join(A.words)!r}: new to the site (index of {idx['generated']}, {idx['all']} items)")
sys.exit(0 if hits else 1)
