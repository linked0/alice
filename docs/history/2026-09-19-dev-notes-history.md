# 2026-09-19 — dev-notes (Knowledge Notes) history

Source docs: `docs/topics/README.md` (rules: Key expressions, landing section, status roll, section numbering), `docs/topics/english/README.md` (Eng format), memory rules for the daily alice-tech read and the one-conversation-per-day Eng rule. Items came from jay's pasted video briefings (source `chat`), so no task/design file is the origin of the content itself.

### Daily checks

- **alice-tech:** `alice-tech-2026-09-19.md` does not exist (Saturday, no morning report). Yesterday's file (09-18) still has two unused candidates: Four Pillars (순유동성 — the indicator that explained nothing this week) and 서비스 (npm 공급망 위생: `pnpm audit`, `--frozen-lockfile`, Dependabot). They stay in play. jay's pastes won for every item today.
- **Gemini folder:** not due (Saturday; last check 2026-09-18).
- **Eng:** one conversation for the day → #35 (below).

### Tech #96–#102: seven items from jay's pasted video briefings

- **Cause:** jay pasted seven YouTube briefings over the evening ("add items in detail", "add this", "add this also with your new researched information", "add also") and said "you can push it".
- **Reasoning:** all seven are engineering talks, so Tech (NEW) rather than Life or Invest; jay asked which category and number the Shopify one got (Tech, #98). Homa, the AI-engineer roadmap, Shopify and the Blender demo were written by hand; Microduck, the ADK voice agent and MLflow were drafted by parallel subagents from `scratchpad/ITEM-INSTRUCTIONS.md` and validated (headings, summary/meta blocks, ≥12 vocab rows). Microduck used fresh web research (TechCrunch, The Register, Pollen's page, 2026-08-27/28 coverage) as jay asked.
- **Change:** `add-tech-item.py --status new --source chat --date 2026-09-19` × 7, slots 96–102 (first planned slot, so they sit at the end of the NEW block):
  - #96 `homa-receiver-driven-transport` — Ousterhout's Homa: message/RPC transport, receiver-driven grants, SRPT, switch priority queues; p99 of short messages 13× lower than TCP in the talk's benchmark.
  - #97 `ai-engineer-builds-the-car` — IBM Technology's three-tier AI-engineer roadmap; judgment about architecture as the scarce skill.
  - #98 `shopify-six-decisions` — 헤이제임스 on Shopify's six decisions; fix the tool instead of replacing it; reverse a bet when its premise dies.
  - #99 `vibe-modeling-blender-mcp` — AZTechnology: GPT 6 + Blender MCP builds and self-inspects the Sagrada Família in 28:49.
  - #100 `microduck-open-source-biped` — Pollen Robotics / Hugging Face Microduck, $399 sim-to-real RL biped.
  - #101 `adk-gemini-live-voice-agent` — Google ADK + Gemini Live: open stream not pipeline, queue decoupling, `send_realtime` vs `send_content`, Interrupted events.
  - #102 `mlflow-tracing-llm-as-judge` — IBM Technology: four silent failures, traces/spans, LLM-as-a-judge, evaluation as a CI gate.
  Each page has Key expressions (18–22 rows incl. acronyms) and "Where it lands in Jayverse"; the label "Foundations" in the drafts was replaced by Theory.
- **Result:** Tech 61/248, overall 68/490; index card now points at #72 (first NEW); rail = card = kicker = nav verified for every item.

### Eng #35 "The mean is fine. Which percentile hurts?"

- **Cause:** the one-conversation-per-day rule; today's items made tail latency the natural subject.
- **Change:** `docs/topics/english/english-35.md` (Interview): a Berlin payments system-design interview where Jay rejects the mean, asks for p99 per region, names two hypotheses in check order (FIFO queue behind large payloads; a fixed-timeout retry), states the falsifying condition, and proposes p99 next to the mean on the dashboard; three techniques, eleven expressions. Built with `english-notes.py` (Eng 1/35).
