## en
- **Bridge: extend EIP-712-style domain separation to relayer mint/release messages.** Tag them with chainId and the bridge contract address, so a signed lock message from Anvil can never be replayed as a valid mint authorization on Sepolia, or the reverse.
- **Rabbit: give session-key mandates their own domain tag, distinct from Verex orders.** Audit that mandate signing doesn't reuse a hash construction that could let a mandate be replayed as an order or across a different contract.
- **Personas: use length-prefixed or fixed-width encoding when signing off-chain listings or offers.** Concatenating variable-length fields before hashing risks two different listings producing the same signed message.

## ko
- **Bridge: EIP-712식 도메인 분리를 릴레이어의 민팅/방출 메시지에도 적용한다.** chainId와 브릿지 컨트랙트 주소로 태그를 달아, Anvil에서 서명된 lock 메시지가 Sepolia에서 유효한 민팅 승인으로 재생될 수 없게, 그 반대도 마찬가지로 한다.
- **Rabbit: 세션 키 mandate에 Verex 주문과 별개인 자체 도메인 태그를 준다.** mandate 서명이 다른 컨트랙트나 주문으로 재생될 수 있는 해시 구성을 재사용하지 않는지 점검한다.
- **Personas: 오프체인 리스팅이나 오퍼에 서명할 때 길이 접두사나 고정폭 인코딩을 쓴다.** 가변 길이 필드를 그냥 이어붙여 해시하면 서로 다른 두 리스팅이 같은 서명 메시지를 만들어낼 위험이 있다.
