| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| physical prompting | 물리적 프롬프팅(시연 데이터를 가중치 업데이트 없이 컨텍스트로 넣는 방식) · 이 항목의 핵심 용어, LLM 프롬프팅의 로봇 버전. "The mechanism is what the video calls physical prompting" |
| in-context learning | 인컨텍스트 러닝(가중치 갱신 없이 프롬프트만으로 작업을 이해·수행) · LLM에서 온 개념을 로봇에 적용. "the LLM-style \"put it in the prompt\" trick" |
| context window | 컨텍스트 윈도우(모델이 한 번에 참조하는 입력 구간) · 시연 데이터가 들어가는 자리. "go straight into the model's context window" |
| few-shot | 퓨샷(예시 몇 개만으로 하는 프롬프팅) · 3~12초 시연이 여기 해당. "the same slot an LLM's few-shot prompt occupies" |
| fine-tuning | 파인튜닝(가중치를 새로 학습시켜 조정) · physical prompting과 대비되는 기존 방식. "instead of a separate long fine-tuning run" |
| gradient step | 그레이디언트 스텝(경사하강 1회 갱신) · 가중치가 실제로 필요한 경우의 비용 단위. "1-10 gradient steps as enough" |
| backpropagation | 역전파(오차를 거슬러 전달해 가중치를 갱신하는 알고리즘) · 파인튜닝의 내부 메커니즘. "No backpropagation happens for the task itself" |
| weight update | 가중치 업데이트 · physical prompting이 생략하는 단계. "no weight update for the task itself" |
| sim-to-real | 시뮬레이션에서 현실로의 전이 · 시뮬레이터에서 배운 행동이 실제 로봇에 통함. "a behavior prompted inside a simulator carries over to the physical robot" |
| human-to-robot (in-context learning) | 사람에서 로봇으로(맨손 시연을 로봇이 바로 모방) · 로봇 전용 시연 없이 되는 전이. "the robot hand imitate it immediately" |
| short-horizon (task) | 짧은 호흡의 작업(몇 초~몇 분 안에 끝나는 단위 작업) · 59% 수치가 측정된 작업 범주. "short-horizon manipulation tasks" |
| multimodal transformer | 멀티모달 트랜스포머(영상·센서·언어 등 여러 입력 종류를 함께 처리) · GEN-1.5의 아키텍처. "a large multimodal transformer" |
| proprioceptive | 고유수용성의(관절 각도·힘 등 몸 내부 감각) · 로봇 입력 신호의 한 종류. "sensor and proprioceptive signal" |
| 100Hz | 100헤르츠(초당 100회 갱신) · 행동 궤적 출력 주기, 실시간 제어에 필요한 빈도. "outputs robot action trajectories at 100Hz" |
| held-out | 홀드아웃(학습에 쓰지 않고 평가용으로 따로 뗀) · 성공률이 신뢰할 만하려면 필요한 조건. "a held-out, stated success rate" |
| long tail | 롱테일(빈도는 낮지만 종류가 매우 많은 항목들) · 개별 파인튜닝으로는 못 감당하는 소작업들. "the long tail of small household or warehouse tasks" |
| marginal cost | 한계비용(작업 하나를 더 추가할 때 드는 추가 비용) · 파인튜닝 대신 시연 하나로 줄어드는 비용. "the marginal cost of teaching a robot a new task" |
| highlight reel | 하이라이트 릴(가장 인상적인 장면만 모은 영상) · 평가가 아니라 마케팅일 수 있다는 경고의 대상. "a highlight reel of a robot swapping a banana" |
| success rate | 성공률 · 59%라는 이 항목의 핵심 검증 가능 수치. "a 59% average success rate" |
| foundation model | 파운데이션 모델(대규모 사전학습 후 다양한 작업에 범용으로 쓰는 모델) · Generalist AI가 만드는 것의 범주. "a robotics foundation-model startup" |
