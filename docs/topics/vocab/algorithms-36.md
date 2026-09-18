| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| as long as | ~하는 한, ~이기만 하면 · 단일 스레드 의미만 지켜지면 재배열이 허용됨 · "As long as single-thread semantics are preserved" |
| pair with | ~과 짝을 이루다 · release store와 acquire load가 짝지어질 때 관계가 성립함 · "a release store pairs with an acquire load" |
| happens-before | (일어난 후에 일어남을 보장하는) 선행 관계 · 두 연산 사이의 순서 보장을 나타내는 용어 · "a happens-before relationship is established" |
| go further | 한 단계 더 나아가다 · seq_cst가 다른 정렬 방식보다 더 강한 보장을 함 · "seq_cst goes further and guarantees a single global order" |
| show up | (문제가) 드러나다, 나타나다 · 약한 메모리 모델이나 고부하에서만 버그가 드러남 · "only shows up under a weaker memory model" |
| hard-to-reproduce | 재현하기 어려운 · 순서 오류 버그가 흔히 이런 성격을 가짐 · "an extremely hard-to-reproduce bug" |
| the standard for judging | 판단 기준 · 뮤텍스와 원자적 연산 중 어디를 써야 할지 가르는 기준 · "it's the standard for judging where atomic operations suffice" |
| ARM | ARM(Advanced RISC Machine) 아키텍처 · x86과 달리 약한 메모리 모델이라 정렬 버그가 여기서 드러남. "only shows up under a weaker memory model like ARM" |
| seq_cst | 순차적 일관성(sequentially consistent, seq_cst) · 모든 seq_cst 연산에 걸쳐 전역적으로 하나의 순서를 보장하는, 가장 비싼 정렬 수준. "seq_cst goes further and guarantees a single global order" |
| sync/atomic | sync/atomic · Go가 acquire/release 같은 명시적 옵션 대신 채널·뮤텍스와 함께 happens-before 규칙을 표현하는 패키지. "channels, mutexes, and sync/atomic" |
<!-- acronyms 2026-09-18 -->
