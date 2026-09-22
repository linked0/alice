# 2026-09-22 — Knowledge Notes (alice) dev notes

Source docs this day's work implements: [`docs/topics/README.md`](../topics/README.md) (the schema),
[`docs/topics/raw/README.md`](../topics/raw/README.md) (the raw layer), and for the first entry the
Gemini briefing at [`docs/topics/raw/2026-09-22-gemini-youtube.md`](../topics/raw/2026-09-22-gemini-youtube.md).
Yesterday's file: [`2026-09-21-dev-notes-history.md`](2026-09-21-dev-notes-history.md).

### Eng #399 pushed, and merge/push becomes standing

- **Cause:** a commit sat unpushed on `main` from 08:08 — Eng #399, a flapping node, for talking about intermittent bugs. It had also gone straight onto `main` rather than through a branch. jay then said: "You can merge and push at your will from now on."
- **Change:** the commit was put on a branch, pushed, `main` pushed, branch deleted — a fast-forward, so the history is identical to a direct push but the shape matches every other change. The standing authorisation is saved to memory; it supersedes the global rule that pushes need an explicit ask, for directed work only. Rewriting published history, force-pushes and deletions still stop and ask.
- **Result:** Eng 399 items, the new one shown at #2375. The worktree branch `claude/number-benchmark` was checked at the same time: fully merged, nothing stranded.

### Tech #72: assistance is optimised to look right

- **Cause:** jay pasted a Gemini summary of an AI Engineer conference talk arguing that today's models fail at unattended automation by design, and asked for it as an item.
- **Reasoning:** the claim worth keeping is not "models are unreliable" but that the unreliability has a named cause you did not choose and cannot see — RLHF scores answers by human preference, so a plausible wrong answer beats an honest "I don't know", and confidence becomes a style rather than a signal. That is yesterday's Tech #72 lesson one level down: there a tool's own "high-confidence" label was not a measurement, here the model's confident tone is not one either, and in both cases the label came from the thing being judged. So the item is built around a calibration harness — fifty known-answer questions, answer plus stated confidence, bucketed and compared against actual accuracy — because a flat curve means there is no threshold to automate behind, and no prompt fixes that. The proposed cure, a third post-training path beside preference and verifiable reward, is a company's direction with no published results and is marked as such.
- **Change:** `docs/topics/pocs-assistance-optimised-to-look-right.html` at Tech #72 (type Talk, bin `deep`, source `gemini`), with a three-target comparison table, the five-step harness, a curve-reading block, the Jayverse landing and 16 key expressions. `raw/2026-09-22-gemini-youtube.md` keeps the citation and the timestamped claims rather than the generated prose, since the URL plus the claims are what make the source reopenable.
- **Result:** Tech 282 items, site total 925. The speaker's name and company as transcribed are flagged unverified — machine transcription garbles names, and the page points at the video rather than asserting them.
