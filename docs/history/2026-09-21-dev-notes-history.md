# 2026-09-21 — dev-notes (Knowledge Notes) history

Source docs: `docs/topics/README.md` (item rules), `docs/topics/gemini-checked.md` (Mon/Thu Gemini check log), `docs/topics/english/README.md` (Eng format). Content came from jay's pasted post (source `chat`) and the Gemini briefing `~/Documents/Gemini/YouTube-2026-09-21.md` (source `gemini`).

### Daily checks

- **alice-tech:** no `alice-tech-2026-09-20.md` or `-21.md` at 06:05 KST (latest is 09-18); re-check later in the day if jay asks for items.
- **Gemini folder (Monday):** `YouTube-2026-09-21.md` is new (06:01 KST) — six items, all added below and logged in `gemini-checked.md`.
- **Eng:** one conversation for the day → #37 (below).

### Tech #129: West Africa's first tele-robotic surgery, read as a latency budget

- **Cause:** jay pasted a social post: "BREAKING: Starlink just helped make medical history in Africa… a surgeon near Lagos remotely controlled a robot to remove a cancerous kidney from a patient in Abuja, around 500 km away" — "Add this. And push".
- **Reasoning:** research first (Vanguard, Premium Times, NAN; the surgeon, RoboMed Global, MicroPort's Toumai; the 2025 Fukuoka Starlink telesurgery paper). The press confirms the surgery (2026-09-20, RHV Lagos → Nisa Premier Abuja, Toumai console, right radical nephrectomy, ~3 h, Prof. Obi Ekwenna-Davis) but **no source names Starlink**; the attribution exists only in the post. The item says so, and uses it as the first live case of the galaxy-brain line in Verified and unverified (Tech #125).
- **Change:** `add-tech-item.py --status new --type PoC --source chat` → Tech #129 `nigeria-telesurgery-500km-latency-budget`: the loop budget (capture → encode → transport → decode → render → reaction → command → actuator), the 100–150 ms band from published cases (Lindbergh 2001 ~155 ms; Fukuoka Starlink 2025 ~130 ms), why jitter and dropout matter more than the mean (Eng #35, Tech #96), the on-site team as the fail-safe (microfactory clutch #122, embedded evaluator #128 of yesterday's numbering). Landings: Auditor, Verex, Knowledge Notes, Eng.
- **Result:** Tech 61/276.

### Gemini 2026-09-21: six items — Tech #126–#128, Invest 820, Life 1331–1332

- **Cause:** Monday Gemini check; the briefing had Blockchain 1, Tech 3, Mindset 1, Culture 1.
- **Change (all `--source gemini`, drafted by subagents from `ITEM-INSTRUCTIONS.md`):** Invest 820 Goldstein (BlackRock COO) on tokenization as the third wrapper after the mutual fund and the ETF, with the galaxy-brain test run on the $4T→$8T wallet projection · Tech #126 MoE: sparse vs active parameters, router, load-balancing loss, capacity factor (Mixtral 46.7B/12.9B) · #127 RAG vs long context: rereading tax, attention dilution, hybrid filter-then-attend; the Auditor keeps its rule set whole in context · #128 embeddings, vector DBs, the agent loop and MCP as a primer; the Auditor as an MCP server (`check_rule`, `get_evidence`) · Life 1331 Jocko: discipline from within, reconciled with Santos/Damour (ownership of the next action, not self-contempt) · Life 1332 the Goto island burger shop as a "community living room" — the Culture entry lands in Life by the fallback rule; the design brief for Game #7's street.
- **Result:** Invest 0/21, Life 0/33; `gemini-checked.md` row appended.

### Eng #37 "Start with the latency budget, then the fail-safe"

- **Cause:** the one-conversation-per-day rule; #129 gave the subject.
- **Change:** `docs/topics/english/english-37.md` (Interview, `status: important`): a Zurich medtech system-design interview where Jay sets a ~150 ms end-to-end budget before drawing, moves the question to the p99, proposes a p99-sized jitter buffer, a dead-man hold and an authority floor, and names the surgeon in the room as the fail-safe ("a privilege the link grants and the room can revoke"); three techniques, twelve expressions. Eng 1/37, 12 Important.

### Tech #130: Ethlabs week 13 — Quick Slots, blobs, AA migration flows, FCR

- **Cause:** jay: "https://x.com/ox_shaman/status/2101655774233592281 can read this and add". The X page returns 402 to fetchers, so the article text was pulled through the public tweet API (fxtwitter) — an X Article by Mislav (Ethlabs), 2026-09-20, ~1,070 words, read in full.
- **Reasoning:** the update moves the three Ethereum threads the site tracks (#54 Quick Slots, #72/#79 native AA, #74 delivery chain) one link each, and the author's bags are visible, so it doubles as the second live use of the galaxy-brain reading (#125). Written by hand, type `Essay`.
- **Change:** `add-tech-item.py --status new --type Essay --source chat` → Tech #130 `ethlabs-week13-quick-slots-blobs-aa-migration`: client tier list for EIP-8198 (Teku S, Prysm/Lighthouse A, Lodestar C, Nimbus/Grandine no), PFI → CFI target at the next ACDC in two weeks; L2 blob-demand survey and PeerDAS custody threshold; EIP-8130/8141 traced into three migration flows (Frames, SETCODEFROM, ECDSA key invalidation) plus the cosigner question; FCR gated by RPC providers, zk-provable FCR, decoupled consensus in Lean, three finality speed boosts (1/6, 1/6+, >50% compounded, all research claims). Landings: Rabbit #1 and Wallet #5 (the flows are the next spec), Devnet #6 (expose FCR first), Auditor (finality threshold as a rule with teeth), Knowledge Notes (fork calendar), Eng #4/#16. 26 vocab rows.
- **Result:** Tech 61/277, overall 68/557.

### Tech #131: gadak — Jira cached to one SQLite file, and the empty result that lies to an agent

- **Cause:** jay pasted the gadak landing page (midagedev's local Jira/Confluence cache, v0.24) with "add item". Source `chat`, written by hand from the pasted text — no fetch needed.
- **Reasoning:** the speed table is the headline but not the item. The part worth keeping is the trap the project writes into its own Claude Code skill: Jira translates status and priority names into the account's display language, so an English status name on a Korean account returns **no error and zero rows**, and an agent reads that as "no such issue exists". That generalizes past Jira — any rule that checks for *absence* has to prove the query was well formed before trusting the empty set — so it is filed as a rule for the Auditor, not as a tool review. Type `Product` (first use of that type from this script).
- **Change:** `add-tech-item.py --slot 131 --status new --type Product --source chat` → Tech #131 `gadak-jira-cache-empty-result`: scope by `--projects`/`--spaces` into one SQLite file, reads local and writes Jira-first (nothing queued locally, so no offline reconciliation), the four calls that still hit Jira (attachments, `issue --editmeta`, `fields`, `api`), and the benchmark read honestly — 543→41 ms text search, 4,761→22 ms epic GROUP BY, where the 214× is a statement about pagination, not about SQLite. Landings: alice (the same local-corpus bet, applied to a system jay does not control), Auditor ("an empty result is not a negative answer"), and cache scope as disclosure scope, since an agent that reads the cache sends what it read to its own model. 20 vocab rows.
- **Result:** Tech 61/278, overall 68/558.

### Gotcha: the new-item slot is the end of the NEW run, not the first not-done slot

- **Cause:** the gadak item went in at `--slot 62` first, reading the script's docstring ("a new report takes the first not-done slot"). That put a NEW card above the whole IMPORTANT block.
- **Reasoning:** the section is ordered DONE → IMPORTANT → NEW → PLANNED, and the docstring's "first not-done slot" is the boundary for a *done* report, not for a new one. The check that settles it is where the previous day's items sit: #129 and #130 were at the end of the NEW run, immediately before PLANNED.
- **Change:** `git stash push --include-untracked`, re-ran with `--slot 131`, dropped the stash. Runs now read 62-71 IMPORTANT, 72-131 NEW, 132-278 PLANNED.
- **Result:** correct placement, and the rule to reuse: read the label runs out of `_nav.js` and append to the end of the run matching the item's own status, rather than trusting the slot wording in the docstring.
