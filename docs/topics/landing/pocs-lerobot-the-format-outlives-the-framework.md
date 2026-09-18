## en
- **Number: pick the reading/indicator storage format before picking the analysis framework.** Number's math and algorithm research should settle a stable schema for stored readings and indicators first, the same "format outlives the framework" lesson, since the analysis library will churn faster than the data.
- **Devnet: the indexer's table schema is the asset, not any particular indexing tool.** Whatever indexes Devnet's blocks and events, keep the schema stable and versioned deliberately, since it will outlive whichever indexing framework runs today.
- **gitboard: store dashboard metrics in a durable, tool-agnostic format.** If gitboard ever swaps its metrics pipeline, the stored history should survive that swap; define the schema now rather than after the first framework change.

## ko
- **Number: 분석 프레임워크보다 읽기/지표 저장 형식을 먼저 정한다.** Number의 수학·알고리즘 리서치는 저장된 읽기와 지표에 대한 안정적 스키마를 먼저 정해야 한다. "형식이 프레임워크보다 오래 산다"는 교훈 그대로, 분석 라이브러리는 데이터보다 빨리 바뀐다.
- **Devnet: 인덱서의 테이블 스키마가 자산이지 특정 인덱싱 도구가 아니다.** Devnet의 블록과 이벤트를 무엇으로 인덱싱하든, 스키마를 의도적으로 안정되고 버전 관리되게 유지한다. 오늘 쓰는 인덱싱 프레임워크보다 스키마가 더 오래 살아남기 때문이다.
- **gitboard: 대시보드 지표를 도구에 종속되지 않는 내구성 있는 형식으로 저장한다.** gitboard가 지표 파이프라인을 언젠가 교체하더라도 저장된 이력은 그 교체에서 살아남아야 하므로, 프레임워크를 바꾸고 난 뒤가 아니라 지금 스키마를 정의한다.
