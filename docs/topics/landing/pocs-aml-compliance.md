## en
- **Verex: split AML obligations into protocol-carryable and licensed-entity-only before scaling past devnet.** Address screening and a transfer allowlist are things Verex's contracts or API can enforce; filing an STR or setting a risk rating are not, and that line should be a written doc, not an assumption.
- **Wallet: use the session-signer policy engine as the protocol's screening point.** A scoped app signer can already gate what a transaction is allowed to do, so a destination-address check against a sanctions list is a natural addition to jayverse-wallet's policy layer rather than a separate service.
- **Auditor: keep a decision record from day one for anything with compliance exposure.** Inputs, model or rule version, the score, and what a human did and why — small enough to add now, and the exact gap the AML note calls out as the difference between a PoC and a real filing.

## ko
- **Verex: devnet을 넘어 확장하기 전에 AML 의무를 프로토콜이 감당할 수 있는 것과 라이선스 기관만 할 수 있는 것으로 나눈다.** 주소 스크리닝과 전송 허용목록은 Verex의 컨트랙트나 API가 강제할 수 있지만, STR 제출이나 리스크 등급 결정은 그렇지 않다. 이 구분은 가정이 아니라 문서로 적어둔다.
- **Wallet: 세션 서명자 정책 엔진을 프로토콜의 스크리닝 지점으로 쓴다.** 범위 지정 앱 서명자는 이미 트랜잭션이 무엇을 할 수 있는지 제한하므로, 제재 목록 대비 목적지 주소 확인은 별도 서비스가 아니라 jayverse-wallet의 정책 레이어에 자연스럽게 추가할 수 있다.
- **Auditor: 컴플라이언스 노출이 있는 모든 것에 대해 첫날부터 의사결정 기록을 남긴다.** 입력, 모델/규칙 버전, 점수, 사람이 한 일과 그 이유 — 지금 당장 추가할 만큼 작은 일이며, AML 노트가 PoC와 실제 제출의 차이로 지목한 정확한 그 지점이다.
