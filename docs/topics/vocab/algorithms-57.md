| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| proof of availability | 가용성 증명 · 데이터가 실제로 배포·저장되었음을 검증자 서명으로 보증하는 것 · "collects other validators' signatures (a proof of availability)" |
| becomes independent of | ~와 거의 무관해지다 · 지연시간이 데이터 크기에 더 이상 영향받지 않게 된다는 뜻 · "consensus latency becomes nearly independent of data size" |
| throughput ceiling | 처리량 상한선 · 시스템 전체 성능이 한 지점(리더)에 의해 막히는 한계 · "that leader's bandwidth becomes the system's throughput ceiling" |
| bottleneck | 병목(현상) · 전체 흐름을 느리게 만드는 좁은 지점 · "solve that bottleneck" |
| deterministic rule | 결정론적 규칙 · 같은 입력이면 항상 같은 결과가 나오는 고정된 규칙 · "by a fixed deterministic rule and derives" |
| derive the same total order | (각자) 동일한 전체 순서를 도출해내다 · 별도 통신 없이도 모두가 같은 결론에 도달한다는 뜻 · "derives the same total order as everyone else" |
| BFT | 비잔틴장애허용(Byzantine Fault Tolerance) · 악의적 노드가 있어도 합의가 성립하는 고전적 합의 방식, DAG 기반 설계와 대비됨. "In classic BFT, where a single leader broadcasts" |
| DAG | 방향성 비순환 그래프(Directed Acyclic Graph) · 데이터 전파와 순서 결정을 분리하는 이 글의 핵심 구조. "DAG-based consensus separates" |
| Narwhal | 멤풀(데이터 전파) 계층을 맡는 프로토콜 · 검증자들이 배치를 만들고 가용성 증명을 모으는 계층. "Narwhal is the mempool layer" |
| Bullshark | Narwhal 위에서 순서를 정하는 합의 프로토콜 · 추가 메시지 교환 없이 로컬 DAG만으로 전체 순서를 도출함. "An ordering protocol like Bullshark exchanges almost no extra messages" |
<!-- acronyms 2026-09-18 -->
