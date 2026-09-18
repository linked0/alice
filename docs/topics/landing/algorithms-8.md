## en
- **Verex: use introselect for p99 fill-price/gas-price monitoring.** Compute the CLOB's live p99 fill-price and gas-price metrics with quickselect/introselect instead of sorting, and add a test with sorted or all-equal input to catch the quadratic worst case the page warns about.
- **gitboard: switch p99 latency to selection once volume grows.** Any p99 gitboard displays should move from full sort to selection at scale, with the median-of-medians fallback as the guard if quickselect ever gets gamed by adversarial input.
- **Number: standardize an introselect-based utility for rolling quantiles.** For indicator research needing rolling medians or quantiles over large series, use one shared selection-based utility instead of ad hoc sorting, to keep large backtests linear.

## ko
- **Verex: p99 체결가/가스비 모니터링에 introselect를 쓴다.** CLOB의 실시간 p99 체결가와 가스비 지표를 정렬 대신 quickselect/introselect로 계산하고, 페이지가 경고하는 최악의 경우(정렬된 입력, 전부 동일한 입력)를 잡아내는 테스트를 추가한다.
- **gitboard: 거래량이 늘면 p99 레이턴시 계산을 선택 알고리즘으로 바꾼다.** gitboard가 보여주는 p99 지표는 규모가 커지면 전체 정렬 대신 선택 알고리즘으로 전환하고, quickselect가 적대적 입력에 당할 경우를 대비해 median-of-medians를 백업으로 둔다.
- **Number: 롤링 분위수용 introselect 유틸리티를 표준화한다.** 대량 시계열의 롤링 중앙값·분위수가 필요한 리서치는 임의로 정렬하는 대신 하나의 공용 선택 기반 유틸리티를 사용해 대형 백테스트를 선형 시간으로 유지한다.
