## en
- **gitboard: pick the storage engine per workload, not one database for everything.** Route append-heavy event/history tables (market events, execution logs) to an LSM-backed store and per-account lookup tables (positions, balances) to a B+tree-backed store, and say so in the infra docs.
- **Verex: benchmark both amplification profiles before scaling the indexer.** Order and event history is range-read and append-heavy; open positions per account are point-read-heavy — treat them as two different index problems, not one schema.
- **Auditor: rule out storage-engine mismatch before blaming application logic.** When Devnet sync slows or disk usage spikes, check read/write amplification against the access pattern first, since that's usually the cause, not a bug in the service code.

## ko
- **gitboard: 워크로드별로 스토리지 엔진을 고르지, 모든 것에 하나의 DB를 쓰지 않는다.** 추가 중심인 이벤트·히스토리 테이블(마켓 이벤트, 실행 로그)은 LSM 기반 저장소로, 계정별 조회 테이블(포지션, 잔고)은 B+트리 기반 저장소로 보내고 인프라 문서에 명시한다.
- **Verex: 인덱서를 확장하기 전에 두 증폭 프로파일을 벤치마크한다.** 주문·이벤트 히스토리는 범위 읽기와 추가가 많고, 계정별 오픈 포지션은 포인트 읽기가 많다. 이 둘을 하나의 스키마가 아니라 별개의 인덱스 문제로 다룬다.
- **Auditor: 애플리케이션 로직을 탓하기 전에 스토리지 엔진 불일치를 먼저 배제한다.** Devnet 동기화가 느려지거나 디스크 사용량이 튀면 액세스 패턴 대비 읽기·쓰기 증폭을 먼저 확인한다. 보통 그게 원인이지 서비스 코드의 버그가 아니다.
