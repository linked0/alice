## en
- **CI: apply the cheap-oracle test to agent-generated code per category.** Compiling and tests passing is a cheap oracle for full-stack changes, but a data-model or trust-boundary change has none — require manual review specifically for those two categories instead of trusting green CI.
- **Auditor: don't treat passing tests as a security check.** A test asserts something works, not that nothing else does, so the auditor's checklist needs an explicit trust-boundary review per PR, separate from CI status.
- **DeFi/Devnet: flag architecture and load-shape decisions for written review.** A structure correct at today's load is indistinguishable from one that breaks at ten times it, so liquid-staking design changes need a design note before merge, not just a code review.

## ko
- **CI: 에이전트가 생성한 코드에 카테고리별로 저비용 오라클 테스트를 적용한다.** 풀스택 변경은 컴파일과 테스트 통과가 저비용 오라클이지만 데이터 모델이나 신뢰 경계 변경에는 오라클이 없다. 이 두 카테고리는 CI 통과를 믿는 대신 수동 리뷰를 필수로 요구한다.
- **Auditor: 테스트 통과를 보안 체크로 취급하지 않는다.** 테스트는 무언가가 동작한다는 것만 확인할 뿐 다른 것이 깨지지 않았다는 것은 확인하지 않는다. Auditor 체크리스트는 CI 상태와 별개로 PR마다 명시적인 신뢰 경계 리뷰를 포함해야 한다.
- **DeFi/Devnet: 아키텍처와 부하 형태 결정을 서면 리뷰 대상으로 표시한다.** 오늘 부하에서 맞는 구조는 10배 부하에서 무너지는 구조와 오늘은 구분되지 않는다. 리퀴드 스테이킹 설계 변경은 코드 리뷰만이 아니라 병합 전 설계 노트를 요구한다.
