## en
- **Wallet: bind every signed message to one contract and one chain id.** Session-key grants and permits the embedded wallet produces need an EIP-712 domain separator, checked in simulate-before-sign so a replay attempt is visible before signing.
- **Bridge/Token: test cross-deployment replay across Devnet and Sepolia.** Add a test that replays a signed permit across the bridge's two chains to confirm the domain separator actually blocks it.
- **Auditor: check every Rabbit and Wallet signing path for nonce, domain separator and chain id.** Make it a standing checklist item rather than a one-time review, since this is the exact class EIP-712 exists to close.

## ko
- **Wallet: 모든 서명 메시지를 하나의 컨트랙트와 체인 ID에 묶는다.** 임베디드 월렛이 만드는 세션키 승인과 permit에는 EIP-712 도메인 분리자가 필요하며, simulate-before-sign에서 이를 확인해 서명 전에 리플레이 시도가 보이게 한다.
- **Bridge/Token: Devnet과 Sepolia 간 교차 배포 리플레이를 테스트한다.** 브리지가 걸쳐 있는 두 체인에서 서명된 permit을 리플레이하는 테스트를 추가해 도메인 분리자가 실제로 이를 막는지 확인한다.
- **Auditor: Rabbit과 Wallet의 모든 서명 경로에서 논스, 도메인 분리자, 체인 ID를 점검한다.** 일회성 리뷰가 아니라 상시 체크리스트 항목으로 만든다. EIP-712가 막기 위해 존재하는 바로 그 부류의 버그이기 때문이다.
