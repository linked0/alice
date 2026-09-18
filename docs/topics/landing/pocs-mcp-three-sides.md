## en
- **Rabbit: gate every consumed MCP tool behind a server-side allowlist.** Near session-key signing, an agent must never hold a Zapier-style MCP connection with unrestricted account access; keep the URL and token server-side and scope calls to an explicit allowlist, the same decision this page makes for the client seat.
- **Number: build its first MCP tool server against the 2026-07-28 spec, not the old one.** A stateless server (no session handshake) deploys straight to Cloud Run and lets Claude query readings and indicators directly — do the protocol question first, before any framework wrapper.
- **Auditor: log every MCP tool call as a checked item.** Record which server, which tool and which allowlist entry authorized a call, so "what was checked, by which rule" extends to agent tool use, not just contract state.
- **gitboard: add a row per MCP server deployment.** Track Number's and Rabbit's MCP servers as stateless Cloud Run functions, with OAuth/OIDC status shown per server.

## ko
- **Rabbit: 소비하는 모든 MCP 도구를 서버 사이드 허용목록 뒤에 둔다.** 세션 키 서명 근처에서는 에이전트가 Zapier식 MCP 연결을 무제한 계정 권한으로 가져서는 안 된다. URL과 토큰은 서버 사이드에 두고 호출은 명시적 허용목록으로 제한한다. 이 페이지가 클라이언트 자리에 대해 내리는 결정과 같다.
- **Number: 첫 MCP 도구 서버를 구 스펙이 아니라 2026-07-28 스펙으로 만든다.** 세션 핸드셰이크가 없는 무상태 서버는 Cloud Run에 바로 배포되고 Claude가 읽기와 지표를 직접 조회할 수 있게 한다. 프레임워크 래핑 전에 프로토콜 질문부터 해결한다.
- **Auditor: 모든 MCP 도구 호출을 확인 항목으로 기록한다.** 어느 서버, 어느 도구, 어느 허용목록 항목이 호출을 승인했는지 남겨서 "무엇을 어떤 규칙으로 확인했는지"가 컨트랙트 상태뿐 아니라 에이전트 도구 사용에도 적용되게 한다.
- **gitboard: MCP 서버 배포마다 행을 추가한다.** Number와 Rabbit의 MCP 서버를 무상태 Cloud Run 함수로 추적하고, 서버별 OAuth/OIDC 상태를 표시한다.
