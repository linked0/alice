## en
- **Verex: bound slippage with the LMSR gradient/Hessian.** Beyond price being the cost function's derivative, use its gradient (or Hessian, for curvature) to add a test that asserts price sensitivity stays inside a configured band as the liquidity parameter b changes.
- **OFA: document the solver's learning-rate schedule.** Since gradient-descent-style search underlies bidding/pricing optimization, pick and write down a learning-rate schedule for the ATLAS-style intent solver, using this exercise's divergence-vs-slow-convergence threshold as the design check.
- **Number: standardize one gradient-descent utility.** Build a small shared utility (with the learning-rate diagnostic from the exercise) that every Number research or backtest script reuses, instead of hand-rolling gradient descent per script.

## ko
- **Verex: LMSR의 그래디언트/헤시안으로 슬리피지를 제한한다.** 가격이 비용 함수의 미분이라는 것을 넘어, 그래디언트(곡률을 보려면 헤시안)를 이용해 유동성 파라미터 b가 바뀔 때 가격 민감도가 정해진 범위 안에 머무는지 검증하는 테스트를 추가한다.
- **OFA: 솔버의 학습률 스케줄을 문서화한다.** 입찰/가격 최적화의 바탕이 경사하강법 방식의 탐색이므로, ATLAS 스타일 의도 솔버의 학습률 스케줄을 정하고, 이 연습문제의 발산 대 느린 수렴 임계값을 설계 점검 기준으로 삼는다.
- **Number: 경사하강법 유틸리티를 하나로 표준화한다.** 연습문제의 학습률 진단을 포함한 작은 공용 유틸리티를 만들어 Number의 모든 리서치·백테스트 스크립트가 재사용하게 하고, 스크립트마다 경사하강법을 따로 만들지 않는다.
