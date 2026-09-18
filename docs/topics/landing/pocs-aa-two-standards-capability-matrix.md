## en
- **Rabbit: load a versioned capability manifest per chain instead of branching on chain ID.** Sepolia, the Anvil devnet and any future OP-Stack L2 should each declare batching, sponsorship and session support explicitly, compiled through separate ERC-4337/7702/7715 adapters.
- **Wallet: surface a downgrade before signing, not after.** If a scoped session key would compile down to a full-authority signature on a given chain, the simulate-before-sign screen must show that semantic loss, not silently accept it.
- **CI: run one conformance vector set against every AA adapter Rabbit ships.** Atomic batch, sponsored call, scoped session, expired authorization and recovery should all be tested per adapter, gated in CI so a rail change can't quietly drop a guarantee.

## ko
- **Rabbit: 체인 ID로 분기하는 대신 체인별로 버전이 있는 capability manifest를 로드한다.** Sepolia, Anvil devnet, 그리고 앞으로의 OP-Stack L2는 각각 배칭, 스폰서십, 세션 지원 여부를 명시적으로 선언하고, 별도의 ERC-4337/7702/7715 어댑터를 거쳐 컴파일되어야 한다.
- **Wallet: 서명 전에 다운그레이드를 노출한다, 서명 후가 아니라.** 범위가 제한된 세션 키가 특정 체인에서 전권 서명으로 컴파일된다면, simulate-before-sign 화면이 그 의미 손실을 보여줘야 한다. 조용히 받아들여서는 안 된다.
- **CI: Rabbit이 지원하는 모든 AA 어댑터에 동일한 conformance 벡터 세트를 돌린다.** 원자적 배치, 스폰서 호출, 범위 제한 세션, 만료된 승인, 복구를 어댑터별로 테스트하고 CI에 게이트로 건다. 레일 변경이 조용히 보장을 떨어뜨리지 못하게 한다.
