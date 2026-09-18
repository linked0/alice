## en
- **Wallet/Rabbit: produce an authority graph before installing any AA module or guard.** Any Safe-like module or guard installed on an AA account is a root-key-equivalent change; produce the authority graph and an uninstall/recovery test before shipping it, not just a feature checklist.
- **Bridge: treat a relayer/admin Safe's modules with the same test.** If the bridge's admin multisig is or becomes a Safe, demonstrate any allowance/automation module bypassing the owner threshold on devnet, and keep a guard-rejects-everything recovery path documented and exercised.
- **Auditor: require the four-row checklist on every module install.** Add "callable authority, upgradeability, uninstall permissions, recovery under failure" as a required Auditor row whenever a module or guard is installed on any Jayverse account, not just at initial audit.

## ko
- **Wallet/Rabbit: AA 모듈이나 가드를 설치하기 전에 권한 그래프를 만든다.** AA 계정에 설치되는 Safe류 모듈이나 가드는 루트 키에 준하는 권한 변경이다. 기능 체크리스트만 만들지 말고 출시 전에 권한 그래프와 제거/복구 테스트를 만든다.
- **Bridge: 릴레이어/관리자 Safe의 모듈에도 같은 테스트를 적용한다.** 브릿지 관리자 멀티시그가 Safe이거나 Safe가 된다면, allowance/자동화 모듈이 소유자 임계값을 우회하는 것을 devnet에서 시연하고, 무조건 거부하는 가드의 복구 경로를 문서화하고 실제로 실행해본다.
- **Auditor: 모듈 설치마다 네 항목 체크리스트를 요구한다.** "호출 가능한 권한, 업그레이드 가능성, 제거 권한, 장애 시 복구"를 초기 감사 때뿐 아니라 어떤 Jayverse 계정에 모듈이나 가드가 설치될 때마다 필수 Auditor 항목으로 추가한다.
