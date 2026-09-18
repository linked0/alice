## en
- **Verex: surface withdrawal/settlement latency as "waiting on proof generation," not a generic pending state.** On any future L2, that latency is bounded by proof-generation time, not block time — this is also the fourth clock from pocs-l2-finality-three-clocks, so wire the UI to that clock explicitly.
- **Devnet: track prover cost as an infra line item once Devnet moves off Anvil to an OP-Stack L2.** Whatever proof system that L2 uses, Jayverse inherits its recursion/aggregation cost — budget for it rather than discovering it in withdrawal latency later.
- **Auditor: record which proof system and circuit each settlement path relies on.** Since verification cost is exactly what the Auditor's methodology should state, write down curve/hash choices per path before a consumer asks why a withdrawal took as long as it did.

## ko
- **Verex: 출금/정산 지연을 일반적인 대기 상태가 아니라 "증명 생성 대기 중"으로 보여준다.** 향후 어떤 L2에서든 이 지연은 블록 시간이 아니라 증명 생성 시간에 묶인다. 이는 pocs-l2-finality-three-clocks의 네 번째 클럭이기도 하므로 UI를 그 클럭에 명시적으로 연결한다.
- **Devnet: Devnet이 Anvil을 벗어나 OP-Stack L2로 옮기면 프루버 비용을 인프라 항목으로 추적한다.** 그 L2가 어떤 증명 시스템을 쓰든 Jayverse는 그 재귀/집계 비용을 물려받는다. 나중에 출금 지연에서 발견하지 말고 미리 예산에 넣는다.
- **Auditor: 각 정산 경로가 어떤 증명 시스템과 회로에 의존하는지 기록한다.** 검증 비용이 바로 Auditor의 방법론이 말해야 하는 내용이므로, 소비자가 왜 출금이 그만큼 걸렸는지 묻기 전에 경로별 커브/해시 선택을 적어둔다.
