#!/usr/bin/env bash
# Serve the repo the way GitHub Pages does, so the local page is the live page (jay, 2026-09-22:
# "this should be work on in the local page also").
#
# Why a script rather than just opening the file: Firebase sign-in needs an http origin on a domain
# Firebase knows. A file:// page and http://127.0.0.1 both fail — and both report the same
# auth/unauthorized-domain, which is why it looked like one bug. `localhost` is authorized by
# default, so serving here and browsing to localhost is the whole fix. Use `localhost`, not
# 127.0.0.1 — they are the same machine but not the same origin, and only the name is authorized.
#
# Pages serves the repo ROOT, not docs/, so the root is what we serve — otherwise every path here
# would be one segment off from alice.jaylabs.xyz.
set -euo pipefail
PORT="${1:-4173}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
URL="http://localhost:${PORT}/docs/notes.html"
echo "serving ${ROOT} → ${URL}"
command -v open >/dev/null && (sleep 1; open "$URL") &
exec python3 -m http.server "$PORT" --bind 127.0.0.1 -d "$ROOT"
