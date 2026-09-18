## en
- **Verex: if the CLOB matching engine or its price indexer ever runs multiple instances, serve reads with a ReadIndex-style majority confirmation, not a naive "ask the current leader."** The card's stale-read problem is exactly what a multi-instance matching engine hits right after a leader change.
- **Devnet: add explicit membership-change handling before ever running multiple Anvil/RPC nodes with a leader.** Use joint consensus or one-node-at-a-time changes so a live migration can't form two majorities and split-brain, the failure this page names as the most common.
- **gitboard: choose lease-read speed or ReadIndex safety explicitly for "latest state."** If a stale gitboard view is tolerable, cache with a lease; if not, confirm via a full read before serving it.

## ko
- **Verex: CLOB 매칭 엔진이나 가격 인덱서가 여러 인스턴스로 돌아간다면, "지금 리더에게 물어본다" 식이 아니라 ReadIndex 방식의 과반수 확인으로 읽기를 서비스한다.** 이 카드가 말하는 stale read 문제는 리더 교체 직후 멀티 인스턴스 매칭 엔진이 바로 겪는 문제다.
- **Devnet: 리더가 있는 Anvil/RPC 노드를 여러 개 운영하기 전에 멤버십 변경 처리를 명시적으로 추가한다.** joint consensus나 한 번에 한 노드씩 바꾸는 방식을 써서, 라이브 마이그레이션이 두 개의 과반수를 만들어 split-brain을 일으키지 않게 한다. 이 페이지가 가장 흔한 실패로 꼽는 것이다.
- **gitboard: "최신 상태"에 대해 lease read의 속도와 ReadIndex의 안전성 중 무엇을 쓸지 명시적으로 정한다.** gitboard 화면이 약간 오래돼도 괜찮다면 lease로 캐시하고, 아니라면 서비스하기 전에 전체 읽기로 확인한다.
