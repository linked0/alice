## en
- **Rabbit: keep session-key validation legible enough for a future fast path.** Rabbit already runs ERC-4337 plus EIP-7702/7715 session keys and mandates; write the validation logic so it looks like one of the three recognizable shapes this card describes (named delegation, fixed proxy bytecode, or a deterministic keystore call) so a later L2 can substitute native code for it, instead of retrofitting that legibility after the fact.
- **Devnet: decide EVM-frame vs. native validation before the OP-Stack move.** When devnet's target chain moves from Anvil-forked Sepolia toward an OP-Stack L2, add a design note on whether Rabbit's account validation runs as general EVM code or gets a native fast path at that L2's TPS — the same fork this card documents for 8130 vs. 8141.
- **Bridge: name which side of the L2->L1 asymmetry the relayer sits on.** Anvil<->Sepolia lock-and-mint deposits can be fast; document explicitly that unlocks/withdrawals are bound by whatever challenge window or proving time the relayer uses, so the bridge's own settlement-security page states this asymmetry instead of leaving it implicit.

## ko
- **Rabbit: 세션 키 검증을 나중에 빠른 경로로 대체할 수 있을 만큼 읽기 쉽게 유지한다.** Rabbit은 이미 ERC-4337과 EIP-7702/7715 세션 키·매지트를 쓴다. 검증 로직을 이 카드가 말하는 세 가지 인식 가능한 형태(이름 붙은 위임, 고정된 프록시 바이트코드, 결정적 키스토어 호출) 중 하나처럼 작성해두면 나중에 L2가 네이티브 코드로 대체할 수 있다. 나중에 가서 읽기 쉽게 고치는 것보다 낫다.
- **Devnet: OP-Stack 이전 전에 EVM 프레임 검증인지 네이티브 검증인지 정한다.** devnet의 목표 체인이 Sepolia 포크 Anvil에서 OP-Stack L2로 옮겨갈 때, Rabbit의 계정 검증이 일반 EVM 코드로 돌지 그 L2의 TPS에 맞는 네이티브 빠른 경로를 쓸지 설계 노트로 남긴다. 이 카드가 8130 대 8141로 기록한 것과 같은 갈림길이다.
- **Bridge: 릴레이어가 L2→L1 비대칭 중 어느 쪽에 있는지 명시한다.** Anvil↔Sepolia 락앤민트 입금은 빠를 수 있지만, 언락·출금은 릴레이어가 쓰는 챌린지 기간이나 증명 시간에 묶인다는 것을 명시적으로 문서화해, 브리지 자체의 정산 보안 페이지가 이 비대칭을 암묵적으로 남기지 않고 적어둔다.
