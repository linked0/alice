## en
- **Token/Exchange: decide who holds JYVE's reserve and earns the float before picking a backing model.** The token contract is close to interchangeable across designs; the real decision is who holds reserves, earns interest on them, and can refuse a redemption.
- **Verex: document who takes the FX/spread risk in the Stripe onboarding flow.** Between authorization and settlement someone carries currency or timing risk; name that party explicitly rather than leaving it implicit in the integration.
- **Bridge: define a redemption-desk owner for the Anvil⇄Sepolia relayer.** State who can halt or refuse a mint/burn request and under what condition, the same question this piece raises for a named stablecoin issuer.

## ko
- **Token/Exchange: 백킹 모델을 정하기 전에 JYVE 준비금을 누가 보유하고 float 수익을 가져가는지 결정한다.** 토큰 컨트랙트 자체는 설계 간에 거의 상호교환 가능하다. 진짜 결정은 누가 준비금을 보유하고 이자를 가져가며 상환을 거부할 수 있는가다.
- **Verex: Stripe 온보딩 플로우에서 환율/스프레드 리스크를 누가 지는지 문서화한다.** 승인과 정산 사이에 누군가 통화나 타이밍 리스크를 진다. 연동에 암묵적으로 남기지 말고 그 주체를 명시한다.
- **Bridge: Anvil⇄Sepolia 릴레이어의 상환 데스크 소유자를 정의한다.** 누가 어떤 조건에서 발행/소각 요청을 멈추거나 거부할 수 있는지 명시한다. 이 글이 특정 스테이블코인 발행자에게 던진 것과 같은 질문이다.
