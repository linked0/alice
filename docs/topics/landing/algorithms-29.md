## en
- **Verex: prefer object reuse and pooling over heap or GOGC tuning in the matching engine and block-processing loops.** Add an allocations-per-order metric to the performance budget so the choice between "reduce allocation" and "grow the heap" is measured, not guessed.
- **Devnet: capture a gctrace before changing heap limits on any latency spike.** If the Anvil-forked devnet or a future OP-Stack node ever shows p99 spikes tied to GC pauses, the tuning knobs (GOGC, memory limit) only make sense once the trace shows what the collector is actually spending time on.

## ko
- **Verex: 매칭 엔진과 블록 처리 루프에서는 힙이나 GOGC 튜닝보다 객체 재사용·풀링을 우선한다.** 성능 예산에 주문당 할당량 지표를 추가해서, "할당을 줄인다" 대 "힙을 키운다"의 선택을 추측이 아니라 측정으로 결정한다.
- **Devnet: 지연 스파이크가 생기면 힙 한도를 바꾸기 전에 gctrace부터 확보한다.** Anvil 포크 devnet이나 앞으로의 OP-Stack 노드에서 GC 일시정지와 연결된 p99 스파이크가 보인다면, 튜닝 노브(GOGC, 메모리 한도)는 수집기가 실제로 시간을 어디에 쓰는지 트레이스로 확인한 뒤에야 의미가 있다.
