## en
- **Verex: keep price-triggered resolution and governance-triggered execution separate.** A market whose price directly causes a treasury or contract action is a decision market, not a prediction market — add a check that no Verex market resolution can itself trigger an on-chain action without a separate governance step.
- **Verex: require a manipulation-cost line for any threshold-gated market.** For a market with an execution threshold, compute capital-to-hold-price-above-threshold at current pool depth and at the depth needed to exceed the decision's value, and log both before launch.
- **Devnet: build the TWAP/No-Op formula as a small PoC contract.** Test the manipulation-cost inequality on devnet before trusting any price-triggered resolution path in production.

## ko
- **Verex: 가격 트리거 정산과 거버넌스 트리거 실행을 분리해 유지한다.** 가격이 직접 트레저리나 컨트랙트 액션을 일으키는 마켓은 예측 마켓이 아니라 디시전 마켓이다. 별도의 거버넌스 단계 없이는 어떤 Verex 마켓 정산도 온체인 액션을 스스로 트리거할 수 없도록 체크를 추가한다.
- **Verex: 실행 임계값이 있는 마켓에는 조작 비용 항목을 필수로 둔다.** 실행 임계값이 있는 마켓이라면 현재 풀 깊이와 디시전 가치를 초과하는 깊이 각각에서 가격을 임계값 위로 유지하는 데 필요한 자본을 계산해 출시 전에 둘 다 기록한다.
- **Devnet: TWAP/No-Op 공식을 작은 PoC 컨트랙트로 구현한다.** 프로덕션에서 가격 트리거 정산 경로를 신뢰하기 전에 devnet에서 조작 비용 부등식을 테스트한다.
