## en
- **Verex: wire a flame-graph/perf capture into the CI step that runs before a matching-engine performance change ships.** That turns "guess and fix" into a stored artifact — IPC, cache-miss and branch-miss counters checked in alongside the change that supposedly fixed throughput.
- **Devnet: run the cache-miss/branch-mispredict pair as a load test against the indexer before scaling hardware.** Distinguishing genuine load from bad memory locality decides whether the fix is a bigger machine or a data-structure change, and Devnet is the cheap place to run that test first.

## ko
- **Verex: 매칭 엔진 성능 변경이 배포되기 전에 CI 단계에 flame graph/perf 캡처를 연결한다.** 이렇게 하면 '추측 후 수정'이 변경과 함께 저장되는 산출물이 된다 — IPC, 캐시 미스, 분기 예측 실패 카운터가 처리량을 고쳤다고 주장하는 변경과 함께 커밋된다.
- **Devnet: 하드웨어를 늘리기 전에 캐시 미스/분기 예측 실패 쌍을 인덱서 대상 부하 테스트로 돌린다.** 진짜 부하인지 메모리 지역성 문제인지 구분하는 것이 더 큰 머신을 살지 자료구조를 바꿀지를 결정하며, Devnet이 이 테스트를 먼저 돌리기 가장 싼 곳이다.
