## en
- **Verex: pick the settlement commitment scheme deliberately, and write down the cost.** KZG for smallest calldata if a trusted setup is acceptable, FRI if no-setup/post-quantum matters more than proof size — decide before building the off-chain batch settlement.
- **Devnet: benchmark commitment size vs verification gas on-chain.** Run both candidates through a devnet PoC before committing to one scheme in the contracts package.
- **Auditor: log the trust assumption of whichever scheme is chosen.** Trusted setup for KZG, hash assumptions for FRI — record it as a standing line in the settlement runbook.

## ko
- **Verex: 정산 커밋먼트 스킴을 의도적으로 고르고 비용을 적어둔다.** 트러스티드 세팅업을 감수할 수 있다면 콜데이터가 가장 작은 KZG, 증명 크기보다 세팅업 없음/양자내성이 더 중요하다면 FRI를 쓴다. 오프체인 배치 정산을 만들기 전에 결정한다.
- **Devnet: 온체인에서 커밋먼트 크기 대 검증 가스를 벤치마크한다.** 컨트랙트 패키지에서 하나의 스킴으로 확정하기 전에 두 후보를 devnet PoC로 돌려본다.
- **Auditor: 선택한 스킴의 신뢰 가정을 기록한다.** KZG는 트러스티드 세팅업, FRI는 해시 가정을 정산 런북에 상시 항목으로 남긴다.
