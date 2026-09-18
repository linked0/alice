## en
- **Devnet: pick and document the force-inclusion window before it's needed.** When Devnet moves from Anvil-on-Sepolia to a real OP-Stack L2, the force-inclusion delay window becomes a concrete parameter Verex settlement depends on, not a detail to leave for later.
- **Verex: test the redeem path through forced inclusion, not just document it.** Submit a forced-inclusion transaction on testnet for the oracle-result redeem flow specifically, since that path is where a censored sequencer would strand user funds.
- **Auditor: add the censorship-window as a checked field.** Record the force-inclusion delay for any market whose settlement depends on L2 inclusion, alongside the resolution methodology it already tracks.

## ko
- **Devnet: 필요해지기 전에 강제포함 윈도우를 정하고 문서화한다.** Devnet이 Anvil-on-Sepolia에서 실제 OP-Stack L2로 옮겨가면, 강제포함 지연 윈도우는 나중에 남겨둘 디테일이 아니라 Verex 정산이 의존하는 구체적 파라미터가 된다.
- **Verex: redeem 경로를 문서화만 하지 말고 강제포함으로 실제 테스트한다.** 오라클 결과 redeem 플로우에 대해 테스트넷에서 강제포함 트랜잭션을 직접 제출해본다. 시퀀서가 검열할 경우 사용자 자금이 묶이는 지점이 바로 이 경로이기 때문이다.
- **Auditor: 검열 윈도우를 점검 항목에 추가한다.** L2 인클루전에 정산이 의존하는 모든 마켓에 대해, 이미 추적 중인 정산 방법론 옆에 강제포함 지연 시간을 기록한다.
