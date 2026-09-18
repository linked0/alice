## en
- **Bridge/Token: test the redeem path as hard as the mint path.** The JYVE lock-and-mint bridge only pegs while both directions stay open; add a test that redeem still works when the Sepolia side looks "closed" (the AMC off-hours failure mode), not just the happy-path mint.
- **Wallet: show the loop's state, not just the balance.** The bridge screen should surface whether mint/redeem is currently open on both sides, since a premium on any wrapped Jayverse asset is a broken-plumbing signal to flag, not a gain to celebrate.
- **Number: keep any distributed reading issuer-led, not synthetic.** If a Number index is ever wrapped as a token, give holders the real claim and redemption right the data represents, matching the issuer-led model over Robinhood's consent-less synthetic structure.

## ko
- **Bridge/Token: redeem 경로도 mint 경로만큼 엄격히 테스트한다.** JYVE lock-and-mint 브리지는 양방향이 모두 열려 있을 때만 페그가 유지된다. Sepolia 쪽이 "닫힌" 것처럼 보일 때도(AMC의 장 마감 시간대 실패 사례) redeem이 동작하는지 테스트를 추가한다, mint만 되는 해피 패스가 아니라.
- **Wallet: 잔액이 아니라 루프의 상태를 보여준다.** 브리지 화면은 mint/redeem이 양쪽 모두에서 현재 열려 있는지를 노출해야 한다. 래핑된 Jayverse 자산에 프리미엄이 붙는 것은 축하할 이득이 아니라 배관이 고장났다는 신호이기 때문이다.
- **Number: 배포되는 읽기는 신세틱이 아니라 발행자 주도로 유지한다.** Number 지수가 토큰으로 감싸진다면 보유자에게 데이터가 나타내는 실제 청구권과 상환권을 준다. 동의 없는 신세틱 구조인 로빈후드 방식이 아니라 발행자 주도 모델을 따른다.
