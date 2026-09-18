## en
- **gitboard: route agent-driven updates as CLI-then-MCP-then-CLI.** Any Claude/agent change to gitboard should generate a reviewable, re-runnable script first (the CLI half), use interactive tool calls only to inspect live state and adjust, then re-run the batch step to output and verify — never leave the change living only in a conversation.
- **CI: keep CI on the reproducible/batch side only.** Frozen-lockfile builds, contract deploys and gitboard data jobs belong in the CLI/batch bucket — durable, diffable, re-runnable; reserve interactive, stateful tool use for local exploration and keep it out of the CI path entirely.
- **Number: separate research scripts from research exploration in the repo.** Indicator-generation and reading pipelines are the CLI/batch side (durable, re-runnable); ad hoc data exploration during research is the MCP-style stateful side — keep the two in visibly different places so a reading's provenance script is always the reviewable artifact.

## ko
- **gitboard: 에이전트가 만든 변경은 CLI→MCP→CLI 순서로 처리한다.** Claude나 에이전트가 gitboard를 바꿀 때는 먼저 검토 가능하고 재실행 가능한 스크립트(CLI 쪽)를 생성하고, 대화형 도구 호출은 실시간 상태를 확인하고 조정하는 데만 쓰고, 다시 배치 단계를 돌려 출력하고 검증한다. 변경이 대화 안에만 남아 있게 두지 않는다.
- **CI: CI는 재현 가능한 배치 쪽만 담당한다.** 락파일 고정 빌드, 컨트랙트 배포, gitboard 데이터 작업은 CLI/배치 범주에 속한다 — 영속적이고 diff 가능하고 재실행 가능해야 한다. 대화형·상태 유지 도구 사용은 로컬 탐색용으로만 두고 CI 경로에서 완전히 배제한다.
- **Number: 리서치 스크립트와 리서치 탐색을 저장소에서 분리한다.** 지표 생성과 읽기 파이프라인은 CLI/배치 쪽(영속적, 재실행 가능)이고, 리서치 중 즉흥적인 데이터 탐색은 MCP식 상태 유지 쪽이다. 읽기 자료의 출처 스크립트가 항상 검토 가능한 산출물로 남도록 둘을 눈에 띄게 다른 위치에 둔다.
