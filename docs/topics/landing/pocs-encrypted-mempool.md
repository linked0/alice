## en
- **Verex: test residual-MEV before trusting any private settlement path.** If Verex ever routes resolution or large order transactions through an encrypted or private mempool, check whether sender, nonce, gas and size alone still let a bot target the largest settlement transactions.
- **Devnet: build the threshold-encryption simulator before adopting the primitive.** Reproduce the PoC's n-provider, k-threshold, one-colluding-subset simulator on devnet; if withheld, leaked and late keys aren't distinguishable, don't treat the scheme as usable for Verex order flow.
- **OFA: price the commit-before-decrypt cost into the auction.** A solver that must commit before it can decrypt pays for failed matches, so model that latency and failure cost explicitly in the intent/solver design, not just as extra gas.

## ko
- **Verex: 어떤 프라이빗 정산 경로든 신뢰하기 전에 잔여 MEV를 테스트한다.** Verex가 정산이나 대형 주문 트랜잭션을 암호화되거나 프라이빗한 멤풀로 보낸다면, 발신자, 논스, 가스, 크기만으로도 봇이 가장 큰 정산 트랜잭션을 여전히 노릴 수 있는지 확인한다.
- **Devnet: 그 원리를 채택하기 전에 임계값 암호화 시뮬레이터를 만든다.** PoC의 n개 제공자, k 임계값, 하나의 담합 부분집합 시뮬레이터를 devnet에서 재현한다. 키가 보류됐는지, 유출됐는지, 단순히 늦었는지 구별이 안 된다면 그 방식을 Verex 주문 흐름에 쓸 수 있다고 보지 않는다.
- **OFA: 복호화 전 커밋 비용을 경매에 반영한다.** 복호화하기 전에 커밋해야 하는 솔버는 실패한 매칭에 대한 비용을 치르므로, 그 지연과 실패 비용을 가스 외에 인텐트/솔버 설계에 명시적으로 반영한다.
