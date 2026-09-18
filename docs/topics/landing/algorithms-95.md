## en
- **Wallet: keep the client-side signing path pluggable too.** Not just Verex's contracts — the embedded wallet's signing logic should accept a swappable curve/scheme, so a future hybrid PQ transition doesn't force a full wallet rewrite.
- **Bridge: put a scheme-version field in the message format now.** Add a signature-scheme identifier to the relayer's cross-chain message format while it only ever holds today's ECDSA value, so a later hybrid transition is a version bump, not a breaking change.
- **Personas: route persona signature checks through the same shared verifier.** Don't hardcode secp256k1 verification inside the persona token contract; reuse Verex's swappable verifier module so a future migration is one shared upgrade instead of four separate ones.

## ko
- **Wallet: 클라이언트 측 서명 경로도 교체 가능하게 유지한다.** Verex 컨트랙트뿐 아니라 임베디드 지갑의 서명 로직도 교체 가능한 곡선·스킴을 받아들여야, 향후 하이브리드 PQ 전환이 지갑 전체 재작성을 강요하지 않는다.
- **Bridge: 지금 메시지 포맷에 스킴 버전 필드를 넣는다.** 릴레이어의 크로스체인 메시지 포맷에 지금은 ECDSA 값만 들어가더라도 서명 스킴 식별자를 추가해둔다. 나중의 하이브리드 전환이 breaking change가 아니라 버전 업이 되도록.
- **Personas: 페르소나 서명 검증도 같은 공유 검증 모듈을 거치게 한다.** 페르소나 토큰 컨트랙트 안에 secp256k1 검증을 하드코딩하지 않는다. Verex의 교체 가능한 검증 모듈을 재사용해 향후 마이그레이션이 네 번이 아니라 한 번의 공유 업그레이드가 되게 한다.
