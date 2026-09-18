## en
- **Bridge/Token: log who holds locked collateral on each side.** The lock-and-mint bridge between Anvil and Sepolia should record whether JYVE collateral sits on the source or destination chain, since collateral location — not deliverability — is what decides where a token's price actually forms.
- **DeFi: run the lead-lag test between Devnet and Sepolia rates.** Sample the liquid-staking token's Devnet price and its Sepolia-forked reference at a common frequency and compute rolling correlation, before assuming Devnet's price mirrors Sepolia's rather than leading or lagging it.
- **Verex: separate "restriction size" from "demand" in resolution design.** For a market on an asset whose real venue is hard to reach, the resolution field should say which venue's price is used and whether volume there reflects genuine demand or a workaround around the restriction.

## ko
- **Bridge/Token: 각 측에 잠긴 담보의 보유 주체를 기록한다.** Anvil↔Sepolia 락앤민트 브리지는 JYVE 담보가 소스 체인과 목적지 체인 중 어디에 있는지 기록해야 한다. 토큰 가격이 실제로 형성되는 곳을 결정하는 것은 태환 가능성이 아니라 담보의 위치이기 때문이다.
- **DeFi: Devnet과 Sepolia 가격 사이에 선후 관계 테스트를 돌린다.** 유동성 스테이킹 토큰의 Devnet 가격과 Sepolia 포크 기준 가격을 같은 주기로 샘플링해 롤링 상관관계를 계산하고, Devnet 가격이 Sepolia를 그대로 따라간다고 가정하기 전에 어느 쪽이 선행하는지 확인한다.
- **Verex: 정산 설계에서 "제한의 크기"와 "수요"를 구분한다.** 실제 거래 venue에 접근하기 어려운 자산의 마켓이라면, 정산 필드는 어느 venue의 가격을 쓰는지, 그 거래량이 진짜 수요인지 제한을 우회한 결과인지를 밝혀야 한다.
