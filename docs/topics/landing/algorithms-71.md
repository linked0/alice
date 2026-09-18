## en
- **Verex: pick leveled compaction for the event indexer, not tiered.** Per-market range queries need low read and space amplification more than raw write throughput, so leveled compaction fits Verex's time-ordered, per-market query pattern better.
- **gitboard: track write amplification and lookup p99 as indexer dashboard metrics.** Per this PoC's exercise, keep the actual-disk-bytes-vs-logical-bytes ratio and p99 latency visible, so a compaction-lag spike is diagnosed against real numbers instead of guessed at.
- **Devnet: run the write-amplification benchmark against Verex's real key schema, not a synthetic one.** Vary compaction style and level fan-out on the actual per-market, time-ordered key design before picking defaults.

## ko
- **Verex: 이벤트 인덱서에는 tiered가 아니라 leveled 컴팩션을 선택한다.** 마켓별 범위 쿼리는 원시 쓰기 처리량보다 낮은 읽기·공간 증폭이 더 필요하므로, leveled 컴팩션이 Verex의 시간순, 마켓별 쿼리 패턴에 더 맞는다.
- **gitboard: write amplification과 조회 p99를 인덱서 대시보드 지표로 추적한다.** 이 PoC의 연습문제에 따라, 실제 디스크 바이트 대 논리 바이트 비율과 p99 지연시간을 계속 보이게 해서 컴팩션 지연 급증을 추측이 아니라 실제 숫자로 진단한다.
- **Devnet: 합성 스키마가 아니라 Verex의 실제 키 스키마로 write amplification 벤치마크를 실행한다.** 기본값을 고르기 전에 실제 마켓별, 시간순 키 설계에 대해 컴팩션 스타일과 레벨 팬아웃을 바꿔가며 테스트한다.
