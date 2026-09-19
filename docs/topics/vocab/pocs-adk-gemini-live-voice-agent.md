| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| STT | Speech-to-Text(음성을 텍스트로 변환) · 옛 파이프라인의 첫 단계. "speech-to-text, then an LLM call, then text-to-speech" |
| LLM | Large Language Model(대형 언어 모델) · 파이프라인의 가운데 단계, 추론을 맡는 부분. "then an LLM call" |
| TTS | Text-to-Speech(텍스트를 음성으로 변환) · 옛 파이프라인의 마지막 단계. "text-to-speech" |
| ADK | Agent Development Kit(구글의 에이전트 개발 키트) · Agent·Runner·Session 개념을 제공하는 오픈소스 파이썬 프레임워크. "Google's Agent Development Kit (ADK) supplies the plumbing" |
| VAD | Voice Activity Detection(음성 활동 감지) · 침묵 속에서 문장의 끝을 인식하는 기능, `send_realtime`이 계속 오디오를 보내야 하는 이유. "Gemini's own voice-activity detection (VAD)" |
| WebSocket | 웹소켓(브라우저와 서버 사이 상시 양방향 연결 프로토콜) · 음성 스트림을 나르는 표준 전송 수단. "keeps one always-open WebSocket to the backend" |
| barge-in | 말 끼어들기(상대가 말하는 도중에 끼어드는 것) · 전화 통화형 설계가 지원해야 하는 핵심 기능. "the user cutting the agent off mid-sentence" |
| turn-taking | 발화 순서 교대(대화에서 말할 차례를 주고받는 것) · 파이프라인이 아니라 열린 스트림이 필요한 이유. "a live turn-taking loop" |
| in-memory (session) | 인메모리(디스크·네트워크 없이 메모리에 상태를 두는 방식) · 원격 세션 저장소의 네트워크 I/O를 피해 지연을 줄이는 선택. "in-memory session storage is what keeps the round trip fast" |
| LiveRequestQueue | ADK의 실시간 요청 큐(송신·수신을 분리하는 큐 객체) · 업스트림과 다운스트림을 잇는 핵심 구조. "one async task keeps pushing browser audio chunks onto the LiveRequestQueue" |
| send_realtime | 연속 스트림 입력 함수(끝이 없는 데이터, 예: 마이크용) · 침묵 구간도 계속 보내야 VAD가 작동. "send_realtime is for an open-ended continuous stream" |
| send_content | 완성된 단일 입력 함수(사용자가 전송을 명시적으로 끝낸 데이터용) · 타이핑 텍스트·이미지 등에 사용. "send_content is for a single, already-complete piece of data" |
| upstream / downstream | 업스트림(보내는 방향) / 다운스트림(받는 방향) · 큐로 분리된 두 비동기 작업을 가리키는 말. "one async task... (upstream); a separate task... (downstream)" |
| non-blocking | 논블로킹(한쪽 작업이 다른 쪽을 막지 않는 방식) · ADK 층이 스트림을 중계하는 방식. "relays the bidirectional stream... without blocking on either side" |
| Interrupted event | 인터럽트 이벤트(사용자가 끼어들었을 때 모델이 내려보내는 신호) · 백엔드가 즉시 재생을 멈춰야 하는 신호. "the Live API sends down an Interrupted event" |
| persona | 페르소나(에이전트의 성격·지침 설정) · Agent 객체를 구성하는 세 요소 중 하나. "model, persona/instructions, and capabilities" |
| hard floor (on latency) | 지연의 바닥값(더 줄일 수 없는 최소 대기 시간) · 순차 구조 자체가 만드는 한계를 설명하는 표현. "A sequential pipeline puts a hard floor on latency" |
| gated step | 문지기 단계(앞 단계가 끝나야만 다음이 시작되는 구조) · 파이프라인의 근본적 결함을 가리키는 말. "three gated steps" |
| dispatch (on event type) | 타입별로 분기 처리하다 · 이벤트 스트림을 재생·자막·함수 호출로 나눠 처리하는 방식. "the app dispatches on event type" |
