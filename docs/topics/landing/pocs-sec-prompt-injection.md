## en
- **Rabbit: treat any content an agent reads (a fetched page, a tool result) as data, never instruction.** Isolate the read path from the mandate/transaction-proposal path, and allowlist what an agent-read page is allowed to trigger.
- **gitboard/CI: require human-in-the-loop before any LLM-parsed output drives an action.** If a CI or gitboard automation step ever feeds model output into auto-merge or auto-deploy, don't trust the parsed intent without a human check.

## ko
- **Rabbit: 에이전트가 읽는 모든 콘텐츠(가져온 페이지, 툴 결과)를 지시가 아니라 데이터로 취급한다.** 읽기 경로를 매니데이트/트랜잭션 제안 경로와 분리하고, 에이전트가 읽은 페이지가 무엇을 트리거할 수 있는지 화이트리스트로 제한한다.
- **gitboard/CI: LLM이 파싱한 출력이 액션을 구동하기 전에 사람 개입을 요구한다.** CI나 gitboard 자동화 단계가 모델 출력을 자동 머지나 자동 배포에 연결한다면, 사람 확인 없이 파싱된 의도를 신뢰하지 않는다.
