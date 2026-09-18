## en
- **Verex: label CLOB order-book state as eventually consistent pre-finality, and gate settlement or payout logic on finalized state only.** This matches the reorg risk this page names for pre-finality data.
- **Bridge: have the lock-and-mint relayer wait for source-chain finality before minting on the destination.** Treat pre-finality confirmations as a weaker guarantee than linearizable rather than as good enough.
- **gitboard: label any indexer-sourced dashboard figure as pre-finality or finalized.** So a reorg-able number is never displayed as settled.

## ko
- **Verex: CLOB 오더북 상태를 파이널리티 이전에는 최종적으로만 수렴하는 상태로 표시하고, 정산·지급 로직은 파이널라이즈된 상태에만 게이트한다.** 이 페이지가 파이널리티 이전 데이터에 대해 말하는 리오그 리스크와 같다.
- **Bridge: lock-and-mint 릴레이어가 목적지 체인에서 민팅하기 전에 소스 체인의 파이널리티를 기다리게 한다.** 파이널리티 이전 확인을 충분히 안전한 것이 아니라 linearizable보다 약한 보장으로 취급한다.
- **gitboard: 인덱서에서 가져온 모든 대시보드 수치에 파이널리티 이전인지 파이널라이즈됨인지 표시한다.** 리오그될 수 있는 숫자가 정산된 것처럼 보이지 않게 한다.
