## en
- **Verex: stress-test market maker exposure with a fat-tailed generator, not just Gaussian.** LMSR inventory risk under a simulated crash should be modeled with a fat-tailed path generator, since a thin-tailed simulation will systematically underprice the disaster scenario that actually threatens the maker's collateral.
- **DeFi: run the same paired-generator test on liquid-staking slashing risk.** Simulate validator slashing paths with both a Gaussian and a fat-tailed generator on the same staked position, and compare the tail loss estimates before sizing any buffer.
- **OFA: use Monte Carlo to price solver default risk.** Simulate thousands of auction paths with a fat-tailed model for solver failure, since a closed-form estimate of default risk is unlikely to exist for an ATLAS-style auction.

## ko
- **Verex: 마켓 메이커 노출을 가우시안이 아니라 팻테일 생성기로 스트레스 테스트한다.** LMSR 재고 위험을 시뮬레이션한 폭락 아래서 팻테일 경로 생성기로 모델링해야 한다. 씬테일 시뮬레이션은 메이커의 담보를 실제로 위협하는 재난 시나리오를 체계적으로 저평가하기 때문이다.
- **DeFi: 같은 페어 생성기 테스트를 유동성 스테이킹 슬래싱 위험에 돌린다.** 스테이킹된 포지션 하나에 대해 가우시안과 팻테일 생성기 양쪽으로 밸리데이터 슬래싱 경로를 시뮬레이션하고, 버퍼를 정하기 전에 꼬리 손실 추정치를 비교한다.
- **OFA: 몬테카를로로 솔버 디폴트 위험 가격을 매긴다.** 솔버 실패에 대한 팻테일 모델로 경매 경로 수천 개를 시뮬레이션한다. ATLAS식 경매의 디폴트 위험에 닫힌 형태 추정치는 존재하지 않을 가능성이 높다.
