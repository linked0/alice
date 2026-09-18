## en
- **Wallet: simulate-before-sign is the on-device-screen equivalent.** Treat what the simulation actually parses and renders before signing as a security-critical decision, the same role a hardware wallet's own screen plays against blind signing — not just a convenience feature.
- **Rabbit: write the mandate's scope down, not just its existence.** EIP-7702/7715 session keys and mandates are the "what may this key sign without a human" question the card raises for delegated signing; each mandate needs an explicit spend cap, target-contract list and expiry before it ships.
- **Bridge: define the relayer key's at-rest backup separately from its in-use protection.** The relayer's signing key is a bearer secret like a seed; document its backup/rotation scheme (who holds shares, how many are needed) on its own, since no signing hardware covers that gap.

## ko
- **Wallet: simulate-before-sign은 온디바이스 화면과 같은 역할을 한다.** 서명 전에 시뮬레이션이 실제로 무엇을 파싱하고 보여주는지를 블라인드 서명에 맞서는 하드웨어 지갑 화면과 같은 보안 핵심 결정으로 취급한다. 단순한 편의 기능이 아니다.
- **Rabbit: 권한(mandate)의 존재가 아니라 범위를 적어둔다.** EIP-7702/7715 세션 키와 mandate는 이 카드가 위임 서명에 대해 묻는 "이 키가 사람 없이 무엇에 서명할 수 있는가"라는 질문 그 자체다. 각 mandate는 출시 전에 명시적인 지출 한도, 대상 컨트랙트 목록, 만기를 가져야 한다.
- **Bridge: 릴레이어 키의 저장 백업을 사용 중 보호와 별도로 정의한다.** 릴레이어 서명 키는 시드처럼 소지자가 곧 소유자인 비밀이다. 백업·로테이션 방식(누가 몇 개의 조각을 갖는지)을 따로 문서화한다. 어떤 서명 하드웨어도 이 저장 단계의 공백을 막아주지 않기 때문이다.
