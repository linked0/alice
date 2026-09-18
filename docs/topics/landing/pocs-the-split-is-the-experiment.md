## en
- **Number: split any address-level dataset by time and group, always.** If Number ever builds a labelled dataset from onchain data (e.g. did an address get drained within 30 days), use a time-ordered, address-grouped split with an embargo equal to the label horizon, and report the gap against a naive random split as the actual result.
- **Auditor: require the gap, not a single score.** When Auditor reviews an internal model or heuristic, make it show random-split performance next to honest-split performance; a single unqualified score should not pass review, since it is unfalsifiable on its own.
- **DeFi/Verex: fit preprocessing inside the fold.** Any risk score built for liquid-staking or market resolution must fit its scalers, encoders or thresholds only on training data, never on the full dataset before splitting — add this as a pre-ship checklist item.

## ko
- **Number: 주소 단위 데이터셋은 항상 시간·그룹 기준으로 분할한다.** Number가 온체인 데이터로 라벨 데이터셋을 만든다면 (예: 이 주소가 30일 안에 털렸는가), 라벨 기간만큼의 엠바고를 둔 시간순·주소 그룹 분할을 쓰고, 단순 무작위 분할과의 격차를 실제 결과로 보고한다.
- **Auditor: 단일 점수가 아니라 격차를 요구한다.** Auditor가 내부 모델이나 휴리스틱을 검토할 때는 무작위 분할 성능과 정직한 분할 성능을 나란히 보여주게 한다. 단일 점수는 그 자체로는 반증 불가능하므로 검토를 통과시키지 않는다.
- **DeFi/Verex: 전처리는 폴드 안에서만 학습시킨다.** 유동성 스테이킹이나 마켓 정산을 위한 리스크 점수는 스케일러, 인코더, 임곗값을 훈련 데이터에만 맞추고 분할 전 전체 데이터셋에는 맞추지 않는다. 이를 출시 전 체크리스트 항목으로 추가한다.
