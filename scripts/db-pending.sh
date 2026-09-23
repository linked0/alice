#!/usr/bin/env bash
# What is sitting in Firestore that the repo has not folded in yet (jay, 2026-09-23).
#
# The status overlay writes a document per item whenever a status is changed from a phone or browser.
# The built pages stay the truth, so those documents are a *queue*: they describe changes the repo has
# not applied. Nothing announced that the queue was non-empty, which is how two "done" taps from
# 2026-09-21 sat unapplied for two days while the public site kept showing 71 instead of 73.
#
# Signed out — which is every visitor, and jay on any page he has not tapped Edit on — the site shows
# the built numbers. So a queue entry is invisible to almost everyone, including jay most of the time.
# This is the thing to run.
set -euo pipefail
P=doubletree-498007
T=$(gcloud auth print-access-token)
for C in status health; do
  echo "--- $C"
  curl -s -H "Authorization: Bearer $T" \
    "https://firestore.googleapis.com/v1/projects/$P/databases/(default)/documents/$C?pageSize=100" |
  python3 -c '
import sys, json
d = json.load(sys.stdin); docs = d.get("documents", [])
if not docs: print("  (empty — nothing waiting)"); raise SystemExit
for x in docs:
    f = x.get("fields", {})
    v = {k: (list(val.values())[0] if isinstance(val, dict) else val) for k, val in f.items()}
    print(" ", x["name"].split("/")[-1], "->", str(v)[:110])
print(f"  {len(docs)} document(s)")'
done
echo
echo "To apply one:  python3 scripts/set-status.py --key <item> --status <status> --done-at <ISO+09:00>"
