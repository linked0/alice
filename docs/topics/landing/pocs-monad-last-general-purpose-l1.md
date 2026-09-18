## en
- **Verex: state which finality you quote.** If Verex or any resolution logic ever touches a chain with split ordering/execution finality (Monad's own gap), settlement code and the resolution field must name explicitly which finality it waits on, since resolution depends on the execution result, not just ordering.
- **Bridge/Token: report net, not gross.** When Token/Bridge dashboards show TVL or volume for the mini-AMM or the Anvil↔Sepolia bridge, compute deposits minus withdrawals as the net figure and flag any period covered by a liquidity-incentive program, the way Monad's gross/net split exposed a 3.9x recycling multiple.
- **DeFi/Devnet: watch for chain-level foreclosure.** Before building a liquid-staking feature in jayverse-defi, check whether devnet's own design (or a future L2's) could absorb the same job the app does, like Monad's precompiled staking crowding out LSTs, and design around that risk rather than assuming the app owns the category.
- **Auditor/Number: publish incentive-adjusted figures.** Any metric Number or the Auditor reports that overlaps a rewards or incentive period should carry the adjusted post-incentive number alongside the headline one, not just the raw total.

## ko
- **Verex: 어떤 파이널리티를 쓰는지 명시한다.** Verex나 정산 로직이 순서 파이널리티와 실행 파이널리티가 분리된 체인(Monad가 가진 바로 그 간극)에 닿는다면, 정산은 실행 결과에 의존하므로 정산 코드와 정산 필드는 어느 파이널리티를 기다리는지 명시해야 한다.
- **Bridge/Token: 총액이 아니라 순액을 보고한다.** Token/Bridge 대시보드가 미니 AMM이나 Anvil↔Sepolia 브리지의 TVL이나 거래량을 보여줄 때는 예치에서 인출을 뺀 순액을 계산하고 유동성 인센티브 프로그램이 걸린 기간은 표시한다. Monad의 총액/순액 구분이 3.9배 리사이클링 배수를 드러낸 것과 같은 이유다.
- **DeFi/Devnet: 체인 레벨의 잠식을 경계한다.** jayverse-defi에 리퀴드 스테이킹 기능을 만들기 전에 devnet 자체(또는 향후 L2)의 설계가 그 앱이 하는 일을 그대로 흡수할 수 있는지 확인한다. Monad의 프리컴파일 스테이킹이 LST를 밀어낸 것처럼, 앱이 그 카테고리를 당연히 소유한다고 가정하지 않고 이 위험을 감안해 설계한다.
- **Auditor/Number: 인센티브 조정 수치를 함께 공개한다.** Number나 Auditor가 보고하는 지표가 보상/인센티브 기간과 겹친다면, 원시 총액뿐 아니라 인센티브 종료 후로 조정한 수치도 함께 싣는다.
