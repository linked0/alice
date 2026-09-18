## en
- **Rabbit/Personas: if semantic search over skills, personas, or mandate lookups is ever added, budget for the embedding model's quality as the retrieval ceiling, and test where similarity diverges from intended meaning before shipping.**
- **Number: any RAG-style lookup over Number's readings should log retrieval misses — semantically similar but wrong-intent matches — as a metric, not assume nearest-neighbor equals correct.**

## ko
- **Rabbit/Personas: 스킬, 페르소나, 위임 조회에 시맨틱 검색을 추가한다면 임베딩 모델의 품질이 검색 성능의 상한임을 전제하고, 출시 전에 유사도가 의도한 의미와 갈리는 지점을 테스트한다.**
- **Number: Number 리딩에 RAG 방식 조회를 쓴다면, 최근접 이웃이 곧 정답이라고 가정하지 말고 의미상 비슷하지만 의도가 틀린 매칭을 지표로 로깅한다.**
