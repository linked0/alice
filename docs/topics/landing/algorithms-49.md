## en
- **Devnet: define an SLO (availability + p99 latency) for the hosted Anvil devnet itself, since every service targets it.** Track the 30-day error budget on gitboard so a single flaky devnet doesn't turn into a silent tax on every other service's reliability.
- **Verex: set an explicit SLO/error budget for RPC and settlement-confirmation latency.** Use the budget to gate feature releases vs reliability work — when it's exhausted, that's the trigger to stop shipping and fix the settlement path, not a judgment call each time.
- **gitboard: surface error-budget burn rate as a first-class panel per service.** That number, not a green/red badge, is what should decide "ship vs stabilize" across Rabbit, Verex, Wallet and Devnet.

## ko
- **Devnet: 모든 서비스가 대상으로 삼는 호스팅 Anvil devnet 자체에 SLO(가용성 + p99 지연)를 정의한다.** 30일 에러 예산을 gitboard에서 추적해, 불안정한 devnet 하나가 다른 모든 서비스의 신뢰성에 조용한 세금이 되지 않게 한다.
- **Verex: RPC와 정산 확인 지연에 명시적 SLO/에러 예산을 정한다.** 이 예산으로 기능 출시와 신뢰성 작업 중 무엇을 우선할지 정한다. 예산이 소진되면 그때그때 판단하지 말고 출시를 멈추고 정산 경로를 고치는 것을 트리거로 삼는다.
- **gitboard: 서비스별 에러 예산 소진율을 1급 패널로 보여준다.** Rabbit, Verex, Wallet, Devnet 전반에서 "출시할지 안정화할지"를 결정해야 하는 것은 초록/빨강 배지가 아니라 이 숫자다.
