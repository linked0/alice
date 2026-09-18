## en
- **Devnet: when moving from forked Anvil to an OP-Stack L2, write down which finality model it inherits.** Probabilistic like L1, or BFT-style instant finality from the sequencer — that decides every downstream confirmation-depth policy.
- **Verex: set settlement confirmation-depth policy explicitly per chain.** Don't reuse an Ethereum-style probabilistic-finality wait time on a chain with instant finality, and don't assume instant finality where it doesn't hold.
- **Bridge: justify the lock-and-mint relayer's "safe to mint" threshold by the source chain's actual quorum/finality assumptions.** Not a fixed block-confirmation constant copied from elsewhere.

## ko
- **Devnet: 포크된 Anvil에서 OP-Stack L2로 옮길 때 어떤 파이널리티 모델을 물려받는지 명시한다.** L1처럼 확률적인지, 시퀀서의 BFT식 즉시 파이널리티인지가 이후의 모든 컨펌 깊이 정책을 결정한다.
- **Verex: 정산 컨펌 깊이 정책을 체인별로 명시적으로 정한다.** 즉시 파이널리티를 가진 체인에 이더리움식 확률적 파이널리티 대기 시간을 재사용하지 않고, 즉시 파이널리티가 없는 체인에서 있다고 가정하지도 않는다.
- **Bridge: lock-and-mint 릴레이어의 "민팅해도 안전함" 임계값을 소스 체인의 실제 쿼럼/파이널리티 가정으로 정당화한다.** 다른 곳에서 복사한 고정 블록 컨펌 상수가 아니다.
