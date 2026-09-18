## en
- **Verex: attach an hours class to every price feed.** Any market that can be priced off official trading hours needs a Regular/Extended/24-5/24-7 field on its feed, and liquidation or resolution should only fire on a live primary market unless the open-gap risk is written into the market's own docs.
- **Verex: adopt the consumer policy table.** Map each action (display, funding, margin call, liquidation) to a minimum hours class and confidence threshold before wiring any TradFi-symbol market, the same discipline as the reference-rate rule from the Kaiko item.
- **Auditor: require the off-hours methodology in writing before the first market resolves against it.** Whether the feed uses last close, futures-implied, or a synthetic index, publish which one and why before any consumer relies on it.

## ko
- **Verex: 모든 가격 피드에 거래 시간 등급을 붙인다.** 공식 거래 시간 밖에서 가격이 매겨질 수 있는 마켓은 피드에 Regular/Extended/24-5/24-7 필드가 있어야 하고, 청산이나 정산은 마켓 자체 문서에 갭 리스크를 명시하지 않는 한 라이브 프라이머리 마켓에서만 발동해야 한다.
- **Verex: 소비자 정책 표를 도입한다.** TradFi 심볼 마켓을 연결하기 전에 각 액션(표시, 펀딩, 마진콜, 청산)을 최소 거래 시간 등급과 신뢰도 임계값에 매핑한다. Kaiko 항목의 참조 금리 원칙과 같은 규율이다.
- **Auditor: 첫 마켓이 그 가격으로 정산되기 전에 시간외 방법론을 문서로 요구한다.** 피드가 마지막 종가, 선물 내재가, 합성 지수 중 무엇을 쓰든 어느 것을 왜 쓰는지 먼저 공개한다.
