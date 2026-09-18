## en
- **Verex: name the query list and its latency target before any schema change.** List positions-by-user, orders-by-market and resolution lookups with a target latency each, then verify with an execution plan that the design resolves to a single index lookup — make this the checklist an API review must pass.
- **gitboard: track scanned-row counts for Verex's hot paths.** A regression there is the early signal that an index patch has stopped buying enough, and that a genuine model change is due.
- **Auditor: log which query pattern justified each table's key design.** When storage is separated by access pattern, as Verex already does, record the reasoning so a future migration has it, not just the resulting schema.

## ko
- **Verex: 스키마를 바꾸기 전에 쿼리 목록과 지연시간 목표부터 정한다.** 사용자별 포지션, 마켓별 주문, 정산 조회를 각각 목표 지연시간과 함께 나열하고, 실행 계획으로 설계가 단일 인덱스 조회로 귀결되는지 확인한다 — 이를 API 리뷰가 통과해야 할 체크리스트로 삼는다.
- **gitboard: Verex의 핫 패스에 대한 스캔 행 수를 추적한다.** 여기서의 회귀는 인덱스 패치만으로는 더 이상 충분하지 않고 진짜 모델 변경이 필요하다는 조기 신호다.
- **Auditor: 각 테이블의 키 설계를 정당화한 쿼리 패턴을 기록한다.** Verex가 이미 하듯 저장소를 접근 패턴별로 분리할 때, 그 이유를 기록해두면 이후 마이그레이션이 결과 스키마뿐 아니라 근거도 갖게 된다.
