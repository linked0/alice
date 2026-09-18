## en
- **Verex: use tail-based sampling keyed on transaction status and latency, not random sampling.** Keep 100% of traces where a chain-confirmation-bound order fails or runs long, so post-mortems never lose exactly the traces they need.
- **gitboard: record the sampling rate alongside trace metrics on the dashboard.** Per this PoC's note, aggregate latency numbers need the sampling rate attached or they're silently biased.
- **CI: add a trace-context propagation check across the API-to-matching-engine-to-settlement path.** A broken trace/parent-span header should fail CI, not surface as a fragmented trace during an incident.

## ko
- **Verex: 무작위 샘플링이 아니라 트랜잭션 상태와 지연시간을 기준으로 한 tail-based 샘플링을 쓴다.** 체인 컨펌에 묶인 주문이 실패하거나 오래 걸리는 트레이스는 100% 보존해, 포스트모템에서 정작 필요한 트레이스를 놓치지 않게 한다.
- **gitboard: 대시보드의 트레이스 지표 옆에 샘플링 비율을 함께 기록한다.** 이 PoC의 지적대로, 집계 지연시간 숫자는 샘플링 비율이 붙어있지 않으면 조용히 편향된다.
- **CI: API → 매칭 엔진 → 정산 제출 경로 전체에 걸친 trace-context 전파 체크를 추가한다.** 깨진 trace/parent-span 헤더는 사고 중 조각난 트레이스로 드러나는 대신 CI에서 실패해야 한다.
