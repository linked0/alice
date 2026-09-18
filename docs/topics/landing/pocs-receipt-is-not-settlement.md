## en
- **Verex: credit reversible ledger entries at included, pay out at finalized.** Encode the six-state machine (detected/included/safe/finalized/reorged/pending-reinclusion) so a bet credits early but a withdrawal or other irreversible payout waits for the configured finality tier, not a single paid boolean.
- **Wallet: record which tier a given action requires, per chain.** Included versus finalized means different clocks on Sepolia today than on the future OP-Stack Devnet L2, so the simulate-before-sign flow needs a per-chain policy table, not one global setting.
- **Devnet: build the reorg test locally before it ships.** Use anvil's snapshot/revert or anvil_reorg to mine a payment, revert it, and re-mine without it, then assert the indexer notices the receipt vanish — the same rehearsal the Liquid-issuance invariant work needs.

## ko
- **Verex: 가역적 원장 항목은 included에서, 지급은 finalized에서 한다.** 여섯 단계 상태 머신(detected/included/safe/finalized/reorged/pending-reinclusion)을 인코딩해서, 베팅은 일찍 크레딧되지만 출금 같은 비가역 지급은 하나의 paid 불리언이 아니라 설정된 파이널리티 단계를 기다리게 한다.
- **Wallet: 어떤 동작이 어느 단계를 요구하는지 체인별로 기록한다.** included와 finalized 사이의 시간은 오늘의 Sepolia와 향후 OP-Stack Devnet L2에서 서로 다른 시계를 의미하므로, 서명 전 시뮬레이션 플로우는 전역 설정 하나가 아니라 체인별 정책 표가 필요하다.
- **Devnet: 출시 전에 리오그 테스트를 로컬에서 만들어둔다.** anvil의 snapshot/revert나 anvil_reorg로 결제를 채굴하고, 되돌리고, 그것 없이 다시 채굴한 뒤, 인덱서가 영수증이 사라진 것을 알아채는지 확인한다. Liquid 발행 불변식 작업에 필요한 것과 같은 리허설이다.
