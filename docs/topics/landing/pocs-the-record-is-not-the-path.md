## en
- **Personas: give each persona a stable ID, not a filename or off-chain path.** Metadata should keep identity across renames/moves; version each persona's metadata by content digest so an update is provably the same persona, not a new one.
- **Number: address each distributed reading by a content digest, and make stale writes conflict instead of silently overwriting.** A reading's filename should not be its identity; a revision-conflict on stale automation is safer than a silent overwrite of an indicator.
- **Auditor: record which model — on-chain-provable registry or off-chain digest-addressed record — each Jayverse identity artifact follows, and who is accountable for it.** Persona metadata and Number readings don't need the same answer, but each needs a stated one.

## ko
- **Personas: 각 페르소나에 파일명이나 오프체인 경로가 아니라 고정된 ID를 부여한다.** 이름 변경이나 이동에도 정체성이 유지되어야 하며, 페르소나 메타데이터 버전은 콘텐츠 다이제스트로 관리해 업데이트가 새 페르소나가 아니라 같은 페르소나임을 증명할 수 있게 한다.
- **Number: 배포되는 각 리딩을 콘텐츠 다이제스트로 주소화하고, 오래된 쓰기는 덮어쓰지 않고 충돌시킨다.** 리딩의 정체성은 파일명이 아니어야 하며, 오래된 자동화가 지표를 조용히 덮어쓰는 것보다 리비전 충돌이 더 안전하다.
- **Auditor: 페르소나 메타데이터와 Number 리딩 각각이 온체인 증명 레지스트리 모델인지 오프체인 다이제스트 기록 모델인지, 누가 책임지는지 기록한다.** 둘이 같은 답일 필요는 없지만 각각 명시된 답은 있어야 한다.
