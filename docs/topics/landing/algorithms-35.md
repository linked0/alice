## en
- **CI: add a gas-regression bisector as a build step.** When gas usage changes on a Verex or Wallet contract diff, use this stage map to bucket it — compiler/optimizer settings, EVM opcode pricing, or contract logic — before treating it as a real regression.
- **Verex: pin the Solidity optimizer settings in CI, next to the frozen lockfiles.** A silent optimizer-run-count or via-IR change is indistinguishable from a logic change in a raw gas diff, so pin it explicitly.
- **gitboard: track per-contract gas-per-function over time as a dashboard series.** Catch a regression at the stage that caused it, not just as "gas went up."

## ko
- **CI: 가스 회귀 원인 분리 단계를 빌드에 추가한다.** Verex나 Wallet 컨트랙트 diff에서 가스 사용량이 바뀌면, 이 단계 지도를 이용해 컴파일러/옵티마이저 설정인지, EVM 옵코드 가격 변화인지, 컨트랙트 로직 변경인지 먼저 분류한 뒤에야 실제 회귀로 취급한다.
- **Verex: Solidity 옵티마이저 설정을 고정 lockfile 옆에 CI에서 고정한다.** 옵티마이저 실행 횟수나 via-IR 설정이 조용히 바뀌면 원시 가스 diff에서는 로직 변경과 구분이 안 되므로 명시적으로 고정한다.
- **gitboard: 컨트랙트별 함수당 가스를 시계열로 대시보드에 추적한다.** "가스가 올랐다"는 것만 알아채는 게 아니라 회귀를 일으킨 단계를 바로 짚어낸다.
