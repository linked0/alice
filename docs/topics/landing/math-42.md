## en
- **Bridge: model the lock-and-mint state machine as a Markov chain.** Estimate expected time-to-finality and its tail for pending → finalized → minted, feeding directly into the refill-rate window design.
- **Rabbit: use absorption probabilities for mandate/session-key expiry.** A mandate ends executed, expired, or revoked — compute expected time-to-absorption to size default session-key expiry windows.
- **Verex: model the settlement queue the same way.** Estimate expected wait before inclusion from transition probabilities instead of assuming a fixed block count.

## ko
- **Bridge: 락앤민트 상태 머신을 마르코프 체인으로 모델링한다.** 대기 → 확정 → 민팅 상태에 대해 기대 확정 시간과 그 테일을 추정해 리필 레이트 윈도우 설계에 바로 반영한다.
- **Rabbit: 위임/세션 키 만료에 흡수 확률을 사용한다.** 위임은 실행됨, 만료됨, 철회됨 중 하나로 끝난다. 기대 흡수 시간을 계산해 기본 세션 키 만료 윈도우 크기를 정한다.
- **Verex: 정산 큐도 같은 방식으로 모델링한다.** 고정 블록 수를 가정하는 대신 전이 확률로부터 포함까지 기대 대기 시간을 추정한다.
