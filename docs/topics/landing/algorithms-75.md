## en
- **Verex: add a byte-for-byte replay test to CI.** Beyond just having replayable indexing, CI should index a fixed block range twice and diff the resulting tables, catching any non-deterministic transform before it reaches production P&L numbers.
- **gitboard: store its own metrics with a reorg-safe cursor.** If gitboard reads on-chain events for dashboards, its ingestion needs the same (block number, log index) cursor and unfinalized-range rollback Verex's indexer needs, or a reorg silently corrupts a dashboard number nobody double-checks.
- **Devnet: expose a reliable finality signal for any indexer built on top.** Every service indexing Devnet needs to know which ranges are still reorg-able, so Devnet's node setup should make block finality status a first-class, queryable fact.

## ko
- **Verex: CI에 바이트 단위 재생 테스트를 추가한다.** 재생 가능한 인덱싱을 갖추는 것을 넘어, CI는 고정된 블록 범위를 두 번 인덱싱해 결과 테이블을 diff해야 한다. 어떤 비결정적 변환이든 프로덕션 P&L 수치에 닿기 전에 잡아낸다.
- **gitboard: 자체 지표를 리오그에 안전한 커서로 저장한다.** gitboard가 대시보드용으로 온체인 이벤트를 읽는다면, Verex의 인덱서와 같은 (블록 번호, 로그 인덱스) 커서와 미확정 범위 롤백이 필요하다. 그렇지 않으면 아무도 다시 확인하지 않는 대시보드 수치가 리오그로 조용히 망가진다.
- **Devnet: 그 위에 올라가는 어떤 인덱서에도 신뢰할 수 있는 파이널리티 신호를 제공한다.** Devnet을 인덱싱하는 모든 서비스는 어느 범위가 아직 리오그될 수 있는지 알아야 하므로, Devnet의 노드 설정은 블록 파이널리티 상태를 일급 조회 가능한 사실로 만들어야 한다.
