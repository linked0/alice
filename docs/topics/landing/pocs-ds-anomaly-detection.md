## en
- **Auditor: report precision/recall at multiple thresholds for any anomaly flag it raises.** An Auditor alert on suspicious settlement or transaction activity is only useful with an ROC curve behind it, not a single silent threshold nobody chose deliberately.
- **Verex: run an isolation-forest pass over order and fill data before trusting manual fraud rules.** Compare a statistical anomaly detector's flagged trades against Verex's existing rule-based checks and report where they disagree.
- **gitboard: surface the threshold, not just the alert.** Any anomaly-based alert gitboard displays should show what threshold produced it, so a noisy or missed alert can be tuned instead of silently ignored.

## ko
- **Auditor: 이상 신호를 띄울 때마다 여러 임계값에서의 정밀도/재현율을 함께 보고한다.** 정산이나 거래 활동에 대한 Auditor 알림은 아무도 신중히 고르지 않은 단일 임계값이 아니라 ROC 곡선이 뒷받침해야 의미가 있다.
- **Verex: 수동 사기 규칙을 신뢰하기 전에 주문·체결 데이터에 isolation-forest를 돌려본다.** 통계적 이상 탐지기가 표시한 거래를 Verex의 기존 규칙 기반 검사와 비교하고, 둘이 어디서 어긋나는지 보고한다.
- **gitboard: 알림뿐 아니라 임계값도 함께 보여준다.** gitboard가 표시하는 이상 기반 알림마다 어떤 임계값에서 나왔는지 보여야 시끄럽거나 놓친 알림을 조용히 무시하는 대신 조정할 수 있다.
