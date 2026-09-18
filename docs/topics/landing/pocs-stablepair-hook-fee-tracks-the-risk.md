## en
- **Token: give the JYVE mini-AMM a risk-tracking fee, not a fixed tier.** If any pool pairs JYVE against a stable asset, the same LVR problem applies — a low fee wins calm-day volume and a spiking fee protects LPs during a depeg-like move, so the fee needs to read pool state rather than sit at one constant.
- **Verex: treat a fixed spread or fee in the CLOB/LMSR path as the same wrong invariant.** The pattern this page names — a single constant that ignores the regime — is the identical bet as pricing risk with one number; make Verex's fee or spread a function of order-book imbalance or volatility before assuming a flat fee is safe.
- **DeFi: if the liquid-staking study ever routes through an AMM leg, reuse the hook pattern instead of a fixed pool fee.** A constant fee on a staked-asset pool fails the same two regimes — calm and stressed — so price the risk dynamically there too rather than copy a fixed-tier design.

## ko
- **Token: JYVE 미니 AMM에 고정 요율이 아니라 리스크를 추적하는 수수료를 준다.** JYVE가 스테이블 자산과 페어를 이루는 풀이 있다면 같은 LVR 문제가 적용된다. 평온할 때는 낮은 수수료가 거래량을 얻고, 디페그성 움직임에서는 치솟는 수수료가 LP를 보호해야 하므로 수수료는 상수가 아니라 풀 상태를 읽어야 한다.
- **Verex: CLOB/LMSR 경로의 고정 스프레드나 수수료도 같은 잘못된 불변량으로 취급한다.** 이 페이지가 지목하는 패턴 — 레짐을 무시하는 상수 하나 — 은 리스크를 숫자 하나로 가격 매기는 것과 동일한 베팅이다. 고정 수수료가 안전하다고 가정하기 전에 Verex의 수수료나 스프레드를 오더북 불균형이나 변동성의 함수로 만든다.
- **DeFi: 유동성 스테이킹 연구가 언젠가 AMM 레그를 거친다면 고정 풀 수수료 대신 이 훅 패턴을 재사용한다.** 스테이킹 자산 풀의 고정 수수료도 평온·스트레스 두 레짐에서 똑같이 실패하므로, 거기서도 리스크를 동적으로 가격 매긴다.
