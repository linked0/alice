| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| hide in | ~에 숨어 있다 · 진짜 비용이 점근 복잡도가 아니라 상수항에 숨어있음을 설명 · "the real cost hides not in the asymptotic complexity" |
| scatter across | ~에 흩어지다, 산재하다 · 새 노드들이 힙 여기저기에 흩어져 캐시 효율을 해침 · "scatters nodes across the heap" |
| pointer chasing | 포인터를 따라가며 메모리 접근하는 것 · 흩어진 노드 때문에 포인터 추적이 잦아짐 · "hurts cache locality due to more pointer chasing" |
| on the upside | 반면 좋은 점은, 긍정적인 면으로는 · 구조 공유 덕분에 diff가 빨라진다는 대목 도입 · "On the upside, since the previous version stays intact" |
| skip (entire subtrees) | (전체 부분트리를) 건너뛰다 · 참조가 같은 부분은 비교할 필요 없이 넘어감 · "diffing two versions can skip entire subtrees" |
| basically free | 사실상 공짜다, 거의 비용이 없다 · 로그 복잡도라 비용이 없다고 착각하는 흔한 가정 · "copying is O(log n), so it's basically free" |
| bounded by | ~로 상한이 정해지다, ~이내로 제한되다 · 업데이트 1회가 O(log n) 복사로 제한됨 · "a single update is bounded by O(log n) node copies" |
