## en
- **Rabbit: thirdweb's paymaster only sponsors gas for 4337 accounts.** Since Rabbit's mandate story is built on 7702/7715 accounts, record that switching account types drops thirdweb's sponsored-gas pillar and needs its own paymaster.
- **Rabbit: tie the agent PoC's D1 gas decision to this exact tradeoff.** Document the 4337-vs-7702 account-type mismatch as the named reason for whichever paymaster path the agent PoC chooses, not just a footnote.
- **Game: evaluate thirdweb's Unity SDK against a direct chain integration before committing.** The Unity SDK is one candidate for the game's chain bridge; treat it as a benchmarked option, not the default, given the breadth-vs-best-in-class pattern this note names.

## ko
- **Rabbit: thirdweb의 paymaster는 4337 계정에만 가스를 후원한다.** Rabbit의 mandate 구조는 7702/7715 계정 위에 있으므로, 계정 타입을 바꾸면 thirdweb의 가스 후원 축이 빠지고 별도 paymaster가 필요하다는 것을 기록해 둔다.
- **Rabbit: 에이전트 PoC의 D1 가스 결정을 이 트레이드오프와 명시적으로 연결한다.** 4337 대 7702 계정 타입 불일치를 에이전트 PoC가 어떤 paymaster 경로를 택하든 그 이유로 문서화한다.
- **Game: thirdweb Unity SDK를 직접 체인 연동과 비교 평가한 뒤 채택한다.** Unity SDK는 게임의 체인 브리지 후보 중 하나다. 이 글이 말하는 범용성 대 최상 파트 패턴을 감안해 기본값이 아니라 벤치마크 대상으로 다룬다.
