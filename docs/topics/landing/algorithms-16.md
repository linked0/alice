## en
- **Verex: document which specific heuristic batch-matching uses (e.g., greedy by price-time priority) along with its known approximation ratio, instead of an ad hoc matching loop; note that an exact ILP/SAT solver stays exponential-worst-case and isn't a real fallback at scale.**
- **Auditor: since P != NP, require the batch-matching module's doc to state its heuristic and rationale, so market-quality complaints don't turn into an attempt to optimize an impossible exact solution.**
- **OFA: identify which known NP-complete problem (e.g., knapsack, set packing) the solver/auction's bundle-selection reduces from, before choosing its heuristic.**

## ko
- **Verex: 배치 매칭에 쓰는 구체적 휴리스틱(예: 가격-시간 우선순위 그리디)과 그 근사 비율을 문서화한다.** 임의의 매칭 루프 대신, 정확한 ILP/SAT 솔버는 최악의 경우 여전히 지수 시간이라 규모가 커지면 실질적 대안이 아님을 적어둔다.
- **Auditor: P ≠ NP이므로 배치 매칭 모듈 문서에 어떤 휴리스틱을 왜 쓰는지 명시하도록 요구한다.** 그래야 시장 품질 불만이 불가능한 정확 해를 최적화하려는 시도로 이어지지 않는다.
- **OFA: 솔버/경매의 번들 선택 문제가 어떤 알려진 NP-완전 문제(예: 배낭 문제, 집합 패킹)로부터 환원되는지 먼저 식별한 뒤 휴리스틱을 선택한다.**
