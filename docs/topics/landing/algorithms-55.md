## en
- **Devnet: set the sequencer's quorum explicitly for the OP-Stack L2.** When the OP-Stack stage happens, choose Q1/Q2 deliberately (not just "majority") using the size(Q1)+size(Q2)>N condition, and document the latency/failure-tolerance tradeoff the way the exercise's (3,3)/(4,2)/(2,4) table does.
- **Verex: apply the same rule if resolution ever becomes multi-source.** Should market resolution move from a single oracle to a committee, use size(Q1)+size(Q2)>N for propose vs confirm quorums instead of assuming a plain majority in both.
- **Bridge: tune the relayer's confirmation quorum on purpose.** Decide explicitly how many relayer/attester signatures gate a mint, trading steady-state latency against failure recovery, rather than defaulting to "majority" without stating the tradeoff.

## ko
- **Devnet: OP-Stack L2의 시퀀서 쿼럼을 명시적으로 정한다.** OP-Stack 단계가 오면 "과반"이라고 막연히 두지 말고 size(Q1)+size(Q2)>N 조건을 써서 Q1/Q2를 의도적으로 정하고, 연습문제의 (3,3)/(4,2)/(2,4) 표처럼 레이턴시와 장애 허용의 트레이드오프를 문서화한다.
- **Verex: 정산이 다중 소스가 되면 같은 규칙을 적용한다.** 마켓 정산이 단일 오라클에서 위원회 방식으로 바뀐다면, 제안 쿼럼과 확정 쿼럼 모두에 단순 과반을 가정하는 대신 size(Q1)+size(Q2)>N을 적용한다.
- **Bridge: 릴레이어 확인 쿼럼을 의도적으로 조율한다.** 민트를 승인하기 위해 몇 개의 릴레이어/어테스터 서명이 필요한지 정상 상태 레이턴시와 장애 복구 사이의 트레이드오프를 밝히며 명시적으로 정하고, 트레이드오프를 말하지 않은 채 "과반"으로 기본값을 두지 않는다.
