## en
- **Devnet indexer: tune merge fan-in and buffer size as a benchmarked config.** When rebuilding chain-event indexes from genesis, measure the optimum rather than using a default, and record the chosen k with the benchmark it came from.
- **gitboard: apply the same tuning to cross-service log exports.** If gitboard re-sorts large exported logs from multiple services, don't assume an off-the-shelf sort library scales; apply the same buffer/fan-in benchmark used for the indexer.
- **CI: track bytes read/written, not just wall-clock time, in resync benchmarks.** Add an I/O-efficiency metric to any reindex or resync test in CI, since the card's point is that memory bandwidth, not comparisons, is the real bottleneck.

## ko
- **Devnet 인덱서: merge fan-in과 버퍼 크기를 벤치마크된 설정값으로 정한다.** 제네시스부터 체인 이벤트 인덱스를 다시 만들 때 기본값을 쓰지 않고 최적값을 측정하며, 선택한 k값을 그 벤치마크와 함께 기록한다.
- **gitboard: 서비스 간 로그 내보내기에도 같은 튜닝을 적용한다.** gitboard가 여러 서비스에서 내보낸 대용량 로그를 다시 정렬한다면 기성 정렬 라이브러리가 알아서 규모에 맞을 거라 가정하지 않고, 인덱서에 쓴 것과 같은 버퍼·fan-in 벤치마크를 적용한다.
- **CI: 재동기화 벤치마크에서 벽시계 시간뿐 아니라 읽고 쓴 바이트 수도 추적한다.** 카드의 요지는 병목이 비교 횟수가 아니라 메모리 대역폭이라는 것이므로, CI의 리인덱스·재동기화 테스트에 I/O 효율 지표를 추가한다.
