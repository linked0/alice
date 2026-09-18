## en
- **Wallet: model wallet-linking as an authorization graph.** Require the remaining wallet's signature to unlink another, add a time-locked grace period, and keep purchase/settlement history with the account rather than the wallet.
- **Rabbit: apply the same three policy rows to session keys.** A valid ERC-4337/7702 session proves control of a key, not identity, so Rabbit's account and support model needs the same unlink-authority, history-ownership and shared-wallet tests as any linked-wallet account.
- **Personas: decide the shared-wallet policy before the market ships.** Reject, allow-many, or transfer-with-consent for a persona NFT tied to a wallet a team or multiple people control — pick one and test it, not after the first support ticket.

## ko
- **Wallet: 지갑 연결을 권한 그래프로 모델링한다.** 다른 지갑을 연결 해제하려면 남는 지갑의 서명을 요구하고, 시간 잠금 유예기간을 두며, 구매/정산 이력은 지갑이 아니라 계정에 귀속시킨다.
- **Rabbit: 같은 세 가지 정책 행을 세션 키에도 적용한다.** 유효한 ERC-4337/7702 세션은 키를 통제한다는 증명일 뿐 신원 증명이 아니므로, Rabbit의 계정 및 지원 모델도 연결된 지갑 계정과 동일한 연결해제 권한, 이력 소유권, 공유 지갑 테스트를 갖춰야 한다.
- **Personas: 마켓 출시 전에 공유 지갑 정책을 정한다.** 팀이나 여러 사람이 통제하는 지갑에 묶인 페르소나 NFT에 대해 거부, 다중 허용, 동의 기반 이전 중 하나를 고르고 테스트한다, 첫 지원 티켓이 들어온 뒤가 아니라.
