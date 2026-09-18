## en
- **OFA: choose the solver auction's payment rule deliberately, not by default.** A second-price rule removes solvers' need to guess competitors' bids, which matters more than revenue once the solver count is small.
- **Verex: for any liquidation auction, decide own-bid versus second-highest explicitly.** Revenue converges between formats only under the theorem's assumptions, so pick based on strategic robustness when a thin, correlated-value market might break them.
- **Devnet: run the PoC's Monte Carlo simulation on synthetic liquidation or solver data first.** Check whether revenue actually converges in Jayverse's real bidder-count regime before committing to a live auction format.

## ko
- **OFA: 솔버 경매의 지불 규칙을 기본값이 아니라 의도적으로 고른다.** second-price 규칙은 솔버가 경쟁자의 입찰을 추측할 필요를 없앤다. 솔버 수가 적을 때는 이게 수익보다 더 중요하다.
- **Verex: 청산 경매마다 own-bid냐 second-highest냐를 명시적으로 결정한다.** 두 방식의 수익 수렴은 정리의 가정 하에서만 성립하므로, 얇고 상관된 시장에서 가정이 깨질 수 있다면 전략적 견고함을 기준으로 고른다.
- **Devnet: 실제 경매 방식을 정하기 전에 이 PoC의 몬테카를로 시뮬레이션을 합성 청산·솔버 데이터로 먼저 돌려본다.** Jayverse 실제 입찰자 수 구간에서 수익이 정말 수렴하는지 확인한다.
