## en
- **OFA: keep mandate, execution, settlement and audit as separate layers.** The intent+solver auction must not let the solver that proposes a fill also decide the spend policy — the same separation this card requires between AP2 mandate, x402 execution and Kora settlement.
- **Rabbit: give session-key mandates the same field list.** Add merchant/API allowlist, per-call cap, cumulative cap, expiry and a replay nonce to the ERC-7702/7715 mandate contract, the concrete fields this card's Korea-safe PoC uses.
- **Auditor: adopt this card's audit-log schema.** For any Jayverse payment flow — Verex Stripe onboarding, JYVE bridge transfers — log mandate hash, quote, payment proof, response hash, cumulative spend and denial reason as one joined record.

## ko
- **OFA: mandate, 실행, 정산, 감사를 분리된 레이어로 유지한다.** 인텐트+솔버 옥션은 체결을 제안하는 솔버가 지출 정책까지 결정하게 해서는 안 된다. 이 카드가 AP2 mandate, x402 실행, Kora 정산 사이에 요구하는 것과 같은 분리다.
- **Rabbit: 세션키 mandate에 같은 필드 목록을 준다.** ERC-7702/7715 mandate 컨트랙트에 머천트/API 허용목록, 콜당 한도, 누적 한도, 만료 시각, 리플레이 논스를 추가한다. 이 카드의 한국형 안전 PoC가 쓰는 구체적 필드다.
- **Auditor: 이 카드의 감사 로그 스키마를 채택한다.** Verex Stripe 온보딩, JYVE 브리지 전송 등 모든 Jayverse 결제 플로우에 대해 mandate 해시, 견적, 결제 증빙, 응답 해시, 누적 지출, 거부 사유를 하나의 결합 레코드로 남긴다.
