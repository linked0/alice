## en
- **Verex: document which hash construction backs condition ID and position ID generation.** Confirm it's Keccak-family sponge (inherited from Solidity), and confirm the input encoding can't let two different conditions collide on the same ID — an encoding ambiguity, not the hash itself, is the usual source of that bug.
- **Auditor: add a length-extension test to the checklist for any hash-based authentication scheme.** If Verex or another service ever signs API tokens or session data on top of a raw hash, confirm it's HMAC or a sponge construction rather than naive secret-prefix Merkle-Damgård before trusting it as a MAC.

## ko
- **Verex: 컨디션 ID와 포지션 ID 생성을 뒷받침하는 해시 구성을 문서화한다.** Solidity에서 물려받은 Keccak 계열 스펀지 구성인지 확인하고, 입력 인코딩이 서로 다른 두 컨디션을 같은 ID로 충돌시킬 수 없는지 확인한다. 보통 이 버그의 원인은 해시 자체가 아니라 인코딩의 모호함이다.
- **Auditor: 해시 기반 인증 방식에는 길이 확장 공격 테스트를 체크리스트에 추가한다.** Verex나 다른 서비스가 원시 해시 위에 API 토큰이나 세션 데이터를 서명한다면, 이를 MAC으로 신뢰하기 전에 순진한 secret-prefix 머클-담고르가 아니라 HMAC이거나 스펀지 구성인지 확인한다.
