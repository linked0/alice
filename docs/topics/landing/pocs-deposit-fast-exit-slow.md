## en
- **Bridge: document which clock each direction waits on.** In the Anvil↔Sepolia lock-and-mint relayer, write down explicitly what the deposit leg waits for (confirmation depth vs finality) and what the exit leg waits for (challenge window or proof), since the two directions cannot be sped up the same way.
- **Wallet: show the security clock, not a spinner.** Simulate-before-sign should tell the user which of the two clocks a pending bridge transaction is on, a gradable trust wait on deposit, an unshortenable proof wait on exit, instead of a generic "processing" state.
- **Bridge: treat the RPC dependency as a supply chain.** If the relayer watches L1 state through an external RPC provider, add a test for what happens when that provider lags or fails, since a fast confirmation rule is useless until the middleware watching L1 actually ships it.

## ko
- **Bridge: 각 방향이 무엇을 기다리는지 문서화한다.** Anvil↔Sepolia 락앤민트 릴레이어에서 예치 구간이 무엇을 기다리는지(확인 깊이 대 파이널리티), 출금 구간이 무엇을 기다리는지(챌린지 윈도우 또는 증명)를 명시한다. 두 방향은 같은 방식으로 빨라질 수 없기 때문이다.
- **Wallet: 스피너가 아니라 보안 시계를 보여준다.** 서명 전 시뮬레이션은 대기 중인 브리지 트랜잭션이 두 시계 중 어디에 있는지, 예치의 등급 매길 수 있는 신뢰 대기인지 출금의 단축 불가능한 증명 대기인지를 일반적인 "처리 중" 상태 대신 보여줘야 한다.
- **Bridge: RPC 의존성을 공급망 문제로 취급한다.** 릴레이어가 외부 RPC 제공자를 통해 L1 상태를 관찰한다면, 그 제공자가 지연되거나 실패할 때 무슨 일이 벌어지는지 테스트를 추가한다. 빠른 확인 규칙도 L1을 지켜보는 미들웨어가 실제로 이를 지원하기 전까지는 무용하다.
