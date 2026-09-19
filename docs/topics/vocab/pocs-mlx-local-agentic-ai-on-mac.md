| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| MLX | Machine Learning eXchange(Apple의 Apple Silicon용 오픈소스 어레이 프레임워크) · 스택의 최하단 계층. "MLX, the open-source array framework Apple built for Apple Silicon" |
| mlx-lm | MLX 위의 언어모델 CLI·Python API(로드·양자화·LoRA 파인튜닝·서버 실행) · 스택의 모델 계층. "mlx-lm, a CLI and Python API on top of it" |
| CLI | Command-Line Interface(명령줄 인터페이스) · mlx-lm과 `gh`, `xcodebuild`를 부르는 방식. "a CLI and Python API on top of it" |
| API | Application Programming Interface(응용 프로그램 프로그래밍 인터페이스) · Python API, OpenAI Chat Completions API 모두 이 뜻. "a CLI and Python API" |
| HTTP | HyperText Transfer Protocol(하이퍼텍스트 전송 프로토콜) · mlx-lm 서버가 여는 프로토콜. "an mlx-lm HTTP server" |
| OpenAI-compatible | OpenAI Chat Completions 규격과 호환됨 · 에이전트를 무수정으로 붙일 수 있게 하는 핵심 표면. "any agent that already speaks that format" |
| tool calling | 툴 콜(모델이 외부 함수·명령을 호출하도록 구조화된 출력을 내는 방식) · 에이전트 루프의 핵심 기능. "structured tool calling and reasoning models" |
| reasoning model | 추론 모델(중간 사고 과정을 거치는 모델 부류) · mlx-lm 서버가 지원하는 모델 종류. "structured tool calling and reasoning models" |
| LoRA | Low-Rank Adaptation(저순위 적응, 가벼운 파인튜닝 기법) · mlx-lm이 지원하는 파인튜닝 방식. "quantizing, and LoRA-fine-tuning models" |
| quantization | 양자화(모델 가중치를 더 적은 비트로 압축해 메모리를 줄이는 기법) · 로컬에서 큰 모델을 돌리기 위한 전제조건. "quantize it to fit in memory" |
| unified memory | 통합 메모리(CPU와 GPU가 복사 없이 공유하는 메모리 풀) · MLX·Apple Silicon의 핵심 이점. "unified memory management" |
| prefill | 프리필(프롬프트 전체를 모델에 통과시켜 컨텍스트를 읽어들이는 연산 단계) · 에이전트 워크로드의 실제 병목. "reading that accumulated context back in (prefill)" |
| decode | 디코드(새 토큰을 한 개씩 생성하는 단계) · prefill과 대비되는 개념, 채팅 워크로드의 병목. "Generating new tokens (decode) was never the bottleneck" |
| GPU | Graphics Processing Unit(그래픽 처리 장치) · MLX의 Metal 가속과 continuous batching이 겨냥하는 하드웨어. "the GPU dynamically group their requests" |
| continuous batching | 연속 배칭(여러 요청을 대기열 없이 GPU에서 동적으로 묶어 처리하는 서빙 기법) · 가속 셋의 두 번째 항목. "Continuous batching lets the GPU dynamically group their requests" |
| RDMA | Remote Direct Memory Access(원격 직접 메모리 접근, 커널을 거치지 않는 고속·저지연 전송) · Thunderbolt로 여러 Mac을 묶는 분산 추론의 기반. "RDMA over Thunderbolt" |
| node | 노드(분산 시스템을 구성하는 개별 머신) · 4노드/3배 수치의 단위. "up to roughly 3x at four nodes" |
| PR | Pull Request(코드 변경 병합 요청) · 첫 번째 데모의 대상. "reading a GitHub PR diff via the `gh` CLI" |
| IDE | Integrated Development Environment(통합 개발 환경) · Xcode를 가리키는 일반 용어, 세 번째 데모의 무대. "to diagnose and patch a bug inside the IDE" |
| MNPI | Material Non-Public Information(중요 비공개 정보) · Rabbit 랜딩에서 로컬 전용이어야 하는 데이터의 성격을 빗댄 표현. "mandates and key material are the MNPI case for local-only" |
| base URL | 베이스 URL(API 호출이 향하는 엔드포인트 주소) · 호스티드 모델에서 로컬 모델로 바꿀 때 실제로 바뀌는 유일한 것. "a base-URL change, not a rewrite" |
