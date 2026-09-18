## en
- **Rabbit: pin the mandate-execution path as a graph, not a loose agent loop.** Verify mandate -> simulate -> sign -> submit is a known sequence — wire it as fan-out/join/router with a shared state, so a failed simulate always routes to a fixer step or human approval instead of letting the agent improvise.
- **CI/gitboard: build PR review as a graph, not a single freeform agent.** The pattern is already named — fan-out the checks in parallel, join on the slowest, route fail to a fixer agent and pass to human merge — and gitboard should show the graph's current node, not just a pass/fail badge.
- **Verex: model market resolution (dispute window -> resolve -> settle) as an explicit graph.** The steps and their order are known in advance, so pin them as nodes and edges with a router on dispute outcome, rather than letting a swarm of checks decide informally.

## ko
- **Rabbit: 맨데이트 실행 경로를 느슨한 에이전트 루프가 아니라 그래프로 고정한다.** 맨데이트 검증 -> 시뮬레이션 -> 서명 -> 제출은 이미 알려진 순서다. 공유 상태를 가진 fan-out/join/router로 배선해, 시뮬레이션 실패가 항상 수정 단계나 사람 승인으로 라우팅되게 하고 에이전트가 즉흥적으로 판단하지 않게 한다.
- **CI/gitboard: PR 리뷰를 자유형 단일 에이전트가 아니라 그래프로 만든다.** 패턴은 이미 이름이 있다. 체크들을 병렬로 fan-out하고 가장 느린 것에서 join하고, 실패는 수정 에이전트로 통과는 사람 머지로 라우팅한다. gitboard는 통과/실패 배지가 아니라 그래프의 현재 노드를 보여줘야 한다.
- **Verex: 마켓 정산(분쟁 기간 -> 정산 -> 결제)을 명시적 그래프로 모델링한다.** 단계와 순서가 미리 알려져 있으므로 분쟁 결과에 대한 라우터를 가진 노드와 엣지로 고정하고, 체크들의 스웜이 비공식적으로 결정하게 두지 않는다.
