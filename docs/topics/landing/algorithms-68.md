## en
- **Verex: write a one-page failure-model doc per component — chain, oracle, sequencer/Devnet, backend — listing failure model, timing model, and trusted parties, and table which of safety or liveness breaks first for each.** Required before any settlement-dispute runbook exists.
- **Auditor: use that one-page doc as what gets checked during an incident — was the component's stated failure model actually the one that broke, or was an undocumented assumption violated instead.**
- **Rabbit: give session-key mandate execution (bundler/relayer) its own failure-model line — crash-stop, omission, or Byzantine — since a mandate's safety guarantee depends on which one actually holds.**

## ko
- **Verex: 체인, 오라클, 시퀀서/Devnet, 백엔드 각 컴포넌트별로 실패 모델, 타이밍 모델, 신뢰 주체를 적은 한 페이지 문서를 작성하고, 각 가정이 깨지면 안전성과 생존성 중 무엇이 먼저 무너지는지 표로 정리한다.** 정산 분쟁 대응 매뉴얼을 만들기 전에 반드시 필요하다.
- **Auditor: 이 한 페이지 문서를 인시던트 발생 시 체크리스트로 쓴다.** 실제로 깨진 것이 컴포넌트가 명시한 실패 모델인지, 아니면 문서화되지 않은 가정이 깨진 것인지 확인한다.
- **Rabbit: 세션 키 위임 실행(번들러/릴레이어)에도 자체 실패 모델 한 줄을 부여한다.** crash-stop인지, omission인지, Byzantine인지에 따라 위임의 안전성 보장이 달라진다.
