## en
- **Rabbit: replace "transaction failed" with the eight-way taxonomy.** The portal's AA flow should classify RPC compatibility, simulation, reputation, quota, expired sponsorship, deposit, inclusion timeout and execution revert separately, since the correct user-facing response differs for each.
- **Wallet: make the sponsored-to-user-paid switch a consent decision.** The embedded wallet must hold a gas-asset fallback, but silently switching from sponsored to user-funded is a policy decision the simulate-before-sign screen should let the user veto, not something it does quietly.
- **Devnet: note the bundler/paymaster single-provider gap.** Anvil devnet today runs one bundler and one sponsorship policy; before mainnet, test the same UserOperation against a second bundler and policy to catch the EntryPoint-version and sponsorship-format differences this card warns about.

## ko
- **Rabbit: "트랜잭션 실패" 대신 여덟 가지 분류를 쓴다.** 포털의 AA 플로우는 RPC 호환성, 시뮬레이션, 평판, 쿼터, 만료된 스폰서십, 디파짓, 인클루전 타임아웃, 실행 리버트를 각각 구분해야 한다. 실패 유형마다 사용자에게 보여줄 올바른 대응이 다르기 때문이다.
- **Wallet: 스폰서-사용자 부담 전환을 동의 결정으로 만든다.** 임베디드 월렛은 가스 자산 폴백을 보유해야 하지만, 스폰서 방식에서 사용자 부담으로 조용히 전환하는 것은 정책 결정이다. simulate-before-sign 화면이 이를 조용히 실행하지 말고 사용자가 거부할 수 있게 해야 한다.
- **Devnet: 번들러/페이마스터 단일 제공자 공백을 기록한다.** 현재 Anvil devnet은 번들러 하나, 스폰서십 정책 하나로 돌아간다. 메인넷 전에 동일한 UserOperation을 두 번째 번들러와 정책으로 테스트해, 이 카드가 경고하는 EntryPoint 버전과 스폰서십 포맷 차이를 미리 잡아낸다.
