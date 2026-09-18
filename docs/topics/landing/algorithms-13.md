## en
- **Verex: extract the dual value from the CLOB's uniform-clearing-price batch auction and use it as the settlement price.** Re-read the matching logic through this lens, and use complementary slackness as a sanity check — a matched order should have a binding constraint, an unmatched one should not.
- **OFA: formulate the solver auction's allocation as an LP and pay solvers the dual (shadow) price.** The fee/rebate a solver earns should fall out of relaxing its winning bid's constraint by one unit, not an arbitrary schedule.
- **Number: publish a small worked LP-duality example (5-10 bids) as a reading.** It's directly reusable for auditing Verex's clearing price later, so it earns its place on Number rather than staying a one-off exercise.

## ko
- **Verex: CLOB의 균일 정산가 배치 옥션에서 듀얼 값을 뽑아 정산가로 쓴다.** 매칭 로직을 이 관점으로 다시 읽고, 상보적 여유성을 검증용으로 쓴다. 매칭된 주문은 묶인 제약이 있어야 하고 매칭되지 않은 주문은 없어야 한다.
- **OFA: 솔버 옥션의 배분을 LP로 공식화하고 솔버에게 듀얼(섀도) 가격을 지불한다.** 솔버가 받는 수수료/리베이트는 임의의 스케줄이 아니라 자신의 낙찰 제약을 한 단위 완화했을 때의 값에서 나와야 한다.
- **Number: 작은 LP 듀얼리티 예제(입찰 5~10개)를 읽기로 발행한다.** 나중에 Verex의 정산가를 감사하는 데 그대로 재사용할 수 있으므로 일회성 연습이 아니라 Number에 남을 가치가 있다.
