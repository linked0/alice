## en
- **Verex: confirm the EIP-712 domain separator actually carries chain id, market, expiry, and nonce, not just message content.** Without all four in what gets signed, an order can be replayed across markets or across Anvil and Sepolia.
- **Wallet: never use a raw signature value as a unique identifier in jayverse-wallet's state.** Because ECDSA signatures are malleable, two different valid signatures can exist for the same message, so dedup keys or idempotency checks built on the signature bytes will fail silently.

## ko
- **Verex: EIP-712 도메인 구분자가 메시지 내용뿐 아니라 chain id, market, expiry, nonce를 실제로 담고 있는지 확인한다.** 이 네 가지가 서명 대상에 모두 포함되지 않으면 주문이 마켓 간에, 또는 Anvil과 Sepolia 간에 재사용될 수 있다.
- **Wallet: jayverse-wallet의 상태에서 서명 값 자체를 고유 식별자로 쓰지 않는다.** ECDSA 서명은 malleable하므로 같은 메시지에 대해 서로 다른 두 유효 서명이 존재할 수 있어, 서명 바이트로 만든 중복 제거 키나 idempotency 체크는 조용히 깨진다.
