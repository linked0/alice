## en
- **Devnet: build the reorg PoC (evm_snapshot → mine → evm_revert → mine) as a standard test harness.** Reuse it for any indexer Jayverse ships — Verex's order book, Rabbit's session-key events — rather than building the reorg test once and forgetting it.
- **Verex: before trusting any indexer as the source of truth for order-book or balance state, add a byte-for-byte replay-vs-rebuild test to CI.** Check derived rows (balances, positions), not raw event rows — that's where reorg bugs actually live.
- **Devnet/Rabbit: size the reorg rollback window to the chain's actual finality lag.** Only the unfinalized window can be orphaned, so that bounds how much undo machinery any Jayverse indexer needs to keep, on both the Anvil fork today and the OP-Stack L2 later.
- **gitboard: add "last clean replay passed" as a per-service indexer status row.** It's the pass/fail signal this page's PoC produces, and it belongs on the dashboard, not just in a test log.

## ko
- **Devnet: 리오그 PoC(evm_snapshot → 마이닝 → evm_revert → 마이닝)를 표준 테스트 하네스로 만든다.** Verex의 오더북, Rabbit의 세션 키 이벤트 등 Jayverse가 배포하는 모든 인덱서에 재사용한다. 한 번 만들고 잊어버리지 않는다.
- **Verex: 오더북이나 잔고 상태의 진실 소스로 인덱서를 신뢰하기 전에 바이트 단위 리플레이-대-재구축 테스트를 CI에 추가한다.** 원시 이벤트 행이 아니라 파생 행(잔고, 포지션)을 검사한다. 리오그 버그가 실제로 사는 곳이다.
- **Devnet/Rabbit: 리오그 롤백 윈도우를 체인의 실제 파이널리티 지연에 맞춘다.** 파이널리티 되지 않은 구간만 고아가 될 수 있으므로, 지금의 Anvil 포크와 이후의 OP-Stack L2 모두에서 어느 정도의 언두 장치가 필요한지가 이걸로 정해진다.
- **gitboard: "마지막 클린 리플레이 통과"를 서비스별 인덱서 상태 행으로 추가한다.** 이 페이지의 PoC가 만들어내는 합격/불합격 신호이며, 테스트 로그가 아니라 대시보드에 있어야 한다.
