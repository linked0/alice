## en
- **Verex: pick a confirmation count per collateral size, not one global number.** Beyond weighing the finality curve, write an explicit table mapping deposit size to required confirmations, since a fixed low number is a subsidized attack surface as stakes grow.
- **Devnet: document the finality assumption once it becomes a real L2.** When Devnet moves past Anvil-forked-Sepolia to an OP-Stack L2, its own reorg/finality rule needs the same probabilistic-vs-absolute distinction spelled out for anything that credits deposits.
- **Bridge: require a minimum confirmation depth before minting on the destination side.** The lock-and-mint bridge's mint step should refuse to fire until the source-chain lock has enough confirmations for the value being moved, sized the way the finality curve suggests.

## ko
- **Verex: 전역으로 하나의 컨펌 수가 아니라 담보 규모별로 컨펌 수를 정한다.** 파이널리티 곡선을 저울질하는 것을 넘어, 입금 규모를 요구 컨펌 수에 매핑하는 표를 명시적으로 만든다. 고정된 낮은 숫자는 스테이크가 커질수록 보조금이 붙은 공격면이 되기 때문이다.
- **Devnet: 실제 L2가 되면 파이널리티 가정을 문서화한다.** Devnet이 Anvil로 포크된 Sepolia를 넘어 OP-Stack L2가 되면, 입금을 크레딧하는 모든 것에 대해 확률적 파이널리티와 절대적 파이널리티를 구분해 명시해야 한다.
- **Bridge: 목적지 측 민팅 전에 최소 컨펌 깊이를 요구한다.** 락앤민트 브리지의 민팅 단계는 소스 체인의 락이 옮기는 가치에 맞는 충분한 컨펌을 쌓기 전에는 발동하지 않아야 한다. 파이널리티 곡선이 제안하는 만큼의 깊이로.
