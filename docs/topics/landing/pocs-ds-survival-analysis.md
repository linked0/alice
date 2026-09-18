## en
- **Wallet: model inactivity as time-to-event, not a 30-day flag.** Fit a Kaplan-Meier curve to embedded-wallet activity so wallets that simply haven't churned yet aren't counted as retained or lost by a fixed cutoff.
- **Verex: censor active traders instead of assuming they've left.** When measuring trader or market-maker retention, treat still-active accounts as censored observations rather than folding them into a naive churn rate.

## ko
- **Wallet: 비활성을 30일 플래그가 아니라 사건까지의 시간으로 모델링한다.** 임베디드 지갑 활동에 Kaplan-Meier 곡선을 적용해, 아직 이탈하지 않은 지갑을 고정 기준으로 유지/이탈로 잘못 분류하지 않게 한다.
- **Verex: 여전히 활성인 트레이더는 단순 이탈로 넣지 않고 중도절단으로 처리한다.** 트레이더나 마켓 메이커 리텐션을 측정할 때 활성 계정을 중도절단 관측치로 다뤄야 순진한 이탈률의 편향을 피한다.
