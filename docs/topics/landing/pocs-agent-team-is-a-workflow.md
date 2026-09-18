## en
- **gitboard: model one real cross-repo workflow as a single case record.** Pick a workflow that crosses rabbit, verex and wallet (say, PR → CI → deploy) and give every run one case ID with an append-only event log, instead of scattering per-repo agent output nobody aggregates.
- **CI: make each stage's completion test machine-checkable.** Lint pass, tests pass, an invariant test pass — an agent's PR should only transition state when the contract is met, not when it merely claims done.
- **Auditor: keep policy and high-risk approvals outside any agent's autonomy.** Mint changes, upgrade calls and permission changes belong behind an explicit gate the workflow enforces, exactly where the authority matrix already lives.

## ko
- **gitboard: 실제 크로스 레포 워크플로우 하나를 단일 케이스 레코드로 모델링한다.** rabbit, verex, wallet을 가로지르는 워크플로우(예: PR → CI → 배포)를 골라 매 실행마다 케이스 ID 하나와 추가전용 이벤트 로그를 부여한다. 아무도 취합하지 않는 레포별 에이전트 출력을 흩어놓는 대신이다.
- **CI: 각 단계의 완료 테스트를 기계로 확인 가능하게 만든다.** 린트 통과, 테스트 통과, 불변식 테스트 통과 — 에이전트의 PR은 단순히 완료라고 주장할 때가 아니라 이 계약을 충족할 때만 상태가 전환되어야 한다.
- **Auditor: 정책과 고위험 승인은 어떤 에이전트의 자율성 밖에 둔다.** 발행량 변경, 업그레이드 호출, 권한 변경은 워크플로우가 강제하는 명시적 게이트 뒤에 있어야 한다. 이는 이미 권한 매트릭스가 있는 바로 그 자리다.
