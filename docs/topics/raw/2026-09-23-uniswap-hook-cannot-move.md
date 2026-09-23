# Source: Trueo migrates Base -> Ethereum L1 (2026-09-21/22)

jay pasted a Korean briefing on 2026-09-23 and asked two questions with it: what the reason for
the decision was, and how they cover the speed. The second is not answered anywhere in the
coverage — see "Not from the sources" below.

## Reported facts

- Trueo announced on 2026-09-21/22 that it moves its prediction market from Base to Ethereum mainnet.
- Launched on Base in March 2025; says Ethereum costs were higher then and parts of the product
  were experimental.
- Stated reasons: network effects, available liquidity, integration opportunities, long-term
  infrastructure. Gas is not given as a reason.
- TRUE token migrates too; the migration window is "open indefinitely".
- Base deployment is not shut down. Existing markets keep trading, settling and redeeming; users
  are discouraged from opening Base markets expiring after 2027-01-31.
- Vitalik Buterin: "Glad to see that Ethereum L1 will have a new strong prediction market contender
  that is dedicated to decentralization, and being ethical and not corposlop, and to actually trying
  to do interesting and meaningful things with this class of economic primitive."
- Price: jay's briefing says TRUE +601% in a day; KuCoin's flash says the token surged tenfold for
  the same window. The disagreement is itself the point — thin float, not a measurement.

## Architecture, from Trueo's own documentation

- Fully onchain, yield-bearing prediction market protocol.
- Liquidity provisioning and order matching happen onchain.
- Built as a specialised **Uniswap v4 hook**; TYD is the payment token for market positions and
  oracle security deposits.
- Market title, resolution criteria and approved data sources are committed onchain at launch.
- Resolution by an **optimistic oracle** with permissionless dispute.

## Sources

- https://www.theblock.co/news/defi/2026-09-22-trueo-ethereum-migration-415999
- https://docs.trueo.com/
- https://coincodex.com/article/92391/vitalik-buterin-backs-trueo-as-prediction-market-moves-to-ethereum-l1-from-base
- https://financefeeds.com/trueo-to-move-prediction-market-from-base-to-ethereum-drawing-vitalik-buterin-praise/

## Not from the sources

**Trueo's announcement does not discuss latency, throughput or gas at all.** The card's entire speed
argument — that an AMM has no matching latency, that the optimistic oracle's dispute window dominates
block time, that a v4 hook inherits its host's deployment and therefore cannot move where the host is
thin, and that the cost paid is retail ticket size — is the card's own reading of the documented
architecture. Attribute it to the card, never to Trueo. Whether L1 v4 liquidity is actually deeper
for their pairs is asserted, not measured.
