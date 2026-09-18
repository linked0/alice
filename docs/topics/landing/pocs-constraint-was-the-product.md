## en
- **Rabbit: separate reading from acting in the agent harness.** Any step where the agentic AA agent reads untrusted text (a PR body, a mandate description, a fetched page) must not sit in the same capability as signing or submitting a transaction — add that boundary to the harness design, not to a prompt.
- **CI: treat PR titles and issue text as attacker-authored by default.** Since instructions hidden in a PR title can steer an agent into leaking secrets, any CI bot with repo write or secret access must not also read untrusted PR/issue text in the same run.
- **gitboard/Devnet: measure the context tax before adding another MCP server.** Dump the tool-list JSON for every server a Jayverse agent connects to, tokenise it, and compare success rate with the full set trimmed to the tools actually called — track that number on gitboard rather than assuming more tools help.

## ko
- **Rabbit: 에이전트 하네스에서 읽기와 실행을 분리한다.** 에이전틱 AA 에이전트가 신뢰할 수 없는 텍스트(PR 본문, 맨데이트 설명, 가져온 페이지)를 읽는 단계는 트랜잭션 서명이나 제출 권한과 같은 곳에 있으면 안 된다. 이 경계는 프롬프트가 아니라 하네스 설계에 넣는다.
- **CI: PR 제목과 이슈 텍스트를 기본적으로 공격자가 쓴 것으로 취급한다.** PR 제목에 숨겨진 지시가 에이전트를 조종해 시크릿을 유출시킬 수 있으므로, 저장소 쓰기 권한이나 시크릿 접근 권한이 있는 CI 봇은 같은 실행에서 신뢰할 수 없는 PR/이슈 텍스트를 읽으면 안 된다.
- **gitboard/Devnet: MCP 서버를 하나 더 추가하기 전에 컨텍스트 세금부터 측정한다.** Jayverse 에이전트가 연결하는 모든 서버의 툴 목록 JSON을 덤프해 토큰화하고, 실제로 호출되는 툴로 줄였을 때의 성공률과 비교한다. 이 숫자는 gitboard에 남겨 "툴이 많을수록 좋다"는 가정 대신 추적한다.
