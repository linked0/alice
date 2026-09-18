## en
- **Rabbit: give each agent in the mandate pipeline an owns/reads/returns/must-not/done-when contract.** Signer, policy checker and executor should each own one decision with a named contract, not share one long conversation that loses context on restart.
- **gitboard: become the durable board, not a log.** Move agent-to-agent state (across Rabbit, Verex, the alice-tech pipeline) through gitboard's task/record view with dependencies and retries, so a restart doesn't lose which stage a handoff was in.
- **Number/alice-tech: build the shared brain before adding more agent roles.** Minimum voice/scope/source files for the alice-tech report should exist first, the same order this card gives — brain, then scout/researcher/editor, before a writer or distribution role gets added.

## ko
- **Rabbit: mandate 파이프라인의 각 에이전트에 owns/reads/returns/must-not/done-when 계약을 준다.** 서명자, 정책 검사자, 실행자는 각각 하나의 결정을 소유해야 하며, 재시작 시 맥락을 잃는 하나의 긴 대화를 공유해서는 안 된다.
- **gitboard: 로그가 아니라 내구성 있는 보드가 된다.** Rabbit, Verex, alice-tech 파이프라인을 가로지르는 에이전트 간 상태를 의존성과 재시도가 있는 gitboard의 작업/기록 뷰로 옮긴다. 그래야 재시작해도 핸드오프가 어느 단계였는지 잃지 않는다.
- **Number/alice-tech: 에이전트 역할을 더 늘리기 전에 공유 브레인부터 만든다.** alice-tech 리포트를 위한 최소한의 voice/scope/source 파일이 먼저 있어야 한다. 이 카드가 제시한 순서와 같다 — 브레인이 먼저고, writer나 배포 역할을 추가하기 전에 scout/researcher/editor부터.
