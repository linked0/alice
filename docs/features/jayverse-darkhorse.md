# Jayverse — Dark Horse (#10) — candidates that could be services, but aren't yet

*Jayverse #10 (added 2026-09-10, jay). **Not committed services** like #1–9 — these are candidate
tracks: each *could* become a real service, none is one yet. Picked up only after the core is
built. Sibling docs indexed in [README.md](README.md); the umbrella plan
[`../tasks/09-02-jayverse.md`](../tasks/09-02-jayverse.md) §10 carries the full step/risk detail.*

> **Why a section, not a backlog line.** Each of these is big or uncertain enough that committing it
> now would distort the build order. Keeping them here — named, with the argument written down —
> means the decision to promote one to a numbered service is deliberate, not accidental.

---

## (a) L1 / L2 — our own chain (start at last)

> **Promoted to #4 on 2026-09-14 (jay).** This candidate is now a committed service row in the
> [hub](README.md#ownership-changes-jay-2026-09-14). The argument below stays as written; the
> "start at last" caveat still holds. Design: [jayverse-devnet.md](jayverse-devnet.md) — phase 1 is a
> hosted Anvil forked from Sepolia; the own chain is its phase 4.

The own-chain ambition, explicitly **start-at-last**, with **supersim** as the local on-ramp. No
repo yet — a `docs/` research folder first, infra-as-code only if we truly commit. The single most
expensive line in the architecture to operate, so: learn locally now, production maybe never. PoC
links: `choosing-a-chain-is-a-lease`, `l2-finality-three-clocks`, `l1-data-pricing-dimensions`.
(Plan §9 has the full writeup.)

## (b) Security-hole research (보안 취약점 연구)

The offensive-security muscle of Jayverse — study the exploit classes that actually drain protocols
(reentrancy, price-oracle manipulation, access-control gaps, signature/permit replay, bridge
message-validation bugs, proxy/upgradeability pitfalls, and the one we ourselves ship: 7702/7715
session-key scope abuse) and run them against **our own contracts on a local fork before anyone else
does**. Dark horse because it compounds across every service — verex caps, the bridge's 1:1 vault
invariant, the wallet's session keys, the agent's mandate enforcers are all attack surfaces — and it
pairs with data-science (exploit detection is on-chain analysis). Skills: Foundry fuzz/invariant
testing, Slither/Aderyn, Echidna, fork-based exploit reproduction, later Halmos/Certora.
**Dual-use guardrail:** exploits live on local forks only; external findings go through responsible
disclosure, always. (Plan ETC section has the full writeup.)

## (c) Base App — Mini App (moved here 2026-09-10, was #8)

What a Base App Mini App **buys** (a funded passkey account, inline market open from a post) versus
what it **rents** (discovery, review, the shape of what you may build, and the host's jurisdiction).
A **strategy / analysis draft** — the argument is written; the build is deferred. It sits here rather
than in the numbered list because it *could* become a service but is not one yet: it's a distribution
lease to make deliberately, not a committed build. Full write-up:
[jayverse-base-app.md](jayverse-base-app.md).

## (d) Canton Network — test usage (added 2026-09-18, jay)

**What.** Run two Jayverse patterns on Canton as a *test*, not a deployment. Canton is Digital
Asset's network: Daml contracts, privacy by default (a participant sees only the sub-transactions it
is party to), permissioned participants, one Global Synchronizer with DevNet / TestNet / MainNet.
It is where S&P Dow Jones Indices and Kaiko put the tokenized iBoxx U.S. Treasuries Index (licence,
data feed and permissions in one token, 2026-03-31) and the ledger the Canton super-validator seat
item describes. Test plan, cheapest first:

1. **Local.** Canton sandbox or the Splice LocalNet (the open-source Canton Network repo ships a
   local compose stack). Write two Daml templates: a **Number reading as a licensed object** — data,
   licence, expiry and permission in one contract, the shape of the tokenized index — and a **verex
   market that resolves on a named reference rate** (administrator, fixing time, methodology
   version as fields, not prose).
2. **DevNet.** Onboard one validator node to the Global Synchronizer DevNet (sponsor onboarding,
   test Canton Coin only) and run the same templates against the shared synchronizer. Measure the
   thing Canton sells: what the counterparty node can and cannot see of our contract.
3. **Write-up.** Compare with the Anvil devnet (#4): where Canton's privacy model changes the
   Auditor's "publish what you checked" rule, and what a licensed-data product would cost us to
   operate there.

**Why dark horse.** The institutions our Tech items keep landing on (S&P, Kaiko, DTCC, Broadridge)
are choosing Canton for regulated data products. If Jayverse ever wants a licensed-data PoC that
talks to that world, a test here is the cheapest way to learn what it costs. **Why not committed.**
Our core is EVM; Canton is Daml, a different language, toolchain and operating model, and nothing in
#1–9 needs it. **Guardrail:** test networks only, no Canton Coin purchase, no MainNet.
PoC links: `canton-sv-seat-is-a-milestone-contract`, `kaiko-reference-rate-is-a-price-with-governance`,
`sp-global-buys-openzeppelin`, `interop-os-one-network`.

---

Every entry here is a **candidate for review**, not committed work. Promote one to a numbered service
only when the core is built and the argument above still holds.
