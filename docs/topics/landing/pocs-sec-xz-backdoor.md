## en
- **CI: pin by commit hash and review handoffs, not just lockfiles.** The frozen-lockfile and OpenZeppelin-pinned-as-submodules policy is the right shape; extend it to pinning by commit hash rather than tag, and reviewing any maintainer handoff before bumping a pin.
- **gitboard/Auditor: track commit-access changes as a monitored event.** Log who has merge rights on each Jayverse repo and when that access last changed, since this attack's vector was social engineering into commit access, not a code flaw.

## ko
- **CI: 락파일뿐 아니라 커밋 해시로 고정하고 인수인계를 검토한다.** 프로즌 락파일과 OpenZeppelin 서브모듈 고정 정책은 방향이 맞다. 여기에 태그가 아니라 커밋 해시로 고정하는 것, 핀을 올리기 전에 메인테이너 인수인계를 검토하는 것을 추가한다.
- **gitboard/Auditor: 커밋 권한 변경을 모니터링 대상 이벤트로 추적한다.** 각 Jayverse 레포에서 누가 머지 권한을 가지고 있고 그 권한이 언제 마지막으로 바뀌었는지 기록한다. 이 공격의 경로는 코드 결함이 아니라 커밋 권한으로의 사회공학이었다.
