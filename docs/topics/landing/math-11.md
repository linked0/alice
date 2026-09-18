## en
- **Rabbit: derive the discount-factor threshold for session-key/mandate slashing, don't assume it.** Compute how large the probability of future interaction needs to be for honest behavior to beat one-shot defection, the way the exercise derives it for the repeated prisoner's dilemma.
- **Verex: check market-maker rebates for a dominant defection strategy.** Before shipping a rebate scheme, verify spoofing or wash-trading isn't the dominant strategy regardless of what other makers do — that's the condition the dominant-strategy analysis is built to catch.
- **Auditor: document the actual safety margin as a checked number, not an assumption.** Any slashing or bond design should state the discount factor or repetition probability it relies on, since that's the number that turns "should deter" into "does deter."

## ko
- **Rabbit: 세션 키·만데이트 슬래싱의 할인율 임계값을 가정이 아니라 유도해서 낸다.** 연습이 반복 죄수의 딜레마에서 하듯, 정직한 행동이 일회성 배신을 이기려면 미래 상호작용 확률이 얼마나 커야 하는지 계산한다.
- **Verex: 마켓 메이커 리베이트에 우월 배신 전략이 있는지 확인한다.** 리베이트 스킴을 배포하기 전에, 다른 메이커가 무엇을 하든 스푸핑이나 워시 트레이딩이 우월 전략이 되지 않는지 검증한다. 이게 우월 전략 분석이 잡아내야 할 조건이다.
- **Auditor: 실제 안전 마진을 가정이 아니라 검증된 숫자로 문서화한다.** 슬래싱이나 본드 설계는 의존하는 할인율이나 반복 확률을 명시해야 한다. 그 숫자가 "억제해야 한다"를 "억제한다"로 바꾸는 숫자다.
