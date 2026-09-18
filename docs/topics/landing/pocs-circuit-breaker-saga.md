## en
- **Verex: write the settlement pipeline as an explicit Saga with a compensating transaction for each step.** Oracle lookup, settlement and payout each need a defined rollback action, not just a sequence that assumes every step succeeds.
- **Rabbit/Devnet: wrap every RPC and indexer call behind a circuit breaker with a stated half-open probe interval.** Fail fast once a threshold trips and probe recovery on a schedule, rather than retrying indefinitely against a degraded RPC endpoint.
- **gitboard: surface each service's breaker state — closed, open, half-open — as a visible metric.** A tripped circuit is operational state worth showing on the dashboard, not something only discoverable in logs after the fact.

## ko
- **Verex: 정산 파이프라인을 각 단계마다 보상 트랜잭션이 있는 명시적 Saga로 작성한다.** 오라클 조회, 정산, 지급 각각에 정의된 롤백 동작이 필요하다. 모든 단계가 성공한다고 가정한 순차 흐름만으로는 부족하다.
- **Rabbit/Devnet: 모든 RPC·인덱서 호출을 명시적인 half-open 프로브 간격을 가진 회로 차단기로 감싼다.** 임계값을 넘으면 빠르게 실패하고 일정에 따라 복구를 프로브한다. 저하된 RPC 엔드포인트에 무한정 재시도하지 않는다.
- **gitboard: 각 서비스의 차단기 상태 — closed, open, half-open — 를 눈에 보이는 지표로 노출한다.** 트립된 회로는 나중에 로그에서만 발견되는 것이 아니라 대시보드에 보여줄 만한 운영 상태다.
