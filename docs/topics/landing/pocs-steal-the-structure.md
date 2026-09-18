## en
- **Rabbit: decide loop vs graph for the payment agent explicitly.** Given irreversible on-chain actions, model mandate execution as a graph of named states (proposed → simulated → approved → sent) rather than an open loop, for auditability.
- **OFA: model solver bidding rounds as a graph, not an open loop.** A named-state design keeps a failed bid from silently retrying into a duplicate, the same failure mode the loop-vs-graph chapter warns about.
- **Auditor/gitboard: borrow the trigger-design discipline for internal runbooks.** Any future SKILL.md-style runbook (e.g., Verex resolution) should state an explicit "when does this fire" line, the way a good skill trigger does.

## ko
- **Rabbit: 결제 에이전트에 대해 루프 대 그래프를 명시적으로 결정한다.** 온체인 액션이 되돌릴 수 없다는 점을 고려해, 위임 실행을 열린 루프가 아니라 이름 붙은 상태들의 그래프(제안 → 시뮬레이션 → 승인 → 전송)로 모델링해 감사 가능성을 확보한다.
- **OFA: 솔버 입찰 라운드를 열린 루프가 아니라 그래프로 모델링한다.** 이름 붙은 상태 설계는 실패한 입찰이 조용히 재시도되어 중복 실행되는 것을 막아준다. 루프 대 그래프 챕터가 경고하는 것과 같은 실패 모드다.
- **Auditor/gitboard: 내부 런북에 트리거 설계 규율을 적용한다.** 향후 SKILL.md 형태의 런북(예: Verex 정산)은 좋은 스킬 트리거처럼 "언제 발동하는가"를 명시적으로 한 줄 적어둔다.
