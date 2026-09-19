| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| mega prompt | 메가 프롬프트(스키마 전체 등을 통째로 시스템 프롬프트에 넣는 방식) · 1단계 아키텍처를 가리키는 이름. "Mega prompt (03:36, 03:50)" |
| chained multi-agent | 체인형 다중 에이전트(역할을 나눠 순서대로 실행하는 파이프라인) · 2단계 아키텍처. "Chained multi-agent (04:57, 05:03, 05:21)" |
| semantic layer | 시맨틱 레이어(원본 테이블 위에 지표·조인 정의를 얹은 층) · 데이터 웨어하우스 표준 용어, 파일로 덤프되는 대상. "dump the warehouse's semantic layer into a sandboxed file system" |
| sandbox | 샌드박스(격리된 실행 환경) · 에이전트가 파일을 안전하게 조작하는 공간. "a local sandbox" |
| file-system agent | 파일 시스템 에이전트(전용 도구 대신 파일 탐색·셸로 동작하는 에이전트) · 4단계, 돌파구가 된 아키텍처. "File-system agent (07:33, 07:42)" |
| emergent behavior | 창발 행동(설계자가 명시적으로 프로그래밍하지 않았는데 나타나는 행동) · 파일 시스템 에이전트가 스스로 탐색·쿼리를 시작한 현상. "behavior nobody programmed" |
| eval | 평가(evaluation, 모델·에이전트 성능을 채점하는 벤치마크) · 각 아키텍처를 비교하는 기준. "the internal eval success rate was only around 30%" |
| SQL | Structured Query Language(구조화 질의 언어, 데이터베이스 조회 언어) · 데이터팀이 대신 짜 주던 바로 그것. "writing SQL and dashboards" |
| YAML | YAML Ain't Markup Language(설정 파일에 흔히 쓰는 데이터 직렬화 형식) · 체인형 에이전트의 격리 도구 중 하나. "YAML config reads" |
| OIDC | OpenID Connect(신원 인증을 위한 개방형 프로토콜) · Vercel Connect가 발급하는 단기 토큰의 표준. "short-lived OIDC tokens" |
| skill file | 스킬 파일(반복 패턴을 절차로 적어 둔 문서) · 백지에서 시작하지 않게 해 주는 기억된 맥락. "roughly 100 'skill' files" |
| skills marketplace | 스킬 마켓플레이스(스킬 파일을 공유·재사용하는 오픈소스 저장소) · `skills.sh`를 가리키는 표현. "Vercel's open-source skill marketplace, skills.sh" |
| declarative convention | 선언적 규약(동작을 절차 코드가 아니라 구조/이름으로 정하는 방식) · Next.js 라우팅과 Eve의 `skills/`·`tools/`·`channels/` 구조에 쓰인 원리. "a file-system convention too" |
| self-hostable | 셀프 호스팅 가능한(자체 인프라에 직접 설치해 운영할 수 있는) · Eve가 오픈소스로 제공하는 배포 옵션. "self-hostable against Postgres, OpenAI and Docker adapters" |
| observability | 관측 가능성(시스템 내부 동작을 스텝 단위로 볼 수 있는 능력) · Auditor 항목과 직접 연결되는 개념. "per-step, per-tool-call and per-cost observability" |
| blank slate | 백지 상태(사전 지식 없이 처음부터 시작하는 상태) · 스킬이 없을 때 에이전트가 놓이는 상태. "starting cold" / "백지에서 탐색을 시작" |
| pretraining data | 사전 훈련 데이터(모델이 학습에 쓴 원본 자료) · 파일 시스템·셸 사용에 모델이 유창한 이유. "pretraining makes a model best at" |
| read-only tool | 읽기 전용 도구(데이터를 바꾸지 못하고 조회만 하는 도구) · Verex처럼 돈이 걸린 데이터에 적용해야 할 안전장치. "keep the tools read-only" |
| shortest path (to something) | 지름길, 가장 짧은 경로 · 기성품보다 직접 구축이 나은 이유를 표현. "the shorter path to something that actually used that context" |
| fail forward | 앞으로만 실패하다(오류가 나도 이전 단계로 돌아가지 못하고 진행만 되는 상태) · 체인형 에이전트의 한계를 설명. "the pipeline could only fail forward" |
