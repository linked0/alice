## en
- **OFA: log the LP-relaxation bound next to every solver result in the intent auction.** Computing that lower bound for each batch turns "the solver did fine" into a measured approximation ratio instead of a feeling.
- **Verex: if a heuristic batch-matcher is ever built, gate its approximation ratio against the LP bound in tests.** Use the free baseline this PoC describes to fail a heuristic that drifts too far from optimal, rather than trusting it on inspection.
- **gitboard: track the gap between heuristic output and the LP bound as a metric.** A widening gap over time is a concrete signal that the matching or auction heuristic needs retuning.

## ko
- **OFA: 인텐트 경매에서 솔버 결과 옆에 LP 완화 하한값을 함께 기록한다.** 각 배치마다 이 하한을 계산하면 "솔버가 잘했다"는 느낌이 아니라 측정된 근사 비율이 된다.
- **Verex: 휴리스틱 배치 매처를 만들게 되면 테스트에서 그 근사 비율을 LP 하한에 걸어둔다.** 이 PoC가 말하는 무료 베이스라인을 이용해, 육안 검사로 신뢰하는 대신 최적값에서 너무 벗어난 휴리스틱을 실패시킨다.
- **gitboard: 휴리스틱 결과와 LP 하한 사이의 격차를 지표로 추적한다.** 시간이 지나며 격차가 벌어지는 것은 매칭이나 경매 휴리스틱을 재튜닝해야 한다는 구체적 신호다.
