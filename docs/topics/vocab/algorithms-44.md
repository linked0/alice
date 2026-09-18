| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| tail latency | 꼬리 지연, 분포의 극단(p99 등)에서의 응답 시간 · 평균이 아니라 최악 사례를 재는 지표. "Tail latency refers to response times in the tail" |
| fan out | 하나의 요청이 여러 곳으로 갈라져 나가다 · 여러 백엔드에 동시에 요청을 보낼 때. "a single request fans out to multiple backends" |
| amplify into | ~로 증폭되어 나타나다 · 작은 지연이 전체 지연으로 확대될 때. "gets amplified into a common delay" |
| hedged request | 헤지 요청, 이중으로 보내 지연에 대비하는 요청 · 첫 응답이 늦으면 두 번째를 추가로 보내는 기법. "A hedged request is a technique where..." |
| at the door | 들어오기 전 초입에서(비유) · 과부하 요청을 아예 받지 않고 거절할 때. "rejects them quickly at the door" |
| pile on top | 위에 겹쳐 쌓이다, 가중되다 · 재시도가 겹쳐 상황이 더 악화될 때. "collapses further once retries pile on top" |
| building blocks | 기본 구성 요소, 토대 · 가용성 설계의 핵심 기법들을 가리킬 때. "basic building blocks of availability design" |
