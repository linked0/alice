## en
- **Number: make normalization an explicit config, not a hidden default.** If Number ships a "similar reading" feature, decide and document cosine similarity versus Euclidean distance and whether vectors are unit-normalized, since the two give different neighbors on the same data.
- **Personas: cluster wallets by direction, not magnitude.** Grouping wallets by on-chain behavior vectors for persona assignment should use cosine similarity so a whale and a casual wallet with the same behavior pattern land in the same cluster instead of being split by transaction-count scale.
- **gitboard: use cosine similarity for "find similar past incidents."** A log-search feature over gitboard's incident history is exactly the embedding-search case this card describes; pick the norm deliberately rather than defaulting to whatever the library ships.

## ko
- **Number: 정규화를 숨은 기본값이 아니라 명시적 설정으로 만든다.** Number가 "비슷한 리딩" 기능을 낸다면, 코사인 유사도와 유클리드 거리 중 무엇을 쓸지, 벡터를 단위 정규화할지를 결정하고 문서화한다. 같은 데이터에서도 둘은 다른 이웃을 내놓는다.
- **Personas: 크기가 아니라 방향으로 지갑을 클러스터링한다.** 온체인 행동 벡터로 지갑을 묶어 페르소나를 배정할 때는 코사인 유사도를 쓴다. 그래야 고래 지갑과 소액 지갑이 같은 행동 패턴이면 트랜잭션 수 규모로 갈리지 않고 같은 클러스터에 들어간다.
- **gitboard: "과거 비슷한 인시던트 찾기"에 코사인 유사도를 쓴다.** gitboard의 인시던트 이력에 대한 로그 검색 기능은 이 카드가 설명하는 임베딩 검색 사례 그대로다. 라이브러리 기본값을 쓰지 말고 노름을 의도적으로 선택한다.
