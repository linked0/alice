## en
- **Rabbit: enforce intent mandates, not just spend caps, on session keys.** A 7715 session key that only bounds an amount lets an agent pass every check while buying the wrong thing; Rabbit's mandate design should commit to (item/action class, max price, counterparty allowlist, expiry) and check settlement against that commitment.
- **Rabbit: add a low-privilege veto window between authorization and settlement.** A separate watcher key that can cancel but not spend, given a short window before finality, is a concrete addition to Rabbit's mandate flow that catches a wrong-target action a spend cap alone would miss.
- **Verex: apply the same two-mechanism split to withdrawal or settlement automation.** Any automated flow (agent-triggered settlement, auto-withdraw) should be checked against a signed intent rather than a balance limit, with enforcement on-chain and the policy decision off-chain.

## ko
- **Rabbit: 세션 키에 지출 한도가 아니라 의도 위임(intent mandate)을 강제한다.** 금액만 제한하는 7715 세션 키는 에이전트가 엉뚱한 것을 사도 모든 검사를 통과하게 둔다. Rabbit의 위임 설계는 (항목/행동 분류, 최대 가격, 상대방 허용목록, 만료)를 커밋하고 정산을 그 커밋과 대조해야 한다.
- **Rabbit: 승인과 정산 사이에 낮은 권한의 거부 윈도우를 둔다.** 지출은 못 하지만 취소는 할 수 있는 별도의 워처 키를, 파이널리티 전 짧은 윈도우와 함께 Rabbit의 위임 흐름에 추가하면 지출 한도만으로는 못 잡는 잘못된 대상 행동을 잡아낸다.
- **Verex: 정산이나 출금 자동화에 같은 이원 메커니즘을 적용한다.** 자동화된 흐름(에이전트가 트리거하는 정산, 자동 출금)은 잔액 한도가 아니라 서명된 의도와 대조해 검사하고, 온체인에서는 집행, 오프체인에서는 정책 결정으로 나눈다.
