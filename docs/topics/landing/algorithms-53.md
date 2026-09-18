## en
- **Verex: adopt a single sequencer or HLC-stamped events for the matching service.** Write a test that deliberately induces clock skew across API instances and confirms order sequencing never reverses.
- **Devnet: use devnet as the fixture for the 3-node concurrency exercise.** Run multiple matching-API instances against the shared devnet chain and find the event pairs only a vector clock or HLC would catch, before production traffic does.
- **gitboard: expose HLC drift as a health metric.** A growing gap between logical and physical time is the early signal that skew is approaching what the matching engine assumes it can tolerate.

## ko
- **Verex: 매칭 서비스에 단일 시퀀서나 HLC 타임스탬프 이벤트를 채택한다.** API 인스턴스 간에 의도적으로 클록 스큐를 유발하는 테스트를 작성해서 주문 순서가 절대 뒤집히지 않는지 확인한다.
- **Devnet: 3노드 동시성 연습의 픽스처로 devnet을 쓴다.** 공유 devnet 체인에 대해 여러 매칭 API 인스턴스를 돌려서, 벡터 클록이나 HLC만이 잡아낼 이벤트 쌍을 프로덕션 트래픽이 겪기 전에 찾아낸다.
- **gitboard: HLC 드리프트를 헬스 지표로 노출한다.** 논리 시간과 물리 시간의 격차가 커지는 것은 스큐가 매칭 엔진이 견딜 수 있다고 가정한 한계에 다가가고 있다는 조기 신호다.
