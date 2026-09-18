| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| fall back to | (대안으로) 물러나 ~을 쓰다 · 참조 대신 인덱스 기반 arena를 쓰는 대안. "you fall back to an arena that uses indices instead of references" |
| sidestep | (문제를) 정면돌파 없이 피해가다 · 설계 단계에서 borrow checker와의 싸움을 우회하는 것. "lets you sidestep that fight at the design stage" |
| as a last resort | 최후의 수단으로 · unsafe 코드를 안전한 API 뒤에 감춰 쓰는 경우. "or, as a last resort, unsafe" |
| push X to runtime | X를 런타임으로 미루다(넘기다) · 컴파일 타임 검사를 실행 시점 검사로 바꾸는 것. "push the check to runtime" |
| run into | (문제·오류에) 부딪히다, 맞닥뜨리다 · 일부러 컴파일 실패를 유발해보는 연습. "deliberately run into a compile failure" |
| reframe | (문제를) 다른 틀로 다시 바라보다 · 소유권 개념을 다른 언어의 동시성 버그에 적용할 때. "directly useful for reframing concurrency bugs" |
| NLL | 비어휘적 생애주기(Non-Lexical Lifetimes) · 참조의 유효 범위를 실제 마지막 사용 지점까지로 좁혀주는 러스트 borrow checker 개선. "NLL (Non-Lexical Lifetimes) computes a borrow's valid range" |
| Rc<RefCell<..>> | 참조 카운팅(Rc) + 내부 가변성(RefCell) 조합 · 컴파일타임 검사를 런타임 검사로 미루는 대표적 러스트 패턴. "Rc and RefCell that push the check to runtime" |
| arena | 인덱스 기반 메모리 풀(arena allocator) · 참조 대신 인덱스를 사용해 borrow checker 제약을 우회하는 대안. "an arena that uses indices instead of references" |
<!-- acronyms 2026-09-18 -->
