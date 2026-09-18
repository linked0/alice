## en
- **CI: treat the build pipeline itself as a target.** Keep OpenZeppelin submodules pinned as already required, and add reproducible-build verification so a compromised runner can't silently inject code into a signed release.
- **Auditor/gitboard: record SLSA-style provenance per release.** Which commit, which runner, which CI config produced a given build artifact, not just contract-level checks.

## ko
- **CI: 빌드 파이프라인 자체를 공격 대상으로 취급한다.** 이미 요구되는 대로 OpenZeppelin 서브모듈을 고정하고, 손상된 러너가 서명된 릴리스에 코드를 조용히 주입할 수 없도록 재현 가능한 빌드 검증을 추가한다.
- **Auditor/gitboard: 릴리스마다 SLSA 스타일 프로비넌스를 기록한다.** 컨트랙트 수준 체크만이 아니라, 어떤 커밋, 어떤 러너, 어떤 CI 설정이 해당 빌드 산출물을 만들었는지 남긴다.
