| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| agent harness | 에이전트 하네스(모델을 둘러싼 실행 껍질: 도구 호출, 루프 제어 등) · 이 글 전체의 핵심 용어. "an AI agent is two separate things, an LLM ... and an agent harness" |
| LLM | Large Language Model(대형 언어모델) · 텍스트만 주고받을 뿐 행동은 못 하는 "두뇌" 쪽. "An LLM only takes in text and emits more text" |
| shift-left | 왼쪽으로 옮기기(검증·품질 관문을 파이프라인 앞단으로 당기는 것) · 오래된 소프트웨어 품질 용어. "push the same guardrail earlier" |
| lazy prompter | 게으른 프롬프터(규칙을 매번 프롬프트에 적지 않고 환경에 한 번만 적어 두는 태도) · 이 엔지니어가 자칭한 철학. "he writes it once into the environment" |
| grounding (v.) | 근거를 인출하다(모델이 답을 지어내지 않고 문서·환경에서 사실을 가져오는 것) · lazy prompter 철학의 목적어. "the model can retrieve (\"ground\") it itself" |
| guardrail | 가드레일(위험한 행동을 사전에 막는 안전장치) · 세 번째 하네스 패턴의 이름. "Guardrail harness ... an interceptor blocks destructive actions" |
| interceptor | 인터셉터(실행 전에 호출을 가로채 검사·차단하는 컴포넌트) · ADK 기반 가드레일 하네스의 핵심 부품. "an interceptor blocks destructive actions ... before they run" |
| closed-loop | 폐루프(결과를 다시 입력으로 되먹이는 구조) · 두 번째 하네스 패턴. "edit, test, capture the failure, feed it back into memory" |
| self-healing | 자가 치유(실패를 스스로 감지하고 재시도해 고치는 성질) · 폐루프 하네스를 요약하는 말. "a self-healing loop" |
| linear harness | 선형 하네스(한 번 읽고 답하고 끝나는 가장 단순한 패턴) · 결정론적 단발 작업용. "read a file once, answer, stop" |
| over-scaffold (v.) | 과잉으로 뼈대를 짜다(꼭 필요하지 않은 구조를 하네스에 덧붙이는 것) · 이 영상의 경고. "Don't over-scaffold the harness itself" |
| tool call | 도구 호출(에이전트가 하네스를 통해 파일 읽기·명령 실행 등을 요청하는 한 스텝) · 루프 횟수를 셀 때 쓰는 단위. "an agent loop makes 20–60 tool calls per task" |
| orchestrator | 오케스트레이터(다른 서브 에이전트들에 작업을 나눠 주고 조율하는 역할) · 하네스 계층 팀 구성의 한 축. "an orchestrator, parallel specialist sub-agents" |
| sub-agent | 서브 에이전트(오케스트레이터 아래에서 특정 작업을 맡는 하위 에이전트) · 병렬로 도는 전문가 역할. "parallel specialist sub-agents" |
| auditor (sub-agent) | 감사자(다른 에이전트의 작업을 규칙에 맞춰 독립적으로 검사하는 역할) · Jayverse의 Auditor 행과 직접 대응. "an independent auditor that checks the others' work" |
| ADK | Agent Development Kit(구글의 에이전트 개발 프레임워크) · 콜백으로 도구 호출을 가로챌 수 있는 실제 프레임워크. "built on Google's Agent Development Kit (ADK)" |
| CI | Continuous Integration(지속적 통합, 코드 변경마다 자동으로 빌드·테스트를 도는 체계) · shift-left 가드레일의 대표 예. "unit test or CI eval that catches the failure" |
| PR | Pull Request(코드 변경을 검토·병합 요청하는 단위) · expanding-the-loop 신뢰 구축의 기본 단위. "small PRs plus an automated review loop" |
| DB | Database(데이터베이스) · 가드레일 하네스가 막는 파괴적 행동의 예. "a DB drop, a forced delete, an unauthorized push" |
| GCP | Google Cloud Platform(구글 클라우드 플랫폼) · Google Skills 지식 계층이 다루는 대표 영역. "things like GCP, Firebase and Flutter" |
