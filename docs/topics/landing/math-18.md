## en
- **Verex: implement market-maker parameter calibration via a stable solve (e.g., LU decomposition) instead of explicit matrix inversion, and log the condition number so a poorly conditioned calibration is flagged rather than silently producing unstable prices.**
- **Number: any regression or state-transition model published on Number's research site should report its condition number alongside coefficients, since that determines how much input error gets amplified.**
- **DeFi: implement the liquid-staking algorithm's state-transition/rebase accounting with the same LU-based solve, and unit-test the from-scratch inverse against NumPy to catch drift.**

## ko
- **Verex: 마켓 메이커 파라미터 캘리브레이션을 명시적 행렬 역산 대신 LU 분해 같은 안정적인 solve로 구현하고, 조건수를 로깅해 불안정한 캘리브레이션이 조용히 가격을 흔들지 않고 플래그되게 한다.**
- **Number: Number 리서치 사이트에 게시하는 회귀나 상태 전이 모델은 계수와 함께 조건수를 보고해야 한다.** 조건수가 입력 오차가 얼마나 증폭되는지를 결정하기 때문이다.
- **DeFi: 유동성 스테이킹 알고리즘의 상태 전이/리베이스 회계를 같은 LU 기반 solve로 구현하고, 직접 구현한 역행렬을 NumPy와 유닛 테스트로 대조해 오차 드리프트를 잡는다.**
