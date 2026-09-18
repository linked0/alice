## en
- **Auditor / gitboard: track prefill vs decode cost separately for any LLM-backed tool.** Agent workflows and Auditor methodology write-ups should prefer cache-read pricing for repeated long-context calls, since that's where the real bill lives.
- **Devnet / alice-tech: reuse the same context prefix across workflow stages.** Running agent-team-style stages against a fixed case record only gets cache reuse if each stage doesn't re-pay prefill from scratch.

## ko
- **Auditor / gitboard: LLM 기반 도구마다 prefill과 decode 비용을 따로 추적한다.** 에이전트 워크플로우와 Auditor 방법론 문서는 반복되는 롱컨텍스트 호출에 캐시 읽기 가격을 우선해야 한다. 실제 비용이 거기서 나오기 때문이다.
- **Devnet / alice-tech: 워크플로우 단계 전체에서 같은 컨텍스트 프리픽스를 재사용한다.** 고정된 케이스 레코드에 대해 agent-team 스타일 단계를 돌릴 때, 각 단계가 prefill을 처음부터 다시 내지 않아야만 캐시 재사용이 실제로 적용된다.
