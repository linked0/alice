## en
- **Verex: measure the CLOB's competitive ratio against an offline-optimal replay of the same order sequence.** The same way LRU is graded against Belady's algorithm, replay a day's order flow through an offline-optimal matcher and compare — that turns "did the matcher do okay" into a number instead of an impression.
- **Rabbit/Devnet: choose an explicit eviction policy for the RPC response cache and test it adversarially.** Pick LRU, FIFO, or random deliberately, then construct an access sequence sized to the cache specifically to hit its worst case, since average-case traffic alone won't reveal it.

## ko
- **Verex: CLOB의 경쟁비를 같은 주문 시퀀스에 대한 오프라인 최적 리플레이와 비교해 측정한다.** LRU를 Belady 알고리즘과 비교해 평가하는 것과 같은 방식으로, 하루치 주문 흐름을 오프라인 최적 매처로 재생해 비교한다. 그러면 "매처가 잘했는지"가 인상이 아니라 숫자가 된다.
- **Rabbit/Devnet: Devnet 앞단의 RPC 응답 캐시에 명시적 퇴거 정책을 정하고 적대적으로 테스트한다.** LRU, FIFO, 랜덤 중 하나를 의도적으로 고른 뒤, 캐시 크기에 맞춰 최악의 경우를 노린 접근 시퀀스를 구성한다. 평균적인 트래픽만으로는 이를 드러낼 수 없다.
