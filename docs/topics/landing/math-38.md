## en
- **Verex: set price-swing risk limits and collateral requirements from a bounded-martingale model, not GBM.** Verex prices are confined to [0,1] and don't follow a lognormal distribution.
- **DeFi: keep the from-scratch staking-rate study's volatility model separate from Verex's.** GBM's continuous-compounding assumption fits DeFi's unbounded rate math far better than Verex's bounded prices.
- **gitboard: state which model — bounded martingale or GBM — backs any displayed expected-price-swing figure for a Verex market.** So a viewer can't read a GBM-shaped confidence interval onto a bounded price.

## ko
- **Verex: 가격 변동 리스크 한도와 담보 요구량은 GBM이 아니라 경계가 있는 마팅게일 모델로 설정한다.** Verex 가격은 [0,1] 사이에 갇혀 있어 로그정규분포를 따르지 않는다.
- **DeFi: 처음부터 구현하는 스테이킹 금리 연구의 변동성 모델은 Verex와 분리해서 유지한다.** GBM의 연속 복리 가정은 경계 있는 Verex 가격보다 상한이 없는 DeFi 금리 수식에 훨씬 잘 맞는다.
- **gitboard: Verex 마켓의 예상 가격 변동폭을 보여줄 때 어떤 모델(경계 있는 마팅게일 대 GBM)을 썼는지 명시한다.** 보는 사람이 GBM 형태의 신뢰구간을 경계 있는 가격에 잘못 대입하지 않게 한다.
