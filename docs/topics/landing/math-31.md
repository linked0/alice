## en
- **DeFi: hard-cap Newton iterations and pick the rounding direction explicitly.** For any invariant with no closed form (a StableSwap-style pool, a rebasing index), round in the protocol's favor and write a test for the extremely-imbalanced-reserves case the exercise asks about.
- **Verex: treat the iteration cap and tolerance as security parameters if the market maker ever needs an iterative solve.** Document them in the contract instead of tuning purely for gas.
- **CI: add a fuzz test that feeds extreme or imbalanced inputs to any on-chain Newton-method solver.** Assert it either converges within the capped iterations or reverts cleanly, never loops or returns a stale value.

## ko
- **DeFi: 뉴턴 반복 횟수를 상한으로 고정하고 반올림 방향을 명시적으로 정한다.** 닫힌 해가 없는 불변식(StableSwap류 풀, 리베이싱 인덱스)은 프로토콜에 유리한 방향으로 반올림하고, 연습문제가 묻는 극단적으로 불균형한 준비금 케이스에 대한 테스트를 작성한다.
- **Verex: 마켓 메이커에 반복적 계산이 필요해지면 반복 상한과 수렴 허용오차를 보안 파라미터로 다룬다.** 가스만 보고 튜닝하지 말고 컨트랙트에 문서화한다.
- **CI: 온체인 뉴턴법 솔버에 극단적/불균형 입력을 넣는 퍼즈 테스트를 추가한다.** 상한 내에서 수렴하거나 깔끔하게 되돌리는지 검증하고, 루프에 빠지거나 오래된 값을 반환하지 않는지 확인한다.
