## en
- **Bridge: split what the Anvil⇄Sepolia bridge actually needs into addressing/routing, price/quote, liquidity/prefunding, and final settlement, and confirm which leg the relayer's ledger is really solving.** Most of the bridge's job is routing and messaging; only settlement atomicity genuinely needs the shared record.
- **Wallet: show prefunded liquidity or queue state on the bridge screen.** Atomic settlement without adequate prefunding is where a hub-style design breaks under contention, so surface that state rather than a spinner.
- **DeFi: when modeling cross-chain flows for the liquid-staking study, treat "which leg needs a shared ledger" as a design question to answer first.** Most of the workflow — addressing, FX/price discovery — doesn't require one.

## ko
- **Bridge: Anvil⇄Sepolia 브리지가 실제로 필요한 일을 주소/라우팅, 가격/견적, 유동성/사전자금, 최종 정산으로 나누고 릴레이어의 원장이 실제로 어느 구간을 해결하는지 확인한다.** 브리지 업무 대부분은 라우팅과 메시징이며, 공유 기록이 진짜 필요한 구간은 정산 원자성뿐이다.
- **Wallet: 브리지 화면에 사전자금 유동성이나 대기열 상태를 보여준다.** 충분한 사전자금 없는 원자적 정산은 허브형 설계가 경합 상황에서 무너지는 지점이므로, 로딩 스피너 대신 그 상태를 노출한다.
- **DeFi: 유동성 스테이킹 연구를 위한 크로스체인 흐름을 모델링할 때 "어느 구간에 공유 원장이 필요한가"를 먼저 답해야 할 설계 질문으로 다룬다.** 주소 지정이나 환율/가격 발견 같은 작업 대부분은 공유 원장이 필요 없다.
