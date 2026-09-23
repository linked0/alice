# Source: Pay.sh / x402 / Facilitator / Kora — session notes, 2026-09-23

Origin: jay's working session with Claude on 2026-09-23, folded into Tech card
`pocs-agent-payments-korea-control-plane`. The card's first version (2026-09-13) was
written from an article summary; this file records the corrections and the primary
sources that produced the rewrite, so the card can be re-derived instead of
re-remembered.

## Primary sources consulted

- Solana Foundation — Pay.sh launch with Google Cloud, 2026-05-05
  https://solana.com/news/solana-foundation-launches-pay-sh-in-collaboration-with-google-cloud
- Pay.sh repository — https://github.com/solana-foundation/pay
- Solana — MPP (Machine Payments Protocol, from Tempo and Stripe)
  https://solana.com/docs/payments/agentic-payments/mpp
- x402 — HTTP 402 core concept — https://docs.x402.org/core-concepts/http-402
- x402 — Facilitator — https://docs.x402.org/core-concepts/facilitator
- x402 v2 specification
  https://github.com/x402-foundation/x402/blob/main/specs/x402-specification-v2.md
- x402 exact SVM scheme
  https://github.com/x402-foundation/x402/blob/main/specs/schemes/exact/scheme_exact_svm.md
- Solana — verify and settle x402 payments on Solana
  https://solana.com/docs/tools/x402-facilitator
- Solana — x402 integration with Kora — https://solana.com/docs/tools/kora/guides/x402
- Solana — Kora fee abstraction
  https://solana.com/docs/payments/send-payments/payment-processing/fee-abstraction
- Solana — Kora operator configuration
  https://solana.com/docs/tools/kora/operators/configuration
- Kora repository — https://github.com/solana-foundation/kora
- Google Cloud — AP2 announcement
  https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol
- AP2 specification
  https://github.com/google-agentic-commerce/AP2/blob/main/docs/ap2/specification.md

## Quoted claims worth keeping

- x402 docs: "The facilitator does not hold funds or act as a custodian."
- Solana x402 facilitator docs: the facilitator calls Kora to co-sign and submit the
  transaction; Kora enforces Solana transaction policy, protects the fee-payer signer,
  submits to the chain, and returns the transaction signature.
- Solana x402 facilitator docs, resource-server checklist: authenticate facilitator
  traffic, validate every response, use strict timeouts, fail closed. Persist consumed
  payment identifiers and transaction signatures in a shared, durable store, and make
  verification-and-consume atomic. Do not rebuild or re-sign a transaction after
  blockhash expiry without asking the payer to authorize the new transaction.
- Kora configuration docs: at least one of allowed_programs, allowed_tokens or
  allowed_spl_paid_tokens must be specified or the node processes nothing; Kora
  validates every instruction against the configured policy before signing.
- Pay.sh: API proxy on Google Cloud in front of BigQuery, Gemini, Cloud Run and 50+
  community APIs (Helius, Dune, Nansen); the agent's Solana wallet is its identity;
  per-request billing, no subscription; settled in stablecoins on Solana and paid to
  providers in fiat.

## Corrections to the card's first version

1. Kora and the Facilitator are stacked, not alternatives — the Facilitator calls Kora.
2. The fee-payer signature is added at /settle, not when the client builds the
   transaction; the client needs only the fee payer's address.
3. x402 v2 header names are PAYMENT-REQUIRED / PAYMENT-SIGNATURE / PAYMENT-RESPONSE;
   the X-PAYMENT family belongs to v1.
4. The public x402.org facilitator is development and testnet only.
5. A payTo address does not establish merchant of record.
6. Catalog prices are live: the BigQuery listing has shown $0.001 per request, against
   the $0.40 used illustratively in the walkthrough.
7. "31 confirmations / 12.8 seconds" is not a protocol guarantee.
8. A YAML mandate in a walkthrough is AP2-inspired, not AP2 wire format. What AP2 does
   require is deterministic-code validation rather than model judgment.
9. It is unconfirmed whether Pay.sh's gateway uses Kora.
10. The policy gate and the audit log are additions, not x402 features.

## Unverified, needs primary Korean sources and counsel

VASP / custody / electronic-finance / foreign-exchange / AML / network-separation / tax
/ sandbox treatment; the exchange's current real-name bank; BOK-Wire+ net settlement
timing for retail net positions; the travel-rule threshold; Pay.sh's regulatory posture
in Korea. Every Korean legal statement in the card is a question, not an answer.
