## en
- **Rabbit: label every balance or wallet screen with the indexer's as-of block, plus a pending-transaction overlay.** The portal's balance view is a projection, not a live read; showing which block it speaks for and overlaying the user's just-submitted transaction is what stops "silently wrong" after every send.
- **Verex: apply the same as-of label to order-book and market-state reads.** The CLOB UI reads an indexer or cache, not the chain directly, so a resolved market or a filled order needs the same cursor label and an optimistic row for the user's own just-placed order.
- **gitboard: show the as-of block or timestamp on any aggregated number.** TVL, volume or the recycling-multiple figures gitboard reports are themselves projections; the dashboard should carry the same honesty device this page derives, not just the headline number.

## ko
- **Rabbit: 모든 잔액/월렛 화면에 인덱서의 as-of 블록과 대기중 트랜잭션 오버레이를 표시한다.** 포털의 잔액 화면은 실시간 읽기가 아니라 프로젝션이다. 어느 블록을 대변하는지 보여주고 사용자가 방금 제출한 트랜잭션을 오버레이하는 것이, 전송 직후 '조용히 틀린' 상태를 막는다.
- **Verex: 오더북·마켓 상태 읽기에도 같은 as-of 라벨을 적용한다.** CLOB UI는 체인을 직접 읽지 않고 인덱서나 캐시를 읽는다. 정산된 마켓이나 체결된 주문에도 같은 커서 라벨과 사용자가 방금 낸 주문에 대한 낙관적 행이 필요하다.
- **gitboard: 집계된 숫자마다 as-of 블록이나 타임스탬프를 보여준다.** gitboard가 보고하는 TVL, 거래량, 재순환 배수 수치도 그 자체가 프로젝션이다. 헤드라인 숫자만이 아니라 이 페이지가 도출한 것과 같은 정직성 장치를 대시보드에 넣는다.
