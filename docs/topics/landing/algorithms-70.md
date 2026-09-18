## en
- **Devnet/indexer: batch DB commits per block (or per N blocks), not per event, for any Verex or Rabbit indexer, and make the sync/async commit tradeoff an explicit config choice rather than a silent default.**
- **Auditor: if the indexer ever runs with async commit, document that a crash can lose the last unflushed block's events, and define the replay-from-chain-state recovery procedure.**
- **gitboard: track indexer commit p99 latency as a dashboard metric, since group-commit tuning is where indexing throughput problems actually live, not the query plan.**

## ko
- **Devnet/indexer: Verex나 Rabbit의 인덱서는 이벤트 단위가 아니라 블록 단위(또는 N블록 단위)로 DB 커밋을 배치 처리하고, 동기/비동기 커밋 트레이드오프를 암묵적 기본값이 아니라 명시적 설정으로 만든다.**
- **Auditor: 인덱서가 비동기 커밋으로 동작한다면, 크래시 시 마지막으로 flush되지 않은 블록의 이벤트가 유실될 수 있음을 문서화하고 체인 상태로부터 재생하는 복구 절차를 정의한다.**
- **gitboard: 인덱서 커밋 p99 지연을 대시보드 지표로 추적한다.** 인덱싱 처리량 문제는 쿼리 플랜이 아니라 그룹 커밋 튜닝에서 실제로 발생하기 때문이다.
