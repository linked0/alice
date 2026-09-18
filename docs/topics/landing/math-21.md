## en
- **Verex: build the covariance matrix across correlated markets before setting position limits.** When two markets share an underlying event, size margin and limits off the portfolio's quadratic-form variance, not the sum of each market's own variance.
- **Wallet: show diversification-adjusted risk in the portfolio view, not summed volatilities.** A holder with positions across correlated Verex markets should see the actual co-movement risk, which is lower or higher than a naive sum depending on correlation sign.
- **Auditor: apply shrinkage when a market is new and flag unstable estimates.** A covariance matrix built from a handful of samples (a newly listed market) is unreliable — note the correction used, or flag the risk number as provisional.

## ko
- **Verex: 포지션 한도를 정하기 전에 상관된 마켓들의 공분산 행렬을 만든다.** 두 마켓이 같은 기초 사건을 공유한다면, 마진과 한도는 각 마켓 분산의 합이 아니라 포트폴리오의 이차형식 분산으로 정한다.
- **Wallet: 포트폴리오 뷰는 변동성 합이 아니라 분산 투자 조정된 리스크를 보여준다.** 상관된 Verex 마켓들에 걸쳐 포지션을 가진 보유자는 상관 부호에 따라 단순 합보다 낮거나 높은 실제 동반 움직임 리스크를 봐야 한다.
- **Auditor: 마켓이 새로 생겼을 때는 shrinkage를 적용하고 불안정한 추정치를 표시한다.** 표본이 적은(신규 상장 마켓) 공분산 행렬은 신뢰할 수 없다. 사용한 보정 방법을 적거나 리스크 숫자를 잠정치로 표시한다.
