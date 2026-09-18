## en
- **Verex/DeFi contracts: treat "stack too deep" as a spill-cost problem.** When a Solidity function hits the limit, shrink live ranges or split the function first, rather than reflexively raising the optimizer's aggressiveness, since the quality-versus-compile-time trade-off is the same one the card describes.
- **CI: lint for functions approaching the stack limit before they fail.** Add a check across Verex, DeFi and Bridge contracts that flags functions with many simultaneously-live locals, since that is the same interference-graph pressure that eventually forces a spill.
- **Auditor: review optimizer-flag changes as a quality-vs-speed decision, not a default toggle.** When a contract needs -O2-equivalent settings to compile, record why, the same way the card frames allocation quality against compile time.

## ko
- **Verex/DeFi 컨트랙트: "stack too deep"를 스필 비용 문제로 취급한다.** Solidity 함수가 한계에 부딪히면 옵티마이저 강도를 반사적으로 올리기보다 먼저 라이브 레인지를 줄이거나 함수를 쪼갠다. 배분 품질과 컴파일 시간의 트레이드오프는 카드가 설명하는 것과 같다.
- **CI: 스택 한계에 근접한 함수를 실패하기 전에 린트로 잡는다.** Verex, DeFi, Bridge 컨트랙트 전체에서 동시에 살아있는 로컬 변수가 많은 함수를 표시하는 체크를 추가한다. 결국 스필을 강제하는 것과 같은 간섭 그래프 압력이기 때문이다.
- **Auditor: 옵티마이저 플래그 변경을 기본 토글이 아니라 품질-대-속도 결정으로 검토한다.** 어떤 컨트랙트가 -O2급 설정 없이는 컴파일되지 않는다면 그 이유를 기록한다. 카드가 배분 품질과 컴파일 시간을 나란히 놓는 방식과 같다.
