| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| write barrier | 쓰기 배리어 · GC가 객체 그래프 변경을 추적하려고 쓰기 시점에 개입하는 장치. "a write barrier records changes to maintain the tri-color invariant" |
| tri-color invariant | 삼색 불변식 · 동시 마킹(concurrent marking)이 지켜야 할 규칙. "maintain the tri-color invariant" |
| pace (동사) | (작업) 속도를 조절하다, 맞추다 · GC가 목표치에 맞춰 마킹 속도를 조정하는 것. "paces its marking rate to hit a GOGC target" |
| wreck | 완전히 망치다, 결딴내다 · GC 혼자서도 p99 지연을 망칠 수 있다는 강한 표현. "GC is a factor that can wreck p99 all by itself" |
| trap ... in | ~에 가두다, 몰아넣다 · 잘못된 이해가 엉성한 해결책만 쓰게 만드는 것. "traps you in the blunt remedy" |
| blunt remedy | 투박한(정교하지 못한) 해결책 · 근본 원인을 안 보고 쓰는 임시방편. "the blunt remedy of just growing the heap" |
| pay off | 이득이 되다, 보람이 있다 · 어떤 조치가 다른 것보다 효과적이라는 뜻. "pays off more than GC tuning does" |
