## en
- **Rabbit: put a bounded queue and load-shedding in front of the ERC-4337 bundler/relayer path.** It has the same fast-intake-slow-settlement shape as Verex; size the queue with Little's Law instead of letting a spike become unbounded retries.
- **OFA: measure p50/p99 latency and queue length at 50/80/95% of service rate before trusting the solver auction under load.** The intake-to-settlement gap in the auction needs the same capacity math the exercise runs.
- **gitboard: surface queue depth and utilization ρ per service.** A service approaching ρ→1 should be visible on the dashboard before latency blows up, not discovered after timeouts start.

## ko
- **Rabbit: ERC-4337 번들러/릴레이어 경로 앞에 바운디드 큐와 로드 셰딩을 둔다.** 인테이크는 빠르고 정산은 느린 Verex와 같은 구조이므로, 스파이크가 무한 재시도로 번지게 두지 말고 Little's Law로 큐 크기를 정한다.
- **OFA: 서비스 레이트의 50/80/95%에서 p50/p99 지연과 큐 길이를 측정한 뒤에야 솔버 경매를 부하 상황에서 신뢰한다.** 경매의 인테이크-정산 간극에도 익서사이즈와 같은 용량 계산이 필요하다.
- **gitboard: 서비스별 큐 깊이와 사용률 ρ를 대시보드에 노출한다.** ρ가 1에 가까워지는 서비스는 지연이 폭발하기 전에 대시보드에서 보여야지, 타임아웃이 시작된 뒤 발견되어서는 안 된다.
