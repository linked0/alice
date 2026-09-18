## en
- **Verex: model a refund as its own payment, not a chargeback, in the Stripe-onboarding path.** Give it a reference to the original paymentId, an approval policy (window, cap, approver role) and a funded refund-budget wallet, since settlement on Verex's rails can't be reversed the way a card network reverses a charge.
- **Wallet: add a reconciliation ledger view that joins a payment and its refund into one net event.** Test double-refund blocked and partial refunds sum-capped before a real refund request happens, the same way the card's PoC does.
- **Auditor: write down who may approve a refund and from which balance, before it's needed.** The same authority-matrix question card networks answered internally has to be answered explicitly for any Jayverse product that takes payments on irreversible rails.

## ko
- **Verex: Stripe 온보딩 경로에서 환불을 차지백이 아니라 그 자체의 결제로 모델링한다.** 원래 paymentId에 대한 참조, 승인 정책(기간, 한도, 승인자 역할), 자금이 채워진 환불 예산 지갑을 부여한다. Verex의 레일 위 정산은 카드 네트워크가 청구를 되돌리는 방식으로는 되돌릴 수 없기 때문이다.
- **Wallet: 결제와 그 환불을 하나의 순 이벤트로 묶어 보여주는 정산 원장 뷰를 추가한다.** 실제 환불 요청이 일어나기 전에, 이 카드의 PoC처럼 이중 환불 차단과 부분 환불 합계 상한을 테스트한다.
- **Auditor: 누가 어떤 잔액에서 환불을 승인할 수 있는지 필요해지기 전에 적어둔다.** 카드 네트워크가 내부적으로 답해온 것과 같은 권한 행렬 질문을, 되돌릴 수 없는 레일 위에서 결제를 받는 모든 Jayverse 상품에 대해 명시적으로 답해야 한다.
