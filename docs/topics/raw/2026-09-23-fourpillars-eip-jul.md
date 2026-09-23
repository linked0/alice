# Monthly EIP Jul 2026 + the issuance governance debate — 2026-09-23

Claims and citations only; the body is not copied (see README.md). jay pasted the piece.

## Provenance

- **Four Pillars**, "Monthly EIP - Jul 2026 (ft. What the Issuance Debate Reveals About Ethereum
  Governance)", by **Jay**, **2026-08-28**, Tech / Article. **No URL captured.** Standard disclaimer.
  EIP data from the official EIP, ERC and RIP GitHub repositories.

## Counts

- **24** new EIPs in July (up 14 from June); **16** existing proposals changed status — **15** advanced,
  **1** withdrawn (**EIP-2542**).

## Core / networking

- **EIP-8243** batched attestations: ~**31,000** attestations per slot at ~1M validators.
  `WireAttestation = Union[SingleAttestation, BatchAttestation]`, selectors 0x00 / 0x01. Validators sign
  a **batch_seal** over (slot, committee_index, batcher); batcher signs aggregation_bits separately.
  Anti-spam by novelty: nodes track `seen_attesters` / `seen_batchers` per (slot, committee_index,
  data_root) and only propagate a batch containing at least one unseen attester. Onchain Attestation
  format and `process_attestation` unchanged. **Caveat:** may reveal that validators share an operator;
  DVT/LST integration unvalidated.
- **EIP-8295** (period-based) vs **EIP-8296** (fixed cutoff) state tiering, both building on **EIP-8188**
  (`last_written_block`). Surcharges on rewriting Inactive state; charged as regular gas, **not refunded
  on revert**; new slots/accounts exempt (they fall under EIP-8037 creation costs). Neither is state
  expiry — Inactive state stays in the state root. Open caveat: **not-written is not not-read**.
- **EIP-8297** Partitioned Binary Tree: merges account and storage trees; zone byte 0x00 header / 0x01
  code / 0xFF storage; LeafNode and BranchNode only; drops RLP; **BLAKE3 provisional**, final hash
  undecided; first 64 storage slots under the account header stem; code in **31-byte** chunks stored by
  `code_hash`. Migration handled separately by **EIP-8347**.
- **EIP-8292** post-quantum attestation aggregators: XMSS-family signatures ~**1.17 KiB** each, no BLS
  aggregation. Dedicated opt-in aggregator role; leaf aggregation via **leanVM**; proposer combines to a
  block-level proof, **MAX_ATTESTATIONS_DATA = 8**. Benchmarks: ~**227 KiB** for 1,000 signatures;
  generation ~**11 s on 2 cores** vs ~**2.6 s on 16**. **No protocol incentive defined** for the extra
  compute; leanVM soundness becomes a new consensus assumption.
- Others: EIP-8219, 8282, 8298, 8310, 8311, 8333, 8337; EIP-8289, 8304.

## Application / accounts

- **ERC-8286** modular accounts for frame transactions: `validateFrame` as the EIP-8141 counterpart to
  `validateUserOp`; ERC-7579 validators are module type **1**, frame validators type **11**.
  `approvalMode` returns 0x1 (pay gas), 0x2 (execute), 0x3 (both); the **account** makes the final
  APPROVE call. **Caveat:** a SENDER frame does not re-check each call after APPROVE_EXECUTION.
- **ERC-8262** zero-knowledge compliance oracle: **nine** circuit types; COMPLIANCE (0x01) takes signals
  and weights from up to **eight** providers as **private inputs** and reveals only `meets_threshold`;
  PATTERN (0x03) keeps up to **16** transactions private. `proofHash = keccak256(abi.encodePacked(proof,
  proofType, block.chainid, address(this)))` binds proof to chain and oracle. Default TTL **24 hours**;
  `getHistoricalProof()` retains expired records.
  **The admission:** in base COMPLIANCE (0x01) and RISK_SCORE (0x02) the `signals[]` array is the user's
  **private witness**, so the circuit proves the inputs meet a threshold, **not** that they came from a
  legitimate AML provider. COMPLIANCE_SIGNED (0x07) / RISK_SCORE_SIGNED (0x08) verify a registered
  provider's secp256k1 signature inside the circuit; COMPLIANCE_MULTI_SIGNED (0x09) can require
  threshold_m of up to **five** providers. Trust levels named: **self-attested, provider-attested,
  credential-attested**.
- **ERC-8325–8330**: six RWA interfaces — anchors (`anchorId = keccak256(abi.encode(legalHash,
  evidenceHash))`), document bundles (`bundleHash`, history per (subjectId, role)), transfer-route
  policy ((sourceDomain, destinationDomain, assetClass), directions configured independently),
  append-only regulatory events (corrections via `correctsIndex`/`correctedByIndex`, never deletion),
  impact metrics, and NAV streams (valuationTimestamp vs publishedAt; optional lower-median aggregation).
  **None proves the underlying document is genuine or the claim enforceable.**
- Advancing: ERC-1450 (registered Transfer Agents control security-token transfers), ERC-1613 (relay gas
  sponsorship / GSN), ERC-8161, ERC-8196 (AI agents constrained to owner-defined policies), EIP-7708,
  EIP-7928 (BALs), EIP-7981, EIP-7997.

## Ethereum Foundation, July

- **1 July**: Global Policy Strategy published "Ethereum Basics for Governments and Institutions".
- **10 July**: Consensus team published a survey of rollups, bridges, payment services, wallets, solvers,
  oracles, staking providers and institution-facing teams on reducing finality from ~**13–19 minutes**;
  proposes separating fork choice from finality and shortening incrementally.
- **29 July**: **pcaversaccio** (SEAL 911 co-founder) joined the board, bringing it to four alongside Aya
  Miyaguchi, Vitalik Buterin and Patrick Storchenegger.

## The issuance debate

- **EIP-8363 Tapered Issuance Burn (TIB)**: burn a rising share of validator rewards as the staking
  ratio rises, reducing net yield to zero beyond a threshold.
- Article's objection is **process**: proposed before agreement on the security budget or validators'
  future role, without prior discussion among stakers, infrastructure providers, DeFi protocols and
  institutions — and submitted **two days before** the Hegotá PFI discussion.
- Notes Ethereum has deliberately avoided formal governing bodies and token voting, so there is **no
  standard** for whose input to seek, at what stage, or how much agreement is required.
