## en
- **Verex: document the memory ordering per shared field in the matching engine.** For the in-memory order book, pick and write down the specific ordering (relaxed / acquire-release / seq_cst) per shared field, and add a stress test flagged for a weak-memory model rather than trusting x86-only test runs.
- **Devnet/CI: make a race-detector run a required CI gate.** Since ordering bugs pass on x86 and only surface under load or a weaker model, add the order-book concurrency tests under a race detector as a mandatory CI job, not optional.
- **OFA: decide ordering for the solver's shared bid-collection state too.** Treat the auction's shared bid state as the same class of hazard as Verex's order book; choose acquire/release vs mutex deliberately rather than assuming atomics are always cheaper.

## ko
- **Verex: 매칭 엔진의 공유 필드별 메모리 순서를 문서화한다.** 인메모리 오더북의 각 공유 필드에 대해 구체적인 순서(relaxed/acquire-release/seq_cst)를 정해 적어두고, x86에서만 통과하는 테스트를 믿는 대신 약한 메모리 모델을 겨냥한 스트레스 테스트를 추가한다.
- **Devnet/CI: 레이스 디텍터 실행을 필수 CI 게이트로 만든다.** 순서 버그는 x86에서는 통과하고 부하나 더 약한 모델에서만 드러나므로, 오더북 동시성 테스트를 레이스 디텍터 아래에서 돌리는 것을 선택 사항이 아니라 필수 CI 작업으로 추가한다.
- **OFA: 솔버의 공유 입찰 수집 상태에도 순서를 정한다.** 경매의 공유 입찰 상태를 Verex 오더북과 같은 부류의 위험으로 취급해, 원자적 연산이 항상 더 싸다고 가정하는 대신 acquire/release와 뮤텍스 중 무엇을 쓸지 의도적으로 정한다.
