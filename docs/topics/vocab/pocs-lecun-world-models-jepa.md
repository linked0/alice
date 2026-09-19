| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| world model | 월드 모델(행동의 결과 상태를 예측하는 내부 모델) · 이 항목 전체의 핵심 개념. "World Models: Enabling the next AI revolution" |
| JEPA | Joint-Embedding Predictive Architecture(결합 임베딩 예측 아키텍처, 표현 공간에서 다음 상태를 예측하는 구조) · 르쿤의 핵심 제안. "predicting the next representation, not the next frame" |
| I-JEPA / V-JEPA | Image-JEPA / Video-JEPA(이미지·비디오에 적용한 JEPA 모델 계열) · 실제 발표된 Meta AI 논문 이름. "I-JEPA, V-JEPA and DINO" |
| EBM | Energy-Based Model(에너지 기반 모델, 에너지 함수를 최소화해 답을 고르는 프레임워크) · 르쿤의 오랜 프레이밍. "energy-based reasoning" |
| energy function | 에너지 함수(후보 답을 채점해 최소화 대상으로 삼는 비용 함수) · 계획을 최적화 문제로 바꾸는 장치. "minimizes an energy (cost) function" |
| guardrail | 가드레일(위반해서는 안 되는 안전 제약) · 프롬프트가 아니라 목적함수 안에 두어야 한다는 논지의 핵심어. "guardrails belong inside the objective, not in the prompt" |
| autoregressive | 자기회귀적(이전 출력을 입력 삼아 한 토큰씩 생성하는 방식) · LLM 디코딩 방식을 가리키는 표준 용어. "autoregressive token generation" |
| representation space | 표현 공간(원시 입력이 아니라 학습된 추상 벡터가 사는 공간) · 토큰 공간과 대비되는 개념. "think in an internal representation space" |
| grounded / grounding | 접지된 / 접지(언어가 아니라 실제 감각·물리 데이터에 뿌리내림) · 텍스트만으로는 부족하다는 논지의 핵심어. "physically-grounded adaptability" |
| Moravec's paradox | 모라벡의 역설(사람에게 쉬운 일이 기계엔 어렵고, 그 반대도 성립한다는 관찰) · 이 강연의 출발점. "machines are already better... while lacking the commonsense" |
| commonsense | 상식(명시적으로 가르치지 않아도 아는 물리적·일상적 지식) · AGI 논의의 핵심 결핍 대상. "physical common sense" |
| hierarchical planning | 계층적 계획(하위 목표를 먼저 세우고 단계별로 세분화하는 계획 방식) · 로보틱스 미해결 과제로 언급됨. "high-level sub-goals... decomposed step by step" |
| representation collapse | 표현 붕괴(인코더가 모든 입력을 같은 상수로 매핑해 오차를 0으로 만드는 실패 모드) · JEPA 학습의 핵심 위험. "map every input to the same constant vector" |
| information maximization | 정보 최대화(표현이 입력의 정보를 최대한 보존하도록 강제하는 원리) · 표현 붕괴를 막는 방법. "information-maximization terms" |
| SIGReg | Sketched Isotropic Gaussian Regularization(투영된 표현 분포를 등방성 가우시안에 가깝게 만드는 정규화 기법) · 르쿤 팀의 붕괴 방지 기법 이름. "SIGReg... pushes the distribution... toward an isotropic Gaussian" |
| isotropic Gaussian | 등방성 가우시안(모든 방향으로 분산이 같은 정규분포) · SIGReg가 목표로 삼는 분포 형태. "an isotropic Gaussian" |
| EMA distillation | 지수이동평균 증류(느리게 갱신되는 교사 모델에서 학생 모델로 지식을 옮기는 자기지도 학습 기법) · I-JEPA·V-JEPA·DINO 공통 기법. "EMA-based teacher-student distillation" |
| DINO / DINOv3 | 메타의 자기지도 비전 모델 계열(라벨 없이 이미지 표현을 학습) · V-JEPA와 비교 대상. "beats DINOv3" |
| AGI | Artificial General Intelligence(범용 인공지능, 특정 과제에 국한되지 않는 인간 수준 지능) · 텍스트만으로는 도달 불가하다는 주장의 목표 지점. "human-level physical intelligence" |
| RL | Reinforcement Learning(강화학습, 시행착오와 보상으로 학습하는 방식) · 표본 비효율성 때문에 우선순위를 낮추라고 제언됨. "sample-inefficient RL" |
| sample-inefficient | 표본 비효율적(원하는 성능에 도달하는 데 매우 많은 시행이 필요함) · RL의 한계를 지적하는 표현. "sample-inefficient RL" |
