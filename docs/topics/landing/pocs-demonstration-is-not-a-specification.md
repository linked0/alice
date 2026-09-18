## en
- **Rabbit: session-key mandates as scoped permission, not a one-time recording.** A 7702/7715 mandate should list exactly which contracts and actions it covers, with an expiry, matching the "field of view" problem raised for screen-recording agents rather than a broad grant approved once.
- **Auditor: require the two-run diff and the broken-precondition run before a skill or workflow ships.** Record the same task twice from different starting states to separate intent from incident, then break one precondition on purpose to check whether failure is visible or silently wrong.
- **CI/gitboard: add a "fails loudly" check, not just a happy-path test.** Before marking an agent skill or automation done, run it against a missing file, expired session, or empty result and confirm the failure is visible rather than a confident wrong output.

## ko
- **Rabbit: 세션 키 위임(mandate)은 한 번 녹화한 승인이 아니라 범위가 정해진 권한으로 만든다.** 7702/7715 위임은 어떤 컨트랙트와 액션을 포함하는지, 만료 시점을 명시해야 한다. 이는 화면 녹화 에이전트의 "시야 범위" 문제와 같은 맥락이다.
- **Auditor: 스킬이나 워크플로를 출시하기 전에 두 번 녹화 diff와 전제조건 깨기 실행을 요구한다.** 같은 작업을 다른 시작 상태에서 두 번 녹화해 의도와 우연을 분리하고, 전제조건 하나를 일부러 깨서 실패가 눈에 보이는지 조용히 틀린 결과를 내는지 확인한다.
- **CI/gitboard: 정상 경로 테스트뿐 아니라 "크게 실패하는지" 체크를 추가한다.** 에이전트 스킬이나 자동화를 완료 처리하기 전에 누락된 파일, 만료된 세션, 빈 결과로 돌려보고 실패가 눈에 보이는지, 자신만만한 오답을 내는지 확인한다.
