## en
- **Verex: audit for unbounded loops before they become a DoS vector.** Settlement and order processing must not scale gas linearly with participant count; replace any array iteration without a cap with pull-based claims where users pay their own gas.
- **Verex: run a two-version gas report in CI.** Compare a storage-write-heavy path against a calldata/event-heavy path, and break down which opcodes dominate, to catch an underpriced operation before it ships.
- **CI: track per-opcode gas regression for Verex and Bridge contracts on every PR.** A single underpriced operation is a DoS vector regardless of intent, so the check belongs in CI, not a one-time review.

## ko
- **Verex: DoS 벡터가 되기 전에 무제한 루프를 감사한다.** 정산과 주문 처리 가스는 참가자 수에 선형으로 늘어나서는 안 된다. 상한 없는 배열 순회는 사용자가 자기 가스를 지불하는 풀 기반 클레임으로 바꾼다.
- **Verex: CI에서 두 버전의 가스 리포트를 돌린다.** 스토리지 쓰기 중심 경로와 콜데이터/이벤트 중심 경로를 비교하고 어떤 옵코드가 비용을 지배하는지 분해해, 저평가된 연산을 출시 전에 잡아낸다.
- **CI: 모든 PR에서 Verex와 Bridge 컨트랙트의 옵코드별 가스 회귀를 추적한다.** 하나의 저평가된 연산도 의도와 무관하게 DoS 벡터이므로, 이 점검은 일회성 리뷰가 아니라 CI에 속해야 한다.
