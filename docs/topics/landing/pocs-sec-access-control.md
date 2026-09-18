## en
- **Verex/Bridge/Token contracts: audit every initializer and admin setter for a missing access-control modifier before each deploy.** This is a checklist item run every time, not a one-time review, since it's the OWASP-top boring bug that causes real losses.
- **CI: run a static access-control check (e.g. Slither's detectors) on every contract PR.** An unguarded initializer should fail CI rather than merge silently.

## ko
- **Verex/Bridge/Token 컨트랙트: 매 배포 전마다 모든 초기화 함수와 관리자 세터에 접근 제어 모디파이어가 빠지지 않았는지 감사한다.** OWASP 최상위이자 실제 손실을 내는 지루한 버그이므로, 한 번의 리뷰가 아니라 매번 도는 체크리스트 항목으로 만든다.
- **CI: 모든 컨트랙트 PR에 정적 접근 제어 검사(예: Slither의 디텍터)를 돌린다.** 접근 제어가 빠진 초기화 함수는 조용히 머지되지 않고 CI에서 실패해야 한다.
