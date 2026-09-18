## en
- **Verex: profile allocator contention before assuming a logic bottleneck.** If the CLOB matching engine's throughput doesn't scale with cores under load, check allocator contention first, the same signal the PoC's benchmark surfaces.
- **Devnet: watch RSS on the hosted Anvil node as a fragmentation signal.** RSS sitting far above actual chain-state size points to the allocator's purge/decay policy, not a leak, before digging further.
- **gitboard: add peak RSS next to throughput and latency for any hot-path service.** A throughput number alone hides what allocator behavior is doing to memory, so track both together.

## ko
- **Verex: 로직 병목이라고 단정하기 전에 할당자 경합부터 프로파일링한다.** CLOB 매칭 엔진의 처리량이 부하 상황에서 코어 수만큼 늘지 않으면 먼저 할당자 경합을 확인한다. 이 PoC의 벤치마크가 보여주는 것과 같은 신호다.
- **Devnet: 호스팅된 Anvil 노드의 RSS를 단편화 신호로 지켜본다.** RSS가 실제 체인 상태 크기보다 훨씬 높게 유지된다면, 더 파기 전에 누수가 아니라 할당자의 purge/decay 정책부터 의심한다.
- **gitboard: 핫패스 서비스마다 처리량·지연 옆에 피크 RSS를 추가한다.** 처리량 수치 하나만으로는 할당자 동작이 메모리에 미치는 영향을 숨기므로 둘을 함께 추적한다.
