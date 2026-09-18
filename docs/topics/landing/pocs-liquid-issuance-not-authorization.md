## en
- **Bridge/Token: wire the invariant test to an automatic halt, not a log line.** "Minted on dest == locked on source, always" needs to be independently computable, live with the mint path rather than the withdraw gate, and halt on violation rather than merely alert.
- **Auditor: state the limit of the authority matrix.** A correct permission list proves who may mint, not that the code they run preserves the supply invariant — write that limitation into what the Auditor publishes, using this incident as the citation.
- **Devnet / Dark Horse: reproduce the class before defending against it.** Build a local-fork PoC where a mint bug yields valid-but-unbacked units and a redeem path honors them, then confirm the invariant test catches it.
- **CI: put simulate-before-sign on the mint transaction itself.** A Foundry-fork check that reads "total issuance changed unexpectedly" before signing is the cheapest place to catch this class, ahead of the peg-out ever seeing the token.

## ko
- **Bridge/Token: 불변식 테스트를 자동 중단에 연결한다, 로그 한 줄이 아니라.** "목적지에서 발행된 양 == 원본에서 잠긴 양, 항상"은 독립적으로 계산 가능해야 하고, 출금 게이트가 아니라 발행 경로에 함께 있어야 하며, 위반 시 알림이 아니라 중단으로 이어져야 한다.
- **Auditor: 권한 매트릭스의 한계를 명시한다.** 올바른 권한 목록은 누가 발행할 수 있는지를 증명할 뿐, 그 코드가 공급 불변식을 지키는지는 증명하지 않는다. 이 사고를 근거로 그 한계를 Auditor가 공개하는 내용에 적어둔다.
- **Devnet / Dark Horse: 방어하기 전에 이 유형을 재현한다.** 발행 버그가 유효하지만 담보되지 않은 단위를 만들고 상환 경로가 이를 받아들이는 로컬 포크 PoC를 만든 뒤, 불변식 테스트가 이를 잡아내는지 확인한다.
- **CI: 서명 전 시뮬레이션을 발행 트랜잭션 자체에 건다.** 서명 전에 "총 발행량이 예상치 못하게 변했다"를 읽는 Foundry 포크 체크가, 페그아웃이 토큰을 보기 전에 이 유형을 잡는 가장 저렴한 지점이다.
