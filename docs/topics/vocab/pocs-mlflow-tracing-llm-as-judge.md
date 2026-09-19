| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| 200 OK | HTTP 성공 상태 코드(요청이 정상 처리됐다는 서버 응답) · "정상"의 대명사이지만 정답을 보장하지 않는다는 대비로 쓰임. "an HTTP monitoring dashboard can show 200 OK and a fine response time" |
| silent failure | 침묵형 장애(에러 신호 없이 조용히 잘못되는 실패) · 관측성 논의의 핵심 개념. "an MCP server or tool call returns empty or malformed data, and the agent has no way to notice" |
| cascading latency | 연쇄 지연(한 구간의 느림이 전체로 번지는 것) · 병목 원인을 못 찾는 상황을 가리킴. "a slow downstream query... inflates the LLM call and the total response time" |
| context overflow | 컨텍스트 오버플로(프롬프트가 모델의 입력 한도를 넘는 것) · LLM 특유의 실패 모드. "too much data gets stuffed into a prompt, and the call fails or times out" |
| non-determinism | 비결정성(같은 입력에도 실행마다 다른 결과) · 재현성·컴플라이언스 문제의 원인. "identical input produces different output across runs" |
| trace | 트레이스(요청 하나의 전체 기록) · 관측성의 최상위 단위. "A trace is the full record of one request from start to finish" |
| span | 스팬(트레이스 안의 한 단계) · LLM 호출·도구 실행 등 세부 단위. "a span is one step inside it" |
| parent-child tree | 부모-자식 트리(스팬들이 중첩되는 구조) · 트레이스 시각화 방식. "spans nest into a parent-child tree that renders as a visual timeline" |
| LLM-as-a-judge | LLM을 심사자로 쓰는 평가 방식(별도 모델이 출력을 채점) · 규칙으로 못 잡는 판단을 대신함. "a separate model whose only job is to grade the output" |
| deterministic scoring | 결정론적 점수(규칙 기반 채점) · LLM-as-a-judge와 짝을 이루는 저비용 평가. "Deterministic scoring covers anything checkable by a rule" |
| tool-call correctness | 도구 호출 정확도(맞는 도구를 골랐는지) · 에이전트 평가 기준의 하나. "did the agent pick the right tool (tool-call correctness)" |
| prompt registry | 프롬프트 레지스트리(검증된 프롬프트의 버전 관리 저장소) · Git처럼 감사·롤백이 되는 것. "Verified system prompts get version control comparable to a Git history" |
| audit trail | 감사 추적(누가 언제 무엇을 바꿨는지의 기록) · 규제 도메인에서 필수. "with an audit trail and the ability to roll back a prompt that regresses" |
| quality gate | 품질 게이트(기준 미달이면 병합을 막는 CI 단계) · 평가를 테스트처럼 자동화하는 자리. "Run mlflow.genai.evaluate as a quality gate" |
| air-gapped | 에어갭(외부 네트워크와 물리적으로 분리된) · 폐쇄망 환경을 가리키는 표준 용어. "An air-gapped environment needs its own judge endpoint" |
| HTTP | HyperText Transfer Protocol(하이퍼텍스트 전송 프로토콜) · 웹 요청/응답의 기본 프로토콜. "an HTTP monitoring dashboard" |
| LLM | Large Language Model(대형 언어 모델) · 이 글 전체가 다루는 대상. "Tracing AI Agents & LLM Workflows" |
| MCP | Model Context Protocol(모델-컨텍스트 프로토콜, 에이전트가 도구·데이터에 접근하는 표준) · 침묵형 장애의 발생 지점. "an MCP server or tool call returns empty or malformed data" |
| CI | Continuous Integration(지속적 통합) · 평가를 자동 게이트로 거는 파이프라인. "Evaluation in CI" |
| OAuth | Open Authorization(개방형 인가 표준) · 프로덕션 백엔드 앞단 보안 요건. "an OAuth proxy in front" |
