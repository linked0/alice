## en
- **Verex: use the exact recipe here for both the Stripe webhook and any oracle-result callback.** HMAC-SHA256 over body plus timestamp, a constant-time compare, a bounded replay window, and an idempotency key — two different external signers, the same verification gate before either reaches settlement.
- **Bridge: gate relayer messages between the Anvil and Sepolia legs with the same signature-plus-timestamp check.** A forged or replayed relayer message does not just corrupt a read — it triggers a mint, so idempotency and the replay window belong on that path before it ships, not after an incident.

## ko
- **Verex: Stripe 웹훅과 오라클 결과 콜백 양쪽에 여기 나온 레시피를 그대로 쓴다.** 본문+타임스탬프에 대한 HMAC-SHA256, 상수 시간 비교, 제한된 재전송 윈도우, 멱등성 키 — 서로 다른 두 외부 서명자에 대해 정산에 도달하기 전 같은 검증 게이트를 둔다.
- **Bridge: Anvil-Sepolia 레그 사이 릴레이어 메시지에도 같은 서명+타임스탬프 검사를 건다.** 위조되거나 재전송된 릴레이어 메시지는 읽기를 망가뜨리는 정도가 아니라 민팅을 유발한다. 사고가 난 뒤가 아니라 출시 전에 멱등성과 재전송 윈도우를 그 경로에 넣는다.
