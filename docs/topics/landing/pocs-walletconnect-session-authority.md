## en
- **Wallet: model every connection as an explicit session state machine, not a boolean.** Track namespaces, chains, methods, accounts and expiry directly, and request the smallest method set by default — no eth_sign unless a flow specifically needs it.
- **Rabbit: apply the same narrow-or-invalidate invariant to EIP-7702/7715 session keys and mandates.** Every mutation event should only shrink authority or force a fresh grant; test explicitly that no event silently widens what a session key can do.
- **Wallet: make expiry and revocation first-class, visible UI, not edge cases.** Surface a session's remaining scope and give the user an explicit revoke action, so a stale-account bug can't hide behind a green "connected" dot.

## ko
- **Wallet: 모든 연결을 불리언이 아니라 명시적 세션 상태 머신으로 모델링한다.** 네임스페이스, 체인, 메서드, 계정, 만료를 직접 추적하고, 기본값으로 가장 좁은 메서드 집합을 요청한다 — 플로우가 특별히 필요로 하지 않는 한 eth_sign은 요청하지 않는다.
- **Rabbit: 같은 "축소 또는 무효화" 불변식을 EIP-7702/7715 세션 키와 맨데이트에도 적용한다.** 모든 변이 이벤트는 권한을 줄이거나 새 승인을 강제해야 하며, 어떤 이벤트도 세션 키의 권한을 조용히 넓히지 않는지 명시적으로 테스트한다.
- **Wallet: 만료와 취소를 예외가 아니라 눈에 보이는 1급 UI로 만든다.** 세션에 남은 권한 범위를 표시하고 명시적인 취소 액션을 제공해, stale-account 버그가 초록색 "연결됨" 표시 뒤에 숨지 못하게 한다.
