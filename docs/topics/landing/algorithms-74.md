## en
- **Devnet: decide node operating cost vs queryable history range up front.** For the hosted Anvil and any future L2, set the pruning/archive tradeoff before an incident needs a past-state query no node was configured to answer.
- **Verex: build the event-indexed DB as the reconstructible source of truth.** Market history, position snapshots and settlement verification should read from your own indexer, so a pruned node is enough and archive-node dependency drops out of the critical path.
- **gitboard: surface indexer completeness and lag as a dashboard metric.** The archive-node-avoidance plan only holds if the indexed DB stays caught up with chain history — make that visible, not assumed.

## ko
- **Devnet: 노드 운영 비용과 조회 가능한 히스토리 범위를 미리 정한다.** 호스팅되는 Anvil과 향후 L2에 대해, 아무 노드도 답하도록 설정되지 않은 과거 상태 조회가 사고 중에 필요해지기 전에 프루닝/아카이브 트레이드오프를 정한다.
- **Verex: 이벤트 인덱싱 DB를 재구성 가능한 진실의 원천으로 만든다.** 마켓 히스토리, 포지션 스냅샷, 정산 검증은 자체 인덱서에서 읽어야 하고, 그러면 프루닝된 노드로 충분해지고 아카이브 노드 의존성이 크리티컬 패스에서 빠진다.
- **gitboard: 인덱서 완전성과 지연을 대시보드 지표로 노출한다.** 아카이브 노드 회피 계획은 인덱싱된 DB가 체인 히스토리를 계속 따라잡을 때만 유효하다 — 가정하지 말고 보이게 한다.
