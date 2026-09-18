## en
- **Verex: set an explicit watermark delay and allowed-lateness window for volume/position aggregation.** Write the completeness-vs-latency tradeoff as a number, not an assumption, since block time and receipt time already diverge.
- **Verex: route late or reorged events down a correction path.** Match receipt-is-not-settlement's reorged state instead of silently mutating an already-emitted aggregate when a reorg flips the past.
- **Auditor: require exactly-once semantics for settlement-relevant aggregation.** Checkpointed state and idempotent sink writes matter here because a duplicated write after a restart is exactly the silent inconsistency an audit should catch.

## ko
- **Verex: 거래량/포지션 집계에 명시적인 워터마크 지연과 허용 지연 창을 설정한다.** 블록 시각과 영수증 시각이 이미 어긋나므로, 완전성 대 지연의 트레이드오프를 가정이 아니라 숫자로 적는다.
- **Verex: 늦게 도착하거나 리오그된 이벤트는 정정 경로로 보낸다.** 리오그가 과거를 뒤집을 때 이미 내보낸 집계를 조용히 바꾸는 대신, receipt-is-not-settlement의 reorged 상태와 맞춘다.
- **Auditor: 정산에 관련된 집계에는 정확히 한 번(exactly-once) 시맨틱을 요구한다.** 체크포인트된 상태와 멱등적인 싱크 쓰기가 중요한 이유는, 재시작 후 중복 쓰기가 바로 감사가 잡아내야 할 조용한 불일치이기 때문이다.
