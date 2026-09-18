## en
- **Verex: confirm the CLOB matching engine runs as a single actor or thread and audit any code path that could block it with a CPU-bound task.** That would stall all matching for every market.
- **Devnet: choose each Cloud Run service's concurrency model from this framework.** An event loop for I/O-bound API routes, a single-actor design for stateful matching or settlement logic.
- **Rabbit: isolate session-key and mandate execution that touches shared state, such as nonces or allowances, per actor rather than guarding it with ad hoc locks.** This avoids the contention and deadlock failure mode named here.

## ko
- **Verex: CLOB 매칭 엔진이 단일 액터·단일 스레드로 동작하는지 확인하고, CPU 바운드 작업으로 이를 블로킹할 수 있는 코드 경로를 감사한다.** 블로킹되면 모든 마켓의 매칭이 함께 멈추기 때문이다.
- **Devnet: 각 Cloud Run 서비스의 동시성 모델을 이 프레임워크로 선택한다.** I/O 바운드 API 라우트에는 이벤트 루프를, 상태를 가진 매칭·정산 로직에는 단일 액터 설계를 쓴다.
- **Rabbit: nonce나 allowance처럼 공유 상태를 건드리는 세션 키·mandate 실행은 임시방편적인 락으로 지키는 대신 액터 단위로 격리한다.** 여기서 말하는 경합·데드락 실패 모드를 피하기 위함이다.
