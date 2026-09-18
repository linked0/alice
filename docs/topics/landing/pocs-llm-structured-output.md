## en
- **Number: use schema-constrained decoding for any LLM-generated reading or indicator.** If Number ever parses model output into structured readings, measure the parse-failure rate of free-form prompting against schema-constrained generation before shipping either.
- **Personas: constrain any LLM-generated persona metadata to a schema.** Persona NFT attributes or descriptions produced by a model should be schema-guided rather than free-form JSON, so a malformed field never reaches the mint step.
- **Auditor: require a parse-failure-rate number for any LLM step in the pipeline.** Wherever a Jayverse service depends on an LLM producing structured output (Number, Personas, or elsewhere), the Auditor row should record the measured failure rate rather than assuming the model's JSON always parses.

## ko
- **Number: LLM이 생성하는 읽기나 지표에 스키마 제약 디코딩을 쓴다.** Number가 언젠가 모델 출력을 구조화된 읽기로 파싱한다면, 어느 쪽을 쓰기 전에 자유형 프롬프팅과 스키마 제약 생성의 파싱 실패율을 측정한다.
- **Personas: LLM이 생성하는 페르소나 메타데이터를 스키마로 제약한다.** 모델이 만드는 Persona NFT 속성이나 설명은 자유형 JSON이 아니라 스키마 유도 방식이어야, 잘못된 필드가 민팅 단계까지 가지 않는다.
- **Auditor: 파이프라인의 모든 LLM 단계에 파싱 실패율 숫자를 요구한다.** Jayverse 서비스(Number든 Personas든 다른 곳이든)가 LLM의 구조화 출력에 의존하는 곳마다, 모델의 JSON이 항상 파싱된다고 가정하지 말고 Auditor 행이 측정된 실패율을 기록하게 한다.
