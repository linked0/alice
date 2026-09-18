## en
- **Bridge: put the lock-and-mint relayer's minting authority behind a (t,n) threshold signature instead of one EOA.** One compromised relayer key currently means unbacked minting; threshold signing removes that single point.
- **Wallet: use BLS's additive threshold structure for session-key/mandate revocation authority once Wallet handles real value.** BLS thresholdizes naturally; retrofitting the same onto ECDSA is a much harder MPC protocol, so the signature scheme choice matters before the design is set.
- **Devnet: prototype Shamir/DKG on devnet first, using the exercise's small-prime-field implementation, before deciding which of Verex, Bridge or Wallet gets threshold signing first.**

## ko
- **Bridge: 락앤민트 릴레이어의 민팅 권한을 단일 EOA가 아니라 (t,n) 임계 서명 뒤에 둔다.** 지금은 릴레이어 키 하나가 뚫리면 담보 없는 민팅으로 이어지는데, 임계 서명은 이 단일 실패 지점을 제거한다.
- **Wallet: Wallet이 실제 자산을 다루게 되면 세션 키/매니데이트 철회 권한에 BLS의 덧셈적 임계 구조를 쓴다.** BLS는 자연스럽게 임계화되지만 같은 것을 ECDSA에 이식하려면 훨씬 복잡한 MPC 프로토콜이 필요하므로, 설계를 굳히기 전에 서명 스킴 선택이 중요하다.
- **Devnet: Verex, Bridge, Wallet 중 어디에 임계 서명을 먼저 넣을지 정하기 전에, 익서사이즈의 작은 소수체 구현으로 Shamir/DKG를 devnet에서 먼저 프로토타이핑한다.**
