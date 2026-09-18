| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| write skew | 쓰기 왜곡(각자는 규칙을 지켰지만 합쳐서 위반되는 이상 현상) · 스냅샷 격리의 대표적 결함. "The classic anomaly is write skew" |
| snapshot isolation | 스냅샷 격리 수준 · 각 트랜잭션이 자신만의 스냅샷을 보는 격리 수준. "Snapshot isolation, built on top of this" |
| dirty reads | 더티 리드(커밋 안 된 값을 읽는 현상) · 스냅샷 격리가 막아주는 이상 현상 중 하나. "prevents dirty reads, non-repeatable reads, and" |
| lost updates | 갱신 손실(동시 쓰기로 한쪽 변경이 사라짐) · 스냅샷 격리가 막아주는 또 다른 이상 현상. "reads, and lost updates, but it does" |
| surface quietly | 조용히(눈에 띄지 않게) 드러나다 · 부하가 커져야 비로소 발견되는 버그를 가리킴. "creates bugs that surface quietly, only once" |
| physicalize the invariant | 불변조건을 물리적 구조(단일 행 등)로 구현하다 · 애플리케이션 규칙을 DB 제약으로 강제하는 해법. "physicalize the invariant as a single row" |
| explicitly lock the rows | 근거로 삼은 행을 명시적으로 잠그다 · 동시성 문제를 막는 수동 잠금 기법. "explicitly lock the rows a decision was based on" |
