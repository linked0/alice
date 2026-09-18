| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| front the gas | 가스비를 대신 먼저 내다 · 번들러가 검증 전 가스를 선지급함을 설명 · "the bundler fronts the gas to land the bundle" |
| stay liable | 계속 책임을 진다 · 실행이 실패해도 페이마스터가 책임에서 못 벗어남 · "the paymaster stays liable even if the call reverts" |
| happy path | (오류 없는) 정상 경로 · 겉보기엔 매끈해 보이는 성공 시나리오를 가리킴 · "the happy path hides a service decision" |
| fall back to | ~로 대체 수단을 쓰다 · 스폰서 실패 시 사용자 부담 결제로 전환 · "fall back to user-funded" |
| single point of failure | 단일 장애점 · 대체 불가능한 번들러 의존을 지적 · "has a single point of failure it is not advertising" |
| best-effort | 최선을 다하되 보장은 없는 · 가스리스가 확실한 약속이 아님을 인정하는 표현 · "gasless is best-effort" |
| throttled or banned | 속도 제한을 받거나 차단당하다 · 시뮬레이션을 낭비하는 계정에 대한 번들러의 제재 · "get throttled or banned" |
| collapse into | (여러 원인이) 하나로 뭉뚱그려지다 · 여덟 가지 실패 원인이 한 메시지로 뭉개짐 · "Eight causes currently collapse into one useless" |
| quietly admits | 은근히 인정하다, 사실상 시인하다 · 문구 하나가 가스리스의 한계를 드러냄을 표현 · "quietly admits gasless is best-effort" |
| veto | 거부권(을 행사하다) · 사용자가 스폰서 전환 결정에 반대할 수 있음 · "a policy decision a user might want to veto" |
| ERC-4337 | 계정 추상화 표준(Account Abstraction, ERC-4337) · 번들러·페이마스터를 통한 가스리스 트랜잭션의 기반 규격. "An ERC-4337 user operation can be valid on-chain" |
| EntryPoint | 엔트리포인트 컨트랙트 · UserOperation을 검증·실행하는 이 스택의 유일한 신뢰 기준 컨트랙트. "The EntryPoint contract is the only trustless party" |
| UserOperation | 사용자 연산(UserOperation, UserOp) · 일반 트랜잭션을 대신하는 ERC-4337의 요청 단위. "A bundler simulates and submits its UserOperation" |
| ERC-7562 | 번들러 검증 규칙 표준(ERC-7562) · 시뮬레이션을 낭비하는 계정·페이마스터에 대한 평판 제재 규칙. "ERC-7562: accounts/paymasters that waste simulations get throttled" |
| griefing | 그리핑(이득 없이 상대에게 손해만 입히는 공격) · 번들러가 검증만 통과한 뒤 다르게 행동하는 악용 시나리오. "a malicious account can make a bundler burn gas" |
<!-- acronyms 2026-09-18 -->
