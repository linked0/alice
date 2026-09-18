## en
- **Rabbit: audit prompt-prefix stability for the payment agent's loop.** The mandate-execution loop is exactly the harness workload this cache cut targets — keep the system prompt and tool schemas byte-stable, then recompute per-transaction cost under the new cache-read price.
- **Number/Auditor: log cache-read vs fresh-read tokens for any Claude-API pipeline.** Recompute the actual bill under the new pricing instead of assuming the cut helps a given research or report-generation job.
- **gitboard: add a cache-hit-ratio line to the dashboard.** For any service calling the Anthropic API, that ratio is now the number that decides the real bill, so track it alongside cost.

## ko
- **Rabbit: 결제 에이전트 루프의 프롬프트 프리픽스 안정성을 점검한다.** 위임 실행 루프는 이 캐시 인하가 겨냥하는 바로 그 하네스형 워크로드다. 시스템 프롬프트와 툴 스키마를 바이트 단위로 고정한 뒤, 새 캐시 읽기 가격으로 트랜잭션당 비용을 다시 계산한다.
- **Number/Auditor: Claude API 파이프라인마다 캐시 읽기와 신규 읽기 토큰을 기록한다.** 인하가 도움이 된다고 가정하지 말고 새 가격표로 실제 청구액을 다시 계산한다.
- **gitboard: 대시보드에 캐시 적중률 항목을 추가한다.** Anthropic API를 호출하는 모든 서비스에서 이 비율이 이제 실제 청구액을 결정하는 숫자이므로 비용과 함께 추적한다.
