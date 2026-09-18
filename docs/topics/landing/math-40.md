## en
- **Verex: implement historical-simulation or EVT-based Expected Shortfall for margin, not normal-assumption VaR.** Set market-maker max loss, collateral ratio and settlement safety margin from CVaR specifically, since normal VaR understates the tail exactly during stress.
- **Auditor: publish the risk-measure methodology as a first-class field.** Which measure (VaR vs CVaR), which confidence level, and which horizon should be documented alongside any settlement safety margin, not left implicit.
- **DeFi: apply the same CVaR-not-VaR argument to jayverse-defi's liquidation thresholds.** A liquid-staking design that looks safe under normal-VaR assumptions is exactly the failure mode this PoC describes.

## ko
- **Verex: 마진에는 정규분포 가정 VaR이 아니라 히스토리컬 시뮬레이션 또는 극단값이론 기반 Expected Shortfall을 구현한다.** 마켓메이커 최대 손실, 담보 비율, 정산 안전 마진을 CVaR로 설정한다. 정규분포 VaR은 스트레스 상황에서 정확히 꼬리 위험을 과소평가하기 때문이다.
- **Auditor: 리스크 측정 방법론을 1급 필드로 공개한다.** 어떤 측정치(VaR 대 CVaR), 어떤 신뢰 수준, 어떤 기간인지를 암묵적으로 두지 말고 정산 안전 마진과 함께 문서화한다.
- **DeFi: 같은 CVaR-not-VaR 논리를 jayverse-defi의 청산 임계값에도 적용한다.** 정규분포 VaR 가정에서는 안전해 보이는 리퀴드 스테이킹 설계가 바로 이 PoC가 설명하는 실패 형태다.
