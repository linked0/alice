## en
- **Bridge: name the relayer as the single prover, and require re-verification.** For the Anvil⇄Sepolia lock-and-mint bridge, one relayer computing state is exactly the "nobody re-executes" risk this PoC describes; require either a second independent relayer or a mandatory local re-check before minting.
- **Wallet: keep simulate-before-sign as re-execution, not proof-checking.** Never let the wallet accept a signed or relayed state without running its own local simulation first — that discipline is the re-execution side of this PoC's window/discount tradeoff.
- **Auditor: publish a shared-dependency list across services.** List which Jayverse services trust the same single relayer, oracle, or library, so a monoculture bug shows up as one line in the audit instead of three separate incidents.

## ko
- **Bridge: 릴레이어를 단일 프루버로 명명하고 재검증을 요구한다.** Anvil⇄Sepolia lock-and-mint 브리지에서 릴레이어 하나가 상태를 계산하는 것은 이 PoC가 말하는 "아무도 재실행하지 않는" 위험 그 자체다. 두 번째 독립 릴레이어나 민팅 전 필수 로컬 재검증 중 하나를 요구한다.
- **Wallet: simulate-before-sign을 프루프 검증이 아니라 재실행으로 유지한다.** 서명되거나 릴레이된 상태를 지갑이 자체 로컬 시뮬레이션 없이 받아들이게 두지 않는다. 이것이 이 PoC의 window/discount 트레이드오프에서 재실행 쪽에 해당하는 원칙이다.
- **Auditor: 서비스 간 공유 의존성 목록을 공개한다.** 어느 Jayverse 서비스들이 같은 릴레이어, 오라클, 라이브러리를 신뢰하는지 나열해, 모노컬처 버그가 세 건의 개별 사고가 아니라 감사 목록의 한 줄로 드러나게 한다.
