## en
- **Devnet: track proof size, not hashing speed, for any future L2.** When Devnet moves from an Anvil fork toward an OP-Stack L2, treat proof-size growth as the metric that decides whether a stateless or light client is feasible, not raw hash throughput.
- **Auditor: flag storage growth in every contract that writes persistent state.** Verex order state, Bridge mint counters and Rabbit's session-key mandates all add to state every node keeps forever; treat that growth as a first-class cost the way Ethereum's Verge roadmap does.
- **gitboard: add a state-size metric per service.** Track storage growth for Verex and Bridge so the "how big does this get" question is visible before it becomes a syncing problem.

## ko
- **Devnet: 미래 L2를 위해 해싱 속도가 아니라 증명 크기를 추적한다.** Devnet이 Anvil 포크에서 OP-Stack L2로 옮겨갈 때, 스테이트리스나 라이트 클라이언트가 가능한지를 결정하는 지표로 원시 해시 처리량이 아니라 증명 크기 증가를 본다.
- **Auditor: 영구 상태를 쓰는 모든 컨트랙트의 상태 증가를 표시한다.** Verex 주문 상태, Bridge의 민팅 카운터, Rabbit의 세션키 매니데이트 모두 모든 노드가 영구히 들고 있어야 하는 상태를 늘린다. Ethereum의 Verge 로드맵처럼 이 증가를 1급 비용으로 취급한다.
- **gitboard: 서비스별 상태 크기 지표를 추가한다.** Verex와 Bridge의 스토리지 증가를 추적해, "이게 얼마나 커지는가"라는 질문이 동기화 문제가 되기 전에 눈에 보이게 한다.
