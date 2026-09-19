| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| ontology | 온톨로지(도메인의 엔티티·관계·속성을 formal하게 정의한 구조) · 이 항목 전체의 핵심 개념. "a formal specification of a shared conceptualization" |
| neuro-symbolic AI | 뉴로-심볼릭 AI(신경망과 규칙 기반 시스템의 결합) · 온톨로지가 신경망의 가드레일로 쓰이는 접근 전체를 가리킴. "a neuro-symbolic layer next to the neural network" |
| formal specification | 형식적 명세(모호함 없이 규칙으로 적은 정의) · 그루버의 온톨로지 정의에서. "a formal specification of a shared conceptualization" |
| top-down / bottom-up | 하향식 / 상향식(전문가가 정의 대 데이터에서 추출) · 온톨로지를 만드는 두 반대 방법. "mine entities and relationships out of operational data" |
| domain and range | 정의역과 공역(관계가 어떤 타입에서 어떤 타입으로 가는지 제약) · 한 문장만으로 역추론하게 해주는 OWL 개념. "Domain and range let the reasoner work backward from a single fact" |
| transitive property | 이행 속성(A→B, B→C면 A→C가 성립) · 조상 관계 같은 연쇄 추론에 쓰임. "Transitive properties propagate a relationship along a chain" |
| functional property | 함수적 속성(관계가 정확히 하나의 값으로만 귀결) · 모순 검출·동일 개체 식별에 쓰임. "Functional properties assert a relationship must resolve to exactly one value" |
| disjoint class | 서로소 클래스(두 클래스가 절대 겹치지 않는다는 선언) · 환불이 상담원에게 가는 걸 막는 제약. "declaring `Customer` and `Support Rep` disjoint classes" |
| Turing-complete | 튜링 완전(순차·조건·반복을 가지면 이론상 무엇이든 계산 가능) · 에이전트가 예측 불가능해지는 이유로 언급됨. "An agent that can sequence, branch and loop over tool calls is Turing-complete" |
| drift | (맥락) 탈선·표류 · 대화가 원래 목표에서 벗어나는 현상. "a conversation drifting away from its original goal" |
| hallucination | 환각(모델이 사실이 아닌 것을 그럴듯하게 생성) · 신경망에 심볼릭 검증이 필요한 이유. "a neural network that can hallucinate" |
| guardrail | 가드레일(범위를 벗어나지 못하게 막는 안전장치) · 온톨로지가 신경망에 대해 하는 역할. "Two lineages, one guardrail" |
| side effect | 부작용(호출이 도메인 상태를 실제로 바꾸는 효과) · 검증이 반드시 이보다 먼저 끝나야 한다는 맥락. "before the call has a side effect" |
| enumeration (enum) | 열거형(정해진 값 목록만 허용) · 상태값 환각을 막는 제약. "declaring status an enumeration" |
| description logic | 기술 논리(온톨로지 추론의 형식 논리 기반) · domain/range, 이행, 함수적 속성이 여기서 나온 개념. "description logic has always had" |
| door / ledger | 입구 / 원장(이 항목이 쓰는 두 단계 검증 지점의 비유) · 입구=타입 검증, 원장=의미 검증. "validate a tool call's types at the "door" with Pydantic" |
| RDFS | Resource Description Framework Schema(자원 기술 프레임워크 스키마) · 그래프에 추론을 더하는 W3C 표준 중 하나. "RDFS and OWL add inference and validation on top of the graph" |
| OWL | Web Ontology Language(웹 온톨로지 언어) · domain/range, 이행·함수적 속성, disjoint 클래스를 표현하는 W3C 표준. "repeatable ways that OWL constraints catch" |
| LLM | Large Language Model(거대 언어 모델) · 확률적이고 탈선하기 쉬운, 이 항목이 검증 계층을 요구하는 대상. "LLM-driven agents are probabilistic and prone to drift" |
| Pydantic | 파이썬 런타임 타입 검증 라이브러리 · "입구" 단계에서 도구 호출의 타입을 검증하는 도구. "Pydantic validates the tool call's input types strictly" |
