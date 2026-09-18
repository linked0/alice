## en
- **Rabbit: classify its own AA dependencies as function or operation.** Bundler and paymaster services Rabbit relies on for ERC-4337/EIP-7702 are exactly the middleware this page describes — track which EIP (8141/8130) would absorb them and don't build a business assumption on a moat with a scheduled expiry.
- **Devnet: budget for the enshrinement timeline, not the announcement.** When planning the move to an OP-Stack L2, treat any middleware Rabbit or Verex depends on (relayers, bundlers) as renting a feature until its absorbing fork ships, and track ACDE status as the signal for when to stop renting.
- **gitboard: add a column for "middleware expiry."** For any external service the stack depends on for a feature rather than an operation, gitboard should note the absorbing proposal and its status, so a dependency's obsolescence is visible before it breaks something.

## ko
- **Rabbit: 자신의 AA 의존성을 기능인지 운영인지로 분류한다.** Rabbit이 ERC-4337/EIP-7702에 쓰는 번들러와 페이마스터는 바로 이 미들웨어이며, 어느 EIP(8141/8130)가 이를 흡수할지 추적하고 만기가 정해진 모트 위에 사업 가정을 쌓지 않는다.
- **Devnet: 발표가 아니라 흡수 시점을 기준으로 예산을 짠다.** Devnet이 OP-Stack L2로 넘어갈 때, Rabbit이나 Verex가 의존하는 릴레이어나 번들러 같은 미들웨어를 흡수 포크가 나올 때까지 빌리는 것으로 취급하고, ACDE 상태를 대여를 멈출 신호로 추적한다.
- **gitboard: "미들웨어 만기" 칼럼을 추가한다.** 운영이 아니라 기능 때문에 의존하는 외부 서비스마다 흡수 제안과 그 상태를 gitboard에 표시해, 의존성의 폐기가 문제를 일으키기 전에 보이게 한다.
