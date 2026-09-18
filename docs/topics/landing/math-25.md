## en
- **Number: check the condition number, not just whether the determinant is zero, before regression on market data.** Before running covariance estimation or regression on Number's price-correlation or risk matrices, screen for near-singular inputs with the condition number, since the determinant is scale-sensitive and misses the near-zero case.
- **DeFi: add a rank check before trusting any derived hedge ratio in jayverse-defi's risk model.** If collateral or asset correlations feed a hedge calculation, a rank check catches redundant columns before they produce an unstable result.

## ko
- **Number: 마켓 데이터에 회귀분석을 돌리기 전에 행렬식이 0인지가 아니라 condition number를 확인한다.** Number의 가격 상관행렬이나 리스크 행렬에 공분산 추정이나 회귀분석을 돌리기 전에 condition number로 near-singular 입력을 걸러낸다. 행렬식은 스케일에 민감해 0에 가까운 경우를 놓친다.
- **DeFi: jayverse-defi의 리스크 모델에서 파생된 헤지 비율을 신뢰하기 전에 rank 체크를 추가한다.** 담보나 자산 간 상관관계가 헤지 계산에 들어간다면, rank 체크로 불안정한 결과를 만들기 전에 중복된 열을 잡아낸다.
