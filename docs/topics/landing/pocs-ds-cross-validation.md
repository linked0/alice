## en
- **Number: use walk-forward splitting, never random k-fold, on time-series readings.** Any backtested reading or indicator built on time-series data leaks the future into the past under random k-fold; the published performance number must come from a time-aware split.
- **DeFi: apply the same split to liquid-staking backtests.** Yield or risk-parameter backtests built on historical data need time-aware validation before any parameter is called validated, not just a k-fold score.

## ko
- **Number: 시계열 리딩에는 랜덤 k-fold 대신 워크포워드 분할을 쓴다.** 시계열 데이터로 만든 백테스트 리딩이나 지표는 랜덤 k-fold에서 미래가 과거로 새어 들어간다. 공개하는 성능 수치는 시간을 고려한 분할에서 나와야 한다.
- **DeFi: 유동성 스테이킹 백테스트에도 같은 분할을 적용한다.** 과거 데이터로 만든 수익률이나 리스크 파라미터 백테스트는 k-fold 점수만으로 "검증됐다"고 부르기 전에 시간을 고려한 검증이 필요하다.
