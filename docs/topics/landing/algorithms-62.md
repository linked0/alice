## en
- **Verex: build the settlement watcher on state proofs, not on trusting a single RPC response.** Verify positions and settlement results with an eth_getProof-style inclusion proof against the header's stateRoot, which removes the RPC provider from the trust set entirely.
- **Wallet: verify any balance simulate-before-sign shows via Merkle proof, not a raw RPC read.** Same fix as the watcher — the wallet's displayed state shouldn't depend on trusting whichever node answered.
- **Devnet: note that witness size becomes the bottleneck once Devnet moves to a real OP-Stack L2.** Track whether that future chain adopts Verkle trees or STARK-based commitments, since that decides how cheap Verex's light-client-style verification can be.

## ko
- **Verex: 결제 워처를 단일 RPC 응답을 신뢰하는 대신 상태 증명 위에 만든다.** 포지션과 정산 결과를 헤더의 stateRoot에 대한 eth_getProof 방식 포함 증명으로 검증하면 RPC 제공자를 신뢰 집합에서 완전히 제거할 수 있다.
- **Wallet: 서명 전 시뮬레이션이 보여주는 잔액도 raw RPC 읽기가 아니라 머클 증명으로 검증한다.** 워처와 같은 해법이다. Wallet이 보여주는 상태가 어느 노드가 응답했는지에 의존해서는 안 된다.
- **Devnet: Devnet이 실제 OP-Stack L2로 옮겨가면 증인 크기가 병목이 된다는 점을 기록해둔다.** 그 미래 체인이 Verkle 트리나 STARK 기반 커밋먼트를 채택하는지 추적한다. 이것이 Verex의 라이트 클라이언트식 검증이 얼마나 저렴할 수 있는지를 결정한다.
