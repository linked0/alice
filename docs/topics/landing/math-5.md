## en
- **Verex: since it's a ctf-exchange fork, verify condition-ID and position-ID derivation follows the exact hash scheme, and add a test that changing one input (oracle, questionId, outcome count) changes only that ID.** A silent collision in the hash-link derivation would corrupt the whole condition tree.
- **gitboard: model service dependency (token before bridge before wallet, etc.) as an explicit DAG with a topological order.** Deploy and migration order should be derived from the graph, not remembered by whoever runs it.
- **Bridge: use a hash-linked snapshot (a Merkle root of locked balances) as the thing the relayer commits to.** Tampering with one locked deposit becomes detectable by a root mismatch alone, without walking the whole ledger.

## ko
- **Verex: ctf-exchange 포크이므로, condition ID와 position ID 도출이 정확히 같은 해시 방식을 따르는지 확인하고 하나의 입력(오라클, questionId, outcome 수)을 바꾸면 그 ID만 바뀌는지 테스트를 추가한다.** 해시 링크 도출에서 조용한 충돌이 나면 condition 트리 전체가 손상된다.
- **gitboard: 서비스 의존관계(token 다음 bridge, 그다음 wallet 등)를 위상 정렬이 있는 명시적 DAG로 모델링한다.** 배포와 마이그레이션 순서는 운영자가 기억하는 것이 아니라 그래프에서 도출돼야 한다.
- **Bridge: 릴레이어가 커밋하는 대상으로 해시 링크된 스냅샷(잠긴 잔액의 머클 루트)을 사용한다.** 잠긴 예치금 하나를 조작하면 전체 원장을 훑지 않고도 루트 불일치만으로 감지할 수 있다.
