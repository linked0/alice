## en
- **Bridge/Token: write the four-failure table for JYVE's Anvil⇄Sepolia bridge.** Custodian fails, relayer halts, relayer is compromised and mints, destination chain reorgs — for each, state what a holder sees and who can act without depending on the failed party.
- **Bridge/Token: publish Σ(supply across chains) ≤ locked reserve as a checked number, not an assumption.** Decide who besides the issuer can halt minting when the two disagree, and how often the number is published relative to how fast minting can happen.
- **Auditor: record whether the bridge design traded surface area for blast radius, explicitly.** A single relayer holding mint authority on every chain is a correlated-failure bet; write down that it was chosen on purpose, not defaulted into.

## ko
- **Bridge/Token: JYVE의 Anvil⇄Sepolia 브리지에 대해 4가지 실패 표를 작성한다.** 커스터디언 실패, 릴레이어 정지, 릴레이어 탈취 후 발행, 목적지 체인 재구성 각각에 대해 보유자가 무엇을 보게 되는지, 실패한 당사자에 의존하지 않고 누가 조치할 수 있는지 적는다.
- **Bridge/Token: 모든 체인의 공급량 합 ≤ 잠긴 준비금을 가정이 아니라 확인된 숫자로 공개한다.** 둘이 어긋날 때 발행자 외에 누가 발행을 멈출 수 있는지, 발행 속도 대비 이 숫자가 얼마나 자주 공개되는지 정한다.
- **Auditor: 브리지 설계가 노출 면적을 줄이는 대신 폭발 반경을 키웠는지 명시적으로 기록한다.** 하나의 릴레이어가 모든 체인의 발행 권한을 갖는 것은 상관된 실패를 감수하는 선택이다. 기본값으로 떨어진 게 아니라 의도적으로 선택했음을 적어둔다.
