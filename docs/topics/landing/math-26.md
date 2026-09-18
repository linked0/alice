## en
- **Verex: fit LMSR's liquidity parameter and the slippage/fee model via QR or SVD, not the normal equations.** Log the condition number so a badly conditioned fit is visible instead of silently wobbling.
- **Verex: add ridge regularization for the gas-cost-vs-block-parameter regression.** Near-dependent columns there are a plausible place for accidentally noisy fee estimates to hide.
- **Auditor / Number: publish the fitting method alongside any indicator derived this way.** State QR/SVD and any regularization used, so consumers can tell a numerically stable fit from a fragile one.

## ko
- **Verex: LMSR 유동성 파라미터와 슬리피지/수수료 모델을 정규방정식이 아니라 QR이나 SVD로 피팅한다.** 조건수를 기록해서 잘못 조건화된 피팅이 조용히 흔들리는 대신 눈에 보이게 한다.
- **Verex: 가스 비용 대 블록 파라미터 회귀에 릿지 정규화를 추가한다.** 거의 종속적인 열들이 있는 이곳이 우연히 노이즈 낀 수수료 추정치가 숨기 좋은 자리다.
- **Auditor / Number: 이 방식으로 도출된 지표에는 피팅 방법을 함께 공개한다.** 사용한 QR/SVD와 정규화 여부를 명시해서, 소비자가 수치적으로 안정적인 피팅과 취약한 피팅을 구분할 수 있게 한다.
