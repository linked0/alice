## en
- **Rabbit: implement the gate for the AA payment agent explicitly.** Pre-signing simulation via Tenderly, an amount cap per mandate, and nonce-based idempotency keys so a retry never double-sends — the concrete design the card's exercise asks for.
- **Wallet: make simulate-before-sign the mandatory gate the agent loop calls.** Not an optional UI step, and log which model version approved each transaction for provenance.
- **Auditor: require every irreversible-action tool to declare its gate and idempotency key.** Transfers, bridge calls, market-resolution triggers — check this in one place per release.

## ko
- **Rabbit: AA 결제 에이전트에 게이트를 명시적으로 구현한다.** Tenderly를 통한 사전 서명 시뮬레이션, 위임당 금액 상한, 논스 기반 idempotency 키로 재시도가 절대 이중 전송되지 않게 한다. 카드의 연습문제가 요구하는 구체적 설계다.
- **Wallet: simulate-before-sign을 에이전트 루프가 반드시 호출하는 게이트로 만든다.** 선택적 UI 단계가 아니라 필수로 하고, 어떤 모델 버전이 각 트랜잭션을 승인했는지 프로비넌스로 기록한다.
- **Auditor: 되돌릴 수 없는 액션을 수행하는 모든 도구가 게이트와 idempotency 키를 선언하도록 요구한다.** 전송, 브리지 호출, 마켓 정산 트리거를 릴리스마다 한 곳에서 확인한다.
