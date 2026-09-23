# Blockchain Needs HTTPS (Zama) — 2026-09-23

Claims and citations only; the body is not copied (see README.md). jay pasted the piece.

## Provenance

- **Four Pillars**, "Blockchain Needs HTTPS", by **100y**, **2026-08-26**, Crypto / Comment.
  **No URL captured.** Standard disclaimer.

## Claims (unverified here)

- Global e-commerce ~**$6–7 trillion**, ~**20%** of total retail (source given as EMARKETER).
- **Netscape introduced SSL in 1994**; HTTPS via SSL/TLS made browser–server exchange secure. The
  article's point: HTTP was a **general-purpose** protocol first, and HTTPS added a security layer over
  that flexible foundation.
- **Three generalities** a confidentiality layer must scale across: **chain**, **activity**, **asset**.
  - Zcash / Monero: weak on chain and asset generality — chain and native asset designed around
    confidentiality from the start.
  - Tornado Cash: weak on activity generality — primarily transfers.
- **Zama**: FHE-based; **does not build a separate blockchain**; adds a confidentiality layer on top of
  existing public chains; aims at issuance, transfers, DeFi and broader onchain computation over
  encrypted data.
  - **Activity**: *Steakhouse Confidential Prime USDC Vault* — individual deposit sizes and positions
    confidential onchain, built on existing DeFi infrastructure.
  - **Asset**: confidential wrappers on Ethereum for **USDC, USDT, WETH, ZAMA, tGBP, XAUt**.
  - **Chain**: **Polygon (chain ID 137)** appears in Zama's official mainnet onchain contract registry
    on GitHub, with host-side components — **FHEVM Executor, ACL, Input Verifier, KMS Verifier, Protocol
    Config** — not just a bridged token.
- **Explicitly not confirmed**: Zama's existing address documentation still lists Polygon as a
  **testnet** deployment; the article says it would not treat this as an official mainnet launch.
- Polygon context: **Open Money Stack** — stablecoin settlement, cross-border payments, on/off-ramps,
  compliance; Polygon has highlighted confidentiality as an operational requirement for institutional
  payment flows.

## Not in the article

- **No performance or cost figure for FHE anywhere** — no gas multiple, latency or throughput. This
  note's added argument is that HTTPS became universal when its cost approached zero (hardware AES,
  session resumption, Let's Encrypt), so "cost generality" is a fourth requirement the piece omits.
