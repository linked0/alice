## en
- **Verex: set any resolution-side anomaly alert threshold from the actual base rate.** A "99% accurate" suspicious-settlement detector on a rare event still produces mostly false positives, so compute the real base rate before trusting alert volume.
- **Auditor: apply the same base-rate correction to Tenderly/invariant alerts.** Log the false-positive rate against the true incident base rate before treating alert frequency as signal.
- **Number: flag normality assumptions on fat-tailed data before publishing.** Any Number model that assumes a normal distribution on return-like data should state how much it underestimates tail risk.

## ko
- **Verex: 정산 측 이상 탐지 알림 임계값을 실제 기저율로 설정한다.** 드문 사건에 대해 "정확도 99%"인 의심 정산 탐지기도 대부분 오탐을 낸다. 알림량을 신뢰하기 전에 실제 기저율을 계산한다.
- **Auditor: Tenderly/불변량 알림에도 같은 기저율 보정을 적용한다.** 알림 빈도를 신호로 취급하기 전에 실제 사고 기저율 대비 오탐률을 기록한다.
- **Number: 팻테일 데이터에 정규성을 가정했다면 발행 전 표시한다.** 수익률류 데이터에 정규분포를 가정하는 Number 모델은 테일 리스크를 얼마나 과소평가하는지 명시해야 한다.
