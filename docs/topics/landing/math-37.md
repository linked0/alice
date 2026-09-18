## en
- **Verex: compute a Hoeffding-based minimum sample size before trusting a simulated fill-rate or latency number from the CLOB backtest.** Log the confidence level next to any published dev metric, and drop the guarantee the moment samples aren't independent (same block, correlated fills).
- **OFA: size the number of auction rounds needed before trusting a "solver X wins Y% of the time" claim, using the Hoeffding bound since outcomes are bounded.** Flag it void when rounds share a solver or a block, since that breaks independence.
- **Number: state the sample size behind any published indicator backtest in Hoeffding terms.** Add it as a field on the reading so a reader can tell over-fit noise from a genuine edge.

## ko
- **Verex: CLOB 백테스트의 시뮬레이션 체결률이나 지연시간 숫자를 신뢰하기 전에 Hoeffding 기반 최소 표본 크기를 계산한다.** 발행하는 개발 지표 옆에 신뢰수준을 함께 기록하고, 표본이 독립적이지 않은 순간(같은 블록, 상관된 체결) 그 보장을 폐기한다.
- **OFA: "솔버 X가 Y%의 확률로 이긴다"는 주장을 믿기 전에 필요한 경매 라운드 수를 Hoeffding 경계로 산정한다.** 결과가 유계이기 때문에 이 경계를 쓸 수 있다. 라운드가 같은 솔버나 같은 블록을 공유하면 독립성이 깨지므로 무효로 표시한다.
- **Number: 발행하는 모든 지표 백테스트의 표본 크기를 Hoeffding 식 용어로 명시한다.** 읽기 객체에 필드로 추가해서 독자가 과적합 노이즈와 진짜 엣지를 구분할 수 있게 한다.
