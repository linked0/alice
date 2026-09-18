## en
- **Verex: set the market maker's liquidity/spread parameter as a KKT problem under an explicit max-loss cap.** Read the multiplier as the marginal value of relaxing that cap by one unit, so raising the cap becomes a priced decision instead of a guess.
- **DeFi: apply the same constrained-optimization shape to collateral/health-factor limits in the liquid-staking study.** The multiplier on the collateral constraint tells you exactly what one more unit of headroom is worth, which is the number a from-scratch DeFi project should be deriving anyway.
- **OFA: check which resource/gas constraints actually bind in the solver's fee schedule via complementary slackness.** A constraint with slack should carry a zero shadow price — if the fee schedule charges for a constraint that isn't binding, that's a bug the KKT conditions catch directly.

## ko
- **Verex: 마켓 메이커의 유동성/스프레드 파라미터를 명시적 최대 손실 상한 아래의 KKT 문제로 설정한다.** 승수를 그 상한을 한 단위 완화했을 때의 한계 가치로 읽으면, 상한을 올리는 것이 추측이 아니라 가격이 매겨진 결정이 된다.
- **DeFi: 유동 스테이킹 연구의 담보/건전성 한도에도 같은 제약 최적화 형태를 적용한다.** 담보 제약의 승수는 여유를 한 단위 더 확보하는 것의 정확한 가치를 알려준다. 이는 처음부터 만드는 DeFi 프로젝트가 어차피 도출해야 하는 숫자다.
- **OFA: 상보적 여유성으로 솔버 수수료 체계에서 실제로 묶이는 자원/가스 제약이 무엇인지 확인한다.** 여유가 있는 제약은 섀도 가격이 0이어야 한다. 수수료 체계가 묶이지 않은 제약에 대해 비용을 매긴다면 KKT 조건이 바로 잡아내는 버그다.
