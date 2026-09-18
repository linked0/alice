## en
- **Wallet: budget key storage and biometrics twice, not once.** If jayverse-wallet ever ships a mobile companion, treat Keychain/Secure Enclave and Keystore/StrongBox as two separate implementations to write and test, not one cross-platform abstraction.
- **Rabbit: table the feature list before picking a mobile framework.** Session-key mandate execution and settlement push notifications sit in the unshared column, so list Rabbit's actual mobile features and mark each shared-by-framework or per-platform before choosing React Native, Flutter or KMP.
- **Devnet: no action until a mobile client exists.** Treat the self-test table as the gate — nothing in Jayverse's current stack changes until a service commits to shipping mobile.

## ko
- **Wallet: 키 저장과 생체인증은 한 번이 아니라 두 번 예산을 잡는다.** jayverse-wallet이 모바일 동반 앱을 낸다면 Keychain/Secure Enclave와 Keystore/StrongBox를 하나의 크로스플랫폼 추상화가 아니라 각각 작성하고 테스트해야 할 별도 구현으로 다룬다.
- **Rabbit: 모바일 프레임워크를 고르기 전에 기능 목록부터 표로 만든다.** 세션 키 위임 실행과 정산 푸시 알림은 공유되지 않는 칸에 속하므로, React Native, Flutter, KMP를 고르기 전에 Rabbit의 실제 모바일 기능을 나열하고 각각 프레임워크로 공유되는지 플랫폼별인지 표시한다.
- **Devnet: 모바일 클라이언트가 생기기 전까지는 조치 없음.** 자가 점검 표를 관문으로 삼는다 — Jayverse의 현재 스택은 어떤 서비스가 모바일 출시를 확정하기 전까지 바뀌지 않는다.
