## en
- **Devnet: set alert thresholds by repair time, not model accuracy.** For any Devnet/Anvil node-health or RPC-failure monitor, log the actual restart/redeploy time first — that number is the horizon below which an alert is worthless, and it comes from ops, not from a model.
- **gitboard: report threshold, lead time, and false-alarm rate, not a red/green light.** Any anomaly indicator on the dashboard should ship with the cost ratio it was tuned against, so a viewer can see what it costs to ignore versus to chase.
- **Auditor: write the cost ratio k before tuning any alert.** For liquidation, slashing, or oracle-dispute monitors, state cost(missed event) versus cost(false alarm) up front, and compare against the honest baseline — the schedule or check already in place — not against doing nothing.

## ko
- **Devnet: 알림 임계값은 수리 시간으로 정하지, 모델 정확도로 정하지 않는다.** Devnet/Anvil 노드 상태나 RPC 장애 모니터는 실제 재시작·재배포 시간을 먼저 기록한다. 이 숫자가 알림이 무의미해지는 기준선이고, 모델이 아니라 운영에서 나온다.
- **gitboard: 대시보드는 빨강/초록이 아니라 임계값, 리드타임, 오탐률을 보고한다.** 대시보드의 이상 지표는 어떤 비용비로 튜닝됐는지와 함께 나와야, 무시할 때의 비용과 쫓을 때의 비용을 볼 수 있다.
- **Auditor: 알림을 튜닝하기 전에 비용비 k를 적어둔다.** 청산, 슬래싱, 오라클 분쟁 모니터라면 놓친 사건의 비용과 오탐 비용을 먼저 명시하고, 아무것도 안 하는 것이 아니라 이미 있는 일정 기반 점검과 비교한다.
