## en
- **Verex: measure the no-trade band, don't assume it.** Compute the YES+NO price band width the same way this card computes the perp basis band — as a readout of the cheapest arbitrageur's cost floor (fees, slippage, capital) — and publish that width as the honest bound on how tight Verex's own prices can ever be.
- **Verex market maker: treat any hedged inventory as a margin-logistics problem, not a pricing one.** If the market maker ever carries offsetting positions across venues or legs, add continuous margin and collateral monitoring as its own test, separate from the entry-signal logic, since a hedge only holds if both legs survive to be unwound together.
- **Auditor: publish the cost-floor methodology next to the resolution methodology.** The band a market trades inside is public information anyone can measure from the order book; write down how Verex computes it so "how accurate can our prices be" has a documented answer, not just a resolution rule.

## ko
- **Verex: 무거래 밴드를 가정하지 말고 측정한다.** 이 카드가 펀딩 베이시스 밴드를 계산하는 방식 그대로, YES+NO 가격 밴드 폭을 가장 싼 차익거래자의 비용(수수료, 슬리피지, 자본 비용) 지표로 계산하고, 그 폭을 Verex 가격이 얼마나 정확할 수 있는지에 대한 정직한 하한으로 공개한다.
- **Verex 마켓 메이커: 헤지된 포지션은 가격 문제가 아니라 마진 물류 문제로 다룬다.** 마켓 메이커가 여러 거래소나 레그에 걸쳐 상쇄 포지션을 보유한다면, 진입 신호 로직과 별개로 지속적인 마진·담보 모니터링을 독립된 테스트로 추가한다. 헤지는 두 레그가 함께 청산될 때까지 살아남아야만 헤지이기 때문이다.
- **Auditor: 정산 방법론 옆에 비용 하한 방법론도 공개한다.** 마켓이 그 안에서 거래되는 밴드는 누구나 오더북에서 측정할 수 있는 공개 정보다. Verex가 이를 어떻게 계산하는지 적어두면 "우리 가격이 얼마나 정확할 수 있는가"에 정산 규칙뿐 아니라 문서화된 답이 생긴다.
