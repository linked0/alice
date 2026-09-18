## en
- **Verex / Devnet: prove amortized cost with a potential function before assuming O(1).** Any resizing structure (an order-book level array, an indexer's growable buffer) should get the Φ argument written down once, rather than assuming a resize-and-copy averages out.
- **gitboard: log real cost per push alongside the running potential.** That distinguishes a genuine O(n) regression in a growable per-market array from a normal, bounded amortized spike.

## ko
- **Verex / Devnet: O(1)을 가정하기 전에 potential function으로 상각 비용을 증명한다.** 크기가 늘어나는 어떤 구조든(오더북 레벨 배열, 인덱서의 확장 버퍼) resize-and-copy가 평균적으로 괜찮을 거라 가정하는 대신 Φ 논증을 한 번 적어둔다.
- **gitboard: push마다 실제 비용을 진행 중인 potential과 함께 기록한다.** 이렇게 하면 마켓별 확장 버퍼의 진짜 O(n) 회귀를 정상적이고 유한한 상각 스파이크와 구분할 수 있다.
