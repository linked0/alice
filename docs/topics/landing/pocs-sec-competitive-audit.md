## en
- **Auditor: record every Jayverse audit as a scoped snapshot — firm or contest, scope, date, and exact commit hash — not a badge.** An "audited" claim without those four fields is not checkable, and this row is exactly where the fields belong before any contract carries real value.
- **Bridge/CI: pin the audited commit in CI so a passing audit stays tied to a frozen state.** OpenZeppelin is already pinned as submodules; extend that discipline to the bridge's own lock-and-mint contracts so a later dependency bump can't silently invalidate what was actually reviewed.

## ko
- **Auditor: Jayverse의 모든 감사를 배지가 아니라 범위가 정해진 스냅샷으로 기록한다 — 수행 기관/콘테스트, 범위, 날짜, 정확한 커밋 해시.** 이 네 항목 없는 "감사됨" 주장은 검증할 수 없다. 어떤 컨트랙트든 실제 가치를 담기 전에 이 필드들이 있어야 할 곳이 바로 이 행이다.
- **Bridge/CI: 감사받은 커밋을 CI에 고정해 통과한 감사가 동결된 상태에 묶이게 한다.** OpenZeppelin은 이미 서브모듈로 고정돼 있다. 이후 의존성 업데이트가 실제로 검토된 내용을 조용히 무효화하지 않도록 브릿지 자체의 lock-and-mint 컨트랙트에도 같은 규율을 확장한다.
