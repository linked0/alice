# Optimum: Rethinking the Blockchain Network Layer — 2026-09-22

Claims and citations only; the article body is not copied (see README.md). jay pasted the piece.

## Provenance

- **Four Pillars**, "Optimum: Rethinking the Blockchain Network Layer", by **c4lvin**, **2026-08-18**,
  Crypto / Issue. **No URL captured.** Standard Four Pillars disclaimer.
- Conflict to note: RLNC was co-invented by **Muriel Médard** (MIT), described as Optimum's CEO's
  co-inventor; the March 2026 revenue research is by "the Optimum team and Professor Medard". The
  analysis and the product share authors.

## Measurements (Optimum's own, unverified here)

- Hoodi testnet average block propagation ~**150 ms** vs a GossipSub baseline of ~**1 s** — and that
  baseline is the **fastest** value from ethPandaOps' **xatu-mimicry**, chosen as conservative.
- Head-to-head: **2.42×** faster average (**2.50×** median); variance **7.88×** lower (**2.81×** on
  std-dev). p50 **132 → 53 ms**; p95 **425 → 170 ms**; std dev **124 → 46 ms**.
- Method: **30 gateways** worldwide, every block propagated through **both** paths simultaneously.

## Validator economics (Optimum + Médard, March 2026)

- Extra slot time comes from the p80 propagation-delay difference.
- **MEV:** 50–150 ms ⇒ **13–16%** average bid-value increase; **20–30%** of cases above 30%;
  **150–190 ETH** cumulative over the analysed week. One slot: a higher bid arrived **60 ms** late.
- **Head votes:** network accuracy **98.6% → 98.8–99.1%** ⇒ **1,000–2,000 ETH**/year. ~**0.6%** of
  slots are missed so the ceiling is ~**99.4%**.
- **APR:** **0.66–1.97%** for the largest operators ⇒ **6–19 ETH**/yr on **32,000 ETH**.
- **~91.6%** of validators use MEV-Boost.
- Bandwidth cost also falls (non-redundant shards).

## Architecture

- **RLNC**: k fragments → n coded shards by random linear combination; any k independent shards
  reconstruct. **Recoding** lets an intermediate node forward before holding the whole message.
- **mump2p** layers RLNC on a standard **libp2p** host, keeping a GossipSub-like mesh. Publish:
  round-robin distinct shards to mesh peers. Receive: discard duplicates, decode at threshold, recode
  and forward above a threshold.
- **Security**: source authentication — hash + publisher signature bound to the message, verified after
  decode; bad-shard senders lose reputation. **No slashing identified.** Inherits libp2p's Noise/TLS
  and Sybil/eclipse defences.
- **Sidecar** ("Optimum Gateway") beside Lighthouse/Prysm/Teku, **in parallel with GossipSub**; attest
  on whichever arrives first; no key access, no role in leader election or signing; sidecar failure is
  a no-op.
- **Adoption**: **40+** Hoodi testnet partners, ~**$30B** of ETH stake — Kiln, P2P.org, Everstake,
  Blockdaemon, Infstones, Luganodes, Ebunker. Mainnet integration underway; waitlist open.
- **Flexnodes** are the accelerator/supply side; a permissionless model is envisioned. Payment via a
  **"Latency Marketplace"** whose pricing, settlement cycle and token role are **undisclosed**.

## Roadmap claims

- Shorter slot times, larger blobs / PeerDAS composition, and validator decentralisation (tail
  compression helps remote nodes most; article cites validator concentration in the "Atlantic
  corridor" and a liveness-coefficient concern).
- Chain-agnostic by design; documentation mentions Solana's **Turbine** and Cosmos/IBC. Solana's
  ~**400 ms** slot makes 100 ms delays more consequential. December 2025 blog post analysed Turbine,
  ShredStream, JetStreamer.
