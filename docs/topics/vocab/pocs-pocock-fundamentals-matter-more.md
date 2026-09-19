| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| software entropy | 소프트웨어 엔트로피(감시 없이 방치하면 코드베이스가 무질서로 흘러가는 경향) · 구조가 무너지는 속도를 가리키는 말. "accumulate software entropy fast" |
| specs to code | 사양서를 AI에게 넘겨 코드로 바꾸게 하고 결과를 읽지 않는 워크플로 · 이 강연이 경고하는 함정의 이름. "The specs-to-code trap" |
| Grill me | 그릴 미(에이전트에게 "나를 집요하게 인터뷰하라"고 지시하는 스킬 이름) · Eng #33과 이어지는 고유 스킬명, 번역하지 않고 그대로 쓴다. "**Grill me**: tell the agent to interview you relentlessly" |
| decision tree | 결정 트리(선택마다 가지가 갈라지는 구조) · Grill me에서 "모든 가지를 따라가라"고 할 때의 그 가지. "following every branch of the decision tree" |
| Ubiquitous Language | 유비쿼터스 언어(도메인 전체에서 팀과 코드가 공유하는 하나의 용어 체계) · 에릭 에반스의 DDD 핵심 개념. "**Ubiquitous Language**, Eric Evans' Domain-Driven Design term" |
| DDD | Domain-Driven Design(도메인 주도 설계) · Ubiquitous Language가 나온 원 개념 체계. "Domain-Driven Design term" |
| red-green-refactor | 레드-그린-리팩터(실패하는 테스트를 먼저 쓰고, 통과시키고, 정리하는 순환) · TDD의 표준 사이클, 켄트 벡이 정리. "Kent Beck's red-green-refactor cycle" |
| TDD | Test-Driven Development(테스트 주도 개발) · 코드를 쓰기 전에 테스트부터 쓰는 방법론. "Enforced **TDD**: small failing test, make it pass, refactor" |
| outrun your headlights | 헤드라이트를 앞질러 달리다(피드백이 따라잡기 전에 너무 빨리 나아가는 것) · *The Pragmatic Programmer*의 표현, 에이전트가 에러 없이 수백 줄을 쏟아내는 상태. "it 'outruns its headlights'" |
| deep module | 딥 모듈(인터페이스는 단순하지만 뒤에 실질적 기능을 숨긴 모듈) · 오스터하우트의 핵심 설계 단위, 에이전트에게 맡길 수 있는 경계. "**Deep modules** (Ousterhout)" |
| shallow module | 섈로우 모듈(인터페이스가 숨긴 기능만큼이나 복잡한 모듈) · deep module의 반대, 에이전트가 길을 잃는 원인. "Many shallow modules force a long dependency chain" |
| gray box | 회색 상자(내부는 에이전트에게 맡기고 외부 계약만 사람이 고정한 모듈) · 화이트박스와 블랙박스 사이, 이 글에서 Verex 매칭 코어에 쓰는 비유. "the module's interior becomes a gray box" |
| sergeant, not general | 장군이 아니라 하사관(에이전트는 전술 실행자이지 전략가가 아니라는 비유) · Life 1301과 직접 이어지는 표현. "the agent is a good sergeant... not a general" |
| tactical vs strategic | 전술 대 전략 · 하사관/장군 비유를 풀어 쓴 짝. "Pocock's closing frame is tactical versus strategic" |
| load-bearing | 하중을 지탱하는(빠지면 전체가 무너지는 필수 요소) · 고전 원칙들이 지금은 선택이 아니라는 뜻으로. "these classic disciplines... are now load-bearing" |
| boundary-file check | 경계 파일 검사(선언된 모듈 경계를 코드가 넘었는지 자동으로 확인하는 CI 단계) · Dark Horse와 이어지는 CI 아이디어. "a Dark Horse boundary-file check" |
| CI | Continuous Integration(지속적 통합, 머지 전 자동 검증 파이프라인) · TDD 게이트와 경계 검사가 실제로 도는 위치. "CI: TDD is the pace-setter for agent-authored diffs" |
| PR | Pull Request(변경 사항을 병합해 달라고 올리는 요청) · 경계 검사가 실패시키는 대상. "fails a PR if it reaches across a declared module boundary" |
| CLOB | Central Limit Order Book(중앙 집중식 주문장, 가격-시간 우선순위로 매칭하는 거래소 코어) · Verex 매칭 엔진을 가리키는 이름, 이 글에서 deep module의 예. "the CLOB matching core is the deep module" |
| SDK | Software Development Kit(소프트웨어 개발 키트, 외부에 공개하는 인터페이스 패키지) · Verex의 `sdk` 패키지, 사람이 설계하는 강한 인터페이스. "the `sdk` package is the interface" |
