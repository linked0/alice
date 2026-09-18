## en
- **Verex: write out, and test, what defines "same market" and "same outcome."** Formally check reflexivity, symmetry and transitivity for the chosen equality fields, and add a counterexample test (same question, different resolution source) that must NOT be treated as equal.
- **Rabbit/Wallet: test transitivity specifically for nonce/tx-hash replay protection.** A dedup rule that is reflexive and symmetric but not transitive can still merge two different transactions as "equivalent" — add a test that catches this shape directly.
- **Bridge: define "same transfer" across the lock and mint legs as an explicit relation.** State which fields must match for a retry to be treated as the same transfer as an earlier one, so dedup logic can't accidentally collapse two different transfers into one.

## ko
- **Verex: "같은 마켓"과 "같은 아웃컴"이 무엇으로 정의되는지 적고 테스트한다.** 선택한 동등성 필드에 대해 반사성, 대칭성, 추이성을 형식적으로 확인하고, 같은 질문이지만 정산 소스가 다른 경우처럼 같다고 취급되면 안 되는 반례 테스트를 추가한다.
- **Rabbit/Wallet: nonce·tx-hash 재전송 방지 로직에서 추이성을 따로 테스트한다.** 반사적이고 대칭적이지만 추이적이지 않은 중복 제거 규칙은 서로 다른 두 트랜잭션을 "같다"고 합쳐버릴 수 있다. 이 형태를 직접 잡아내는 테스트를 추가한다.
- **Bridge: 락과 민트 구간에 걸친 "같은 전송"을 명시적 관계로 정의한다.** 재시도를 이전 전송과 같다고 볼 때 어떤 필드가 일치해야 하는지 명시해, 중복 제거 로직이 서로 다른 두 전송을 실수로 하나로 합치지 않게 한다.
