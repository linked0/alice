## en
- **Verex: measure the matching engine's actual span, not just its work.** Before adding worker threads to the off-chain matching engine, compute the critical path of order dependencies; if span dominates, more workers won't help and the code structure needs to change, not the worker count.
- **Devnet: decide whether Amdahl or Gustafson is the right model for a future L2's block execution.** If Devnet's OP-Stack L2 pursues parallel transaction execution, state upfront whether the goal is a fixed workload going faster (Amdahl) or bigger blocks in the same time (Gustafson), since they call for different engineering.
- **CI: benchmark ChainJob-style batch settlement against core count.** Overlay Verex's batch settlement throughput against increasing parallelism to find where the serial fraction (session-key nonce lane, DB writes) caps the speedup, rather than assuming more concurrency helps indefinitely.

## ko
- **Verex: 매칭 엔진의 실제 스팬을 측정하지, 작업량만 보지 않는다.** 오프체인 매칭 엔진에 워커 스레드를 추가하기 전에 주문 의존성의 임계 경로를 계산한다. 스팬이 지배적이면 워커를 늘려도 소용없고 워커 수가 아니라 코드 구조를 바꿔야 한다.
- **Devnet: 미래 L2의 블록 실행에 Amdahl과 Gustafson 중 어느 모델이 맞는지 정한다.** Devnet의 OP-Stack L2가 병렬 트랜잭션 실행을 추진한다면, 목표가 고정된 작업을 더 빠르게(Amdahl) 하는 것인지 같은 시간에 더 큰 블록(Gustafson)을 처리하는 것인지 먼저 밝힌다. 둘은 다른 엔지니어링을 요구한다.
- **CI: ChainJob식 배치 정산을 코어 수 대비 벤치마크한다.** Verex의 배치 정산 처리량을 늘어나는 병렬성에 겹쳐 그려, 직렬 부분(세션 키 논스 레인, DB 쓰기)이 어디서 속도 향상을 막는지 찾는다. 동시성이 늘면 무조건 도움이 된다고 가정하지 않는다.
