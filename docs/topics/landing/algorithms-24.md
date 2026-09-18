## en
- **Verex: audit the matching engine's hot-path order object for shape consistency as a standing check.** Same fields, same types, same order across call sites — not a one-time fix, since a single polymorphic call site can silently push a hot loop out of the optimized tier and cut throughput for no visible reason.
- **Verex: add a warmup-discard step to CI's perf checks.** The p99 numbers feeding the performance budget (see algorithms-51) are only meaningful once the JIT's warmup period is excluded, so make that exclusion part of the benchmark script, not a manual step someone forgets.

## ko
- **Verex: 매칭 엔진의 핫패스 주문 객체가 형태 일관성을 유지하는지 상시 점검한다.** 모든 호출 지점에서 같은 필드, 같은 타입, 같은 순서를 유지한다. 한 번 고치고 끝나는 문제가 아니다. 다형적인 호출 지점 하나가 핫 루프를 조용히 최적화 티어 밖으로 밀어내고 눈에 띄는 이유 없이 처리량을 떨어뜨릴 수 있기 때문이다.
- **Verex: CI 성능 체크에 워밍업 제외 단계를 추가한다.** 성능 예산(algorithms-51 참고)에 들어가는 p99 수치는 JIT 워밍업 구간을 제외해야만 의미가 있으므로, 이를 누군가 잊어버릴 수 있는 수동 단계가 아니라 벤치마크 스크립트 자체의 일부로 만든다.
