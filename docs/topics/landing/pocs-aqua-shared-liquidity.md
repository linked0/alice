## en
- **Verex: log fillable depth, not just quoted depth.** Instrument the LMSR quote centers so realized fill rate is tracked against advertised depth, especially in the minutes before an event resolves when demand concentrates.
- **Verex: keep LMSR as the default b-bounded maker.** Prediction-market takers need fill certainty, so if a CLOB layer with withdrawable LP balances is ever added, require a bond or reputation penalty for high-revert quoters, or the honest strategy becomes quote wide and pull.
- **Wallet: flag standing allowances as a distinct risk class.** Simulate-before-sign should warn on approve-and-pull style long-lived allowances differently from one-shot signatures or session-key grants, since the leaked right and the cost to revoke differ.
- **Devnet: build the liquidity-stress fixture.** Reuse the PoC's anvil test — one balance backing three positions quoting 3x, swept to 10% of depth — as a reusable fixture for any future AMM/CLOB hybrid before it ships.

## ko
- **Verex: 체결 가능 깊이를 로그로 남긴다, 호가 깊이만이 아니라.** LMSR 퀘이트 센터를 계측해서 실제 체결률을 광고된 깊이 대비 추적한다, 특히 이벤트 정산 직전 수요가 몰리는 시점에.
- **Verex: 기본 메이커는 b로 제한된 LMSR을 유지한다.** 예측 마켓의 테이커는 체결 확실성이 필요하므로, LP 잔고를 인출 가능한 CLOB 레이어를 추가한다면 리버트율이 높은 메이커에게 보증금이나 평판 페널티를 요구해야 한다, 아니면 넓게 호가하고 위험할 때 빼는 전략이 지배적이 된다.
- **Wallet: 상시 허용량을 별도 위험군으로 표시한다.** simulate-before-sign은 approve-and-pull 방식의 장기 허용량을 일회성 서명이나 세션 키 부여와 다르게 경고해야 한다, 노출되는 권리와 철회 비용이 다르기 때문이다.
- **Devnet: 유동성 스트레스 픽스처를 만든다.** PoC의 anvil 테스트를 재사용한다 — 하나의 잔고가 3배 호가하는 세 포지션을 지원하고 깊이의 10%까지 쓸어내리는 테스트 — 향후 어떤 AMM/CLOB 하이브리드에도 출시 전 재사용 가능한 픽스처로.
