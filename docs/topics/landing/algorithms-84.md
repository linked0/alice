## en
- **Wallet: draw key/session-key derivation from an OS CSPRNG, never a userspace equivalent.** Add the exercise's fork/VM-clone reproducibility test to Wallet's key-generation suite to catch state duplication before it ships.
- **Bridge relayer: verify the relayer's signing nonce uses a deterministic-nonce spec (RFC 6979), not a custom RNG.** A long-lived relayer key is exactly the kind of signer this piece warns leaks a private key through nonce reuse.
- **Devnet: keep Anvil's deterministic test-mode RNG walled off from anything trusting Sepolia or mainnet.** Enforce that boundary in config so a devnet-seeded value never becomes the entropy source for a real signer.

## ko
- **Wallet: 키/세션 키 파생은 유저스페이스 대체물이 아니라 반드시 OS의 CSPRNG에서 뽑는다.** 익서사이즈의 fork/VM 클론 재현성 테스트를 Wallet의 키 생성 테스트 스위트에 추가해 상태 중복을 출시 전에 잡아낸다.
- **Bridge 릴레이어: 릴레이어의 서명 nonce가 커스텀 RNG가 아니라 결정론적 nonce 스펙(RFC 6979)을 쓰는지 확인한다.** 오래 사는 릴레이어 키는 이 글이 경고하는, nonce 재사용으로 개인키가 새는 바로 그 유형의 서명자다.
- **Devnet: Anvil의 결정론적 테스트 모드 RNG를 Sepolia나 메인넷을 신뢰하는 어떤 것과도 분리해 둔다.** devnet에서 시드된 값이 실제 서명자의 엔트로피 소스가 되지 않도록 설정으로 그 경계를 강제한다.
