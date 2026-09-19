| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| harness | 하네스(에이전트를 실행시키는 인프라 전체: 샌드박스·메모리·스케줄링·도구 실행) · build-vs-buy 논의의 핵심 대상. "does the harness define your product's unique value" |
| Managed Agents | Anthropic이 제공하는 서버 호스팅 관리형 에이전트 서비스 이름 · 이 글의 주제. "shipped Claude Managed Agents to production" |
| clean context | 이전 작업의 흔적이 섞이지 않은 깨끗한 컨텍스트 · 독립 검증자를 실행 에이전트와 분리할 때 쓰는 조건. "a verifier agent that runs in a clean context" |
| rubric | 채점 기준표(무엇을, 어떤 기준으로 통과시킬지 명시한 규칙) · 검증 에이전트가 출력을 평가하는 잣대. "scoring the output against a rubric" |
| fail-silent | 실패했을 때 조용히 아무것도 보여주지 않는 설계 · 틀린 답보다 침묵을 택하는 원칙. "a fail-silent / graceful-degradation choice" |
| graceful degradation | 우아한 성능 저하(품질이 기준 미달일 때 조용히 물러나는 설계) · fail-silent와 짝을 이루는 표현. 위와 같은 문맥. |
| sandbox(ing) | 샌드박스(격리된 실행 환경), 격리하는 행위 · 고객 소스 코드를 안전하게 다루기 위한 필수 장치. "isolation... non-negotiable" |
| fan out | 하나의 작업을 여러 갈래로 병렬로 퍼뜨려 처리하다 · 상위 에이전트가 수백 개 계정 메모리를 동시에 훑을 때. "fan out across roughly 500 accounts' memory" |
| roll-up | 여러 항목(거래처·마켓 등)을 하나의 요약으로 집계한 것 · Watchtower의 핵심 산출물. "a roll-up agent above it" |
| PR | Pull Request(풀 리퀘스트, 코드 변경을 제안하는 단위) · 코드 자가 치유 제품이 제출하는 결과물. "proposes a fix PR" |
| UX | User Experience(사용자 경험) · PR 제출 시 함께 검토하는 대상. "reviews UX and instrumentation" |
| PMF | Product-Market Fit(제품-시장 적합성, 제품이 시장 수요에 맞아떨어지는 상태) · 초기 스타트업이 최적화하는 목표. "toward product-market fit" |
| funnel conversion | 퍼널(단계별 유입-전환 흐름) 전환율 · 이 지표가 떨어지면 코드 분석이 트리거된다. "when funnel conversion drops" |
| dogfooding | 자사 직원이 자사 제품을 직접 써보며 검증하는 관행 · 초기 평가의 한계로 지적됨. "internal dogfooding is vibes-based" |
| overfit | 특정 데이터(팀 자신의 사용 패턴)에만 맞춰져 일반화가 안 되는 상태 · dogfooding의 부작용. "overfits to the team's own usage" |
| stateful | 상태를 유지하는(이전 상호작용·외부 변화가 다음 결과에 영향을 미치는) · 정적 eval이 잘 안 맞는 이유. "stateful systems that resist static evals" |
| batch mode | 실시간이 아니라 모아서 일괄 처리하는 방식 · 비용을 크게 아끼지만 지연이 늘어나는 트레이드오프. "batch mode's roughly 50-75 percent cost savings" |
| runway | 활주로(스타트업이 자금이 바닥나기 전까지 버틸 수 있는 기간) · build 대신 buy를 택하는 이유. "spend your runway on plumbing" |
| core competency | 핵심 경쟁력(그 회사만이 잘할 수 있는 영역) · build-vs-buy 판단의 기준 문구. "is this infrastructure our core competency" |
| plumbing | 배관(눈에 띄지 않지만 필수적인 기반 인프라를 가리키는 비유) · 하네스를 제품과 대비시키는 말. "spend your runway on plumbing instead of product" |
| veto | 거부권(승인을 막을 권한) · Rabbit의 mandate enforcer가 갖는 역할을 설명할 때. "the verifier-with-veto matters more here than for a briefing" |
