## en
- **Verex: log every agent probability against the market's own price.** For any pricing or resolution agent that outputs a probability, persist forecast p, the market's implied price at the same instant, and the outcome — the Brier score against the market price is the only test that proves the agent has edge.
- **OFA: grade solver/router confidence with Brier or log score, not accuracy.** A solver that reports a win-probability for a route needs a proper scoring rule, since a threshold-based accuracy number discards the size the auction actually bid.
- **Rabbit: decompose calibration from resolution before sizing anything.** Any agentic component that sizes an action off a probability (session-key risk, position size) should log the reliability/resolution split, since an overconfident-but-well-ranked model sizes wrong even when it looks accurate.

## ko
- **Verex: 모든 에이전트 확률을 시장 자체 가격과 대조해 기록한다.** 확률을 내는 가격결정·정산 에이전트는 예측 확률 p, 같은 시점의 시장 내재 확률, 실제 결과를 저장한다. 시장 가격 대비 브라이어 점수만이 에이전트에 엣지가 있는지 증명하는 유일한 테스트다.
- **OFA: 솔버·라우터의 확신도는 정확도가 아니라 브라이어나 로그 점수로 채점한다.** 경로의 승률을 보고하는 솔버는 적정 채점 규칙이 필요하다. 임계값 기반 정확도는 경매가 실제로 베팅한 크기를 버리기 때문이다.
- **Rabbit: 무언가의 크기를 정하기 전에 캘리브레이션과 해상도를 분리해 본다.** 확률로 행동 크기를 정하는 에이전트 요소(세션 키 리스크, 포지션 크기)는 신뢰도·해상도 분해를 기록해야 한다. 순위는 잘 매기지만 과신하는 모델은 정확해 보여도 크기를 잘못 정하기 때문이다.
