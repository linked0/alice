## en
- **Verex: design the subgraph schema for markets, orders and settlements before the first deploy.** What is not indexed at deploy time cannot be queried later without a re-sync, and Verex's query ergonomics depend entirely on decisions made before any data exists.
- **gitboard: treat The Graph as one option for the projection layer this dashboard already needs.** The comparison against raw RPC this PoC produces is the concrete evidence for choosing between a subgraph and the hand-rolled indexer from the-app-reads-a-projection.

## ko
- **Verex: 첫 배포 전에 마켓, 주문, 정산에 대한 서브그래프 스키마를 설계한다.** 배포 시점에 인덱싱하지 않은 것은 나중에 재동기화 없이 쿼리할 수 없다. Verex의 쿼리 편의성은 데이터가 존재하기 전에 내린 결정에 전적으로 달려 있다.
- **gitboard: The Graph를 이 대시보드가 이미 필요로 하는 프로젝션 레이어의 한 옵션으로 다룬다.** 이 PoC가 만드는 raw RPC 대비 비교가, 서브그래프와 the-app-reads-a-projection의 수작업 인덱서 중 무엇을 고를지에 대한 구체적 근거가 된다.
