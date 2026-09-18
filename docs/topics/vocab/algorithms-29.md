| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| write barrier | 쓰기 배리어 · GC가 객체 그래프 변경을 추적하려고 쓰기 시점에 개입하는 장치. "a write barrier records changes to maintain the tri-color invariant" |
| tri-color invariant | 삼색 불변식 · 동시 마킹(concurrent marking)이 지켜야 할 규칙. "maintain the tri-color invariant" |
| pace (동사) | (작업) 속도를 조절하다, 맞추다 · GC가 목표치에 맞춰 마킹 속도를 조정하는 것. "paces its marking rate to hit a GOGC target" |
| wreck | 완전히 망치다, 결딴내다 · GC 혼자서도 p99 지연을 망칠 수 있다는 강한 표현. "GC is a factor that can wreck p99 all by itself" |
| trap ... in | ~에 가두다, 몰아넣다 · 잘못된 이해가 엉성한 해결책만 쓰게 만드는 것. "traps you in the blunt remedy" |
| blunt remedy | 투박한(정교하지 못한) 해결책 · 근본 원인을 안 보고 쓰는 임시방편. "the blunt remedy of just growing the heap" |
| pay off | 이득이 되다, 보람이 있다 · 어떤 조치가 다른 것보다 효과적이라는 뜻. "pays off more than GC tuning does" |
| GC | 가비지 컬렉션(Garbage Collection) · 더 이상 쓰지 않는 메모리를 자동 회수하는 런타임 기능, 이 카드 전체의 주제. "Region-based GC divides the heap into uniformly sized regions" |
| GOGC | Go 런타임의 GC 목표치 환경변수 · 힙 증가율 대비 마킹 속도를 조절하는 튜닝 파라미터. "paces its marking rate to hit a GOGC target" |
| ZGC | Z 가비지 컬렉터(Java용) · 컬러드 포인터와 로드 배리어로 압축까지 동시에 수행하는 저지연 GC. "ZGC uses colored pointers and load barriers" |
| GODEBUG | Go 런타임 디버그 환경변수 · gctrace=1로 설정해 GC 동작을 로그로 확인하는 옵션. "Turn on GODEBUG=gctrace=1 for a Go service" |
<!-- acronyms 2026-09-18 -->
