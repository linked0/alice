## en
- **Verex: run a cointegration test, not just a correlation check, between complementary outcome tokens or duplicate-event markets.** Unit-root test each series, then test the residual of their relationship for stationarity — a correlation on price levels can look fine while the peg is actually drifting.
- **Auditor: when the spread fails to mean-revert, name the cause in the methodology note.** State explicitly whether it's a liquidity shortfall or a settlement-terms mismatch between the two markets — two different fixes for one symptom.
- **Number: publish the cointegration/spread-reversion routine as a reusable indicator.** Point it at any pair of related Verex markets on demand instead of re-deriving the test per incident.

## ko
- **Verex: 상호보완적 결과 토큰이나 중복 이벤트 마켓 사이에는 상관관계가 아니라 공적분 테스트를 돌린다.** 각 시계열에 단위근 검정을 하고, 관계의 잔차가 정상성을 갖는지 검정한다 — 가격 수준의 상관관계는 페그가 실제로는 벌어지고 있어도 멀쩡해 보일 수 있다.
- **Auditor: 스프레드가 평균회귀하지 않을 때 원인을 방법론 노트에 명시한다.** 유동성 부족 때문인지 두 마켓 간 정산 조건 불일치 때문인지를 명시적으로 밝힌다 — 하나의 증상에 대한 서로 다른 두 해법이다.
- **Number: 공적분/스프레드 회귀 루틴을 재사용 가능한 지표로 공개한다.** 사고마다 테스트를 다시 만드는 대신, 관련된 Verex 마켓 쌍 어디에나 필요할 때 적용한다.
