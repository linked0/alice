## en
- **Verex: use the gradient directly to quote exact slippage.** Since the LMSR price is the gradient of the cost function, compute exact slippage for a given order size before showing it in the UI, instead of approximating.
- **Verex: document the liquidity parameter b as a tradeoff, not a constant.** A larger b flattens the gradient (less slippage, less informative price movement) — write the b-selection rule down explicitly.
- **DeFi: run the same gradient-based sensitivity check on any future AMM curve.** Catch a curve that's too flat or too steep at the operating point before launch.

## ko
- **Verex: 그래디언트를 그대로 써서 정확한 슬리피지를 제시한다.** LMSR 가격이 비용 함수의 그래디언트이므로, 근사하지 말고 주어진 주문 크기에 대한 정확한 슬리피지를 계산해 UI에 보여준다.
- **Verex: 유동성 파라미터 b를 상수가 아니라 트레이드오프로 문서화한다.** b가 커지면 그래디언트가 평평해진다(슬리피지는 줄지만 가격 변화가 담는 정보는 준다). b 선택 규칙을 명시적으로 적어둔다.
- **DeFi: 향후 AMM 커브에도 같은 그래디언트 기반 민감도 체크를 실행한다.** 출시 전에 운영 지점에서 너무 평평하거나 너무 가파른 커브를 잡아낸다.
