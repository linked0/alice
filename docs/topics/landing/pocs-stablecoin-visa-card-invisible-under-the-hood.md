## en
- **Wallet: the bridge screen should feel like a balance, not a rail.** Follow the card's seam — convert only at the moment of action — so a user moving value between Anvil and Sepolia sees one balance and a single confirm, not chain names, gas, or the lock-and-mint mechanics underneath.
- **Token/Exchange: if JYVE is ever spendable outside the mini-AMM, keep it off the "merchant" layer entirely.** Any future payment integration should convert JYVE to whatever the counterpart expects at authorization time only, the same seam that keeps Visa and the merchant from ever touching the stablecoin.
- **Bridge: name each party's one job, the way the card names issuer, program manager and FX provider.** Write down, per hop of the lock-and-mint path, which party (relayer, Anvil contract, Sepolia contract) is trusted for which single fact — this becomes the Auditor's methodology note for the bridge.

## ko
- **Wallet: 브리지 화면은 레일이 아니라 잔액처럼 느껴져야 한다.** 카드의 이음매 원칙을 따라 행동하는 순간에만 변환하면, Anvil과 Sepolia 사이에서 가치를 옮기는 사용자는 체인 이름이나 가스, 그 아래의 락앤민트 메커니즘이 아니라 잔액 하나와 확인 버튼 하나만 본다.
- **Token/Exchange: JYVE가 미니 AMM 밖에서 사용 가능해지더라도 "가맹점" 계층에서는 완전히 떼어놓는다.** 향후 결제 연동은 인가 시점에만 JYVE를 상대방이 기대하는 자산으로 변환해야 한다. Visa와 가맹점이 스테이블코인을 절대 만지지 않게 하는 것과 같은 이음매다.
- **Bridge: 카드가 발행사, 프로그램 매니저, FX 제공자를 각각 명명하듯 각 주체의 역할 하나씩을 명확히 한다.** 락앤민트 경로의 각 홉마다 어느 주체(릴레이어, Anvil 컨트랙트, Sepolia 컨트랙트)가 어떤 단일 사실에 대해 신뢰받는지 적어둔다. 이것이 브리지에 대한 Auditor의 방법론 노트가 된다.
