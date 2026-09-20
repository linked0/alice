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
