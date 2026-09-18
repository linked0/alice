| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| idempotent | 멱등의, 같은 요청을 여러 번 보내도 결과가 같은 · API·결제 요청 설계에서 핵심 성질. "protect one idempotent API route" |
| idempotency key | 멱등성 키 · 같은 요청을 식별해 중복 처리를 막는 값. "Stripe's Idempotency-Key and a durable state machine" |
| plumbing | (비유) 배후 인프라, 배관 작업 · 겉으로 안 보이는 기반 시스템을 가리킬 때. "removes blockchain plumbing from the seller" |
| atomic | 원자적인, 쪼갤 수 없는 · 여러 단계가 한 번에 전부 성공하거나 실패해야 할 때. "distributed transactions cannot be made atomic" |
| reconciliation | 대사, 대조 확인 · 서로 다른 시스템의 기록이 일치하는지 맞춰보는 절차. "reconciliation between facilitator results and canonical receipts" |
| canonical | 기준이 되는, 정본의 · 여러 기록 중 진짜로 신뢰할 원본을 가리킬 때. "the canonical receipt on chain is the authority" |
| durable | 영속적인, 사라지지 않는 · 장애가 나도 남아 있어야 하는 상태·기록을 말할 때. "one durable entitlement per settled payment" |
| eat the response | 응답을 삼켜버리다, 유실시키다 · 네트워크 장애로 응답이 사라지는 상황. "a network boundary that can eat the response" |
| misclassify | 잘못 분류하다 · 상황을 틀리게 판단해 엉뚱하게 대응할 때. "gets an error screen for a payment that worked" |
| structural (guarantee) | 구조적인 (보장) · 사람의 주의력이 아니라 설계로 담보되는 안전장치. "the guarantee has to be structural" |
| x402 | HTTP 402(Payment Required) 상태 코드를 이용해 스테이블코인 결제를 HTTP 미들웨어로 만드는 프로토콜 · 에이전트가 계정·API 키 없이 요청마다 결제하게 하는 레일. "x402 turns payment into HTTP middleware" |
| facilitator | 결제 검증·정산을 대행하는 제3자 서비스(x402 프로토콜의 역할) · 블록체인 연동 작업을 판매자 대신 처리하지만 분산 트랜잭션 문제까지 없애주지는 않음. "The facilitator removes blockchain plumbing from the seller" |
| HTTP 402 | "결제 필요(Payment Required)" HTTP 상태 코드 · 원래 거의 쓰이지 않던 코드를 x402가 실제 결제 트리거로 되살려 쓰는 것. "Returning HTTP 402 with payment requirements is an hour of work" |
<!-- acronyms 2026-09-18 -->
