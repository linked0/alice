## en
- **Bridge/Token: give every lock-mint-burn operation one reference ID spanning both chains.** Track a single ID from the Anvil-side lock request through mint, and later through burn and Sepolia-side unlock, so reconciling JYVE's circulation doesn't get rebuilt from raw events after the fact.
- **Token: write JYVE's own redemption path — eligibility, SLA, suspension conditions, audit trail — even at devnet scale.** The card's claim is that circulation is won at the redemption desk, not on the chain; that applies to a mini-AMM token as much as to a stablecoin.
- **Auditor: add "which chain is this unit actually redeemable on right now" as an explicit field.** Once JYVE exists on more than one chain, balance alone doesn't answer that question, and the audit checklist should ask it directly rather than assume it.

## ko
- **Bridge/Token: 락-민트-번 작업마다 두 체인을 아우르는 참조 ID 하나를 부여한다.** Anvil 쪽 락 요청부터 민트, 이후 번과 Sepolia 쪽 언락까지 하나의 ID로 추적해서, JYVE 유통량 정산을 나중에 원시 이벤트에서 다시 짜맞추지 않게 한다.
- **Token: devnet 규모에서도 JYVE 자체의 상환 경로 — 자격, SLA, 정지 조건, 감사 추적 — 를 적어둔다.** 이 카드의 주장은 유통량이 체인이 아니라 상환 데스크에서 결정된다는 것이며, 이는 스테이블코인만큼 미니 AMM 토큰에도 적용된다.
- **Auditor: "이 단위가 지금 실제로 어느 체인에서 상환 가능한가"를 명시적인 필드로 추가한다.** JYVE가 두 체인 이상에 존재하게 되면 잔액만으로는 이 질문에 답할 수 없으므로, 감사 체크리스트가 이를 가정하지 않고 직접 묻는다.
