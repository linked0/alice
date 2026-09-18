## en
- **Verex: give every Buy action an intent ID, deduped client- and server-side.** Build the control-vs-fixed test the PoC describes — double-click under an artificially slow RPC and assert the fixed version settles exactly one order.
- **Token: apply the same intent-ID dedupe to the JYVE mint/AMM front end.** A double-click on mint is the same bug with a worse name; store id → txHash so a retry returns the existing receipt.
- **Wallet: disable the action button on a pending intent ID.** This is the cheapest layer of the fix — one UUID, one lookup table, one disabled button — and it belongs in Wallet's shared checkout component, not per-service.

## ko
- **Verex: 모든 Buy 액션에 클라이언트·서버 양쪽에서 중복 제거되는 의도 ID를 부여한다.** PoC가 설명하는 대조군 테스트를 만든다 — 인위적으로 느린 RPC에서 더블클릭하고, 고정된 버전이 정확히 하나의 주문만 정산하는지 검증한다.
- **Token: JYVE 민트/AMM 프론트엔드에도 같은 의도 ID 중복 제거를 적용한다.** 민트에서의 더블클릭은 같은 버그에 더 나쁜 이름이 붙은 것뿐이다. id → txHash를 저장해 재시도가 새 트랜잭션이 아니라 기존 영수증을 돌려주게 한다.
- **Wallet: 대기 중인 의도 ID가 있으면 액션 버튼을 비활성화한다.** UUID 하나, 조회 테이블 하나, 비활성화된 버튼 하나로 끝나는 가장 저렴한 방어층이며, 서비스마다 따로가 아니라 Wallet의 공용 체크아웃 컴포넌트에 넣어야 한다.
