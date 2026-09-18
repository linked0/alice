## en
- **Verex: decide the settlement-proof scheme now, as a written tradeoff.** If a light-client verifier for settlement results is ever built, choose between MPT-style branch proofs and a Verkle-style constant-size commitment, and record the proof-size-vs-update-cost tradeoff before writing the contract.
- **Devnet: benchmark actual MPT proof sizes for Verex's real state keys before considering Verkle.** Anvil and Sepolia already use MPT, so measure the branching-factor-driven proof size for the specific keys Verex would need to prove, turning "when do we need Verkle" into a number.
- **gitboard: track settlement-proof byte size as a dashboard metric.** Once the exercise's node-count/byte-size table exists, keep the real number on gitboard so a future light-client feature is scoped against data, not assumption.

## ko
- **Verex: 정산 프루프 스킴을 지금 문서화된 트레이드오프로 결정한다.** 정산 결과를 위한 라이트클라이언트 검증기를 언젠가 만든다면, MPT 방식 브랜치 프루프와 Verkle 방식 상수 크기 커밋먼트 중 선택하고, 컨트랙트를 쓰기 전에 프루프 크기 대 업데이트 비용 트레이드오프를 기록해둔다.
- **Devnet: Verkle을 고려하기 전에 Verex의 실제 상태 키에 대한 실제 MPT 프루프 크기를 벤치마크한다.** Anvil과 Sepolia는 이미 MPT를 쓰므로, Verex가 증명해야 할 구체적 키에 대해 분기 계수가 만드는 프루프 크기를 측정해 "언제 Verkle이 필요한가"를 추측이 아니라 숫자로 만든다.
- **gitboard: 정산 프루프 바이트 크기를 대시보드 지표로 추적한다.** 이 연습문제의 노드 수/바이트 크기 표가 만들어지면 그 실제 숫자를 gitboard에 유지해, 향후 라이트클라이언트 기능이 추측이 아니라 데이터로 범위가 정해지게 한다.
