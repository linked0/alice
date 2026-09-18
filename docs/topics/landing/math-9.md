## en
- **Verex: compute multi-outcome market payout and outcome counts with the exact permutation and C(n,k) formulas here, not an approximation.** An off-by-one in outcome counting directly misprices a market.
- **Bridge: size relayer quorum thresholds, and OFA solver-set quorum, as a direct binomial-coefficient calculation.** Not by picking a round number.
- **CI: apply the birthday-problem bound from this page to any ID or hash scheme — market IDs, session-key nonces.** This sizes the space needed for negligible collision probability.

## ko
- **Verex: 다중 결과 마켓의 지급과 결과 경우의 수는 근사치가 아니라 이 페이지의 순열·C(n,k) 공식으로 정확히 계산한다.** 경우의 수 계산에서 하나만 틀려도 마켓 가격이 바로 잘못 매겨지기 때문이다.
- **Bridge: 릴레이어 쿼럼 임계값과 OFA 솔버 집합의 쿼럼은 이항계수 계산으로 직접 산정한다.** 적당한 반올림 숫자를 고르는 대신 이렇게 한다.
- **CI: 이 페이지의 생일 문제 한계를 마켓 ID, 세션 키 nonce 같은 모든 ID·해시 체계에 적용한다.** 충돌 확률을 무시할 수준으로 만드는 데 필요한 공간 크기를 정한다.
