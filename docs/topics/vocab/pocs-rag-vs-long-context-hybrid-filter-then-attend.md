| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| RAG | Retrieval-Augmented Generation(검색 증강 생성, 검색기+생성기 결합 아키텍처) · 이 항목 전체의 주제. "Is RAG Still Needed?" |
| LLM | Large Language Model(거대 언어 모델) · 컨텍스트 윈도우 논의의 대상. "Choosing the Best Approach for LLMs" |
| NIAH | Needle-In-A-Haystack(건초더미 속 바늘 찾기, 긴 컨텍스트 회상 벤치마크) · 주의 희석을 측정하는 표준 테스트군. "the broader NIAH benchmark family" |
| rereading tax | 다시 읽기 세금(같은 텍스트를 매 요청마다 다시 처리하는 비용) · 긴 컨텍스트의 핵심 단점을 부르는 말. "a quadratic 'rereading tax' on every request" |
| retrieval lottery | 검색 로또(맞는 청크가 뽑힐지 운에 달린 상황) · RAG의 조용한 실패 모드를 가리키는 표현. "No retrieval lottery." |
| silent failure | 조용한 실패(에러 없이 틀린 결과가 나오는 것) · 이 항목에서 가장 중요한 위험 개념. "That is a silent failure, not a crash." |
| attention dilution | 주의 희석(컨텍스트가 커질수록 특정 사실에 대한 집중이 흐려지는 현상) · RAG를 옹호하는 핵심 근거. "measurable attention dilution on needle-in-a-haystack lookups" |
| needle-in-a-haystack | 건초더미 속 바늘 찾기(거대한 컨텍스트 속 특정 사실 회상 과제) · NIAH 벤치마크의 별칭이자 관용구. "needle-in-a-haystack lookups" |
| cosine similarity | 코사인 유사도(두 벡터 방향의 유사성 측정값) · 벡터 검색의 표준 유사도 지표. "whichever chunk scored highest on cosine similarity" |
| cross-encoder re-ranker | 크로스 인코더 재순위화기(검색 결과를 다시 정밀하게 순위 매기는 모델) · RAG 파이프라인의 마지막 단계. "cross-encoder re-rankers" |
| quadratic cost | 제곱 비용(입력 길이의 제곱에 비례하는 연산 비용) · 셀프어텐션의 근본적 한계를 설명하는 말. "quadratic self-attention cost on every request" |
| prompt caching | 프롬프트 캐싱(고정된 프롬프트 앞부분을 재사용해 비용을 아끼는 기법) · 긴 컨텍스트 비용을 부분적으로 완화하는 수단. "Prompt caching only discounts a static prefix" |
| context window | 컨텍스트 윈도우(모델이 한 번에 볼 수 있는 토큰 범위) · 이 논쟁 전체를 가능하게 만든 변수. "frontier context windows reach 1–2 million tokens" |
| vector database | 벡터 데이터베이스(임베딩을 저장하고 유사도 검색하는 저장소) · RAG 인프라의 중심 구성요소. "a vector database" |
| chunking | 청킹(문서를 검색 단위로 잘게 나누는 작업) · RAG 파이프라인의 첫 단계이자 흔한 실패 지점. "chunking heuristics" |
| decision matrix | 의사결정 매트릭스(선택 기준을 표로 정리한 것) · RAG vs 긴 컨텍스트 선택을 위한 도구. "### Decision matrix" |
| hybrid pattern | 하이브리드 패턴(두 접근을 순서대로 결합하는 설계) · 이 항목이 최종적으로 권하는 답. "a hybrid pattern" |
| semantic unit | 의미 단위(함수, 절 등 의미가 온전한 최소 덩어리) · 좋은 청킹 기준. "chunk boundaries should still follow semantic units" |
| index time | 색인 시점(질의 시점이 아니라 데이터를 미리 색인해 두는 단계) · RAG의 비용이 발생하는 시점. "RAG pays once, at index time" |
| coarse filter | 성긴 필터(정밀하지 않아도 되는 1차 거르기 단계) · 하이브리드 패턴에서 RAG의 역할. "Use RAG as a coarse filter over the unbounded corpus" |
