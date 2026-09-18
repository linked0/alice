## en
- **Wallet: give every bridge transfer a reconciliation field.** The bridge screen should attach a memo or reference (an order id, an obligation) to each JYVE transfer, since an amount, an address and a timestamp alone cannot answer what the transfer paid for.
- **Bridge/Token: log which leg takes the conversion spread.** Even without a fiat peg, the lock-and-mint relayer should record explicitly which side (Anvil or Sepolia) absorbs any conversion spread, mirroring the "who holds the record" question the FX Act forces on the stablecoin deal.
- **Auditor: require an owner for reconciliation on any cross-chain payment feature.** Before shipping a payment or bridge feature, name who owns matching a transfer to its obligation and who would file any reporting duty, so compressing the float is not mistaken for solving the whole problem.

## ko
- **Wallet: 모든 브리지 송금에 대사(reconciliation) 필드를 붙인다.** 브리지 화면은 각 JYVE 송금에 메모나 참조(주문 ID, 채무)를 붙여야 한다. 금액, 주소, 타임스탬프만으로는 그 송금이 무엇을 지불했는지 답할 수 없기 때문이다.
- **Bridge/Token: 어느 레그가 환전 스프레드를 가져가는지 기록한다.** 법정화폐 페그가 없더라도 lock-and-mint 릴레이어는 어느 쪽(Anvil 또는 Sepolia)이 환전 스프레드를 흡수하는지 명시적으로 기록해야 한다. 외환거래법이 스테이블코인 거래에 강제하는 "누가 기록을 갖는가" 질문과 같다.
- **Auditor: 체인 간 결제 기능마다 대사 책임자를 요구한다.** 결제나 브리지 기능을 출시하기 전에 송금을 채무와 매칭하는 책임자와 신고 의무가 있다면 누가 제출하는지 지정한다. float 압축을 전체 문제 해결로 착각하지 않기 위해서다.
