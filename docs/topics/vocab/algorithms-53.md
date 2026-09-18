| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| hurt scalability | 확장성을 해치다 · 노드 수가 늘수록 오버헤드가 커져 시스템이 커지기 힘들어질 때. "scales with the number of nodes, hurting scalability" |
| stay close to | ~에 가깝게 유지되다 · 논리 시계 값이 실제 물리 시간과 크게 어긋나지 않을 때. "stays close to physical time" |
| survive (clock skew) | (오차·왜곡을) 견뎌내다, 살아남다 · 시계가 어긋나도 인과 순서가 무너지지 않을 때. "causal order survives clock skew" |
| come down to | 결국 ~로 귀결되다 · 여러 요인을 정리하면 결국 하나의 선택 문제로 좁혀질 때. "ultimately comes down to which clock you use" |
| look reversed | (실제와 반대로) 뒤바뀐 것처럼 보이다 · 원인과 결과의 순서가 잘못 정렬되어 보일 때. "can make cause and effect look reversed" |
| skew (n.) | (시계·시간의) 오차, 어긋남 · 서버 간 물리 시계가 서로 안 맞는 정도. "gets the order reversed by skew" |
| the converse doesn't hold | 그 역은 성립하지 않는다 · 한쪽 방향은 참이지만 반대 방향은 참이 아닐 때. "but the converse doesn't hold" |
| HLC | 하이브리드 논리 시계(Hybrid Logical Clock) · 물리 시간과 논리 카운터를 결합해 인과성을 지키면서 물리 시간에 가까운 타임스탬프를 만드는 기법, 분산 DB의 버전 타임스탬프로 쓰임. "HLCs are used as version timestamps in distributed databases" |
| Lamport clock | 램포트 시계 · 각 노드가 카운터를 증가시키며 인과관계는 보장하지만 동시성은 구분 못 하는 논리 시계. "A Lamport clock has each node keep a counter" |
| vector clock | 벡터 시계 · 노드마다 카운터 배열을 두어 두 이벤트가 인과적으로 순서가 있는지 동시적인지 정확히 판별하지만, 메타데이터가 노드 수에 비례해 커지는 논리 시계. "A vector clock carries an array of counters, one per node" |
<!-- acronyms 2026-09-18 -->
