## en
- **Verex: treat Stripe onboarding as the actual identity join.** Log which addresses were bound to a verified identity, when, and by which check, since the chain itself never carries a name and Verex's onboarding is the one place it does.
- **Wallet + Verex: don't pool the join across services by default.** When Wallet addresses need to be checked against Verex's verified accounts, prefer a match/no-match query over sharing raw KYC records between the two repos.
- **Auditor: record the join, not just the transaction.** The methodology doc should name which identity provider verified which account for a given resolution or dispute, mirroring the operation's own finding that the participant list is the real artifact.

## ko
- **Verex: Stripe 온보딩을 실제 신원 결합(join)으로 취급한다.** 어떤 주소가 언제 어떤 검사로 검증된 신원과 묶였는지 기록한다. 체인 자체는 이름을 담지 않으며 Verex 온보딩이 그것을 담는 유일한 지점이기 때문이다.
- **Wallet + Verex: 기본적으로 서비스 간 결합을 풀링하지 않는다.** Wallet 주소를 Verex의 검증된 계정과 대조해야 한다면, 두 저장소 사이에 원본 KYC 기록을 공유하기보다 일치/불일치만 반환하는 쿼리를 우선한다.
- **Auditor: 트랜잭션이 아니라 결합 자체를 기록한다.** 방법론 문서에는 특정 정산이나 분쟁에 대해 어떤 신원 제공자가 어떤 계정을 검증했는지 명시한다. 이 작전에서 참가자 목록 자체가 진짜 산출물이었다는 발견과 같은 맥락이다.
