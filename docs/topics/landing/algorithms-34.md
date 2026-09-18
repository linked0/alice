## en
- **Verex: write the invariant test this week, not just the property.** Add the Foundry invariant "sum of outcome-slot balances ≤ collateral" to the Conditional Tokens path now, then run the same property through Halmos with an explicit bound (market count, loop-unrolling depth) written into the test file itself.
- **DeFi: give liquid-staking accounting the same conservation invariant.** "Total shares priced ≤ total assets held" is the EtherFi-style equivalent of Verex's collateral check — add it as a Foundry invariant before any devnet deploy of the staking contracts.
- **Bridge: state the lock-mint conservation invariant and its bound.** "Locked amount on Anvil equals minted amount on Sepolia" is the bridge's version of the same property — write it as a Foundry invariant first, and once the contract is small enough, check it with Halmos under a stated bound.

## ko
- **Verex: 속성뿐 아니라 인바리언트 테스트를 이번 주에 작성한다.** "각 조건의 결과 슬롯 잔액 합 ≤ 담보"라는 Foundry 인바리언트를 Conditional Tokens 경로에 지금 추가하고, 같은 속성을 Halmos로도 돌리되 테스트 파일 안에 명시적 경계(마켓 수, 루프 언롤링 깊이)를 적어둔다.
- **DeFi: 유동성 스테이킹 회계에도 같은 보존 인바리언트를 적용한다.** "가격이 매겨진 총 지분 ≤ 보유 총자산"이 EtherFi식 스테이킹에서 Verex 담보 체크에 대응하는 값이다. devnet에 스테이킹 컨트랙트를 배포하기 전에 Foundry 인바리언트로 추가한다.
- **Bridge: lock-mint 보존 인바리언트와 그 경계를 명시한다.** "Anvil에서 잠긴 양 = Sepolia에서 발행된 양"이 브릿지 버전의 같은 속성이다. 먼저 Foundry 인바리언트로 적고, 컨트랙트가 충분히 작아지면 명시된 경계 아래 Halmos로도 확인한다.
