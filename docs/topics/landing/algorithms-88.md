## en
- **Verex/Auditor: choose Montgomery vs. Barrett by the actual access pattern.** If Verex ever adds a ZK-based resolution or privacy feature, benchmark both against the specific modulus used — Montgomery for repeated multiplications under one modulus, Barrett for one-off reductions — rather than defaulting to one.
- **Auditor: add constant-time verification to the review checklist.** Any custom elliptic-curve or modular-exponentiation code that bypasses the standard EVM precompiles must be checked for branching on secret values, since timing leaks are the risk the card names explicitly.
- **DeFi: prefer the standard precompiles over hand-rolled bignum math.** Where DeFi's algorithms need modular exponentiation, route through Ethereum's priced precompiles rather than a custom implementation, since their gas pricing already reflects this layer's real cost.

## ko
- **Verex/Auditor: 실제 접근 패턴에 따라 몽고메리와 바렛 중 고른다.** Verex가 ZK 기반 정산이나 프라이버시 기능을 추가한다면, 사용하는 실제 모듈러스를 놓고 둘 다 벤치마크한다. 같은 모듈러스로 반복 곱셈이 많다면 몽고메리, 일회성 환원이면 바렛을 쓴다. 하나를 기본값으로 정하지 않는다.
- **Auditor: 상수 시간 검증을 리뷰 체크리스트에 추가한다.** 표준 EVM 프리컴파일을 우회하는 타원곡선·모듈러 거듭제곱 커스텀 코드는 비밀값에 따라 분기하지 않는지 확인해야 한다. 카드가 명시하는 위험이 타이밍 누출이기 때문이다.
- **DeFi: 직접 만든 bignum 수학보다 표준 프리컴파일을 우선한다.** DeFi 알고리즘이 모듈러 거듭제곱이 필요하다면 커스텀 구현 대신 이더리움의 가격 매겨진 프리컴파일을 거친다. 그 가스 가격이 이미 이 계층의 실제 비용을 반영하고 있기 때문이다.
