## en
- **Verex: give every payment/order an idempotency key and a durable state machine.** Track received → verified → submitted → settled → fulfilled per order so a retried checkout call after a lost response can't double-charge or double-fulfill.
- **Wallet: treat "already used" as success, not error.** When the wallet resubmits a signed tx after a lost response and the chain refuses a second settle, surface that as "this already went through," not a failure screen.
- **Auditor: write down that the onchain receipt outranks a facilitator's "settled" claim.** For any payment rail Verex adds, the canonical receipt is the authority; a service saying settlement completed is only a claim to reconcile against it.

## ko
- **Verex: 모든 결제/주문에 idempotency 키와 durable 상태 머신을 붙인다.** received → verified → submitted → settled → fulfilled 단계를 주문 단위로 추적해서, 응답이 유실된 뒤 재시도된 체크아웃 호출이 이중 청구나 이중 이행으로 이어지지 않게 한다.
- **Wallet: "이미 사용됨"을 실패가 아니라 성공으로 취급한다.** 응답 유실 후 지갑이 서명된 트랜잭션을 재전송했는데 체인이 두 번째 정산을 거부하면, 이를 오류 화면이 아니라 "이미 처리됨"으로 보여준다.
- **Auditor: 온체인 영수증이 facilitator의 "정산됨" 주장보다 우선한다고 명시한다.** Verex가 추가하는 어떤 결제 레일이든 캐노니컬 영수증이 최종 권위이고, 서비스가 정산 완료라고 말하는 것은 그것과 대조해야 할 하나의 주장일 뿐이다.
