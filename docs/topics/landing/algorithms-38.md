## en
- **Verex: swap the order-book/market-state cache with an atomic pointer instead of a mutex.** Reads (quote lookups) vastly outnumber writes (new orders), which is exactly the read-heavy shape RCU is for — a lock here is pure cache-line contention.
- **Devnet: use epoch-based reclamation for any hosted-Anvil config or state snapshot service with many readers.** A copy-on-write swap avoids the RW-lock bottleneck the same way it does for a routing table or symbol table.
- **Wallet: read the simulate-before-sign state snapshot through an atomic swap, not a lock.** Simulation latency matters per signature request, and RCU-style publish keeps concurrent simulations from blocking on each other.

## ko
- **Verex: 오더북·마켓 상태 캐시는 뮤텍스 대신 원자적 포인터로 교체한다.** 읽기(호가 조회)가 쓰기(신규 주문)보다 압도적으로 많다. 정확히 RCU가 다루는 읽기 편중 모양이고, 여기서 락은 순수한 캐시라인 경합일 뿐이다.
- **Devnet: 리더가 많은 호스팅 Anvil 설정이나 상태 스냅샷 서비스에는 epoch 기반 회수를 쓴다.** copy-on-write 스왑은 라우팅 테이블이나 심볼 테이블에서처럼 RW-lock 병목을 피한다.
- **Wallet: simulate-before-sign 상태 스냅샷은 락이 아니라 원자적 스왑으로 읽는다.** 서명 요청마다 시뮬레이션 지연이 중요하고, RCU 방식의 퍼블리시는 동시 시뮬레이션들이 서로 블로킹하지 않게 한다.
