## en
- **Verex: size the Bloom filter to a stated false-positive budget.** Before wiring it into event-log processing, pick m and k for a concrete target — e.g. under 0.1% FP at 10M processed order IDs — and fall back to an exact check on every positive hit, since Bloom never gives false negatives but the exact check is still required.
- **gitboard: use a Count-Min sketch or HyperLogLog for high-cardinality metrics.** Track approximate event volume or distinct-error counts across services without storing every log line, for dashboard metrics that don't need exactness.
- **Devnet: prefer a Cuckoo filter for the rolling seen-tx cache.** Anvil devnet resets and forks periodically, so an already-seen-tx cache needs deletion support, which a Bloom filter doesn't offer but a Cuckoo filter does.

## ko
- **Verex: Bloom 필터를 명시된 오탐 예산에 맞춰 사이징한다.** 이벤트 로그 처리에 붙이기 전에, 예컨대 처리된 주문 ID 1000만 건에서 오탐률 0.1% 미만이라는 구체적 목표에 맞춰 m과 k를 정하고, 모든 양성 히트는 정확 검사로 재확인한다. Bloom은 거짓 음성은 없지만 정확 검사는 여전히 필요하다.
- **gitboard: 카디널리티가 높은 지표에는 Count-Min 스케치나 HyperLogLog를 쓴다.** 모든 로그 줄을 저장하지 않고도 서비스 전체의 대략적 이벤트 볼륨이나 고유 에러 수를 추적한다. 정확할 필요가 없는 대시보드 지표에 적합하다.
- **Devnet: 롤링 "이미 본 트랜잭션" 캐시에는 Cuckoo 필터를 선호한다.** Anvil devnet은 주기적으로 리셋되고 포크되므로, 이미 본 트랜잭션 캐시에는 삭제 지원이 필요하다. Bloom 필터는 이를 제공하지 않지만 Cuckoo 필터는 제공한다.
