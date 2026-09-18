## en
- **Verex: route split orders as min-cost max-flow, not a greedy allocator.** When a large order fills across multiple liquidity sources or market makers, model it as a flow problem rather than an ad hoc split.
- **Verex: net settlement obligations as min-cost flow before pushing on-chain transfers.** Add a test verifying the netted result matches gross obligations, so batching debts and credits actually reduces the number of on-chain transfers it claims to.
- **OFA: match solvers to intents as bipartite matching.** Reason about the auction's worst case with Dinic's/König's theorem rather than an unbounded search, when assigning solvers to competing intents.

## ko
- **Verex: 분할 주문을 그리디 할당이 아니라 최소비용 최대유량으로 라우팅한다.** 큰 주문이 여러 유동성 소스나 마켓 메이커에 걸쳐 체결될 때, 임기응변식 분할 대신 유량 문제로 모델링한다.
- **Verex: 온체인 송금 전에 정산 채무를 최소비용 유량으로 네팅한다.** 네팅된 결과가 총 채무와 일치하는지 검증하는 테스트를 추가해, 채무·채권 배치가 실제로 온체인 송금 수를 줄이는지 확인한다.
- **OFA: 솔버-인텐트 매칭을 이분 매칭으로 다룬다.** 경쟁하는 인텐트에 솔버를 배정할 때 무제한 탐색 대신 Dinic 알고리즘/쾨니그 정리로 경매의 최악의 경우를 추론한다.
