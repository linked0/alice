## en
- **Verex: implement the nullifier scheme in the actual settlement contract.** Beyond deciding what stays public, build the deposit/withdrawal gate itself — same secret always yields the same nullifier, so a second withdrawal attempt is blocked at the contract level, exactly as the exercise describes.
- **Wallet: consider stealth addresses for the receive flow.** So a user's incoming-payment history doesn't accumulate under one visible address, a separate privacy question from what Verex publishes as settlement events.
- **Number: a ring-signature-style proof could gate licensed readings.** A consumer proves they hold one of N valid licenses without revealing which subscriber they are, fitting the "reading as a licensed token" design.

## ko
- **Verex: 실제 정산 컨트랙트에 nullifier 방식을 구현한다.** 무엇을 공개할지 결정하는 것을 넘어, 입금/출금 게이트 자체를 만든다. 같은 시크릿은 항상 같은 nullifier를 내므로 두 번째 출금 시도는 컨트랙트 단에서 차단된다. 연습문제가 설명하는 그대로다.
- **Wallet: 수신 흐름에 스텔스 주소를 고려한다.** 사용자의 입금 내역이 하나의 눈에 보이는 주소 아래 쌓이지 않게 한다. Verex가 정산 이벤트로 무엇을 공개하는지와는 별개의 프라이버시 문제다.
- **Number: 링 서명 방식으로 라이선스된 읽기를 게이트할 수 있다.** 소비자가 어느 구독자인지 밝히지 않고도 N개의 유효 라이선스 중 하나를 보유했음을 증명한다. "라이선스된 토큰으로서의 읽기" 설계와 맞는다.
