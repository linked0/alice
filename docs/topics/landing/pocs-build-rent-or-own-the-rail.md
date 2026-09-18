## en
- **Bridge: write down the failure state for a stuck mint.** The Anvil⇄Sepolia lock-and-mint relayer sits exactly on the mismatch this card describes — a lock is final onchain, so document now what happens when the mint leg fails after the lock succeeds, since no card-style chargeback exists to fall back on.
- **Devnet: check whether "own it" still scales down.** Devnet is Jayverse's own-it-together answer, a hosted Anvil forked from Sepolia; watch whether its running cost stays flat as more services depend on it, and decide the point at which renting a public testnet for some workloads beats owning devnet for all of them.
- **Verex: model the settlement leg, not just the authorization leg.** Stripe onboarding and CLOB matching are the reversible, message-based leg; onchain settlement is final. Write out the netting/float window between them explicitly, the way the card's card-settlement leg does, since that is where money actually sits before finality.

## ko
- **Bridge: 민팅이 멈췄을 때의 실패 상태를 미리 적어둔다.** Anvil⇄Sepolia 락앤민트 릴레이어는 이 카드가 말하는 불일치에 정확히 걸려 있다. 락은 온체인에서 최종적이므로, 락이 성공한 뒤 민트가 실패하면 어떻게 할지 지금 문서화한다. 카드 결제 같은 차지백이 존재하지 않기 때문이다.
- **Devnet: "직접 소유"가 계속 규모에 맞는지 점검한다.** Devnet은 Jayverse의 "함께 소유" 답이자 Sepolia를 포크한 호스팅 Anvil이다. 더 많은 서비스가 의존할수록 운영 비용이 평평하게 유지되는지 지켜보고, 일부 워크로드는 퍼블릭 테스트넷을 빌리는 편이 devnet 전체를 소유하는 것보다 나아지는 지점을 정한다.
- **Verex: 인증 구간이 아니라 정산 구간을 모델링한다.** Stripe 온보딩과 CLOB 매칭은 되돌릴 수 있는 메시지 기반 구간이고, 온체인 정산은 최종적이다. 카드의 카드 결제 구간처럼 둘 사이의 네팅·플로트 구간을 명시적으로 적는다. 파이널리티 전에 실제로 돈이 머무는 곳이기 때문이다.
