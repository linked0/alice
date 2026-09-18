## en
- **Verex: evaluate adopting OpenZeppelin Relayer for ChainJob's nonce/gas lane.** Relayer would delete the hand-rolled nonce sequencing, gas pricing, and retry ladder in ChainJob, but the onFailed DB-reversal logic has to stay, since no relayer can know a failed SETTLE_MATCH means two balances must be un-credited.
- **Verex: test whether widening ChainJob's single serial lane breaks business-logic ordering.** The lane was quietly serializing more than nonces; before parallelizing it, check for another balanceOf-timing bug like the one already found in the settlement ladder.
- **Auditor/gitboard: add Monitor-style on-chain alerting as a vendor-independence check.** OpenZeppelin Defender shutting down with a working open-source successor is the "what remains when the vendor leaves" test — apply it to any other managed service Jayverse depends on.

## ko
- **Verex: ChainJob의 논스/가스 레인에 OpenZeppelin Relayer 도입을 검토한다.** Relayer는 ChainJob에 손으로 짠 논스 시퀀싱, 가스 가격 책정, 재시도 사다리를 없애줄 수 있지만, onFailed의 DB 롤백 로직은 남아야 한다. 실패한 SETTLE_MATCH가 두 사용자의 잔액을 되돌려야 한다는 것을 어떤 릴레이어도 알 수 없기 때문이다.
- **Verex: ChainJob의 단일 직렬 레인을 넓혔을 때 비즈니스 로직 순서가 깨지는지 테스트한다.** 그 레인은 논스만이 아니라 더 많은 것을 조용히 직렬화하고 있었다. 병렬화하기 전에, 정산 사다리에서 이미 발견된 정산 전 balanceOf 타이밍 버그 같은 것이 또 있는지 확인한다.
- **Auditor/gitboard: Monitor식 온체인 알림을 벤더 독립성 점검으로 추가한다.** OpenZeppelin Defender가 작동하는 오픈소스 후속작을 남기고 종료된 것은 "벤더가 떠나면 무엇이 남는가" 테스트이며, Jayverse가 의존하는 다른 관리형 서비스에도 이 테스트를 적용한다.
