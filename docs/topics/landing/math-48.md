## en
- **Verex: if the market maker or settlement path ever aggregates BLS signatures or posts KZG-style commitments, document the trusted setup's parameters and administrator as part of the resolution methodology.** A leaked SRS secret breaks the whole proof silently, so it belongs in the trust-assumption list, not left implicit.
- **Auditor: check that verification cost is actually cheaper than re-execution for the specific circuit used.** The card's core claim only holds when this is confirmed per use case, not assumed because it's "a pairing-based system."
- **Bridge: name the trusted-setup dependency for any blob or commitment structure the Anvil-Sepolia relayer or a future L2 posting relies on.** Treat it as a fourth attack surface next to the relayer key and the multisig, not a separate cryptography concern.

## ko
- **Verex: 마켓 메이커나 정산 경로가 BLS 서명을 집계하거나 KZG 방식 커밋먼트를 게시한다면, trusted setup의 파라미터와 관리자를 정산 방법론의 일부로 문서화한다.** SRS 비밀이 유출되면 증명 전체가 조용히 깨지므로, 암묵적으로 두지 말고 신뢰 가정 목록에 명시한다.
- **Auditor: 사용된 구체적 회로에서 검증 비용이 실제로 재실행보다 싼지 확인한다.** 이 카드의 핵심 주장은 사용 사례별로 확인됐을 때만 성립하지, "페어링 기반 시스템이니까"로 가정해서는 안 된다.
- **Bridge: Anvil-Sepolia 릴레이어나 향후 L2 게시가 의존하는 blob이나 커밋먼트 구조의 trusted-setup 의존성을 명시한다.** 이를 릴레이어 키, 멀티시그 옆의 네 번째 공격 표면으로 다루지, 별개의 암호학 문제로 취급하지 않는다.
