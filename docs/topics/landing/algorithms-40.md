## en
- **Verex: profile the CLOB matching engine's hot loop with perf for branch-miss/cache-miss counters before assuming instruction count explains latency.** Restructure the order/position struct as SoA if pointer-chasing shows up.
- **Devnet: lay out any indexer's per-event derived state as contiguous arrays, not object graphs.** Applies directly to the Ponder-style reorg indexer already planned for devnet.
- **gitboard: add branch-miss/cache-miss counters to the matching engine's benchmark dashboard, not just wall-clock latency.** Per this page, those are the actual explanatory variables when performance differs by multiples at equal complexity.

## ko
- **Verex: 명령어 수가 지연을 설명한다고 가정하기 전에 CLOB 매칭 엔진의 핫 루프를 perf로 프로파일링해 branch-miss/cache-miss 카운터를 본다.** 포인터 체이싱이 드러나면 주문/포지션 구조체를 SoA로 재구성한다.
- **Devnet: 인덱서의 이벤트별 파생 상태를 객체 그래프가 아니라 연속 배열로 배치한다.** devnet에 이미 계획된 Ponder식 리오그 인덱서에 바로 적용된다.
- **gitboard: 매칭 엔진 벤치마크 대시보드에 벽시계 지연뿐 아니라 branch-miss/cache-miss 카운터도 추가한다.** 이 페이지에 따르면 동일한 복잡도에서 성능이 몇 배씩 차이 날 때 실제 설명 변수는 이것이다.
