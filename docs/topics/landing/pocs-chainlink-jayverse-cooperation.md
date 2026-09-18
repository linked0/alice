## en
- **Rabbit: evaluate Chainlink Automation for triggering scheduled intents or mandates instead of a server timer.** This carries the same "a missed tick delays settlement" risk this page names for schedulers.
- **gitboard: surface feed staleness and liveness as a monitored dashboard row, not only a contract-level check.** Data Feeds heartbeat, later CCIP message status — so a stale price is visible before it causes a wrong resolution.
- **CI: add a regression test asserting the JYVE pricing path never calls a Chainlink feed.** This guards the deliberate non-use decision against an accidental future wiring.

## ko
- **Rabbit: 예약된 Rabbit intent나 mandate를 서버 타이머 대신 Chainlink Automation으로 트리거하는 방안을 검토한다.** 이 페이지가 스케줄러에 대해 말한 "틱을 놓치면 정산이 지연된다"는 위험이 동일하게 적용된다.
- **gitboard: 피드의 stale 여부와 생존 여부를 컨트랙트 레벨 점검뿐 아니라 대시보드 모니터링 행으로도 노출한다.** Data Feeds 하트비트, 이후 CCIP 메시지 상태를 대상으로 하며, 그래야 잘못된 정산이 나기 전에 오래된 가격이 눈에 띈다.
- **CI: JYVE 가격 결정 경로가 Chainlink 피드를 절대 호출하지 않는지 확인하는 회귀 테스트를 추가한다.** 오라클을 쓰지 않기로 한 결정이 훗날 실수로 연결되지 않도록 지킨다.
