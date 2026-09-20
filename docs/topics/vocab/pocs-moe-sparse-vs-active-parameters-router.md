| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| Mixture of Experts (MoE) | 여러 전문화된 서브 네트워크와 라우터로 구성된 아키텍처 · 이 항목 전체의 주제. "how MoE replaces a Transformer's dense feed-forward layer" |
| dense (model) | 밀집(모든 파라미터가 매 토큰에 활성화되는 모델) · sparse와 대비되는 기준 아키텍처. "A dense Transformer ties compute cost to total parameter count" |
| feed-forward network (FFN) | 피드포워드 네트워크(트랜스포머 블록에서 어텐션 다음에 오는 층) · MoE가 대체하는 대상. "a feed-forward network (FFN) that every token passes through" |
| router / gating (mechanism) | 라우터 / 게이팅(토큰마다 어느 전문가를 쓸지 정하는 장치) · MoE의 핵심 구성요소. "A gating mechanism, the router, decides" |
| logits | 로짓(softmax 이전의 원점수) · 분류·라우팅에서 공통으로 쓰는 용어. "producing logits H(x) = X · W" |
| softmax | 점수 벡터를 확률 분포로 바꾸는 함수 · 라우팅과 어텐션 모두에 쓰이는 재사용 가능한 도구. "A softmax turns these logits into a probability distribution" |
| top-K routing | 상위 K개만 선택하는 라우팅 방식 · 나머지는 마스킹되어 계산에서 빠짐. "In top-K routing, only the K highest-scoring experts keep a non-zero weight" |
| masked to −∞ | 음의 무한대로 마스킹(softmax 전에 로짓을 −∞로 만들어 확률을 0으로 만드는 방법) · top-K 구현의 표준 트릭. "every other expert's logit is masked to −∞" |
| load-balancing loss / auxiliary loss | 로드 밸런싱 손실 / 보조 손실(전문가 쏠림을 막는 학습 시 벌점 항) · Auditor 비유의 핵심. "an auxiliary load-balancing loss added to the training objective" |
| coefficient of variation | 변동 계수(표준편차/평균, 고르지 않음을 재는 지표) · 로드 밸런싱 손실 계산의 기반. "computed from the coefficient of variation... of routing probabilities" |
| rich get richer | 부익부(초기에 앞선 쪽이 계속 더 유리해지는 현상) · 로드 밸런싱이 막으려는 실패 모드를 부르는 관용구. "a 'rich get richer' failure" |
| expert capacity | 전문가 용량(한 배치에서 전문가가 받을 수 있는 토큰 수의 상한) · GPU 메모리를 고정 배정하기 위한 제약. "each expert gets a hard capacity limit" |
| capacity factor | 용량 계수(용량 공식의 배수 항) · Switch Transformer가 도입한 튜닝 파라미터. "C = (tokens / experts) × capacity factor" |
| token dropping | 토큰 드롭(용량 초과 시 토큰이 전문가 계산에서 빠지는 것) · 용량 제한의 직접적 결과. "overflow tokens either fall through... or bypass the FFN" |
| residual bypass | 잔차 우회(FFN을 건너뛰고 잔차 연결만 통과시키는 경로) · 드롭된 토큰의 대안 경로. "bypass the FFN entirely via a residual connection" |
| sparse parameters | sparse 파라미터(모델에 로드된 전체 파라미터 수, 쓰이든 안 쓰이든) · VRAM 요구량을 정하는 숫자. "'Sparse parameters'... is everything loaded into memory" |
| active parameters | active 파라미터(토큰 하나당 실제로 실행되는 파라미터 수) · 지연 시간과 FLOPs를 정하는 숫자. "'Active parameters' is what actually runs per token" |
| VRAM | 그래픽 메모리(모델 가중치를 올려두는 GPU 메모리) · sparse 파라미터 수가 정하는 제약. "VRAM sizing is governed by the sparse count" |
| FLOPs | 초당 부동소수점 연산 수(연산량의 표준 단위) · active 파라미터 수가 정하는 비용. "inference latency and FLOPs are governed by the active count" |
| routing entropy | 라우팅 엔트로피(라우터가 전문가들에 얼마나 고르게 분산해서 배정하는지 재는 지표) · 학습 중 모니터링 대상. "one reason routing entropy is worth monitoring" |
| Soft-MoE | 소프트 MoE(비전 트랜스포머용 MoE 변형, 이미지 패치를 라우팅) · 텍스트 밖으로의 확장 사례. "Soft-MoE applies the same idea to Vision Transformers" |
