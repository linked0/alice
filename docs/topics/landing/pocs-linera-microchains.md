## en
- **Verex: keep the CLOB on one shared chain rather than assuming it composes under sharding.** The order book is exactly the shared-state case this note flags as hard for a per-user microchain model, so if Jayverse ever considers sharding by user, exclude Verex's book from that plan explicitly.
- **Devnet: read this as confirmation that Devnet's single shared chain is a deliberate choice.** Most Jayverse services (Verex, Token/Bridge) depend on shared state that a per-user chain would fragment, so contention-removal-by-sharding is not a direction to pursue without a specific reason.

## ko
- **Verex: 샤딩해도 자연히 합성될 거라 가정하지 말고 CLOB을 하나의 공유 체인에 둔다.** 오더북은 이 노트가 사용자별 마이크로체인 모델에서 어렵다고 지적하는 바로 그 공유 상태 사례이므로, 사용자별 샤딩을 고려하게 되더라도 Verex의 오더북은 명시적으로 그 계획에서 제외한다.
- **Devnet: 이 노트를 Devnet이 단일 공유 체인을 쓰는 것이 의도된 선택이라는 확인으로 읽는다.** Verex, Token/Bridge 같은 대부분의 Jayverse 서비스는 사용자별 체인이 쪼개버릴 공유 상태에 의존하므로, 샤딩으로 경합을 없애는 방향은 특별한 이유 없이는 추구할 방향이 아니다.
