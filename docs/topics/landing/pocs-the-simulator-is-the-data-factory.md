## en
- **Devnet: measure transfer rate, not just devnet throughput.** Treat Devnet like the card treats MuJoCo — a cheap simulator for contract and bridge behavior — and track how often a devnet-passing scenario also holds on Sepolia, not just how many scenarios devnet runs per hour.
- **OFA: randomize the simulated auction, don't let a solver overfit devnet.** Vary fee levels, latency and competing-solver counts when testing the intent/solver mechanism, so a solver tuned on one fixed devnet setup doesn't just learn that setup's quirks.
- **Game: log productivity as throughput times success, not throughput alone.** If Game ever scripts or trains board/NPC behavior against simulated market data, report the combined number the way the card does, since a faster test loop that doesn't transfer is a downgrade.

## ko
- **Devnet: devnet 처리량이 아니라 전이율을 측정한다.** 이 카드가 MuJoCo를 다루듯 Devnet을 컨트랙트·브리지 동작을 위한 값싼 시뮬레이터로 취급하고, devnet을 시간당 몇 번 돌리는지가 아니라 devnet에서 통과한 시나리오가 Sepolia에서도 성립하는 비율을 추적한다.
- **OFA: 시뮬레이션 경매를 무작위화해 솔버가 devnet에 과적합되지 않게 한다.** intent/solver 메커니즘을 테스트할 때 수수료 수준, 지연시간, 경쟁 솔버 수를 다양화한다. 고정된 devnet 설정 하나에 맞춰진 솔버가 그 설정의 버릇만 배우지 않도록 한다.
- **Game: 처리량이 아니라 처리량×성공률을 생산성으로 기록한다.** Game이 시뮬레이션 마켓 데이터로 보드·NPC 동작을 스크립트하거나 학습시킨다면 카드처럼 결합된 숫자를 보고한다. 전이되지 않는 더 빠른 테스트 루프는 개선이 아니라 퇴보다.
