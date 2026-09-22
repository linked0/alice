# Ethlabs weekly update, week 13 — 2026-09-22

Claims and citations only; the body is not copied (see README.md). jay pasted the piece.
A protocol team's own progress note: read every item as an intention, not a result.

## Provenance

- **Ethlabs** weekly update, week 13, by **Julian Ma**, **2026-09-21**. **No URL captured.**

## Quick Slots (EIP-8198)

- Ecosystem article by **Binji** and **Barnabé** with quotes from **20+** teams; argues for groundwork
  in **Hegotá** and an initial reduction **12 → 10 seconds**.
- Client tier lists for Hegotá inclusion: **Teku S**, **Prysm A**, **Lighthouse A**, **Lodestar C**,
  **Nimbus** and **Grandine** prefer not to include.
- Status **"Proposed for Inclusion"**; aiming for **"Consider for Inclusion"** at the next ACDC in two
  weeks. Specs being completed (review by Jihoon Song, EF Protocol CL Specs); **Terence Tsao** (Prysm)
  prototyping.

## Blobs

- **Ansgar's framing:** "while we may not be limited by the current capacity, we may be limited by
  unclear expectations on future capacity."
- Caspar, Derek, Francesco planned an **L2 survey** of actual and expected blob demand feeding a report
  on where targets should go and when; **Derek** started outreach; survey **not yet sent**.
- Francesco also working on a blob-capacity report and a proposal to increase the **PeerDAS custody
  threshold**.

## Native account abstraction

- **EIP-8130** and **EIP-8141** previously reconciled; focus moved to migration flows.
- **Ansgar** identified gaps "that only show up when you trace a real account through them".
- **Julian** owns mapping the flows: existing accounts migrating into **Frames**, delegation via
  **SETCODEFROM**, invalidating a compromised or retired **ECDSA** key. Output is a
  **personas-and-user-stories** draft for wallets.
- Open design question: whether **cosigners** belong in a new portable-account standard across 8130 and
  8141, or sit alongside it.

## FCR and finality

- **FCR:** **RPC providers are the adoption gate**. Implementation guidance being written covering
  interaction with the justification-based **`safe`** tag.
- Francesco found a path to proving a block is fast-confirmed with **succinct zk proofs**, while
  extending FCR to weaker observer-network assumptions; modified **Lean** proofs in hand. Derek
  exploring product opportunities.
- **Decoupled consensus:** all properties currently formally verified; Lean repo pending cleanup and
  audit before publication.
- **Three potential finality speed-ups:** (1) check the **2/3** threshold every slot instead of every
  **6.4 minutes** ⇒ ~**1/6** reduction; (2) heavier validators vote first ⇒ another **1/6** or more;
  (3) process **justification** early too ⇒ compounds to **>50%** overall.

## Also

- Derek, Binji and Julian appeared on the **Milk Road** show.
- Next week: ACDC prep for Quick Slots, sending the DA demand survey, AA migration flows into a
  wallet-support plan, liveness for the finality model, FCR RPC guidance.
