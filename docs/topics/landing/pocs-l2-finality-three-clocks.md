## en
- **Bridge: gate minting on the L1-finalization clock, not on inclusion.** The lock-and-mint relayer should treat the Anvil-side lock the way OP Stack treats unsafe -> safe -> finalized, and only mint on Sepolia after finality, not the moment the lock transaction is included.
- **Wallet: replace a single "confirmed" badge with the unsafe/safe/finalized ladder.** UI feedback can ride the fast clock, but anything the Wallet treats as custody-affecting (a bridge release, a balance change) should wait for the finalized state, mirroring rpc-view-not-consensus and receipt-is-not-settlement.
- **Devnet: document which clock Devnet actually simulates today, and add the fourth clock when moving to an OP-Stack L2.** Anvil-forked-from-Sepolia has no real sequencer/finality ladder yet — write down that gap now so the future OP-Stack migration's test plan includes the withdrawal-proof clock, not just three.

## ko
- **Bridge: 민팅을 포함이 아니라 L1 파이널리티 클럭에 걸어둔다.** 락앤민트 릴레이어는 Anvil 쪽 락을 OP Stack이 unsafe -> safe -> finalized로 다루듯 취급해야 하고, 락 트랜잭션이 포함된 순간이 아니라 파이널리티 이후에만 Sepolia에 민팅한다.
- **Wallet: 단일 "확인됨" 배지를 unsafe/safe/finalized 사다리로 바꾼다.** UI 피드백은 빠른 클럭을 타도 되지만, Wallet이 커스터디에 영향을 준다고 보는 것(브리지 해제, 잔액 변경)은 rpc-view-not-consensus와 receipt-is-not-settlement처럼 finalized 상태를 기다려야 한다.
- **Devnet: Devnet이 오늘 실제로 시뮬레이션하는 클럭이 무엇인지 문서화하고, OP-Stack L2로 옮길 때 네 번째 클럭을 추가한다.** Sepolia를 포크한 Anvil에는 아직 실제 시퀀서/파이널리티 사다리가 없다. 이 간극을 지금 적어두면 나중 OP-Stack 마이그레이션의 테스트 계획에 출금 증명 클럭까지 세 개가 아니라 네 개가 포함된다.
