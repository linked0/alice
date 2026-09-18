## en
- **CI: add a gas-snapshot check that diffs IR-level (Yul) output, not just gas totals, for Verex, Token and Bridge contracts.** A regression becomes traceable to what stopped folding rather than just a number moving.
- **Token: when tuning the mini-AMM or bridge contracts for gas, read the Yul/SSA dump before hand-optimizing Solidity.** This follows this page's own method for judging what survives at the IR level.
- **gitboard: surface a per-contract gas-cost trend on the dashboard.** An IR-level regression shows up before it reaches real gas costs.

## ko
- **CI: Verex, Token, Bridge 컨트랙트에 대해 가스 총량뿐 아니라 IR 레벨(Yul) 출력 자체를 비교하는 가스 스냅샷 체크를 추가한다.** 회귀가 발생했을 때 숫자가 움직였다는 사실이 아니라 무엇이 더 이상 접히지 않았는지까지 추적된다.
- **Token: mini-AMM이나 브리지 컨트랙트의 가스를 튜닝할 때, Solidity를 손으로 최적화하기 전에 Yul/SSA 덤프를 먼저 읽는다.** 이 페이지가 제시하는, IR 레벨에서 무엇이 살아남는지로 판단하는 방법 그대로다.
- **gitboard: 컨트랙트별 가스 비용 추세를 대시보드에 노출한다.** IR 레벨 회귀가 실제 가스 비용에 반영되기 전에 드러나게 한다.
