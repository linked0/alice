| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| write amplification | 쓰기 증폭 · 논리적으로 한 번 쓴 데이터가 디스크에 여러 번 다시 쓰이는 정도를 가리키는 스토리지 용어. "Write amplification is the multiple by which one logical write" |
| read amplification | 읽기 증폭 · 조회 한 번에 여러 레벨·파일을 확인해야 하는 비용을 가리킬 때. "Read amplification is the cost of a single lookup" |
| space amplification | 공간 증폭 · 실제 데이터보다 저장 공간을 얼마나 더 차지하는지 나타내는 비율. "Space amplification is the ratio by which stored data exceeds" |
| fan-out | 팬아웃, 한 레벨이 갖는 파일 개수 비율 · 컴팩션 설정을 튜닝할 때 쓰는 용어. "vary the compaction style and level fan-out" |
| at the cost of | ~을 대가로, ~을 희생하고 · 한쪽 장점을 얻는 대신 다른 쪽이 나빠질 때. "at the cost of high write amplification" |
| table out | 표로 정리해서 나타내다 · 실험 결과를 비교 가능한 표로 만들 때 쓰는 구동사. "table out actual disk bytes written against logical bytes" |
| piled up | 쌓이다, 누적되다 · 파일이나 작업이 정리되지 않고 계속 쌓일 때. "the files piled up across levels via compaction" |
| LSM (tree) | 로그구조병합트리(Log-Structured Merge tree) · 쓰기를 버퍼링 후 정렬된 파일로 플러시·병합하는 스토리지 엔진 구조, 이 카드의 주제. "An LSM tree buffers writes into an in-memory memtable" |
| SSTable | 정렬된 불변 파일(Sorted String Table) · 메모리의 memtable이 디스크로 flush될 때 만들어지는 파일 포맷. "flushes it as a sorted, immutable file (an SSTable)" |
| RocksDB | 페이스북이 만든 LSM 기반 임베디드 키밸류 스토어 · 실습에서 쓰기 증폭을 측정할 실제 엔진으로 언급. "Load a random-key write workload onto RocksDB or a similar engine" |
| Bloom filter | 블룸 필터(확률적 멤버십 검사 자료구조) · 읽기 증폭을 줄이는 튜닝 손잡이 중 하나로 언급. "tuning knobs like Bloom filters, block cache, file size" |
<!-- acronyms 2026-09-18 -->
