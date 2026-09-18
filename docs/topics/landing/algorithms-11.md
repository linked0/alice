## en
- **Verex: implement the conflict-DAG + Kahn's-algorithm batching from the practical connection as an actual settlement module.** Expose the computed critical-path length as a per-batch metric to see how close throughput gets to the theoretical bound.
- **OFA: build the same state-access-conflict DAG for solver-auction intents.** Batch non-conflicting solver settlements together the same way independent-market Verex trades get batched.
- **gitboard: surface "batch critical-path length vs number of parallel layers" as a Verex settlement metric.** It's the number that says whether parallelization is actually being captured, not just attempted.

## ko
- **Verex: 실무 연결에서 나온 충돌 DAG + Kahn 알고리즘 배칭을 실제 정산 모듈로 구현한다.** 계산된 임계 경로 길이를 배치별 지표로 노출해, 처리량이 이론적 한계에 얼마나 가까운지 본다.
- **OFA: 솔버 경매 인텐트에도 같은 상태 접근 충돌 DAG를 만든다.** 서로 다른 마켓의 Verex 거래를 배치하듯, 충돌하지 않는 솔버 정산들을 함께 배치한다.
- **gitboard: "배치 임계 경로 길이 대 병렬 레이어 수"를 Verex 정산 지표로 노출한다.** 병렬화가 시도되고 있는지가 아니라 실제로 포착되고 있는지를 말해주는 숫자다.
