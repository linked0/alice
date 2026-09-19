| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| grep loop | grep으로 코드를 처음부터 반복 탐색하는 루프 · 에이전트가 컨텍스트를 낭비하는 방식을 가리킴. "grepping and opening files turn after turn" |
| token budget | 토큰 예산(한 세션에서 쓸 수 있는 토큰의 한도) · 컨텍스트가 커질수록 빨리 소진됨. "which burns the token budget" |
| dependency graph | 의존성 그래프(무엇이 무엇에 의존하는지 나타낸 구조) · 이 항목의 핵심 개념. "a static dependency graph of a codebase" |
| RAG | Retrieval-Augmented Generation(검색 증강 생성, 벡터 검색으로 문서를 찾아 답에 활용하는 기법) · 여기서는 그 한계를 지적하는 맥락. "vector search (RAG) fails at this job" |
| semantic similarity | 시맨틱 유사도(의미가 비슷한 정도) · 의존 관계와는 다른 축임을 강조. "semantic similarity is not the same relation as dependency" |
| embedding | 임베딩(텍스트·코드를 벡터로 표현한 것) · 유사도 검색의 기반이자 이 글의 한계 사례. "An embedding index puts ... close together" |
| call edge / import edge | 호출 엣지 / import 엣지(그래프에서 함수 호출·모듈 임포트 관계를 나타내는 선) · 그래프의 구성 요소. "call edges, import edges, class membership" |
| knowledge graph | 지식 그래프(노드와 엣지로 지식을 구조화한 것) · Graft가 만드는 산출물. "turns it into a knowledge graph" |
| blast radius | 영향 범위(변경이 퍼지는 반경) · 무엇이 깨질지 추적할 때 쓰는 표현. "immediate blast-radius tracing along edges" |
| MCP | Model Context Protocol(에이전트가 외부 도구를 호출하도록 하는 프로토콜) · 두 연동 모드 중 하나. "calls Graft as an MCP tool" |
| hook mode / injection | hook 모드 / 주입(프롬프트에 내용을 자동으로 끼워 넣는 방식) · CLI 연동 모드를 가리킴. "Graft injects the graph-derived related files" |
| CLI | Command-Line Interface(명령줄 인터페이스) · Graft를 설치·실행하는 방식. "Install the CLI via npm or pip" |
| incremental (re-)parse | 점진적 재파싱(바뀐 부분만 다시 분석) · 그래프를 싸게 유지하는 방법. "Graft re-parses incrementally" |
| front-load | 비용을 앞당겨 치르다 · 그래프를 미리 만들어 이후 비용을 아끼는 패턴을 설명. "Graft front-loads a one-time graph-build cost" |
| cold build | 콜드 빌드(그래프나 캐시가 없는 상태에서 처음 하는 빌드) · 그래프의 이점이 없는 경우. "not on the first cold build" |
| JSON | JavaScript Object Notation(자바스크립트 객체 표기법, 데이터 교환용 텍스트 포맷) · 그래프의 저장 형식. "written out as a local JSON file" |
| impact analysis | 영향 분석(변경이 어디까지 영향을 주는지 파악) · CI에 붙일 수 있는 응용. "a graph gives impact analysis for free" |
| PR | Pull Request(병합 요청) · CI 단계에서 검사 대상. "which modules does this PR touch" |
| CI | Continuous Integration(지속적 통합, 코드 변경을 자동으로 빌드·검사하는 파이프라인) · 그래프를 붙일 위치. "worth adding as a CI step" |
| deep module | 깊은 모듈(단순한 인터페이스 뒤에 복잡한 기능을 숨긴 모듈, Pocock/Ousterhout식 개념) · 그래프를 작고 얕게 유지하는 요인. "a codebase of deep modules keeps this graph small and shallow" |
