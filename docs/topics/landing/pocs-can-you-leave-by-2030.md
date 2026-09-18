## en
- **Bridge/Token: write the exit clause before the lock-in chain forms.** Before Anvil<->Sepolia contracts, account structures and relayer back-office all get built around one shape, decide now what a future migration (a new chain, a new token contract, a move off devnet) would require, so a later redesign isn't blocked by its own sunk cost.
- **Verex: state settlement invariants, not implementation locks, if Verex ever targets Korean users.** Model the resolution and payout rules on "no duplicate issuance of the same right" rather than "no movement between venues," the same rewrite this card asks of the enforcement decree, so a jurisdiction rule doesn't accidentally become a permanent architecture constraint.
- **Number: track the KR token-securities enforcement decree as a watched item, not a design input yet.** Log whether the eventual decree scores against the five exit asks (re-evaluation clause, verified migration, open APIs, tech-neutral criteria, an interop sandbox before 2027) since it sets the regulatory ceiling any distributed reading or investment product would operate under.

## ko
- **Bridge/Token: 락인 체인이 굳기 전에 탈출 조항부터 적는다.** Anvil↔Sepolia 컨트랙트, 계정 구조, 릴레이어 백오피스가 모두 하나의 형태로 굳어지기 전에, 앞으로의 마이그레이션(새 체인, 새 토큰 컨트랙트, devnet 이탈)에 무엇이 필요할지 지금 정해서, 나중의 재설계가 자기 자신의 매몰비용에 막히지 않게 한다.
- **Verex: 한국 사용자를 대상으로 한다면 구현 잠금이 아니라 정산 불변식을 명시한다.** "거래소 간 이동 금지"가 아니라 "같은 권리의 중복 발행 금지"를 기준으로 정산·지급 규칙을 설계한다. 이 카드가 시행령에 요구하는 것과 같은 재작성이며, 관할권 규칙이 뜻하지 않게 영구적인 아키텍처 제약이 되는 것을 막는다.
- **Number: 한국 토큰증권 시행령을 아직 설계 입력이 아니라 감시 항목으로 추적한다.** 최종 시행령이 다섯 가지 탈출 요구(재평가 조항, 검증된 마이그레이션, 오픈 API, 기술중립 기준, 2027년 전 상호운용 샌드박스)에 몇 점을 받는지 기록한다. 이것이 배포되는 읽기나 투자 상품이 놓일 규제 천장을 정하기 때문이다.
