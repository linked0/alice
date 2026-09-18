## en
- **CI: agent-authored changes need a verifier gate, not just green tests.** Since Jayverse contracts and services are largely built with coding agents, add Foundry invariant tests as the "verifier" the agent must satisfy before a merge, not just unit tests it wrote itself.
- **gitboard: track spec-before-build, not just build status.** Add a field per service linking to the written spec the current code implements, so the dashboard shows whether judgment went into what to build, not only whether it shipped.
- **Auditor: publish which prompt or spec produced a change.** Extend the "what was checked, by which rule" instinct to agent-generated commits — record the spec or prompt behind a change alongside the diff, so an agent's non-deterministic output stays auditable after the fact.

## ko
- **CI: 에이전트가 작성한 변경은 테스트 통과가 아니라 검증자 게이트가 필요하다.** Jayverse 컨트랙트와 서비스 상당수가 코딩 에이전트로 만들어지므로, 에이전트가 직접 작성한 유닛 테스트만이 아니라 머지 전에 통과해야 하는 Foundry 불변조건 테스트를 "검증자"로 추가한다.
- **gitboard: 빌드 상태가 아니라 스펙-먼저 여부를 추적한다.** 서비스마다 현재 코드가 구현하는 작성된 스펙 링크 필드를 추가해, 대시보드가 배포 여부만이 아니라 무엇을 만들지에 판단이 들어갔는지도 보여주게 한다.
- **Auditor: 어떤 프롬프트나 스펙이 변경을 만들었는지 공개한다.** "무엇을 어떤 규칙으로 확인했는지"라는 직관을 에이전트가 만든 커밋까지 확장한다. 변경 배후의 스펙이나 프롬프트를 diff와 함께 기록해, 에이전트의 비결정적 출력도 사후에 감사 가능하게 남긴다.
