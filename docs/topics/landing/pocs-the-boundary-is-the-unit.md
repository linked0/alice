## en
- **Bridge: draw the trust boundary for the lock-and-mint relayer.** Contracts we control go inside, RPC providers and relayer keys and future CCIP messages go outside, and for each crossing write what it can do if it turns hostile, not just whether it's authorized.
- **Wallet: extend simulate-before-sign's what-can-this-call-do check to the dApp-connection boundary itself.** Not just the transaction — an authorized connection is exactly where this page says attacks hide.
- **OFA: a solver that wins the auction is authorized by construction.** Write separately what a winning solver can do if hostile — front-run, wrong fill, censor — rather than trusting the auction result as a safety check.
- **Auditor: adopt boundary-diagram-first as the standing review step.** Do it before consulting any external vulnerability checklist for a new Jayverse service.

## ko
- **Bridge: lock-and-mint 릴레이어의 신뢰 경계를 그린다.** 우리가 통제하는 컨트랙트는 안쪽에, RPC 제공자와 릴레이어 키, 향후 CCIP 메시지는 바깥쪽에 두고, 각 경계 통과 지점마다 인가 여부가 아니라 적대적으로 변했을 때 무엇을 할 수 있는지를 적는다.
- **Wallet: simulate-before-sign의 "이 호출이 무엇을 할 수 있는가" 점검을 dApp 연결 경계 자체로 확장한다.** 트랜잭션뿐만이 아니다. 이 페이지가 말하는 공격의 은신처가 바로 인가된 연결이기 때문이다.
- **OFA: 경매에서 이긴 솔버는 구조상 이미 인가된 상태다.** 인가된 결과 자체를 안전 점검으로 믿는 대신, 이긴 솔버가 적대적으로 변했을 때 할 수 있는 것 — 프런트러닝, 잘못된 체결, 검열 — 을 별도로 적는다.
- **Auditor: 경계 다이어그램을 먼저 그리는 것을 표준 리뷰 단계로 채택한다.** 새 Jayverse 서비스에 외부 취약점 체크리스트를 참고하기 전에 이를 먼저 한다.
