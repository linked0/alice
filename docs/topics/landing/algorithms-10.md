## en
- **Rabbit/Devnet: pick the state that gets persistent-segment-tree treatment.** Make session-key/mandate balances or nonce state on the indexer persistent-segment-tree-backed, so a reorg on the Anvil devnet rolls back at O(log n) instead of a full re-index.
- **Verex: use a lazy segment tree for order-book aggregates.** Best bid/ask and depth-in-range are a range-sum/range-min workload; reach for a lazy segment tree instead of recomputing aggregates on every order.
- **gitboard: use it as the answer to "state at block N."** When gitboard needs a past state for a given service, treat the persistent segment tree as the structure to reach for, instead of snapshotting the whole database.

## ko
- **Rabbit/Devnet: 영속 세그먼트 트리를 적용할 상태를 정한다.** 인덱서의 세션 키/위임 잔액이나 논스 상태를 영속 세그먼트 트리 기반으로 만들어, Anvil devnet에서 리오그가 나도 전체 재인덱싱 대신 O(log n)으로 롤백한다.
- **Verex: 오더북 집계에 lazy 세그먼트 트리를 쓴다.** 최우선 매수/매도호가와 구간별 깊이는 구간 합/구간 최소 워크로드이므로, 매 주문마다 집계를 다시 계산하는 대신 lazy 세그먼트 트리를 사용한다.
- **gitboard: "블록 N 시점 상태"의 답으로 쓴다.** gitboard가 특정 서비스의 과거 상태를 필요로 할 때, 전체 DB를 스냅샷하는 대신 영속 세그먼트 트리를 우선 고려할 구조로 삼는다.
