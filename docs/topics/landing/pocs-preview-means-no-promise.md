## en
- **Devnet: never treat a third-party data source's "Preview" status as a promise.** Any service that reads chain data from an external warehouse or indexer for Devnet or Sepolia should record freshness (lag vs block head), completeness (reorg handling), and schema stability separately, and not build a settlement or liquidation trigger on an unSLA'd source.
- **Auditor: define "available" and "unavailable" before consuming external data.** Write down what freshness lag and reorg handling the Auditor row expects from any indexer or data provider it relies on, the same methodology-first discipline the row already claims for markets.
- **Number: run the three-measurement checklist on any distributed reading's data source.** Freshness gap, completeness under reorg, and schema diff are cheap tests to run on any external chain-data feed before Number republishes numbers derived from it.

## ko
- **Devnet: 외부 데이터 소스의 "Preview" 상태를 약속으로 여기지 않는다.** Devnet이나 Sepolia용 체인 데이터를 외부 웨어하우스나 인덱서에서 읽는 서비스는 신선도(블록 헤드 대비 지연), 완전성(리오그 처리), 스키마 안정성을 각각 기록하고, SLA 없는 소스 위에 정산이나 청산 트리거를 얹지 않는다.
- **Auditor: 외부 데이터를 소비하기 전에 "available"과 "unavailable"을 정의해둔다.** Auditor 행이 의존하는 인덱서나 데이터 제공자에게 기대하는 신선도 지연과 리오그 처리 방식을 적어두는 것은, 이 행이 마켓에 대해 이미 주장하는 방법론 우선 원칙과 같다.
- **Number: 배포되는 모든 외부 체인 데이터 피드에 세 가지 측정을 돌린다.** 신선도 격차, 리오그 하에서의 완전성, 스키마 diff는 Number가 파생 수치를 다시 배포하기 전에 돌려볼 값싼 테스트다.
