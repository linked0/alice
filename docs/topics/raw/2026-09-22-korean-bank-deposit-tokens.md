# Briefing — tokenised deposits as a strategy for Korean banks

Collected: 2026-09-22, jay pasted a Korean-language strategy summary into chat. **No URL was captured**,
so unlike most files here the source cannot be reopened by link; what is kept below is the structured
claim and number list, which is the part the item was built from. The summary attributes the
three-track framing to "Tempo", which is not identified further in the text and is unverified here.
Per docs/topics/raw/README.md this file is append-only.

## Claims as given

- Bank deposits are moving onchain; spreading stablecoins risk eroding the deposit base.
- A tokenised deposit is meant to combine onchain settlement with what a deposit already has: deposit
  insurance, interest, and the lending relationship.
- J.P. Morgan and other global banks already run tokenised deposits (JPMD is named) on public chains
  under KYC whitelisting.
- Korea's Project Hangang is a two-tier experiment: the Bank of Korea issues a wholesale CBDC, and
  commercial banks issue deposit tokens on top of it.
- Project Hangang runs on a permissioned Hyperledger Besu network; global cases extend to public chains
  via KYC whitelists. Korea could extend similarly once legal constraints are resolved.
- CBDC and deposit token are described as complementary, not competing: the CBDC is central-bank money,
  the deposit token is a commercial-bank liability that can pay interest and carry insurance.

## The three tracks

1. **Tokenised deposit.** The customer's deposit claim is unchanged; only settlement moves onchain.
   Stability and regulatory treatment are retained. Said to be implementable now within Project Hangang.
2. **First-party (bank-issued) stablecoin.** Backed by separate reserves rather than deposits. Heavier
   liquidity burden, and possible only after the Digital Asset Basic Act passes. Currently only
   consortium infrastructure work.
3. **Third-party stablecoin.** The bank does not issue; it connects to an external (e.g. dollar)
   stablecoin. Already used for offshore and overseas-exchange flows. Carries asset-outflow and
   fee-loss risk.

## Numbers and competitive claims, all as given by the summary and unverified here

- Government subsidy payments of about 110 trillion won per year named as a real use case.
- More than 60 trillion won said to flow offshore between 2025 and 2026, costing domestic banks
  intermediation and fee income.
- Kakao, Naver, Toss and global issuers such as Circle are said to be preparing won-stablecoin
  infrastructure.
