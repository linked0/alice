## en
- **Verex: give every fiat-priced order or Stripe onboarding quote a TTL and a visible re-quote flow.** Decide the drift policy explicitly (merchant absorbs, buyer absorbs, or a band with re-quote) instead of letting it fall out of whichever code path shipped first.
- **Wallet/Bridge: any displayed amount that can move before settlement needs an expiresAt.** A bridge conversion or a balance shown mid-transfer is the same short-dated option as the checkout — show the countdown and a one-click re-quote rather than a silently stale number.
- **Token/Exchange (mini-AMM): pick one of the three drift policies for slippage and document it.** The AMM already has this decision implicitly in its slippage tolerance; make it an explicit product choice (who eats movement inside the quote window) rather than a default parameter nobody chose on purpose.

## ko
- **Verex: 법정통화로 가격이 매겨진 모든 주문이나 Stripe 온보딩 견적에 TTL과 눈에 보이는 재견적 흐름을 준다.** 드리프트 정책(가맹점 부담, 구매자 부담, 재견적이 있는 밴드)을 먼저 배포된 코드 경로가 우연히 정하게 두지 말고 명시적으로 결정한다.
- **Wallet/Bridge: 정산 전에 움직일 수 있는 표시 금액에는 모두 expiresAt을 준다.** 브리지 변환이나 전송 중에 보여지는 잔액은 체크아웃과 같은 단기 옵션이다. 조용히 낡아버리는 숫자 대신 카운트다운과 원클릭 재견적을 보여준다.
- **Token/Exchange (미니 AMM): 슬리피지에 대해 세 드리프트 정책 중 하나를 골라 문서화한다.** AMM은 이미 슬리피지 허용치라는 형태로 이 결정을 암묵적으로 갖고 있다. 견적 창 안에서 움직임을 누가 부담하는지 아무도 의도적으로 고르지 않은 기본값이 아니라 명시적 제품 선택으로 만든다.
