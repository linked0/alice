## en
- **Verex: benchmark before choosing path copying for the order book.** Turn the trade-off the concept describes into an actual decision — measure GC pressure and cache-miss cost of HAMT-style snapshots against a mutable book under real order volume, then pick, instead of assuming O(log n) makes it free.
- **Wallet: give transaction simulation the same structural sharing.** When a user edits a simulated transaction before signing, snapshot and revert speculative state cheaply with path copying rather than deep-copying the whole simulated state each edit.
- **gitboard: diff dashboard states by reference, not by value.** If gitboard shows how a service's state changed between refreshes, skip subtrees whose references are unchanged instead of deep-diffing the whole payload each time.

## ko
- **Verex: 오더북에 패스 카피를 적용하기 전에 벤치마크부터 한다.** 개념이 설명하는 트레이드오프를 실제 결정으로 바꾼다. 실제 주문량 아래에서 HAMT 방식 스냅샷의 GC 압력과 캐시 미스 비용을 뮤터블 오더북과 비교해 측정한 뒤 고른다. O(log n)이라서 공짜라고 가정하지 않는다.
- **Wallet: 트랜잭션 시뮬레이션에도 같은 구조적 공유를 적용한다.** 사용자가 서명 전 시뮬레이션된 트랜잭션을 수정할 때, 매번 전체 시뮬레이션 상태를 깊이 복사하는 대신 패스 카피로 추측 상태를 값싸게 스냅샷하고 되돌린다.
- **gitboard: 대시보드 상태는 값이 아니라 참조로 diff한다.** gitboard가 새로고침 사이 서비스 상태 변화를 보여준다면, 매번 전체 페이로드를 깊이 비교하는 대신 참조가 바뀌지 않은 서브트리는 건너뛴다.
