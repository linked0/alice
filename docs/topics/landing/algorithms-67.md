## en
- **Bridge: apply the outbox pattern to the lock-and-mint relayer.** Commit the lock event and the mint-request message in one DB transaction, and make mint processing on the receiving chain idempotent, the same fix Verex needs for settlement.
- **Rabbit: attach an idempotency key to UserOp/bundler retries.** A resubmitted mandate execution should not double-execute when the bundler retries the same operation.
- **CI: require the kill-and-restart idempotency test on any service with retries.** Standardize "force-kill right after publish, restart, verify exactly one effect" as a required test for Verex settlement and the Bridge relayer alike, not a one-off exercise.

## ko
- **Bridge: lock-and-mint 릴레이어에 outbox 패턴을 적용한다.** lock 이벤트와 민트 요청 메시지를 하나의 DB 트랜잭션으로 커밋하고, 수신 체인의 민트 처리를 멱등하게 만든다. Verex 정산에 필요한 것과 같은 수정이다.
- **Rabbit: UserOp/번들러 재시도에 idempotency key를 붙인다.** 번들러가 같은 작업을 재시도할 때 재제출된 mandate 실행이 중복 실행되지 않게 한다.
- **CI: 재시도가 있는 모든 서비스에 kill-and-restart 멱등성 테스트를 요구한다.** "게시 직후 강제 종료, 재시작, 효과가 정확히 한 번인지 확인"을 Verex 정산과 Bridge 릴레이어 모두에 대한 필수 테스트로 표준화한다. 일회성 연습문제로 남기지 않는다.
