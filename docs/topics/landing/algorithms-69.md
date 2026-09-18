## en
- **Verex: audit every "read then write based on it" path for write skew.** Remaining order quantity and collateral/margin checks are the textbook case; lock the rows involved or run those checks at SERIALIZABLE isolation under concurrent load.
- **Verex: physicalize on-chain invariants as a single atomic state update.** Don't assume a balance or collateral invariant is safe just because it is on-chain; enforce it as one check-and-set on one storage slot.
- **Auditor: add a standing write-skew reproduction test for any new off-chain service.** Reproduce a concurrent-session violation of a balance-sum invariant before shipping, rather than trusting an isolation level's name.

## ko
- **Verex: "읽고 그 값을 근거로 쓰는" 모든 경로에서 쓰기 왜곡(write skew)을 점검한다.** 남은 주문 수량과 담보/마진 체크가 교과서적 사례이며, 해당 행을 잠그거나 동시 부하 하에서 SERIALIZABLE 격리 수준으로 실행한다.
- **Verex: 온체인 불변식을 단일 원자적 상태 업데이트로 물리화한다.** 온체인이라는 이유만으로 잔고나 담보 불변식이 안전하다고 가정하지 않고, 하나의 스토리지 슬롯에 대한 단일 체크-앤-셋으로 강제한다.
- **Auditor: 새 오프체인 서비스마다 상시 write skew 재현 테스트를 추가한다.** 격리 수준의 이름을 믿는 대신, 출시 전에 잔고 합 불변식을 위반하는 동시 세션을 재현해본다.
