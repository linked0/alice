## en
- **Wallet: expand "sent"/"success" into named states with named witnesses.** Simulate-before-sign should show submitted, included and finalized separately, each backed by its own witness (a receipt, then finality) — never let the submitting transaction's own status stand in for "done."
- **Bridge/relayer: "bridged" must split into lock-confirmed, relayed and minted, each owned by a different party.** Build the four-column table (state, owner, event, invariant) for the Anvil-to-Sepolia lock-and-mint path, and never mint before the lock's own finality clock, not just its inclusion.
- **Rabbit: session-key "authorized" is an authority status, so it may only shrink or be re-granted.** Add an explicit test that every mandate mutation event narrows or invalidates scope, and that an expired or revoked session never renders as the same green dot as a current one.

## ko
- **Wallet: "전송됨"/"성공" 같은 불린을 이름 붙은 증인이 있는 상태들로 펼친다.** 서명 전 시뮬레이션은 제출됨, 포함됨, 파이널됨을 각각 보여줘야 하고 각각 고유한 증인(영수증, 그다음 파이널리티)을 가져야 한다. 제출 트랜잭션 자신의 상태를 "완료"로 대신 쓰면 안 된다.
- **Bridge/릴레이어: "브리지됨"은 각각 다른 주체가 소유하는 락 확정, 릴레이됨, 민팅됨으로 나뉘어야 한다.** Anvil-Sepolia 락앤민트 경로에 상태·소유자·이벤트·불변식 4열 표를 만들고, 락의 단순 포함이 아니라 그 자체의 파이널리티 클럭 이전에는 민팅하지 않는다.
- **Rabbit: 세션 키의 "인가됨"은 권한 상태이므로 축소되거나 재부여될 때만 바뀐다.** 모든 맨데이트 변경 이벤트가 범위를 좁히거나 무효화하는지 명시적으로 테스트하고, 만료되거나 취소된 세션이 현재 세션과 같은 초록 점으로 표시되지 않게 한다.
