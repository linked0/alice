## en
- **Verex: inventory every hardcoded settlement opinion.** List every place Verex's settlement path hardcodes a fact it does not own — signature format and length, oracle payload encoding, resolution record shape, collateral decimals, address size — and mark each as variable-length-capable or not; that table is useful even if nothing ever migrates.
- **Verex: keep the resolver a scheme-neutral transport.** A resolver should convert vendor-specific evidence into a canonical status/outcome/resolvedAt struct with no arbitrary custody authority, pinned at market creation; approve a replacement resolver only for future markets, never retroactively.
- **Auditor: require a flip criterion for any one-way admin switch.** Before any irreversible switch ships (a BLS-retirement-style flag, a resolver lock), write down what evidence is sufficient to flip it and whether that evidence can be gathered without flipping — and land the invariant guarding the call in the same commit as the switch.
- **Devnet/CI: bound every variable-length field.** Any field that becomes variable-length to accommodate a future scheme must carry an explicit size bound, tested on devnet before it reaches Verex's settlement contracts, so a generalization never opens a gas/DoS hole.

## ko
- **Verex: 정산 경로의 모든 고정 가정을 목록화한다.** Verex 정산 경로가 소유하지 않은 사실을 하드코딩하는 모든 곳 — 서명 형식과 길이, 오라클 페이로드 인코딩, 정산 기록 형태, 담보 소수점 자리수, 주소 크기 — 을 나열하고 각각 가변 길이로 바꿀 수 있는지 표시한다. 이 표는 마이그레이션이 실제로 일어나지 않아도 유용하다.
- **Verex: 리졸버를 스킴 중립 전송 계층으로 유지한다.** 리졸버는 벤더별 증거를 status/outcome/resolvedAt 형태의 표준 구조체로 변환할 뿐 임의의 커스터디 권한을 가지면 안 되며, 마켓 생성 시 고정한다. 교체 리졸버는 미래 마켓에만 적용하고 소급하지 않는다.
- **Auditor: 되돌릴 수 없는 관리자 스위치마다 전환 기준을 요구한다.** BLS 은퇴 방식의 플래그나 리졸버 잠금 같은 일방향 스위치를 출시하기 전에, 어떤 증거가 있으면 전환해도 되는지, 그 증거를 전환 없이 모을 수 있는지 적어두고, 스위치를 지키는 불변식을 같은 커밋에 넣는다.
- **Devnet/CI: 가변 길이 필드마다 상한을 둔다.** 미래 스킴을 수용하려고 가변 길이가 된 필드는 명시적 크기 상한을 가져야 하며, Verex 정산 컨트랙트에 닿기 전 devnet에서 테스트해 일반화가 가스/DoS 구멍을 열지 않게 한다.
