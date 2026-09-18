## en
- **Bridge: write the lock/mint Merkle inclusion-proof verifier as structural induction on tree height.** A recursive verifier function that mirrors the proof shape, not an ad hoc loop, is what the induction argument requires to actually hold.
- **Verex: test "equal roots imply equal leaf sets" directly for any Merkle-committed state (order-book or balance snapshots).** Construct two different leaf sets and confirm distinct roots, rather than trusting the property by inspection.
- **Auditor: require a written well-founded termination measure for any recursive verifier before it ships.** A decreasing tree depth is trivial to state and cheap to check in review, and it's the difference between a proof and a hope.

## ko
- **Bridge: lock/mint의 머클 포함 증명 검증기를 트리 높이에 대한 구조적 귀납법으로 작성한다.** 임시 루프가 아니라 증명 구조를 그대로 따르는 재귀 검증 함수여야 귀납 논증이 실제로 성립한다.
- **Verex: 머클로 커밋된 모든 상태(오더북이나 잔고 스냅샷)에 대해 "루트가 같으면 리프 집합도 같다"를 직접 테스트한다.** 육안 검토로 믿는 대신 서로 다른 리프 집합 두 개를 만들어 다른 루트가 나오는지 확인한다.
- **Auditor: 재귀 검증기를 배포하기 전에 well-founded 종료 측도를 문서로 요구한다.** 감소하는 트리 깊이는 명시하기 쉽고 리뷰에서 확인하는 비용도 낮다. 증명과 희망의 차이가 바로 이것이다.
