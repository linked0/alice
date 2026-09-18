## en
- **Verex: cache-line-align order-book shards before trusting a parallel design.** If the CLOB order book is ever sharded per core for parallel matching, pad and align each shard's hot counters, then benchmark padded vs unpadded throughput before trusting the scalability claim.
- **Devnet: check for false sharing in parallel chain-data parsing.** When indexing Anvil/Sepolia blocks in parallel for gitboard or Number, check per-thread counters for false sharing the same way — a profiler's per-function time won't reveal it, only a scalability curve will.
- **gitboard: add a padded-vs-unpadded throughput test before scaling cores.** If gitboard's data pipeline parallelizes further, run the one-time padded-vs-unpadded comparison first rather than assuming more cores means more throughput.

## ko
- **Verex: 병렬 설계를 신뢰하기 전에 오더북 샤드를 캐시라인에 맞춰 정렬한다.** CLOB 오더북이 코어별로 샤딩되어 병렬 매칭을 한다면, 각 샤드의 핫 카운터를 패딩·정렬하고, 패딩 유무에 따른 처리량을 벤치마크한 뒤에야 확장성 주장을 신뢰한다.
- **Devnet: 체인 데이터를 병렬로 파싱할 때 false sharing을 확인한다.** gitboard나 Number를 위해 Anvil/Sepolia 블록을 병렬로 인덱싱할 때도 스레드별 카운터의 false sharing을 같은 방식으로 확인한다. 프로파일러의 함수별 시간만으로는 드러나지 않고 확장성 곡선으로만 보인다.
- **gitboard: 코어를 늘리기 전에 패딩 유무 처리량 테스트를 추가한다.** gitboard 데이터 파이프라인을 더 병렬화한다면, 코어가 늘면 처리량도 는다고 가정하지 말고 한 번의 패딩 유무 비교 테스트를 먼저 돌린다.
