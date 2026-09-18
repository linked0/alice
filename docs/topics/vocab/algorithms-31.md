| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| keep ~ under control | ~을 통제 가능한 상태로 유지하다 · 단편화를 관리 가능한 수준으로 억제한다는 뜻 · "keeping fragmentation under control" |
| pull ~ from | ~로부터 (자원을) 끌어오다 · OS로부터 큰 단위로 메모리를 받아옴 · "it pulls memory from the OS in large units" |
| carve up | (큰 덩어리를) 잘게 나누다 · 받아온 큰 메모리 청크를 잘라서 쓰는 것 · "chunks or extents) that it then carves up" |
| cut down on | ~을 줄이다 · 원자적 연산 횟수를 줄이기 위한 free list sharding · "to cut down on atomic operations" |
| fail to scale with | ~에 비례해 늘지 않다, ~만큼 확장되지 않다 · 코어 수를 늘려도 처리량이 안 느는 문제 · "throughput fails to scale with core count" |
| far above | ~보다 훨씬 위로, 크게 웃도는 · 실제 사용량보다 RSS가 과도하게 높은 상태 · "RSS staying far above actual usage" |
| treat ~ as | ~을 ~으로 취급하다, 간주하다 · 메모리 반납 시점을 정책적 결정으로 다룸 · "treating the moment memory is returned to the OS" |
| jemalloc | 제이말록(jemalloc) · 스레드별 아레나와 tcache를 쓰는 범용 메모리 할당자. "jemalloc assigns each thread an arena and adds a thread-local cache" |
| mimalloc | 미말록(mimalloc) · 스레드별 힙과 페이지별 프리리스트를 쓰는 메모리 할당자, free list sharding 기법의 예. "mimalloc gives each thread its own heap and each page its own free list" |
| RSS | 상주 집합 크기(Resident Set Size, RSS) · 프로세스가 실제 점유한 물리 메모리량, 할당자 정책과 괴리될 수 있음. "RSS staying far above actual usage" |
| LD_PRELOAD | LD_PRELOAD · 실행 전 공유 라이브러리를 끼워넣어 기본 malloc을 jemalloc 등으로 바꿔치기하는 리눅스 메커니즘. "swapping in the default malloc versus jemalloc (or mimalloc) via LD_PRELOAD" |
| tcache | 스레드 로컬 캐시(tcache) · jemalloc이 락 없이 할당·해제를 처리하도록 스레드마다 두는 캐시. "adds a thread-local cache called tcache" |
<!-- acronyms 2026-09-18 -->
