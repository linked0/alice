| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| weights | 가중치(학습으로 얻은 모델 파라미터 값) · 로컬 모델 파일의 실체. "you download a model's weight file" |
| parameter (8B, 70B) | 파라미터(모델을 이루는 숫자 하나하나, B=billion) · 모델 크기·능력의 표기 단위. "a bigger parameter count (8B, 70B)" |
| quantization | 양자화(가중치의 수치 정밀도를 낮춰 압축하는 것) · 로컬 모델 배포의 핵심 기법. "trading a small, largely invisible quality loss" |
| Q4 / Q8 | 4비트/8비트 양자화 표기 · 파일 크기·품질의 트레이드오프 레벨. "Q4 roughly quarters the 16-bit size" |
| GGUF | llama.cpp가 정의한 로컬 모델 파일 포맷 이름(특정 확장 약어라기보다 llama.cpp 생태계의 고유 포맷명) · 로컬 배포 모델의 기본 컨테이너. "GGUF is the standard packaging format" |
| inference engine | 추론 엔진(가중치를 적재해 토큰을 생성하는 프로그램) · llama.cpp가 대표 사례. "loads the weights into memory and runs the matrix math" |
| forward pass | 순전파(입력을 모델에 통과시켜 출력을 얻는 한 번의 연산) · 추론 한 스텝을 가리키는 표준 용어. "runs a forward pass" |
| VRAM | Video RAM(GPU 전용 메모리, 시스템 RAM과 분리) · PC/Linux 로컬 추론의 1차 제약. "GPU VRAM specifically" |
| unified memory | 통합 메모리(CPU와 GPU가 공유하는 하나의 물리 메모리 풀) · Apple Silicon의 구조, 큰 모델 적재에 유리. "share one physical memory bank" |
| GPU | Graphics Processing Unit(그래픽 처리 장치) · 로컬 추론의 주 연산 하드웨어. "run inference on your own CPU or GPU" |
| CPU | Central Processing Unit(중앙 처리 장치) · GPU와 함께 추론 하드웨어를 이룸. "your own CPU or GPU" |
| bandwidth | 대역폭(단위 시간당 메모리에서 읽어올 수 있는 데이터량) · tokens/s 속도를 정하는 실제 병목. "memory bandwidth is the bottleneck" |
| KV cache | Key-Value 캐시(이전 토큰들의 키·값을 저장해 재계산을 피하는 메모리) · 컨텍스트가 길어질수록 커지는 추가 메모리. "a KV cache on top of the weights" |
| tokens/s | 초당 생성 토큰 수 · 추론 속도를 재는 표준 단위. "100-200 tokens/s in the video's numbers" |
| REST API | Representational State Transfer API(웹 표준 방식의 요청-응답 인터페이스) · Ollama가 노출하는 인터페이스 형태. "an OpenAI-compatible REST API" |
| HTTP server | HyperText Transfer Protocol 서버 · LM Studio가 로컬로 띄우는 개발용 엔드포인트. "runs a local HTTP server" |
| CLI | Command Line Interface(명령줄 인터페이스) · Ollama를 쓰는 방식(`ollama pull`, `ollama run`). "Ollama is the CLI path" |
| GUI | Graphical User Interface(그래픽 사용자 인터페이스) · LM Studio를 쓰는 방식. "LM Studio is the GUI path" |
| sweet spot | 최적점(투입 대비 효과가 가장 좋은 지점) · 32GB 구간을 부르는 말. "the sweet spot where perceived intelligence jumps the most" |
| rule of thumb | 경험칙(엄밀한 공식이 아닌 대략적인 지침) · 메모리-모델크기 가이드에 붙이는 라벨. "As a rule of thumb from the video" |
