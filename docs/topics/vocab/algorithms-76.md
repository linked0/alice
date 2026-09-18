| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| lay out | 배열하다, 배치하다 · 데이터가 저장되는 방식을 말할 때. "lays out values of the same column contiguously" |
| drop sharply | 급격히 줄어들다 · 수치가 크게 감소할 때. "and I/O drops sharply." |
| operate directly on | ~에 직접 연산을 수행하다 · 데이터를 별도 변환 없이 그대로 처리할 때. "operate directly on compressed data." |
| in batches of | ~단위로 묶어서, 배치로 · 한 번에 여러 개씩 처리할 때. "processes data in batches of thousands of values" |
| cache locality | 캐시 지역성 · 메모리 접근 패턴이 캐시 효율을 높일 때. "exploiting cache locality and SIMD." |
| the tradeoff is that | 대가(단점)는 ~라는 것이다 · 장점과 함께 따라오는 단점을 소개할 때. "The tradeoff is that single-row lookups and frequent updates suffer" |
| mismatched | 서로 맞지 않는, 어긋난 · 두 요소가 궁합이 안 맞을 때. "workload shape and storage layout are mismatched" |
| OLAP | 온라인 분석 처리(Online Analytical Processing) · 대규모 집계·분석 쿼리에 최적화된 워크로드 유형, 컬럼 스토어가 적합. "Column Stores and Vectorized Execution (OLAP)" |
| OLTP | 온라인 트랜잭션 처리(Online Transaction Processing) · 단건 조회·빈번한 업데이트에 최적화된 워크로드, 로우 스토어가 적합. "so OLTP paths still belong on row stores" |
| DuckDB | 임베디드형 OLAP 데이터베이스(제품명) · 컬럼 스토어 실습 비교 대상으로 쓰이는 오픈소스 분석 DB. "Load the same event data into Postgres and DuckDB" |
| RLE | 런렝스 인코딩(Run-Length Encoding) · 같은 값이 연속될 때 압축 효율이 좋은 압축 기법, 컬럼 스토어에서 활용. "compression schemes like RLE, dictionary encoding, delta encoding" |
| SIMD | 단일 명령 다중 데이터(Single Instruction, Multiple Data) · 하나의 명령으로 여러 값을 동시에 처리하는 병렬화 기법. "exploiting cache locality and SIMD" |
<!-- acronyms 2026-09-18 -->
