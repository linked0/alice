## en
- **Wallet: implement transaction resubmission using the 12.5%-per-block cap explicitly — bump max fee by compounding 12.5% over N blocks in the simulate-before-sign flow, rather than an arbitrary multiplier.**
- **Verex: for settlement or oracle-resolution transactions clustered at known times, size the max-fee buffer directly from the AIMD cap — predict the worst case of several consecutive 12.5% increases instead of a flat safety margin.**
- **Devnet: add a config/test mode that replays base-fee changes with the real EIP-1559 formula, since a plain Anvil fork doesn't reproduce real base-fee volatility, so gas-estimation logic can be tested against worst-case sequences.**

## ko
- **Wallet: 트랜잭션 재제출 로직을 블록당 12.5% 상한을 명시적으로 반영해 구현한다.** simulate-before-sign 플로우에서 임의의 배수 대신 N개 블록에 걸친 12.5% 복리 상승으로 max fee를 올린다.
- **Verex: 정산이나 오라클 해소가 특정 시점에 몰리는 트랜잭션은 AIMD 상한에서 직접 max-fee 버퍼를 산정한다.** 균일한 안전 마진 대신 연속된 12.5% 상승이 몇 블록 이어지는 최악의 경우를 예측한다.
- **Devnet: 실제 EIP-1559 공식으로 base fee 변화를 재현하는 설정/테스트 모드를 추가한다.** 단순 Anvil 포크는 실제 base fee 변동성을 재현하지 못하므로, 가스 추정 로직을 최악의 시퀀스에 대해 테스트할 수 있게 한다.
