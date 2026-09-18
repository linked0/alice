## en
- **Auditor: measure judge bias before trusting any LLM-judge score.** Before trusting an LLM-as-judge score on an agent's behavior or a dispute-summary bot, measure its length/position/self-preference bias first, and publish that meta-evaluation the way the Auditor row publishes what-was-checked-by-which-rule.
- **CI: build the small eval set and bias check as a CI artifact.** If any Jayverse agent behavior is ever gated by an LLM judge, keep the eval set and bias measurement versioned in CI, not a one-off script, so judge drift is caught like a test regression.

## ko
- **Auditor: LLM 심사자 점수를 신뢰하기 전에 편향을 측정한다.** 에이전트 행동이나 분쟁 요약 봇에 대한 LLM 심사 점수를 신뢰하기 전에, 그 길이·위치·자기선호 편향을 먼저 측정하고, Auditor 행이 "무엇을 어떤 규칙으로 확인했는지" 공개하는 방식 그대로 이 메타 평가도 공개한다.
- **CI: 소규모 평가셋과 편향 체크를 CI 산출물로 만든다.** Jayverse 에이전트 행동이 LLM 심사로 게이팅된다면, 평가셋과 편향 측정을 일회성 스크립트가 아니라 CI에서 버전 관리해, 테스트 회귀처럼 심사자 드리프트를 잡아낸다.
