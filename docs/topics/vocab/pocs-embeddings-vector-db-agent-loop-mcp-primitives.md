| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| embedding | 임베딩(텍스트·코드·이미지를 벡터로 투영한 것) · 의미 검색의 기본 단위. "project text, code and images into 768–1536-dimension vectors" |
| vector database | 벡터 데이터베이스(임베딩을 저장하고 유사도로 검색하는 저장소) · 의미 검색 인프라의 핵심. "production vector databases use approximate nearest-neighbor (ANN) indexes" |
| cosine similarity | 코사인 유사도(두 벡터 사이 각도로 재는 유사도) · 임베딩 비교의 표준 지표 중 하나. "cosine similarity, dot product or Euclidean distance" |
| dot product | 내적(두 벡터 성분을 곱해 더한 값) · 코사인 유사도와 함께 쓰는 유사도 계산법. "cosine similarity, dot product or Euclidean distance" |
| Euclidean distance | 유클리드 거리(두 점 사이 직선 거리) · 벡터 공간에서의 근접성 측정법. "cosine similarity, dot product or Euclidean distance" |
| ANN (Approximate Nearest Neighbor) | 근사 최근접 이웃(정확도를 약간 포기하고 빠르게 찾는 탐색) · O(N) 전수 탐색의 대안. "approximate nearest-neighbor (ANN) indexes" |
| HNSW | Hierarchical Navigable Small World(계층형 항해 가능 소세계 그래프, ANN 인덱스 알고리즘) · 다층 그래프로 빠르게 근접 벡터를 찾는 방식. "HNSW graphs or IVF" |
| IVF | Inverted File index(역파일 인덱스, ANN 인덱스 알고리즘) · 벡터 공간을 클러스터로 나눠 탐색 범위를 줄이는 기법, FAISS의 핵심. "HNSW graphs or IVF" |
| FAISS | Facebook AI Similarity Search(Meta가 만든 벡터 유사도 검색 라이브러리) · IVF 같은 기법이 구현된 원조 라이브러리. "the technique behind Meta's FAISS library" |
| O(N) | 빅오 표기법으로 입력 크기 N에 비례하는 계산량 · 전수 탐색(브루트포스)의 시간 복잡도. "an O(N) brute-force scan" |
| agent loop | 에이전트 루프(관찰-추론-디스패치-실행을 반복하는 구조) · LLM을 자율 에이전트로 만드는 핵심 구조. "observe, reason, dispatch a structured JSON tool call" |
| tool dispatch | 도구 디스패치(어떤 도구를 어떤 인자로 호출할지 내보내는 단계) · 에이전트 루프의 한 단계. "dispatch a structured JSON tool call" |
| JSON payload | JSON 페이로드(도구 호출에 실어 보내는 구조화된 데이터) · 도구 호출의 구체적 형태. "a structured JSON payload naming a specific tool" |
| MCP | Model Context Protocol(모델 컨텍스트 프로토콜, Anthropic이 만든 에이전트-도구 연결 표준) · 이 항목의 핵심 주제. "Anthropic's Model Context Protocol (MCP)" |
| M×N problem | M곱N 문제(도구 M개와 모델 N개마다 각자 연결 코드가 필요해지는 조합 폭발) · MCP가 풀려는 문제. "an M×N problem that stops scaling" |
| LSP | Language Server Protocol(언어 서버 프로토콜, IDE와 언어 분석기를 표준으로 연결하는 프로토콜) · MCP가 스스로 드는 비유. "the Language Server Protocol in IDEs" |
| authorization boundary | 권한 경계(자격 증명과 접근 범위를 가르는 선) · 프롬프트 밖에 자격 증명을 두는 안전장치. "MCP's authorization boundary" |
| harness engineering | 하니스 엔지니어링(에이전트를 감싸는 실행·검증 장치를 설계하는 일) · 루프의 검증 문제와 직결된 개념. "the harness-and-eval half of the problem" |
| eval | 이밸류에이션(모델·에이전트 성능을 체계적으로 측정하는 평가) · 검증이 실제로 이루어지는지 확인하는 절차. "the harness-and-eval half of the problem" |
| galaxy-brain risk | (비유) 지나치게 자기 확신에 빠진 추론의 위험 · 검증자가 없는 루프의 극단적 실패, 자기 채점 에이전트를 가리키는 표현. "an agent that grades its own homework" |
