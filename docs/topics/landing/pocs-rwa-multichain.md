## en
- **Bridge: adopt the allocator pattern, not reconciliation.** JYVE's Anvil-to-Sepolia lock-and-mint should have the locking side issue a signed, nonce-bearing mint allocation before mint, with the receiving contract checking minted <= allocation locally — no cross-chain call, no after-the-fact audit needed.
- **Devnet: test the stranded-allocation failure.** Simulate one side of the bridge halting after an allocation is granted but unminted, and confirm the relayer cannot silently re-issue that allocation without a defined challenge window and evidence standard.
- **Auditor: assert the global cap as a single-party check.** The relayer or registry keeping sum(allocations) <= locked supply is the invariant Auditor should verify on every bridge state snapshot, separate from each chain's local minted <= allocation check.

## ko
- **Bridge: 사후 대사가 아니라 할당자 패턴을 쓴다.** JYVE의 Anvil-Sepolia lock-and-mint은 락을 거는 쪽이 민팅 전에 서명되고 nonce가 있는 민팅 할당량을 발급하고, 받는 쪽 컨트랙트는 로컬에서 minted <= allocation만 확인하게 한다. 체인 간 호출도, 사후 감사도 필요 없다.
- **Devnet: stranded-allocation 실패를 테스트한다.** 할당은 됐지만 아직 민팅되지 않은 상태에서 브릿지 한쪽이 멈추는 상황을 시뮬레이션하고, 정의된 챌린지 기간과 증빙 기준 없이는 릴레이어가 그 할당을 조용히 재발급할 수 없음을 확인한다.
- **Auditor: 전역 상한을 단일 주체 체크로 검증한다.** 릴레이어나 레지스트리가 sum(allocations) <= locked supply를 지키는지가 Auditor가 모든 브릿지 상태 스냅샷에서 확인해야 할 불변식이며, 각 체인의 로컬 minted <= allocation 체크와는 별개다.
