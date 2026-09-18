## en
- **Rabbit: attribute every sponsored UserOp before shipping gasless UX.** Record `{user, action, gasUsed, costWei, timestamp}` on each sponsored operation from day one, not as a retrofit once the paymaster is already live.
- **gitboard: add sponsored gas as a live COGS tile against a daily budget.** The service dashboard should show cumulative sponsorship spend per service with a kill line, since an unmetered paymaster is a bill someone else writes.
- **Wallet: cap and degrade instead of block, then red-team it.** Ship a per-user daily sponsored-op cap that drops the user to pay-your-own-gas, and test it with a bot spinning up fresh wallets to chart minutes-to-budget-death before launch.

## ko
- **Rabbit: gasless UX를 배포하기 전에 모든 후원 UserOp에 귀속 정보를 남긴다.** paymaster가 이미 라이브가 된 뒤 나중에 추가하는 게 아니라 처음부터 후원된 각 작업에 `{user, action, gasUsed, costWei, timestamp}`를 기록한다.
- **gitboard: 후원 가스를 일일 예산 대비 실시간 COGS 타일로 추가한다.** 서비스 대시보드는 서비스별 누적 후원 지출을 킬라인과 함께 보여줘야 한다. 미터링되지 않은 paymaster는 남이 대신 써주는 청구서이기 때문이다.
- **Wallet: 차단이 아니라 사용자당 캡으로 낮추고, 레드팀으로 검증한다.** 사용자당 일일 후원 작업 캡을 두어 초과 시 본인 부담 가스로 전환시키고, 출시 전 신규 지갑을 대량 생성하는 봇으로 예산 소진까지 걸리는 시간을 측정한다.
