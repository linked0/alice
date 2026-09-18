## en
- **Wallet: test that a stored-XSS payload elsewhere on jaylabs.xyz cannot reach the signing prompt.** The signing call should only be triggerable from Wallet's own trusted script context, not any script running on the page.
- **Rabbit portal: add CSRF tokens and SameSite cookies to every authenticated portal action.** Sanitize any user-generated content path — persona bios, market descriptions — before it ships.

## ko
- **Wallet: jaylabs.xyz 다른 곳의 저장형 XSS 페이로드가 서명 프롬프트에 닿지 못하는지 테스트한다.** 서명 호출은 페이지에서 실행되는 아무 스크립트가 아니라 오직 Wallet 자신의 신뢰된 스크립트 컨텍스트에서만 트리거되어야 한다.
- **Rabbit 포털: 인증된 모든 포털 액션에 CSRF 토큰과 SameSite 쿠키를 추가한다.** 페르소나 소개, 마켓 설명 등 사용자 생성 콘텐츠 경로는 출시 전에 새니타이즈한다.
