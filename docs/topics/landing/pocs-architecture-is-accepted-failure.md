## en
- **Verex: write the three-line failure list for the settlement pipeline first.** For each component — slow, down, wrong — before picking any pattern for it; this is the PoC's own named candidate and the cheapest way to make the pattern choice a decision instead of vocabulary.
- **Devnet: size relayer/bundler capacity with Little's Law, not a guess.** Convert an expected requests-per-second and latency budget into a concrete concurrency number for whatever Devnet infra needs a capacity target.
- **Bridge: treat the lock-and-mint relayer queue as an explicit purchase.** It absorbs spikes but introduces unbounded delay and lost ordering, so the retried lock/mint step needs to be idempotent, not just retried.
- **gitboard: flag 85%+ utilization as a latency-cliff, not a comfortable number.** Plot queueing delay against utilization for any dashboarded service so capacity planning doesn't silently buy a wait-time cliff to save hardware.

## ko
- **Verex: 정산 파이프라인의 3줄 실패 목록부터 작성한다.** 각 컴포넌트에 대해 느릴 때, 다운됐을 때, 잘못된 값을 반환할 때를 먼저 적고 나서 패턴을 고른다. 이 PoC가 직접 지목한 예시이며, 패턴 선택을 용어 암기가 아니라 결정으로 만드는 가장 싼 방법이다.
- **Devnet: 릴레이어/번들러 용량을 추측이 아니라 Little's Law로 산정한다.** 예상 초당 요청 수와 지연 예산을 Devnet 인프라가 필요로 하는 구체적인 동시성 숫자로 변환한다.
- **Bridge: lock-and-mint 릴레이어 큐를 명시적인 구매로 다룬다.** 스파이크는 흡수하지만 무한 지연과 순서 유실을 들여온다. 재시도되는 lock/mint 단계는 그냥 재시도가 아니라 멱등이어야 한다.
- **gitboard: 85% 이상 사용률을 편안한 숫자가 아니라 지연 절벽으로 표시한다.** 대시보드에 올라간 서비스마다 사용률 대비 큐잉 지연을 그려서, 용량 계획이 하드웨어를 아끼려다 조용히 지연 절벽을 사들이지 않게 한다.
