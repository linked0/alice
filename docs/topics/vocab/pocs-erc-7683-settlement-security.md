| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| settlement-agnostic | 정산 방식에 대해 중립적인(어느 쪽도 강제하지 않는) · "ERC-7683 is settlement-agnostic by design" |
| bear the risk | 위험을 떠안다 · "decide who actually bears the bridge risk" |
| reclaim | (담보·에스크로 등을) 되찾다, 회수하다 · "reclaims the 100 USDC escrow" |
| front liquidity | 유동성을 먼저 대주다(선지급하다) · "Fronting liquidity on the destination chain" |
| clear a hurdle rate | 목표수익률(문턱값)을 넘기다 · "requiring a thicker spread to clear hurdle rates" |
| blast radius | 피해가 번지는 범위(장애 확산 반경) · "dispute failure blast radius" |
| slip through | (감시망을) 빠져나가다, 걸러지지 않고 통과하다 · "if a false claim slips through" |
| drain the escrow | 에스크로 자금을 통째로 빼가다 · "a compromised committee drains the escrow" |
| trade off | 하나를 얻는 대신 다른 것을 포기하다 · "silently trading off audit perimeter and blast radius" |
| reduce to | 결국 ~으로 귀결되다, 단순화되다 · "reduces t=2 to someone said so" |
| IOriginSettler | ERC-7683의 표준 인터페이스 중 하나(출발 체인에서 주문을 여는 인터페이스) · 사용자가 에스크로에 예치하고 주문에 서명할 때 호출된다. "IOriginSettler.open()" |
| IDestinationSettler | ERC-7683의 표준 인터페이스 중 하나(목적지 체인에서 주문을 채우는 인터페이스) · 필러가 사용자에게 선지급할 때 호출된다. "IDestinationSettler.fill()" |
| GaslessCrossChainOrder | ERC-7683이 정의하는 크로스체인 주문 구조체 · 가스리스 방식의 주문 포맷을 나타낸다. "The cross-chain order struct (GaslessCrossChainOrder, OnchainCrossChainOrder)" |
| OnchainCrossChainOrder | ERC-7683이 정의하는 크로스체인 주문 구조체 · 온체인 서명 방식의 주문 포맷을 나타낸다. "GaslessCrossChainOrder, OnchainCrossChainOrder" |
| Across | 낙관적 검증 방식을 쓰는 대표적 크로스체인 인텐트 프로토콜 · 세 가지 정산 모델 중 낙관적 검증의 예시로 언급된다. "Optimistic verification (Across style)" |
| filler | 사용자 대신 목적지 체인에서 즉시 자금을 선지급하고 나중에 에스크로에서 정산받는 주체 · "the filler advances their own funds on the destination chain" |
<!-- acronyms 2026-09-18 -->
