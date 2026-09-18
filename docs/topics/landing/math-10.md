## en
- **DeFi: set up compounding/reward-accrual formulas in jayverse-defi as explicit recurrences.** Solve for at least the growth rate, not only a simulation, to catch compounding bugs before they show up as a wrong balance.
- **Bridge: size the relayer's cross-chain confirmation backoff from the closed-form total-wait formula.** Don't tune retry/backoff by trial and error when the exercise's three methods (memoized recursion, iteration, closed form) already give the number.
- **OFA: write the recurrence for any nested or recursive auction step before implementing it.** A solver step that calls itself (recursive matching, nested clearing) should have its asymptotic cost known from the recurrence ahead of time, the same discipline Merkle-proof aggregation needs.

## ko
- **DeFi: jayverse-defi의 복리/리워드 적립 공식을 명시적 점화식으로 세운다.** 시뮬레이션만이 아니라 적어도 증가율을 풀어서 구해, 복리 버그가 잘못된 잔고로 드러나기 전에 잡는다.
- **Bridge: 릴레이어의 크로스체인 확인 백오프를 닫힌 형태의 총 대기시간 공식으로 사이즈한다.** 익서사이즈의 세 가지 방법(메모이제이션 재귀, 반복, 특성방정식 닫힌 형태)이 이미 답을 주는데 시행착오로 재시도/백오프를 튜닝하지 않는다.
- **OFA: 중첩되거나 재귀적인 경매 단계는 구현 전에 점화식부터 적는다.** 자기 자신을 호출하는 솔버 단계(재귀적 매칭, 중첩 클리어링)는 머클 증명 집계와 같은 규율로, 미리 점화식에서 점근적 비용을 알아둬야 한다.
