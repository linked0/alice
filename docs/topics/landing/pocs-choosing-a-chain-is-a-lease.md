## en
- **Devnet: fill the lease term sheet before picking an OP-Stack host.** Before committing devnet's later OP-Stack L2 to any host, fill four rows — who controls the sequencer, how fees split and who can revise it, exit cost in engineering weeks plus liquidity that won't follow, and what happens to open positions if the host stops operating — and price the exit row first.
- **Verex/Bridge: add a host-failure row to the design doc.** For a settlement product, "what happens to open Verex positions or bridge state if the host stops operating" is a correctness question, not a business risk — write the answer down before devnet depends on any rented sequencer.
- **Devnet: compare hosts at the moment of leaving, not joining.** When evaluating any settlement-space host (an OP-Stack provider, an interop engine), compare total cost including migration and re-agreed integrations, since a host that's cheap to join and costly to leave has already priced the difference into the join fee.

## ko
- **Devnet: OP-Stack 호스트를 고르기 전 임대 조건표를 채운다.** devnet의 향후 OP-Stack L2를 어떤 호스트에 맡기기 전에 네 항목 — 시퀀서를 누가 통제하는지, 수수료 분배와 그것을 누가 바꿀 수 있는지, 이탈 비용(엔지니어링 주 단위와 따라오지 않는 유동성), 호스트가 운영을 멈추면 열린 포지션이 어떻게 되는지 — 을 채우고 이탈 항목을 먼저 가격 매긴다.
- **Verex/Bridge: 설계 문서에 호스트 장애 항목을 추가한다.** 정산 상품에서 "호스트가 멈추면 열린 Verex 포지션이나 브릿지 상태가 어떻게 되는가"는 비즈니스 리스크가 아니라 정합성 문제다. devnet이 임대한 시퀀서에 의존하기 전에 답을 적어둔다.
- **Devnet: 가입 시점이 아니라 이탈 시점 기준으로 호스트를 비교한다.** OP-Stack 제공자나 인터롭 엔진 같은 정산 공간 호스트를 평가할 때는 마이그레이션과 재협의해야 할 통합까지 포함한 총비용으로 비교한다. 가입은 싸고 이탈은 비싼 호스트는 이미 그 차이를 가입 비용에 얹어놓은 것이다.
