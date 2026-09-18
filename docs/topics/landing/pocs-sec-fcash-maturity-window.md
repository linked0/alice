## en
- **Auditor: measure pause latency now, before an incident.** For every Jayverse contract with a time delay (challenge window, bridge refill, market settlement), compute (detect + respond) blocks against the window length and log it as a standing number, not something discovered mid-incident.
- **Bridge/Token: watch the xERC20 refill window for the same maturity-window shape.** Add a detector that flags any account's minted balance sitting ahead of backing before the rate-limit refills, mirroring the fCash detection query.
- **gitboard: surface a live "stoppable?" column for every timed mechanism.** Track maturity/challenge/expiry windows minus response latency across Verex settlement, bridge refill and AA session-key expiry in one dashboard row.

## ko
- **Auditor: 사고가 나기 전에 지금 일시정지 지연 시간을 측정한다.** 시간 지연이 있는 모든 Jayverse 컨트랙트(챌린지 윈도우, 브리지 리필, 마켓 정산)에 대해 (탐지+대응) 블록 수를 윈도우 길이와 비교해 계산하고, 사고 도중이 아니라 상시 지표로 기록해둔다.
- **Bridge/Token: xERC20 리필 윈도우에서 같은 만기 윈도우 형태를 살핀다.** fCash 탐지 쿼리를 본떠, 레이트 리밋이 리필되기 전에 담보보다 앞서는 민팅 잔액을 가진 계정을 플래그하는 탐지기를 추가한다.
- **gitboard: 모든 타이머 기반 메커니즘에 실시간 "정지 가능?" 컬럼을 노출한다.** Verex 정산, 브리지 리필, AA 세션 키 만료 전반에서 만기/챌린지/만료 윈도우에서 대응 지연을 뺀 값을 한 대시보드 행에 추적한다.
