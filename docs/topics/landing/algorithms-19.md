## en
- **Verex: apply the checklist to the CLOB's order-book structure.** Since it's write-heavy and p99-latency sensitive, prefer a log-structured/amortization-friendly book over a naive sorted array, and confirm the choice with measurement rather than asymptotics alone.
- **Rabbit/Wallet: for session-key and mandate-check contract code, gas is the dominant constraint, so pick the structure with the smallest constant/storage-slot cost even when it's asymptotically worse, and document why in the contract.**
- **gitboard: for read-heavy dashboard queries (service status, latest block), prefer a static/cached index over recomputation, paying update cost per event instead of per read.**

## ko
- **Verex: CLOB의 오더북 구조에 체크리스트를 적용한다.** 쓰기가 많고 p99 지연에 민감하므로, 단순 정렬 배열보다 로그 구조/상환 친화적 구조를 선호하고, 점근 복잡도만이 아니라 측정으로 그 선택을 확인한다.
- **Rabbit/Wallet: 세션 키와 mandate 검사 컨트랙트 코드는 gas가 지배적 제약이므로, 점근적으로 더 나쁘더라도 상수/스토리지 슬롯 비용이 가장 작은 구조를 고르고 그 이유를 컨트랙트에 문서화한다.**
- **gitboard: 서비스 상태, 최신 블록 같은 읽기가 많은 대시보드 쿼리는 재계산 대신 정적/캐시된 인덱스를 선호하고, 읽기당이 아니라 이벤트당으로 갱신 비용을 지불한다.**
