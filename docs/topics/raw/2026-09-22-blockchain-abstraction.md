# Blockchain Abstraction: The Next Frontier — 2026-09-22

Claims and citations only; the article body is not copied (see README.md). jay pasted the piece.

## Provenance

- **Four Pillars**, "Blockchain Abstraction: The Next Frontier", by **Jun**, **2026-09-10**,
  Crypto / Issue. The paste carried no publisher; it was recovered from the "Recommended" panel of the
  Four Pillars HIP-4 piece pasted the same day, which lists this article with its author and section.
  **No URL captured.** The paste also carried a promotion for **EastPoint:Seoul 2026** (28 Sep 2026,
  co-hosted by **Hashed** and **Bloomingbit** per press releases). Four Pillars' standard disclaimer
  applies: author may hold positions, the firm may hold investments, FP Validated may run nodes.

## Claims taken from the article (all unverified here)

- Privy: embedded wallets Feb 2023, platform launch Feb 2024; email OTP / social / passkey / external
  wallet login; `createOnLogin` creates a wallet at login; TEE config generates the key in an **AWS
  Nitro Enclave** and splits it **2-of-2** with Shamir (enclave share + auth share), recombined in
  isolated memory for the signature and destroyed after.
- Article's own caveat, quoted in the item: "splitting the key alone does not determine control";
  control follows owner / additional signers / quorum; a service authorization key as owner gives the
  **service** control; a compromised email or social login reaches the wallet.
- Privy "more than 75 million accounts by June 2025", acquired by Stripe "the following month, in July".
  **Corrected**: Stripe announced the Privy acquisition on **11 June 2025** (SiliconANGLE, PYMNTS,
  Ledger Insights), after acquiring **Bridge**. So the article's month is wrong.
- ERC-4337: UserOperation, bundler, EntryPoint, smart account, paymaster. EIP-5792 for batched calls
  with atomic execution. Session keys; **ERC-7715 is a draft**.
- Across / ERC-7683 (Uniswap Labs + Across): SpokePool deposit, relayer fronts capital on the
  destination, reimbursed after verification and a challenge period, refund address if unfilled.
  Circle **CCTP**: burn-and-mint with Circle attestation; V2 Fast Transfer mints before finality.
- Ramp + Stripe, **July 2026**: bill pay from a bank account (Bridge converts) and a stablecoin-holding
  account (Privy enterprise wallets). "more than 1,000 companies" paying in stablecoins, **"more than
  70% of the value … moved outside banking hours"**.
- Telegram Wallet / TON: MoonPay on-ramp July 2025 (cards, Apple Pay, Google Pay) and **MoonPay
  Deposits, Feb 2026** for cross-chain incoming transfers; TON Connect for mini apps.
- Naver Pay: non-custodial wallet beta **Aug 2024** using **Magic Labs**; NFTs labelled "art", tx hashes
  "transaction numbers"; **Wallet Community Mar 2026** with ticket-verified rooms (KLPGA example).

## Sources

- The pasted article (publisher and URL not captured).
- https://siliconangle.com/2025/06/11/stripe-acquires-crypto-wallet-infrastructure-provider-privy/
- https://www.eastpoint.xyz/
