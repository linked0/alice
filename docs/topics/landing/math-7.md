## en
- **Verex: audit every loop over an unbounded collection for a gas-limit DoS.** Beyond settlement, check order cancellation, fee distribution, and any other function that iterates over participants or orders, and convert each to a pull-based or paginated design before participant count can grow past the block gas limit.
- **CI: add a gas-growth test, not just a gas-snapshot test.** Run the same function at increasing n (10, 100, 1000 participants) in CI and fail the build if gas grows without bound, rather than only snapshotting gas at a fixed small n.
- **Bridge: check the relayer's per-batch mint/unlock loop the same way.** If the bridge ever batches multiple lock events into one mint transaction, that loop needs the identical bound check before batch size is attacker- or user-controllable.

## ko
- **Verex: 무한정 커질 수 있는 컬렉션을 순회하는 모든 루프에서 가스 한도 DoS를 점검한다.** 정산뿐 아니라 주문 취소, 수수료 분배 등 참가자나 주문을 순회하는 다른 함수도 확인하고, 참가자 수가 블록 가스 한도를 넘기 전에 각각을 풀 기반이나 페이지네이션 설계로 바꾼다.
- **CI: 가스 스냅샷 테스트가 아니라 가스 증가 테스트를 추가한다.** 같은 함수를 n(참가자 10, 100, 1000)을 늘려가며 CI에서 실행하고, 고정된 작은 n에서만 가스를 스냅샷하는 대신 가스가 무한정 늘어나면 빌드를 실패시킨다.
- **Bridge: 릴레이어의 배치당 민트/언락 루프도 같은 방식으로 점검한다.** 브리지가 여러 락 이벤트를 하나의 민트 트랜잭션으로 배치 처리하게 된다면, 배치 크기가 공격자나 사용자에 의해 커질 수 있기 전에 동일한 한도 점검이 필요하다.
