# Injective registers as an SEC transfer agent — 2026-09-23

Claims and citations only; the body is not copied (see README.md). jay pasted the piece.
Legal characterisations are the article's, not legal advice.

## Provenance

- **Four Pillars**, "Blockchains Can No Longer Be Just Tech Providers", by **Eren**, **2026-08-26**,
  Institution / Comment. **No URL captured.** Standard disclaimer.

## Claims (unverified here)

- **2026-08-19**: **Injective Institutional Services**' registration as a **transfer agent** with the
  **SEC** became effective. Injective framed it as the regulatory foundation for official securities
  records.
- A transfer agent maintains the authoritative record of ownership: reconciles issued against
  outstanding, records transfers, determines entitlement to dividends, distributions and voting.
- **SEC classification, January 2026** — tokenized securities split into:
  - **issuer-sponsored**: issuer or its agent tokenizes its own securities; where the DLT is integrated
    into the **master securityholder file**, a token transfer corresponds to a change on the official
    register and holders exercise rights directly against the issuer; existing federal securities laws
    apply as they stand.
  - **third party-sponsored**: an unaffiliated third party custodies the security or issues a
    price-tracking token; holders are **not** shareholders — they hold a claim against the third party
    or a contractual right; requires an additional determination of what the token represents.
- **Injective Mint**: no-code institutional issuance. Asset details, investor eligibility, jurisdiction
  restrictions, custodian connections, issuance authority in one interface. Enforced at chain level via
  native **Tokenfactory** and **Permissions** modules — allowlists, approved jurisdictions, mint/burn
  authority, address freezes; non-compliant transfers rejected by the chain, no custom contract needed.
- **Gap the article names**: Mint's records do **not** automatically become the official register unless
  the issuer adopts that ledger as its master securityholder file. Mint is at **demo stage**, so the
  actual integration "cannot be stated with certainty"; the mapping across one asset lifecycle is
  described as provisional.
- Maintaining securities ownership records on a blockchain for the US market requires a registered
  transfer agent that has filed **Form TA-1** with the SEC.
- Injective since **2021** positioned as a finance-specific chain: sub-second blocks, orderbook matching,
  derivatives modules. Stated ambition spans institutional funds, listed equities, private securities
  and enterprise trade finance.

## This note's own observations (not in the article)

- **Form TA-1 is a registration, not an approval** — the SEC does not certify competence at that point.
- A chain that is **also** the transfer agent for assets issued on it combines **venue and recordkeeper**,
  a separation traditional markets maintain deliberately so the register is checkable by a party with no
  stake in the venue's success.
