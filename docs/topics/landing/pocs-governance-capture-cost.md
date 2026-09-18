## en
- **DeFi: price voting power before granting a role, not after.** Before jayverse-defi hands role_manager, debt manager, or emergency manager on any vault strategy to a governance contract, compute the cost to buy 51% of historical turnout against governed TVL as a design check, not a documentation afterthought.
- **Auditor: add "has any timelocked proposal ever been cancelled or vetoed" as a standing question.** If the answer is never, the audit should flag the timelock as decorative rather than crediting it as a control.
- **Token/Bridge/Personas: tie JYVE voting weight to locked stake or vault shares, not a freely tradeable token.** That makes the invariant self-enforcing — acquiring 51% of votes requires depositing 51% of the value at risk, so half of anything stolen was already the attacker's.
- **Devnet/gitboard: build a monitor, not a one-time audit.** Since the cost-to-capture invariant is time-varying, track governance-token float against DEX depth on devnet continuously and surface it on gitboard rather than checking it once at launch.

## ko
- **DeFi: 권한을 주기 전에 투표권 가격부터 매긴다.** jayverse-defi의 볼트 전략에 role_manager, debt manager, emergency manager를 거버넌스 컨트랙트에 넘기기 전에, 과거 투표 참여율의 51%를 사는 비용을 거버넌스 대상 TVL과 비교해 설계 단계의 점검 항목으로 삼는다. 문서화는 그다음이다.
- **Auditor: "타임락 걸린 제안이 취소되거나 거부된 적 있는가"를 상시 질문으로 추가한다.** 답이 한 번도 없다면, 그 타임락은 통제 장치가 아니라 장식으로 기록해야 한다.
- **Token/Bridge/Personas: JYVE 투표권을 자유거래 토큰이 아니라 락업된 스테이크나 볼트 지분에 묶는다.** 그러면 51%의 투표권을 얻으려면 위험에 노출된 자산의 51%를 예치해야 하므로 불변식이 스스로 강제된다.
- **Devnet/gitboard: 일회성 감사가 아니라 모니터를 만든다.** 탈취 비용 불변식은 시간에 따라 변하므로, 거버넌스 토큰 유통량 대 DEX 깊이를 devnet에서 지속적으로 추적하고 gitboard에 노출하며, 출시 시점에 한 번만 점검하지 않는다.
