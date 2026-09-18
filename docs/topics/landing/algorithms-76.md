## en
- **Verex: pick a specific column-store — DuckDB or a managed OLAP service — for the volume, open-interest and P&L rollups.** Keep the row-store mirror only for per-order lookups; don't let one Postgres instance serve both shapes as usage grows.
- **gitboard: move dashboard metric queries off the operational database once they start scanning large event tables.** Point those read paths at the same column-store rather than tuning indexes on the row-store mirror.
- **Number: plan for the same OLAP shape in the reading pipeline.** Historical market or price-data backtests are column-pruning-friendly workloads too; move past ad hoc scripts to a column-store before it grows large.

## ko
- **Verex: 거래량, 미결제약정, 손익 집계에는 DuckDB나 관리형 OLAP 서비스 같은 구체적인 컬럼 스토어를 고른다.** 로우 스토어 미러는 주문 단위 조회 용도로만 남겨두고, Postgres 인스턴스 하나가 두 형태를 다 감당하게 두지 않는다. 사용량이 늘수록 더 그렇다.
- **gitboard: 대시보드 지표 쿼리가 큰 이벤트 테이블을 스캔하기 시작하면 운영 DB에서 분리한다.** 그 읽기 경로를 로우 스토어 미러 인덱스 튜닝이 아니라 같은 컬럼 스토어로 보낸다.
- **Number: 읽기 파이프라인에도 같은 OLAP 형태를 계획한다.** 과거 마켓/가격 데이터 백테스트도 컬럼 프루닝에 잘 맞는 워크로드다. 규모가 커지기 전에 임시 스크립트에서 컬럼 스토어로 옮긴다.
