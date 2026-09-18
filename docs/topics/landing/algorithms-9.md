## en
- **gitboard: build the suffix-array index once and expose it as a search panel.** Index devnet/Sepolia trace logs once instead of re-grepping raw logs each time an incident needs a specific address, selector or event signature traced.
- **Auditor: point investigations at the indexed search, not raw logs.** Faster trace lookup during an incident is itself evidence the methodology was followed, not just a convenience.
- **CI: let query time be the trigger to build the index.** If ad hoc grep gets slow during a CI-triggered incident replay, that's the signal to build the suffix array rather than optimize the grep further.

## ko
- **gitboard: 접미사 배열 인덱스를 한 번 만들고 검색 패널로 노출한다.** 사고가 발생할 때마다 원시 로그를 다시 grep하는 대신, devnet/Sepolia 트레이스 로그를 한 번 인덱싱해서 특정 주소, 셀렉터, 이벤트 시그니처를 추적한다.
- **Auditor: 조사할 때 원시 로그가 아니라 인덱싱된 검색을 가리킨다.** 사고 중 더 빠른 트레이스 조회 자체가 방법론이 지켜졌다는 증거다, 단순한 편의가 아니라.
- **CI: 쿼리 시간을 인덱스 구축의 트리거로 삼는다.** CI가 유발한 사고 재현 중 임시 grep이 느려지면, grep을 더 최적화하는 대신 접미사 배열을 만들라는 신호다.
