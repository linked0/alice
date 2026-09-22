# HIP-4 permissionless deployment — 2026-09-22

Claims and citations only; the article body is not copied (see README.md). jay pasted the piece.
Legal characterisations below are the article's, not legal advice.

## Provenance

- **Four Pillars**, "Permissionless Deployment Triples HIP-4 Volume, With Permission the Remaining
  Constraint", by **Ponyo**, **2026-09-03**, Crypto / Issue. **No URL captured.** Standard disclaimer.

## Volume and fees

- Aug 1–28 average **$545,000**/day, never above **$781,000**. Permissionless deployment **29 Aug**:
  **$1.63m** (30th), **$1.97m** (31st), trailing 24h **$2.75m**.
- Daily active traders **1,256 → 1,841**; new accounts **~20/day → 229**.
- Protocol fee on since **15 Aug**, split evenly deployer/protocol, effective **8.75 bps**; daily fees
  **$339** (25 Aug) → **$1,422** (30 Aug).

## Venue shares and the rebate

- Outcome **85%** of last 24h vs Skew **1%**. Identical **500k HYPE** bonds, same **7** validator-approved
  templates. Skew **39** markets listed vs Outcome **43**; **7** live at a time vs **24**.
- Outcome's trade-to-earn: **$1m** total, floor **$200k/month**, paid daily in USDC, both sides of a
  fill, any front end. **$26,594 across 1,104 wallets in 4 days** ≈ **1 cent per dollar traded**.
  *This note's arithmetic: ~11× the 8.75 bps fee.*
- Equities, commodities and one Fed market: **0** on 28 Aug → **38%** of layer volume.

## Settlement design (the article calls this the main axis of differentiation)

- HIP-4 imposes **no single settlement source**; the deployer chooses within an approved template.
- Hyperliquid's own markets: protocol oracle, stake-weighted median of validator submissions that are
  themselves weighted medians of **8** spot venues, refreshed every **3 seconds**.
- Outcome: all **27** live markets against Hyperliquid perp marks over **1–3 seconds**; **10** underlyings
  are TradeXYZ HIP-3 assets whose oracle the HIP-3 deployer publishes itself, with validator review
  triggered only on a **50% intraday move**.
- Skew: index products against **Pyth** over **90 seconds**.

## Unified account

- ~**$13.6bn** open interest across core perps and HIP-3; ~**$7.7bn** daily volume.
- Outcome markets ≈ **3 bps** of the perp volume in the same accounts.
- Portfolio margin: HIP-4 page says it composes; portfolio-margin page omits outcome markets. No reason
  published. Eligibility capped at account values below **$25m**.
- Illustrative (the article's): hedging **1%** of OI with tail contracts near **10 cents** ⇒ ~**$13.6m**
  premium per roll, ~**$2m** daily volume at weekly rolls.

## Sports

- **$189.5m** over the 39-day World Cup, **11 Jun – 19 Jul**; **7.1×** the post-tournament **$684,000**
  daily average. **91%** of the record **$12.05m** session on 27 Jun; **89%** on final day (**$5.52m**).
- Estimated ~**3%** of **$5.81bn** reported World Cup volume across the field, vs **0.05%** of total
  prediction-market volume in the week of 24 Aug. Nil since **20 Jul**.
- None of the **7** templates covers sports; restoration requires a validator vote.

## Regulation (the article's characterisations)

- Dodd-Frank special rule on event contracts in an excluded commodity; enumerated activities include
  gaming. Codified at **Rule 40.11**; CFTC proposed a revision in **June** to define "gaming". Perpetuals:
  CFTC policy statement **29 May**, ordinary review under **Regulation 40.3**.
- Book split: **18** crypto binaries (not an excluded commodity ⇒ outside the special rule, but binary
  options still need a registered board of trade for US persons); **4** referencing gold, silver, WTI;
  **13** referencing securities (S&P 500, synthetic Nasdaq-100, Roundhill Memory ETF, SpaceX, SK hynix,
  Nebius, SanDisk) ⇒ **SEC** exclusive jurisdiction, restated **28 Jan**, joint comment with CFTC **18 Jun**.
- **No currently listed market engages the gaming screen. Sports would be the first.**
- Sports ≈ **90%** of Kalshi's 2025 revenue; CFTC June proposal references sports **143** times, digital
  assets **0**; Kalshi valued at **$22bn**.
- **Third Circuit, April**: federal law preempts state gambling statutes for Kalshi's contracts. CFTC
  litigating against **5** states. **19 Aug**: President said the CFTC was working to bring Hyperliquid
  onshore; HYPE **+11%**; no docket since.
- **Korea blocked Polymarket 18 Aug** as criminal gambling and **rejected** the argument that withdrawing
  Korean-language service and won rails placed it beyond domestic law. Singapore blocked **Jan 2025**.
  Japan: no framework.

## Price of access

- Polymarket bought a DCM outright for **$112m**. Bloomberg, **31 Aug**: Hyperliquid in advanced talks to
  route perps to registered US users via **Bitnomial**, acquired by **Payward** this year for up to
  **$550m**. The **500,000 HYPE** bond ≈ **$42.5m**.
