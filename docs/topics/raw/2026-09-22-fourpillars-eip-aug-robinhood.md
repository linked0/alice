# Monthly EIP Aug 2026 + Robinhood Chain's L2 dilemma — 2026-09-22

Claims and citations only; the article body is not copied (see README.md). jay pasted the piece.

## Provenance

- **Four Pillars**, "Monthly EIP - Aug 2026 (ft. What Robinhood Chain's Success Reveals About L2 and
  Ethereum's Dilemma)", by **Jay**, **2026-09-10**, Tech / Article. **No URL captured.**
- Disclaimer on the page: the author may hold positions; Four Pillars may hold investments in assets
  or protocols discussed; FP Validated may operate nodes in networks discussed.
- EIP data said to be collected from the official EIP, ERC and RIP GitHub repositories.

## EIP claims (all unverified here; 8000-series are drafts)

- **10** new EIPs in August (down 14 from July); **25** existing EIPs changed status; **none** withdrawn.
- New Core: **EIP-8321** hash-chain RANDAO (BLAKE3 chain, `mix = blake3(mix + reveal)`, active after 3
  epochs, PREVRANDAO format unchanged); **EIP-8347** offline MPT→PBT migration (ANCHOR_BLOCK snapshot,
  BALs from EIP-7928 to apply post-anchor changes, shadow roots before PBT_ACTIVATION_FORK, **~300 GB**
  extra storage during transition); **EIP-8371** RowDAS (128 row subnets, 64 of 128 cells to
  reconstruct, ~12,000 nodes ⇒ ~94 per subnet, KZG-verified before relay); **EIP-8390** remove the sync
  committee (512 validators, ~27h rotation → ZK proof of full-set finality; issuance falls ~**3.125%**
  since SYNC_REWARD_WEIGHT = 2/64 is not redirected; **does not say who generates or funds the proofs**).
- Also new: EIP-8363 tapered issuance burn, EIP-8368, EIP-8372.
- New ERCs: **ERC-8349** Cento index-based multi-facet proxy (1-byte index, up to 256 facets, vs
  ERC-2535 selector→facet; recommends rejecting EIP-7702 delegated accounts as facets); **ERC-8187**
  Token Puller (`approvePull`/`pullFrom`/`maxPullable`, EIP-712 permit, transferable allowances;
  **not audited**, ERC-1271/6492 verification incomplete); ERC-8354 confidential agent policy verdicts.
- Advanced: EIP-4444 (history expiry), EIP-7732 (ePBS), EIP-8025 (stateless validation via execution
  proofs), EIP-8037 (state gas), EIP-8070 (sparse blobpool), EIP-8189 (BAL-based state sync).
- EF in August: **Platåberget** public testnet (17 Aug) for Glamsterdam — ePBS, BALs, gas repricing;
  gas-repricing analysis against historical mainnet data (24 Aug); **WEBCAT** frontend integrity
  support (5 Aug); **better.codes** formal-verification challenge for post-quantum SNARKs (20 Aug).

## Robinhood Chain claims

- **>600 million** transactions since late April; **~$49,000** total paid to Ethereum, **~$370/day**.
- **3 September**: ~**$4.5 million** in fees collected, ~**$400** paid to Ethereum.
- **L2BEAT** classifies it **"Other"**, not Stage 0–2. Challengers limited to **Offchain Labs** and
  **Alchemy**; centralised sequencer can invalidate a force-included transaction; **8-member Security
  Council**, **7 signatures**, **no waiting period**.
- Gas rose roughly **25× in 11 days**; no priority fees, so ordinary users paid the higher base fee.

## Sources

- The pasted article (URL not captured). Figures attributed by the article to L2BEAT and to "a separate
  onchain analysis" which it does not name.
