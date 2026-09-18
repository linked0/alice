## en
- **DeFi: add an ill-conditioning regression test for the exchange-rate math.** Assert relative error stays bounded as pool size or share price sweeps toward extreme values (near-zero liquidity, near-zero shares), not just a single happy-path check.
- **Verex: sweep the LMSR liquidity parameter toward its lower bound in tests.** Add a test that checks price and error don't blow up in fixed-point as b shrinks, catching the same amplification the card describes before it reaches production.
- **OFA: flag near-singular clearing computations explicitly.** If the solver auction's clearing math involves matrix-like operations, log an ill-conditioning check so a bad auction result is diagnosed as "bad problem" rather than "bad solver," since the fix differs.

## ko
- **DeFi: 교환 비율 수식에 조건수(ill-conditioning) 회귀 테스트를 추가한다.** 풀 크기나 지분 가격이 극단값(유동성 거의 0, 지분 수 거의 0)으로 갈 때도 상대 오차가 유계로 유지되는지 확인한다. 단일 정상 경로 테스트만으로는 부족하다.
- **Verex: LMSR 유동성 파라미터를 하한 쪽으로 스윕하는 테스트를 넣는다.** b가 작아질 때 고정소수점에서 가격과 오차가 폭발하지 않는지 확인하는 테스트를 추가해, 카드가 설명하는 증폭이 프로덕션에 닿기 전에 잡는다.
- **OFA: 거의 특이(singular)한 청산 계산을 명시적으로 표시한다.** 솔버 경매의 청산 수식이 행렬 형태의 연산을 포함한다면 조건수 체크를 로그로 남겨, 나쁜 경매 결과가 "나쁜 솔버"가 아니라 "나쁜 문제"로 진단되게 한다. 대응 방법이 다르기 때문이다.
