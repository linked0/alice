## en
- **Devnet: treat Spectre/Meltdown mitigation as a Cloud Run host assumption, not something Jayverse patches.** Note in infra docs that node isolation for Devnet/Anvil relies on the cloud provider's speculative-execution mitigations.
- **Auditor: add "architectural, not a bug" as a category in security write-ups.** When documenting what was checked and by which rule, distinguish a hardware-level side channel like this from an application-level vulnerability the team actually controls.

## ko
- **Devnet: Spectre/Meltdown 완화는 Jayverse가 패치하는 게 아니라 Cloud Run 호스트의 전제로 다룬다.** Devnet/Anvil의 노드 격리가 클라우드 제공자의 추측 실행 완화에 의존한다는 것을 인프라 문서에 적어둔다.
- **Auditor: 보안 문서에 "아키텍처적 문제, 버그 아님" 카테고리를 추가한다.** 무엇을 어떤 규칙으로 확인했는지 적을 때, 이런 하드웨어 수준 사이드채널과 팀이 실제로 통제하는 애플리케이션 수준 취약점을 구분한다.
