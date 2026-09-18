## en
- **Devnet: an Anvil test suite proves the protocol only, not real support.** Before claiming Rabbit supports EIP-7702/7715, build the separate wallet × chain matrix — does the wallet accept the authorization, render what's delegated, show the delegate address, and allow revocation.
- **Wallet: block or fall back when a wallet renders the authorization as opaque hex instead of plain language.** Track which wallets Jayverse's embedded wallet and any external wallet integration actually render readably, and treat that as a shipping gate, not a nice-to-have.
- **Rabbit: separate "protocol defines it," "chain activated it," and "wallet can show it" in status docs.** Don't collapse the three into one "supports 7702" claim; each is owned by a different party on a different schedule.

## ko
- **Devnet: Anvil 테스트 스위트는 프로토콜 수준만 증명하며, 실제 지원 여부는 아니다.** Rabbit이 EIP-7702/7715을 지원한다고 말하기 전에, 지갑이 위임을 수락하는지, 위임 내용을 보여주는지, 위임 주소를 표시하는지, 철회를 허용하는지를 담은 지갑×체인 매트릭스를 별도로 만든다.
- **Wallet: 지갑이 위임을 평문 대신 불투명한 16진수로 보여준다면 차단하거나 폴백한다.** Jayverse 임베디드 월렛과 외부 지갑 연동이 실제로 읽을 수 있게 렌더링하는지 추적하고, 이를 있으면 좋은 기능이 아니라 출시 게이트로 취급한다.
- **Rabbit: 상태 문서에서 "프로토콜이 정의함", "체인이 활성화함", "지갑이 보여줄 수 있음"을 분리한다.** 셋을 "7702 지원"이라는 하나의 주장으로 뭉치지 않는다. 각각 다른 주체가 다른 일정으로 책임진다.
