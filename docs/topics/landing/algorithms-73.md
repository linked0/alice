## en
- **Number: the research site's historical-reading queries face the same archive-node-versus-reconstructed-DB tradeoff.** Decide up front whether Number reconstructs state from events into its own store rather than paying per-query archive-node cost.
- **Devnet: document whether the hosted Anvil keeps full historical state or prunes it.** This snapshot/pruning policy is the same storage-layout choice, and decides what queries any service can run against devnet.
- **gitboard: price any dashboard query of past settlement state against this lookup-cost table.** Do this before choosing to hit an archive node live instead of a maintained index.

## ko
- **Number: 리서치 사이트의 과거 데이터 조회는 아카이브 노드 의존과 자체 DB 재구성 사이의 동일한 트레이드오프를 겪는다.** Number가 쿼리마다 아카이브 노드 비용을 내는 대신 이벤트로부터 자체 저장소에 상태를 재구성할지 미리 정한다.
- **Devnet: 호스팅된 Anvil이 전체 과거 상태를 보존하는지 가지치기하는지 문서화한다.** 이 스냅샷/가지치기 정책이 바로 이 저장 계층 선택이며, devnet에서 어떤 서비스가 어떤 쿼리를 할 수 있는지를 결정한다.
- **gitboard: 과거 정산 상태를 조회하는 대시보드 쿼리는 이 조회 비용 표에 따라 값을 매긴다.** 유지되는 인덱스 대신 아카이브 노드를 실시간으로 두드리기로 결정하기 전에 이를 한다.
