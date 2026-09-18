## en
- **Verex: name the arithmetization before scoping any off-chain settlement PoC.** PLONKish with lookups suits bit-manipulation-heavy order matching, AIR suits repeated per-order transition logic — write down which one and why before estimating constraint counts.
- **Devnet: run the break-even check with real constraint counts.** Compare proving k orders in one batch against posting them on-chain directly, using actual R1CS/AIR constraint counts from a devnet PoC, not an estimate.
- **Auditor: treat a lookup table as an audited artifact.** PLONKish lookups move correctness risk from constraint count to precomputed-table correctness, so any settlement circuit using lookups needs its table reviewed as its own item.

## ko
- **Verex: 오프체인 정산 PoC를 범위 짓기 전에 산술화 방식부터 정한다.** 비트 조작이 많은 주문 매칭에는 룩업을 쓰는 PLONKish가, 반복되는 주문별 전이 로직에는 AIR가 맞는다. 제약 개수를 추정하기 전에 어떤 것을 왜 쓸지 적어둔다.
- **Devnet: 실제 제약 개수로 손익분기점을 계산한다.** 주문 k개를 한 배치로 증명하는 것과 온체인에 직접 올리는 것을 비교할 때, 추정치가 아니라 devnet PoC에서 나온 실제 R1CS/AIR 제약 개수를 쓴다.
- **Auditor: 룩업 테이블을 감사 대상 산출물로 취급한다.** PLONKish 룩업은 정확성 리스크를 제약 개수에서 사전 계산된 테이블의 정확성으로 옮긴다. 룩업을 쓰는 정산 회로는 그 테이블을 별도 항목으로 검토해야 한다.
