## en
- **Verex: write down which PCS (KZG vs FRI) is chosen for rollup-style settlement proofs, and why, as an Auditor-style methodology note.** Gas cost and trust assumptions are one decision — record it, don't just pick it.
- **Devnet: prototype the settlement-proof PoC on devnet first, one market's worth of matches, before committing to a PCS.** A trusted-setup requirement (KZG) is a one-way door once anything is mainnet-adjacent.
- **Auditor: once a PCS is chosen, track proof size and verifier gas cost as a recurring regression check.** So on-chain settlement cost doesn't silently drift as the circuit grows.

## ko
- **Verex: 롤업식 정산 증명에 어떤 PCS(KZG vs FRI)를 선택했는지, 왜 선택했는지를 Auditor 스타일 방법론 노트로 적어둔다.** 가스 비용과 신뢰 가정은 하나의 결정이다. 그냥 고르지 말고 기록한다.
- **Devnet: PCS를 확정하기 전에 마켓 하나 분량의 매칭으로 정산 증명 PoC를 devnet에서 먼저 시제작한다.** 트러스티드 세팅업 요구사항(KZG)은 메인넷에 가까워지는 순간 되돌릴 수 없는 문이 된다.
- **Auditor: PCS를 선택한 후에는 증명 크기와 검증 가스 비용을 반복 회귀 검사 항목으로 추적한다.** 회로가 커지면서 온체인 정산 비용이 조용히 흘러가지 않도록 한다.
