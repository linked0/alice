## en
- **Verex: admit/drop CLOB matching requests the way continuous batching admits/drops decode requests.** At each matching cycle, drop settled orders and admit new ones instead of holding a fixed batch composition, to cut idle time under load the same way inference serving does.
- **Devnet/Rabbit: if Rabbit's agent reasoning is ever self-hosted, size GPU memory against concurrent session KV cache, not model size alone.** Concurrency, not parameter count, is what runs out first — budget Devnet's infra plan around that.
- **Number: check jayverse-number's indexer for the same fragmentation PagedAttention fixes.** Fixed-size pages instead of one contiguous block is a general fix for growing per-request state — worth a look at how the indexer allocates memory for open queries.

## ko
- **Verex: continuous batching이 디코드 요청을 받아들이고 내보내듯 CLOB 매칭 요청도 그렇게 처리한다.** 매 매칭 사이클마다 고정된 배치 구성을 유지하는 대신 정산된 주문은 빼고 새 주문을 받아들여, 추론 서빙과 같은 방식으로 부하 아래 유휴 시간을 줄인다.
- **Devnet/Rabbit: Rabbit의 에이전트 추론을 언젠가 직접 호스팅한다면 GPU 메모리를 모델 크기가 아니라 동시 세션 KV 캐시에 맞춰 산정한다.** 먼저 바닥나는 것은 파라미터 수가 아니라 동시성이다. Devnet의 인프라 계획을 이 기준으로 잡는다.
- **Number: jayverse-number의 인덱서에 PagedAttention이 고치는 것과 같은 단편화 문제가 있는지 확인한다.** 하나의 연속 블록 대신 고정 크기 페이지를 쓰는 것은 요청별 상태가 커질 때의 일반적 해법이다. 열린 쿼리에 대해 인덱서가 메모리를 어떻게 할당하는지 살펴볼 가치가 있다.
