## en
- **DeFi/Verex: write the conservation invariant equivalent to holdings == issued and make a violation halt, not log.** Total collateral locked == total position tokens issued is the S-tier check; wire it to pause the contract on mismatch, not just emit an event.
- **Auditor: for every invariant tracked, write down explicitly what a violation stops.** Discard or rebuild any invariant whose honest answer is "writes a log" — it trains people to ignore it.
- **Rabbit/Devnet: run the invariant watcher on infrastructure separate from the sign/execute path.** A watcher inside the same Cloud Run service as session-key execution dies in the same incident it's meant to catch; stand it up off-path.
- **Auditor: price the wrong-stop against the missed-violation before adding a new invariant.** One angry hour of manual override versus the reserve — write both numbers down rather than arguing false positives in the abstract.

## ko
- **DeFi/Verex: holdings == issued에 해당하는 보존 불변식을 작성하고, 위반 시 로그가 아니라 정지시킨다.** 잠긴 총 담보 == 발행된 총 포지션 토큰이 S급 체크이며, 불일치 시 이벤트만 발생시키지 않고 컨트랙트를 일시정지하도록 연결한다.
- **Auditor: 추적하는 모든 불변식에 대해 위반이 무엇을 멈추는지 명시적으로 적어둔다.** 정직한 답이 "로그를 남긴다"뿐인 불변식은 폐기하거나 다시 만든다. 그런 불변식은 사람들이 무시하도록 훈련시킬 뿐이다.
- **Rabbit/Devnet: 불변식 감시자를 서명/실행 경로와 분리된 인프라에서 돌린다.** 세션 키 실행과 같은 Cloud Run 서비스 안에 있는 감시자는 잡아야 할 바로 그 사고와 함께 죽는다. 경로 밖에 따로 세운다.
- **Auditor: 새 불변식을 추가하기 전에 잘못된 정지와 놓친 위반의 비용을 나란히 매긴다.** 수동 오버라이드가 필요한 화난 한 시간 대 준비금 전체를 숫자로 적어두고, 추상적으로 거짓 양성을 논쟁하지 않는다.
