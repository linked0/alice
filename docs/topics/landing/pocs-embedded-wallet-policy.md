## en
- **Wallet: draw the authority matrix for jayverse-wallet before shipping.** Fill in who can sign, recover and export for the embedded wallet's own recovery mode, export flow and any server-side session signer, from observed behavior rather than the provider's docs.
- **Rabbit: session keys and mandates are the scoped-app-signer row.** ERC-4337/EIP-7702/7715 session keys need the same test as the PoC's fourth path — what a mandate can do without the user, and whether the app can widen its scope without a fresh user approval.
- **Devnet: run the four failure paths there first.** New device, lost auth factor, key export, and a scoped signer are cheap to reproduce on Devnet before testing them on Sepolia, and the matrix should be filled in from what actually happens, not from the wallet provider's marketing.
- **Auditor: publish the wallet's authority matrix as a standing artifact.** Since the end user never sees who can approve recovery or change signer policy, that matrix — not a custody claim in prose — is what the Auditor row should carry for jayverse-wallet.

## ko
- **Wallet: 출시 전에 jayverse-wallet의 권한 매트릭스를 그린다.** 임베디드 월렛 자체의 복구 모드, 익스포트 플로우, 서버 측 세션 서명자에 대해 누가 서명·복구·익스포트할 수 있는지를 제공자 문서가 아니라 관찰된 동작으로 채운다.
- **Rabbit: 세션 키와 mandate는 범위 지정 앱 서명자 행이다.** ERC-4337/EIP-7702/7715 세션 키에도 PoC의 네 번째 경로와 같은 테스트가 필요하다 — mandate가 사용자 없이 무엇을 할 수 있는지, 앱이 사용자의 재승인 없이 범위를 넓힐 수 있는지.
- **Devnet: 네 가지 실패 경로를 거기서 먼저 돌린다.** 새 기기, 인증 수단 분실, 키 익스포트, 범위 지정 서명자는 Sepolia보다 Devnet에서 재현하기 싸다. 매트릭스는 월렛 제공자의 마케팅이 아니라 실제로 일어나는 일로 채운다.
- **Auditor: 월렛의 권한 매트릭스를 상시 산출물로 공개한다.** 최종 사용자는 누가 복구를 승인하고 서명자 정책을 바꿀 수 있는지 보지 못하므로, Auditor 행이 jayverse-wallet에 대해 들고 있어야 할 것은 산문 속 커스터디 주장이 아니라 이 매트릭스다.
