## en
- **Auditor: never accept a model's chain-of-thought as the audit trail.** For any LLM-assisted decision such as a market-resolution suggestion, the Auditor needs a separate, checkable methodology, since the PoC's own finding is that the trace is a rationalization.
- **OFA: benchmark direct vs. chain-of-thought prompting before defaulting to CoT.** If a solver ever uses an LLM to reason about routing, weigh the accuracy gain against latency and token cost, and don't rely on the trace as a debugging log.

## ko
- **Auditor: 모델의 사고연쇄를 감사 기록으로 절대 받아들이지 않는다.** 마켓 정산 제안 같은 LLM 보조 의사결정에는 별도의 검증 가능한 방법론이 필요하다, PoC 자체의 발견이 그 트레이스는 합리화일 뿐이라는 것이기 때문이다.
- **OFA: CoT를 기본값으로 쓰기 전에 직접 답변과 사고연쇄 프롬프팅을 비교 측정한다.** 솔버가 라우팅을 추론하는 데 LLM을 쓴다면, 정확도 향상을 지연시간과 토큰 비용과 견주고, 그 트레이스를 디버깅 로그로 신뢰하지 않는다.
