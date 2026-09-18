## en
- **Verex: model market-maker settlement funding as a waterfall contract.** If Verex ever advances a market maker or LP working capital against expected settlement receipts, repay principal and interest through a smart-contract waterfall before releasing any surplus, exactly as this PoC's mock issuer does.
- **DeFi: build the just-in-time credit-line variant as a jayverse-defi study.** Size a revolving line from observed throughput rather than posted collateral, and measure idle-capital cost against drawing exactly the shortfall at settlement time.
- **Devnet: test the three invariants on a local fork before any real design.** The credit line must never be drawn past its limit, the waterfall must always repay before releasing surplus, and a draw that misses the settlement deadline must surface as a visible failure, not a silent one.

## ko
- **Verex: 마켓메이커 정산 자금 조달을 워터폴 컨트랙트로 모델링한다.** Verex가 마켓메이커나 LP에게 예상 정산 수취분을 담보로 운전자금을 선지급한다면, 이 PoC의 모의 발행사처럼 잉여를 풀기 전에 스마트컨트랙트 워터폴로 원금과 이자를 먼저 상환한다.
- **DeFi: just-in-time 크레딧 라인 변형을 jayverse-defi 연구로 만든다.** 리볼빙 한도를 담보가 아니라 관측된 처리량으로 산정하고, 정산 시점에 정확히 부족분만 인출하는 방식과 유휴 자본 비용을 비교 측정한다.
- **Devnet: 실제 설계 전에 로컬 포크에서 세 가지 불변식을 테스트한다.** 크레딧 라인은 한도를 넘어 인출될 수 없고, 워터폴은 잉여 방출 전에 항상 먼저 상환하며, 정산 마감을 놓친 인출은 숨겨지지 않고 눈에 보이는 실패로 드러나야 한다.
