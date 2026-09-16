# 2026-09-16 — Dev Notes

Source: jay's request in conversation (screenshot of binji's post "Imagine 'Ethereum, but faster'
… Let's get EIP-8198 into Hegotá": "Add tech item"); no separate task file. Notes live in
`docs/notes.html`, `docs/topics/_nav.js`, and `docs/topics/pocs-<key>.html` (hand-maintained HTML).

### Dev Notes #54: "Quick Slots (EIP-8198) — the change is not 12 → 10 s, it is making slot time a parameter", NEW

- **Cause:** jay pasted the X post about EIP-8198 and asked for it as a tech item.
- **Reasoning:** researched the EIP text, consensus-specs PR #5592, the EF Protocol Hegotá tier post
  (2026-09-07), Ethlabs' Hegotá view, and a review article. The insight worth keeping is that the
  EIP is mostly *not* about speed: it replaces the compile-time slot constant with a per-epoch
  schedule, and the visible work is retuning every slot- or epoch-denominated constant (issuance,
  inactivity leak, blob retention, churn / weak subjectivity, gas per slot) so its wall-clock meaning
  is unchanged. The disagreement is readiness, not direction: EF tier B with four prerequisites and
  a D from client engineering teams for the retuning cascade; Ethlabs S-tier, 10 s in Hegotá,
  "12 s for two more years or 10 s in about a year". For Jayverse the item is a checklist, not a
  feature: the devnet's 1 s Anvil blocks already break any code that converts blocks to time, so
  market close, oracle staleness, keeper timing, and bridge finality must be in seconds or
  `finalized`. Numbering rule kept: done items first, the newest report takes the first not-done
  slot, so this is #54 and the previous 54–225 shift by one (226 total).
- **Change:** `notes.html` — nav entry + card (bilingual copy JSON) at #54, Blockchain section
  renumbered, counters 59/418 overall and 53/226 for the section (the section's own meta counter had
  been left at 222 by earlier inserts; set to 226); `topics/_nav.js` — entry, renumbering, label and
  jump counts; new `topics/pocs-quick-slots-eip-8198.html` from the Alchemy page template with EN
  and KO sections and copy buttons; kicker and prev/next pager rebuilt on all 226 Blockchain pages.
  Also fixed pre-existing drift: from card position 59 on, the card numbers in `notes.html` lagged
  the nav by three (three items had been inserted into the nav without renumbering the cards);
  every card now carries its nav number by key.
- **Result:** working tree on `claude/notes-eip-8198`, branched from the tip of
  `Codex/aa-standards-wallet-matrix` (two commits ahead of `origin/main`, both other-session items),
  uncommitted. Stated as unverified in the item: whether 8198 is scheduled for Hegotá (no decision
  yet), Hegotá's date, and whether 8 s or 10 s lands first.

### Tech Notes #54 correction: the schedule is bookkeeping, not a lever

- **Cause:** jay disagreed with the item's line that the schedule "turns the next cut into a parameter change instead of another fork's worth of refactoring", and with my gloss of it as a mechanism for future cuts.
- **Reasoning:** read PR #5592's own description and `specs/_features/eip8198/beacon-chain.md`. `SLOT_TIMING_SCHEDULE` is an ordered list of eras starting at genesis, each with `EPOCH`, `SLOT_DURATION_MS`, and every intra-slot deadline; "every subsequent entry MUST coincide with a network upgrade", and the PR body says it "is simply a way to loop over historical slot durations" for functions that accumulate time across eras (timestamp ↔ slot), explicitly *not* BPO-style changes between upgrades. The "configuration updates rather than contentious protocol upgrades" line is the EIP's motivation text, which the spec authors walked back. Also corrected: the PR does not scale intra-slot deadlines with the duration (the EIP had them as basis points that do); the values are deferred until testing.
- **Change:** summary paragraph, `SLOT_DURATION_MS` table row, cascade item 4, and the Verified paragraph rewritten in EN and KO; card summary and copy JSON in `notes.html`, and the detail page's lead, body, and copy JSON regenerated from the corrected source text.
- **Result:** working tree, uncommitted, on `main` checkout (the item's branch `claude/notes-eip-8198` is already merged).

### Tech Notes #54 marked done

- jay: "make the 54 done". Dot → RECENTLY DONE (#38bdf8) in `notes.html` and `_nav.js`; counters 54/226 for the section, 60/418 overall.

### Tech Notes #55 (Alchemy app key) marked done

- jay: "make the 55 also done". Dot IMPORTANT → RECENTLY DONE in `notes.html` and `_nav.js`; counters 55/226, 61/418.
