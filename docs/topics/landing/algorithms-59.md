## en
- **Bridge: define the exact finality wait for lock-and-mint release in epochs, not just confirmed blocks.** On Sepolia, require the lock event's checkpoint to be finalized before the relayer mints; align that depth with whatever the Devnet's forked chain or a future OP-Stack L2 sequencer provides.
- **Rabbit: mark session-key and mandate-triggered events as provisional until finalized.** Events between head and finalized should sit in a provisional state in Rabbit's own indexer, promoted to settled only once Casper FFG finality is reached.
- **Devnet: script a synthetic unfinalize test.** Since a single-node Anvil fork has no real Casper FFG voting, roll back N blocks to confirm Bridge and Rabbit indexers actually handle a reorg of already-indexed, not-yet-finalized events instead of assuming devnet never reorgs.

## ko
- **Bridge: lock-and-mint 방출의 파이널리티 대기를 확정 블록 수가 아니라 epoch 단위로 정의한다.** Sepolia에서는 락 이벤트의 체크포인트가 finalized 될 때까지 기다린 뒤 릴레이어가 민팅하게 하고, 그 깊이를 Devnet의 포크 체인이나 향후 OP-Stack L2 시퀀서가 제공하는 값에 맞춘다.
- **Rabbit: 세션 키/mandate로 발생한 이벤트를 finalized 전까지 잠정 상태로 표시한다.** head와 finalized 사이의 이벤트는 Rabbit 자체 인덱서에서 잠정 상태로 두고, Casper FFG 파이널리티에 도달해야만 확정 상태로 승격한다.
- **Devnet: 인위적인 unfinalize 테스트를 스크립트로 만든다.** 단일 노드 Anvil 포크에는 실제 Casper FFG 투표가 없으므로, N개 블록을 되돌려 Bridge와 Rabbit 인덱서가 이미 인덱싱했지만 아직 finalized 안 된 이벤트의 재구성을 실제로 처리하는지 확인한다. devnet은 리오그가 없다고 가정하지 않는다.
