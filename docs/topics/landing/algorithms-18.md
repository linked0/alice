## en
- **Verex: exhaustively enumerate order-state flag combinations in Foundry tests.** Instead of sampling, generate every combination of order-state flags (open/partial/cancelled x maker/taker x resolved/unresolved) as branch tests, using the Gray-code/XOR trick as the generator.
- **Wallet: exhaustively test session-key/mandate permission combinations.** EIP-7702/7715 permission-flag combinations are a small finite space; enumerate them all in tests rather than fuzzing, per the page's own claim that exhaustive coverage beats random fuzzing there.
- **Rabbit: use minimal-change ordering in the mandate config test harness.** When stepping through option combinations for the Chains menu or mandate config, use Gray-code-style minimal-change ordering so each test state updates incrementally instead of recomputing from scratch.

## ko
- **Verex: 주문 상태 플래그 조합을 Foundry 테스트에서 모두 순회한다.** 샘플링 대신 주문 상태 플래그(오픈/부분체결/취소 x 메이커/테이커 x 정산/미정산)의 모든 조합을 그레이 코드/XOR 트릭을 생성기로 삼아 분기 테스트로 만든다.
- **Wallet: 세션 키/위임 권한 조합을 모두 테스트한다.** EIP-7702/7715 권한 플래그 조합은 작고 유한한 공간이므로, 퍼징 대신 모두 열거해 테스트한다. 이런 경우 전수 열거가 랜덤 퍼징보다 낫다는 페이지 자체의 주장을 따른다.
- **Rabbit: 위임 설정 테스트 하네스에 최소 변경 순서를 쓴다.** Chains 메뉴나 위임 설정의 옵션 조합을 순회할 때, 그레이 코드식 최소 변경 순서를 써서 매 테스트 상태를 처음부터 다시 계산하지 않고 증분으로 갱신한다.
