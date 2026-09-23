# Source: DoinGud bid reuse (2026-09-21) + the consumed-authorization thread

jay pasted two Korean briefings on 2026-09-23 — the incident, then his own analysis of the bug
class — and said the second related to the first. They were merged into one card, because the
incident alone is $35k of news and the class is the part worth keeping.

## As reported by jay, NOT independently verified

- DoinGud, an NFT platform on Polygon, lost approximately $35,486 USDC on 2026-09-21.
- Cause: a bug in the Diamond bidding contract — an accepted bid was not cleared, so the same bid
  could be accepted repeatedly.
- Separately: a D'CENT app-wallet abnormal-transfer alert on 2026-09-16; hardware wallets said to
  be unaffected; investigation described as early.

No post-mortem, explorer trace or contract address was checked. The mechanism in the card follows
from the one-line description and from the known shape of this bug class; **the actual code path
was not read.** Before citing the incident anywhere, find the project's own write-up.

## jay's analysis, which is the substance of the card

Three converged answers to "how do you make something usable exactly once":

1. **Sequential nonce** — EIP-2612 `permit`: a per-address incrementing nonce inside the signature,
   bumped on use. Simple, but forces ordering, so no parallel orders.
2. **Counter / bitmap** — Seaport keeps per-order-hash state (`isValidated`, `isCancelled`,
   `totalFilled`) plus a per-offerer counter; bumping the counter invalidates all past signatures
   at once. Uniswap Permit2 uses unordered nonce bitmaps to get parallelism and one-time use
   together.
3. **Nullifier** — privacy protocols publish that something was spent without revealing what.

All three are one sentence: an authorization must store a consumed mark when it is used, with the
check and the consume in the same transaction.

Why now, per jay: (a) after EIP-7702 an EOA signature delegates code, and the authorization carries
a `chainId` — where 0 means every chain — plus a nonce, a detail wallet UX tends to flatten;
(b) it is the pair to the deterministic pre-check in the agent-payments card: the gate asks whether
an action is allowed, the consume mark asks whether the permission is already spent. Agents hit
this as a **retry bug** (network timeout, resubmit), not as an attack.

## Standards to re-check before quoting exact field names

EIP-2612, EIP-712 domain separator, Seaport order state and offerer counter, Uniswap Permit2 nonce
bitmaps, EIP-7702 authorization list. Documented behaviours, but the details move.

## Related

- `pocs-agent-payments-korea-control-plane` (Tech #3) — the deterministic gate this is the pair to,
  and the x402 facilitator rule: persist consumed payment identifiers, make verify-and-consume
  atomic.
