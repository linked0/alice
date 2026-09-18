## en
- **Rabbit: name the single owner of session-key allowance state.** Before implementing concurrent mandate execution under EIP-7702, write down which one component holds write access to a session's remaining allowance at any moment, the same one-mutable-reference rule the borrow checker enforces.
- **Bridge/Token: give the relayer a single-owner claim path.** For concurrent Anvil/Sepolia event processing, use an index-based claim or a single-owner queue for the mint counter and nonce state, instead of shared mutable references two workers could both touch.
- **Auditor: ask "who owns this state right now" for every concurrent off-chain service.** Apply it to the relayer and any indexer, not only to Rust code, since aliased mutable state is the same bug in Go or TypeScript.

## ko
- **Rabbit: 세션키 허용량 상태의 단일 소유자를 지정한다.** EIP-7702 하에서 동시 매니데이트 실행을 구현하기 전에, 어느 한 컴포넌트가 특정 순간 세션의 남은 허용량에 대한 쓰기 권한을 갖는지 적어둔다. 보로우 체커가 강제하는 것과 같은 단일 가변 참조 규칙이다.
- **Bridge/Token: 릴레이어에 단일 소유자 클레임 경로를 준다.** Anvil/Sepolia 동시 이벤트 처리에서, 두 워커가 동시에 건드릴 수 있는 공유 가변 참조 대신 민팅 카운터와 논스 상태에 인덱스 기반 클레임이나 단일 소유자 큐를 쓴다.
- **Auditor: 모든 동시성 오프체인 서비스에 "지금 이 상태를 누가 소유하는가"를 묻는다.** 릴레이어와 인덱서 모두에 적용한다. 별칭된 가변 상태는 Rust뿐 아니라 Go나 TypeScript에서도 같은 버그이기 때문이다.
