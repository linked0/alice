## en
- **Verex: pick epoch-based reclamation for the tick-driven matcher.** The CLOB's price-level structure updates in bursts per tick, which fits epoch batching better than per-node hazard pointers; make that choice explicit rather than defaulting to whichever is easier to implement.
- **CI: add a dedicated ABA stress test.** Beyond general contention testing, write a test that rapidly removes and reinserts an order at the same price level under concurrent access, the exact pattern that triggers ABA.
- **Auditor: publish the concurrency invariant, not just the throughput number.** "No lost or duplicate order under concurrent update" is a checkable invariant the Auditor row can cite when someone asks what was verified about matching-engine correctness.

## ko
- **Verex: 틱 단위 매처에는 에포크 기반 회수를 선택한다.** CLOB의 가격 레벨 구조는 틱마다 몰아서 갱신되므로, 노드별 hazard pointer보다 에포크 배칭에 더 잘 맞는다. 구현하기 쉬운 쪽을 기본값으로 쓰지 말고 이 선택을 명시적으로 남긴다.
- **CI: 전용 ABA 스트레스 테스트를 추가한다.** 일반적인 경합 테스트를 넘어, 동시 접근 상황에서 같은 가격 레벨의 주문을 빠르게 제거했다가 재삽입하는 테스트를 작성한다. ABA를 유발하는 정확한 패턴이다.
- **Auditor: 처리량 수치가 아니라 동시성 불변조건을 공개한다.** "동시 갱신 상황에서 주문 유실이나 중복이 없다"는 것은 검증 가능한 불변조건이다. 매칭 엔진의 정확성에 대해 무엇이 검증됐는지 물을 때 Auditor 행이 인용할 수 있다.
