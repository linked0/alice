## en
- **Rabbit: log the coupling, don't build for it yet.** Today's ERC-7702/7715 mandate contracts check `require(verify(sig, pubkey, hash))` directly against one scheme; note that assumption explicitly so a future move to proof-of-existence checking doesn't silently break mandate verification.
- **Auditor: record what was proven, not just that something was.** When a contract accepts "a proof exists," the methodology field must name which statement it proved, since the card's own warning is that a verified proof and a verified claim are not the same thing.
- **Devnet: a watch item, not an action.** Recursive-STARK-mempool verification is an L1-fork-level change; if the OP-Stack L2 target ever inherits it, mandate verification gas drops, but nothing on the current Anvil devnet needs to change for it yet.

## ko
- **Rabbit: 지금은 대비하지 말고, 결합만 기록해둔다.** 현재 ERC-7702/7715 mandate 컨트랙트는 `require(verify(sig, pubkey, hash))`로 하나의 서명 방식을 직접 검증한다. 이 가정을 명시적으로 남겨두면, 훗날 존재-증명 방식으로 바뀔 때 mandate 검증이 조용히 깨지지 않는다.
- **Auditor: 증명된 대상을 기록하지, 증명됐다는 사실만 기록하지 않는다.** 컨트랙트가 "증명이 존재한다"만 받아들일 경우, 방법론 필드는 어떤 명제가 증명됐는지 명시해야 한다. 이 카드의 경고 자체가 검증된 증명과 검증된 주장은 다르다는 것이기 때문이다.
- **Devnet: 실행 항목이 아니라 관찰 항목.** 재귀 STARK 멤풀 검증은 L1 포크 수준의 변경이다. OP-Stack L2 타깃이 훗날 이를 물려받으면 mandate 검증 가스가 낮아지지만, 현재 Anvil devnet에서는 지금 바꿀 것이 없다.
