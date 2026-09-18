## en
- **Rabbit: size the paymaster's ETH float explicitly.** If Rabbit lets users pay gas in JYVE or USDC via ERC-4337 paymasters, the paymaster is now the party holding and converting ETH; monitor that float rather than assuming gas abstraction removes ETH demand from the system.
- **Wallet: show which token actually funds gas, not just "no ETH needed."** The simulate-before-sign screen should disclose that a paymaster is converting the user's chosen token to ETH under the hood, since holding demand moved, it didn't vanish.
- **DeFi: don't conflate burn activity with ETH's store-of-value demand.** When sizing ETH-denominated collateral or staking assumptions in the liquid-staking study, treat flow demand (gas burned) and stock demand (ETH held) as separate estimates that can move in opposite directions.

## ko
- **Rabbit: 페이마스터의 ETH 보유량을 명시적으로 산정한다.** Rabbit이 ERC-4337 페이마스터를 통해 JYVE나 USDC로 가스비를 내게 한다면, 이제 ETH를 보유하고 변환하는 쪽은 페이마스터다. 가스 추상화가 시스템의 ETH 수요를 없앤다고 가정하지 말고 그 보유량을 모니터링한다.
- **Wallet: "ETH 필요 없음"이 아니라 실제로 가스를 대는 토큰을 보여준다.** simulate-before-sign 화면은 페이마스터가 내부적으로 사용자가 고른 토큰을 ETH로 변환하고 있음을 드러내야 한다. 보유 수요는 사라진 게 아니라 옮겨간 것이다.
- **DeFi: 소각 활동과 ETH의 가치 저장 수요를 혼동하지 않는다.** 유동성 스테이킹 연구에서 ETH 표시 담보나 스테이킹 가정을 산정할 때, 플로우 수요(소각된 가스)와 스톡 수요(보유된 ETH)를 서로 반대로 움직일 수 있는 별개의 추정치로 다룬다.
