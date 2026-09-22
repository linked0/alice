# Gemini briefing — AI Engineer conference talk on why assistance does not become automation

Source: YouTube, https://www.youtube.com/watch?v=cJ0EOzey--o — a talk at the AI Engineer conference.
Collected: 2026-09-22, jay pasted a Gemini summary of the video into chat. The video itself was not
fetched here. Per docs/topics/raw/README.md this file is append-only.

Note on what is and is not recorded below. The raw layer exists so a source can be reopened rather than
re-remembered, and for a talk the URL plus the timestamped claims do that job. So this file keeps the
citation, the speaker's claims with their timestamps, and the numbers — not the generated prose of the
summary itself.

Attribution as transcribed, and UNVERIFIED from here: the summary names the speaker "Diego Almeida"
and his company "Typesafe", and the video title as given renders the company as "Jev". Machine
transcription garbles names routinely, so the item treats the person and company as unconfirmed and
cites the URL instead. Anyone checking should watch the video.

## Claims, with the timestamps the summary gives

- 01:02 — speaker says he co-authored GPT-4, ChatGPT and InstructGPT/RLHF; his team pioneered modern post-training.
- 01:27 — describes himself as one of the few inside OpenAI critical of ChatGPT; argues small early algorithmic design choices produced systemic limits in today's AI.
- 02:13 — camp one: models crush NLP benchmarks, solve open maths problems, agent runtimes expanding fast.
- 02:44 — camp two: overhyped bubble, little enterprise value, mostly chat widgets and point assistants.
- 04:00 — the paradox: models crack advanced benchmarks yet fail mundane tasks such as routine customer-service decisions, so businesses still staff humans.
- 04:34, 04:46 — the cause is the optimisation target: chat and coding assistants are built to please the human in the loop.
- 05:03 — real enterprise work needs the model to run unattended in the background, which current models do not do safely.
- 05:13 — Lesson 1: today's AI is good at human-in-the-loop assistance and fails at high-stakes unattended automation.
- 05:37 — businesses push the cost onto the end user (more documentation) rather than let AI make consequential decisions.
- 06:03, 06:23 — nearly all foundation models use RLHF, which optimises human preference and engagement, not autonomous correctness.
- 07:05 — consequence: overpromising and sycophancy by design; plausible, agreeable, confident answers beat admitting uncertainty.
- 07:42 — the example given: politely praising fart sound effects as an "atmospheric soundscape".
- 08:14 — Lesson 2: models are optimised for assistance, so when wrong they are engineered to look right.
- 10:19 — B2B SaaS architecture largely unchanged since 2019; chat widgets bolted onto existing software.
- 11:04 — lowering the cost of boilerplate automates software generation; it does not make software more expressive, reliable or autonomous.
- 12:24 — Lesson 3: the next paradigm must move from human-pleasing assistance to genuine automation.
- 14:32 — pre-training is not the bottleneck; it compresses human knowledge well. Post-training is where the problem is.
- 15:05 — the reward model carries an asymmetry, likened to GAN dynamics, that penalises low confidence and rewards confident answers, encouraging mode collapse and hallucination.
- 16:23 — RLHF optimises human preference; RLVR optimises verifiable correctness on benchmarks such as maths and unit tests.
- 16:30 — his company is building a third post-training path aimed at calibrated decision-making and reliability, with a redesigned post-training API and execution stack for dependable automation rather than conversation.
