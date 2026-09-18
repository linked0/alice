## en
- **Verex: state the valid range of the LMSR linear estimate.** When implementing the first-order price expansion for slippage/delta, document explicitly the order-size range where the linear estimate stays close to the true LMSR price.
- **Verex: add a test comparing the linear estimate against the true price as order size grows.** Catch the point where the approximation silently becomes wrong, instead of trusting the linearization past its valid range.
- **Auditor: require a centering point and error bound for every linearized formula.** Any place a nonlinear formula (fee curves, funding estimates) is swapped for a linear one needs both documented, not just the approximation itself.

## ko
- **Verex: LMSR 선형 추정치의 유효 범위를 명시한다.** 슬리피지/델타용 1차 가격 전개를 구현할 때, 선형 추정치가 실제 LMSR 가격에 가깝게 유지되는 주문 크기 범위를 명시적으로 문서화한다.
- **Verex: 주문 크기가 커질 때 선형 추정치와 실제 가격을 비교하는 테스트를 추가한다.** 유효 범위를 넘어선 선형화를 그냥 신뢰하는 대신, 근사치가 조용히 틀려지는 지점을 잡아낸다.
- **Auditor: 선형화된 모든 공식에 중심점과 오차 범위를 요구한다.** 비선형 공식(수수료 곡선, 펀딩 추정치)을 선형으로 바꾸는 모든 곳에서 근사치 자체뿐 아니라 이 둘을 문서화해야 한다.
