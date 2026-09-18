## en
- **Verex: keep compliance, FX/settlement, and availability clocks separate.** Stripe onboarding already splits these; when any bank-style or stablecoin rail is added later, record instruction-acceptance, compliance-clearance and beneficiary-availability as separate timestamps rather than one "instant" claim.
- **Auditor: apply the claim-boundary rule to every settlement-time claim.** Before Verex or Bridge cites a rail's speed (a bank deposit account, a stablecoin bridge), separate what the rail capability supports from what's actually published as an end-to-end SLA — the same discipline this page applies to KB's announcement.
- **Bridge: the ledger-moves-relationship-stays model is the right frame.** If the Anvil↔Sepolia bridge ever touches a fiat on/off-ramp, keep onboarding and compliance owned by whichever party already owns them today — moving the settlement rail should not silently move who owns the customer relationship.

## ko
- **Verex: 컴플라이언스, FX/정산, 이용 가능 시각의 시계를 분리해 둔다.** Stripe 온보딩은 이미 이를 분리하고 있다. 향후 은행식 레일이나 스테이블코인 레일이 추가되면 지시 접수, 컴플라이언스 통과, 수취인 이용 가능 시각을 하나의 "즉시" 주장이 아니라 개별 타임스탬프로 기록한다.
- **Auditor: 모든 정산 속도 주장에 클레임 경계 규칙을 적용한다.** Verex나 Bridge가 어떤 레일(은행 예금 계좌, 스테이블코인 브릿지)의 속도를 인용하기 전에, 이 글이 KB 발표에 적용한 것과 같은 방식으로 레일 능력과 실제 공개된 엔드투엔드 SLA를 분리한다.
- **Bridge: "원장은 옮기되 관계는 그대로"라는 모델을 그대로 쓴다.** Anvil↔Sepolia 브릿지가 언젠가 법정화폐 온/오프램프에 닿는다면, 온보딩과 컴플라이언스는 지금 이를 소유한 쪽이 계속 소유하게 한다. 정산 레일이 바뀐다고 고객 관계 소유자가 조용히 바뀌면 안 된다.
