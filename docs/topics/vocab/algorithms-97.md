| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| bottleneck on | ~에서 병목이 걸리다 · 두 단계가 서로 다른 자원 제약에 막힐 때. "the two stages bottleneck on different things" |
| grow with | ~에 비례해서 커지다 · 캐시 크기가 시퀀스 길이에 따라 늘어날 때. "this cache grows with sequence length" |
| cut ... idle time | ~의 유휴 시간을 줄이다 · GPU가 노는 시간을 줄여 효율을 높일 때. "cutting GPU idle time" |
| mimic | 흉내 내다, 모방하다 · 작은 모델이 큰 모델의 출력을 따라 하도록 학습할 때. "trains a small model to mimic a large model's outputs" |
| trade-off across | ~ 사이의 트레이드오프(상충 관계) · 여러 기준(품질, 메모리 등) 사이에서 하나를 얻으면 다른 걸 잃을 때. "a different trade-off across quality, memory, and serving flexibility" |
| the only lever you have left | 남은 유일한 수단 · 다른 최적화 여지가 없어 마지막으로 쓸 수 있는 방법. "the only lever you have left is buying more GPUs" |
| shaped far more by ... than by | ~보다 ~에 의해 훨씬 더 좌우되는 · 어떤 결과의 주된 원인이 통념과 다를 때. "shaped far more by KV cache management" |
| KV cache | 키/값 캐시(Key-Value cache) · 디코드 단계에서 이전 토큰들의 키·값 벡터를 저장해 매 스텝 재계산을 피하는 캐시, 크기가 GPU 메모리 한계를 좌우함. "the key/value vectors of past tokens are kept in a KV cache" |
| PagedAttention | 페이지 단위로 KV 캐시를 관리하는 기법 · 하나의 연속된 블록 대신 고정 크기 페이지로 캐시를 나눠 메모리 단편화·과할당을 없애는 서빙 기법. "PagedAttention manages the KV cache in fixed-size pages" |
| LoRA | 저랭크 적응(Low-Rank Adaptation) · 원래 가중치는 고정하고 작은 저랭크 행렬만 학습·교체해 파인튜닝 비용을 줄이는 기법. "LoRA freezes the original weights and trains/swaps only small low-rank matrices" |
| continuous batching | 연속 배칭 · 매 토큰 생성 스텝마다 끝난 요청을 빼고 새 요청을 받아들여 GPU 유휴시간을 줄이는 서빙 전략. "Continuous batching doesn't fix the batch composition per request" |
| p95 latency | 95번째 백분위 지연시간 · 전체 요청 중 최악에 가까운 5%를 제외한 지연시간 기준, 서빙 성능을 재는 표준 지표. "measure throughput and p95 latency" |
<!-- acronyms 2026-09-18 -->
