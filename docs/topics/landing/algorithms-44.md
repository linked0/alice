## en
- **Verex: implement hedged requests for eth_call and receipt polling as planned, and set the hedge delay at each RPC provider's measured p95, not a static timeout.**
- **Devnet: since the hosted Anvil node is a single backend, decide whether the API layer needs a second RPC endpoint specifically to make hedging possible, because there's nothing to hedge against with one node.**
- **Rabbit: apply load shedding to the bundler/relayer for AA UserOperations — reject new ops fast once queued past a deadline, instead of letting session-key transactions queue unbounded during congestion.**

## ko
- **Verex: 계획대로 eth_call과 영수증 폴링에 헤지드 리퀘스트를 구현하고, 헤지 지연 시간은 고정 타임아웃이 아니라 각 RPC 프로바이더의 실측 p95 값으로 설정한다.**
- **Devnet: 호스팅된 Anvil 노드는 백엔드가 하나뿐이므로, 헤징을 가능하게 하려면 API 레이어에 별도 RPC 엔드포인트가 필요한지 결정한다. 노드가 하나면 헤지할 대상이 없다.**
- **Rabbit: AA UserOperation을 처리하는 번들러/릴레이어에 로드 셰딩을 적용한다.** 혼잡 시 세션 키 트랜잭션이 무한정 쌓이게 두지 말고, 데드라인을 넘겨 대기 중인 새 op은 빠르게 거부한다.
