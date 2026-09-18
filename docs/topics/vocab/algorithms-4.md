| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| hide in | ~에 숨어 있다 · 진짜 비용이 점근 복잡도가 아니라 상수항에 숨어있음을 설명 · "the real cost hides not in the asymptotic complexity" |
| scatter across | ~에 흩어지다, 산재하다 · 새 노드들이 힙 여기저기에 흩어져 캐시 효율을 해침 · "scatters nodes across the heap" |
| pointer chasing | 포인터를 따라가며 메모리 접근하는 것 · 흩어진 노드 때문에 포인터 추적이 잦아짐 · "hurts cache locality due to more pointer chasing" |
| on the upside | 반면 좋은 점은, 긍정적인 면으로는 · 구조 공유 덕분에 diff가 빨라진다는 대목 도입 · "On the upside, since the previous version stays intact" |
| skip (entire subtrees) | (전체 부분트리를) 건너뛰다 · 참조가 같은 부분은 비교할 필요 없이 넘어감 · "diffing two versions can skip entire subtrees" |
| basically free | 사실상 공짜다, 거의 비용이 없다 · 로그 복잡도라 비용이 없다고 착각하는 흔한 가정 · "copying is O(log n), so it's basically free" |
| bounded by | ~로 상한이 정해지다, ~이내로 제한되다 · 업데이트 1회가 O(log n) 복사로 제한됨 · "a single update is bounded by O(log n) node copies" |
| HAMT | 해시 배열 매핑 트라이(Hash Array Mapped Trie, HAMT) · 경로 복사로 구조적 공유를 구현하는 불변 자료구조. "trie-based structures like HAMTs, the path length is O(log n)" |
| GC | 가비지 컬렉션(Garbage Collection, GC) · 매번 새 노드를 할당하는 함수형 업데이트가 늘리는 부담. "increases allocation and GC pressure" |
| copy-on-write | 카피온라이트(복사 후 쓰기, copy-on-write) · 변경분만 복사하고 나머지는 공유하는 구조, EVM 상태 트리도 이 방식. "a direct on-chain instance of a copy-on-write structure" |
<!-- acronyms 2026-09-18 -->
