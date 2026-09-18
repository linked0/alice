## en
- **Verex: pre-publish the outlier/staleness/quorum rulebook.** Write and log the rule for excluding a wick, dropping a stale feed, and the minimum venue quorum with its fallback before the first bad tick arrives, not during the incident.
- **Auditor: require a replayable resolution log.** Every Verex resolution should leave logged inputs and exclusion decisions that Auditor can replay byte-for-byte to reproduce the published outcome, not just the final number.
- **Number: ship the operations layer with the formula.** Any reading or index Number distributes needs source-eligibility criteria and a documented rule-change process alongside the math, since the formula alone is not what makes a reading trustworthy.

## ko
- **Verex: 이상치·정지·쿼럼 규칙을 미리 공개한다.** 와익(wick)을 제외하는 규칙, 정지된 피드를 떨어뜨리는 규칙, 최소 거래소 쿼럼과 그 대체 규칙을 첫 번째 이상 틱이 오기 전에 적어서 기록해둔다. 사고 도중이 아니라.
- **Auditor: 재현 가능한 정산 로그를 요구한다.** 모든 Verex 정산은 입력값과 제외 결정을 로그로 남겨 Auditor가 바이트 단위로 재생해 공개된 결과를 재현할 수 있어야 한다. 최종 숫자만으로는 부족하다.
- **Number: 공식과 함께 운영 계층도 함께 배포한다.** Number가 배포하는 어떤 읽기값이나 지수든 소스 자격 기준과 문서화된 규칙 변경 절차가 수식과 함께 있어야 한다. 공식만으로는 신뢰할 수 있는 읽기값이 되지 않기 때문이다.
