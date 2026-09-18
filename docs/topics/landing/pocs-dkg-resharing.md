## en
- **Bridge: document whether the relayer committee can reshare.** The Anvil↔Sepolia lock-and-mint relayer set is a committee; write down whether adding or removing a relayer preserves the registered bridge public key, or admit plainly that "rotate the operator set" currently means "migrate the bridge."
- **Auditor: require a published ceremony transcript for any threshold setup.** Any multisig or threshold component (the bridge relayer set, a future DVT-style validator group) should publish its ceremony transcript so the threshold is a verifiable fact, not an assertion nobody can check.
- **Wallet: test the three membership events before trusting recovery.** If wallet or bridge recovery ever uses a threshold scheme, run this page's three-event test on devnet first — operator leaves, operator joins, share lost — and check whether "recover a lost share" is distinguishable from "let t colluding operators hand a share to anyone."

## ko
- **Bridge: 릴레이어 위원회가 재분배 가능한지 문서화한다.** Anvil↔Sepolia lock-and-mint 릴레이어 집합은 위원회다. 릴레이어를 추가하거나 제거해도 등록된 브릿지 공개키가 유지되는지 적어두거나, 그렇지 않다면 "운영자 집합 교체"가 사실상 "브릿지 마이그레이션"임을 명시한다.
- **Auditor: 임계값 구성마다 공개된 세레모니 기록을 요구한다.** 브릿지 릴레이어 집합이나 향후 DVT식 검증자 그룹 같은 멀티시그/임계값 구성은 세레모니 기록을 공개해야, 임계값이 아무도 확인할 수 없는 주장이 아니라 검증 가능한 사실이 된다.
- **Wallet: 복구를 신뢰하기 전 세 가지 멤버십 이벤트를 테스트한다.** 지갑이나 브릿지 복구가 임계값 방식을 쓴다면 devnet에서 운영자 이탈·합류·share 분실 세 이벤트를 먼저 테스트하고, "분실된 share 복구"와 "공모한 t명이 아무에게나 share를 건네주는 것"이 구분되는지 확인한다.
