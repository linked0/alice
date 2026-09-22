#!/usr/bin/env bash
# Serve the repo the way GitHub Pages does, so the local page is the live page (jay, 2026-09-22:
# "this should be work on in the local page also", then "make alice accessible at
# http://100.111.162.0:4173" — the Tailscale address, so the phone can reach it).
#
# Binds 0.0.0.0, not 127.0.0.1, because a server bound to the loopback cannot be reached from another
# device. That also exposes it to whatever LAN this Mac is on. The trade is deliberate and cheap here:
# the repo is public documentation already on github.com/linked0/alice, and the health items in it are
# ciphertext whose key never leaves the browser. Do not add anything to this repo that would make that
# untrue — see docs/topics/raw/README.md.
#
# Firebase sign-in needs an http origin on a domain Firebase knows. localhost, 127.0.0.1 and this
# machine's Tailscale address are all on the authorized list now, so Edit works from any of the three.
# A file:// page never will: the SDK requires an http(s) origin, and it reports that as the same
# auth/unauthorized-domain, which is why serving matters rather than double-clicking the HTML.
#
# Pages serves the repo ROOT, not docs/, so the root is what we serve — otherwise every path here
# would be one segment off from alice.jaylabs.xyz.
set -euo pipefail
PORT="${1:-4173}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Tailscale hands out addresses in the CGNAT block 100.64.0.0/10, so the interface carrying one of
# those is Tailscale. Printed, not bound to, so localhost keeps working when Tailscale is off.
TS="$(ifconfig 2>/dev/null | awk '/inet 100\./ {print $2}' \
      | awk -F. '$2 >= 64 && $2 <= 127 {print; exit}')"

echo "serving ${ROOT}"
echo "  here      http://localhost:${PORT}/docs/notes.html"
[ -n "$TS" ] && echo "  phone     http://${TS}:${PORT}/docs/notes.html"
command -v open >/dev/null && (sleep 1; open "http://localhost:${PORT}/docs/notes.html") &
exec python3 -m http.server "$PORT" --bind 0.0.0.0 -d "$ROOT"
