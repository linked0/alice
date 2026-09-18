| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| update in place | 자리에서 그대로 덮어써서 갱신하다 · "updates them in place" |
| come naturally | 자연스럽게 잘 되다 · "range scans come naturally" |
| drive up | (수치를) 끌어올리다 · "driving up write amplification" |
| scattered across | 여기저기 흩어져 있다 · "scattered across multiple levels" |
| mitigated with | ~로 완화되다 · "mitigated with Bloom filters" |
| comes down to | 결국 ~로 귀결되다 · "the choice comes down to the workload's read/write ratio" |
| restructure around | ~을 중심으로 다시 짜다 · "restructure state around flat key layout" |
| LSM tree | 로그 구조 병합 트리(Log-Structured Merge tree) · 쓰기를 순차적으로 모아 처리해 쓰기 처리량을 높이는 저장 구조. "An LSM tree buffers writes into an in-memory table" |
| LevelDB | LevelDB · 구글이 만든 LSM 기반 키-값 저장소, Geth가 오래 사용해 온 스토리지 엔진. "LSM-based storage (LevelDB, later Pebble)" |
| MDBX | MDBX · Erigon이 채택한 B+트리 기반 키-값 저장소, 평평한 키 구조로 읽기 증폭을 낮춤. "the B+tree-based MDBX" |
| SSTables | 정렬된 문자열 테이블(Sorted String Tables) · LSM 트리가 메모리 버퍼를 디스크에 순차 기록할 때 쓰는 파일 형식. "flushes them sequentially as SSTables" |
<!-- acronyms 2026-09-18 -->
