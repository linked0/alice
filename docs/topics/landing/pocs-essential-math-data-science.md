## en
- **Number: require a trimmed mean and staleness cutoff before a reading counts as an indicator.** Implement the book's descriptive-statistics chapter directly as Number's outlier and staleness rules, since those are statistics decisions before they are code.
- **Verex: use the logistic-regression chapter as the resolution-prediction baseline.** Build "did this market resolve Yes" as a logistic regression first, then the from-scratch neural-network capstone over Verex order flow, framework-free.
- **Auditor: require the fitting method and inputs documented for any manipulation-cost curve.** Whether it's fit by gradient descent or a closed form, the methodology needs writing down before a consumer relies on it, the same rule as the Kaiko item.

## ko
- **Number: 읽기가 지표로 인정되기 전에 절사평균과 신선도 컷오프를 요구한다.** 책의 기술통계 챕터를 Number의 이상치·신선도 규칙으로 직접 구현한다. 이는 코드이기 전에 통계적 결정이기 때문이다.
- **Verex: 로지스틱 회귀 챕터를 정산 예측의 베이스라인으로 쓴다.** "이 마켓이 Yes로 정산될까"를 먼저 로지스틱 회귀로 만들고, 그다음 프레임워크 없이 Verex 주문 흐름 위에 처음부터 만든 신경망 캡스톤으로 이어간다.
- **Auditor: 조작 비용 곡선의 피팅 방법과 입력을 문서화하도록 요구한다.** 경사하강법으로 맞추든 닫힌 형태로 맞추든, 소비자가 의존하기 전에 방법론을 적어둔다. Kaiko 항목과 같은 규칙이다.
