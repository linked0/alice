## en
- **Rabbit: track 8141's progress, don't redesign around it yet.** With the proposal at SFI targeting Hegotá (~2027 Q2), keep rabbit's ERC-4337/EIP-7702 session-key and mandate stack as the near-term plan — treat native frame transactions as a decade-scale migration to watch, not a reason to pause current AA work.
- **Rabbit: prototype a session key as a VERIFY frame when a testnet exists.** Once any client exposes frame transactions on a public testnet, build a minimal session-key mandate (expiry, allowed contract, per-tx limit) as VERIFY-frame logic — it maps directly onto rabbit's existing mandate model and is the cheapest way to validate the migration path early.
- **Devnet: gas-bound any custom validateUserOp-style check the same way.** Since an enshrined VERIFY frame must be strictly gas-bounded and cheaply re-checkable to avoid a free DoS vector, apply that same bound-and-recheck discipline to rabbit's own account-validation code running on devnet today.

## ko
- **Rabbit: 8141 진행 상황은 지켜보되 아직 설계를 바꾸지 않는다.** 제안이 SFI 단계로 Hegotá(2027년 2분기 목표)를 향하는 지금, rabbit의 ERC-4337/EIP-7702 세션 키와 위임 스택을 단기 계획으로 유지한다. 네이티브 프레임 트랜잭션은 10년 단위 마이그레이션으로 지켜볼 대상이지 지금 AA 작업을 멈출 이유가 아니다.
- **Rabbit: 테스트넷이 생기면 세션 키를 VERIFY 프레임으로 시제작한다.** 어떤 클라이언트든 공개 테스트넷에서 프레임 트랜잭션을 노출하면, 만료·허용 컨트랙트·트랜잭션당 한도를 갖는 최소 세션 키 위임을 VERIFY 프레임 로직으로 만든다. rabbit의 기존 위임 모델에 바로 대응되며 마이그레이션 경로를 일찍 검증하는 가장 싼 방법이다.
- **Devnet: 커스텀 validateUserOp류 검사도 같은 방식으로 가스를 제한한다.** 제도화된 VERIFY 프레임이 무료 DoS 벡터가 되지 않으려면 엄격히 가스가 제한되고 값싸게 재검사 가능해야 한다는 원칙을, 지금 devnet에서 돌아가는 rabbit 자체 계정 검증 코드에도 그대로 적용한다.
