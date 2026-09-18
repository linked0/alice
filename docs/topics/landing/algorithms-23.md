## en
- **Verex: confirm vectorization on the CLOB matching loop before crediting an algorithm change.** Read the compiler's optimization report or the generated assembly for the matching engine's hot loop, and attribute a speedup to vectorization/inlining only when it's confirmed there, not guessed from wall-clock alone.
- **Verex: check pointer-aliasing first when a hot loop won't vectorize.** For signature-verification or order-matching code, telling the compiler pointers don't alias is often the cheap fix before reaching for an algorithmic rewrite.
- **gitboard: surface "was this loop vectorized" as a checked fact.** If gitboard ever tracks service performance, pull the vectorization status from the build's optimization report next to latency numbers, instead of assuming it happened.

## ko
- **Verex: 알고리즘 변경 덕이라 말하기 전에 CLOB 매칭 루프의 벡터화를 확인한다.** 매칭 엔진의 핫 루프에 대해 컴파일러 최적화 리포트나 생성된 어셈블리를 읽고, 벡터화/인라이닝이 실제로 확인된 경우에만 속도 향상의 원인으로 돌린다. 벽시계 시간만 보고 추측하지 않는다.
- **Verex: 핫 루프가 벡터화되지 않으면 먼저 포인터 앨리어싱을 확인한다.** 서명 검증이나 주문 매칭 코드에서는 포인터가 겹치지 않는다고 컴파일러에 알려주는 것이 알고리즘을 다시 쓰기 전에 시도할 값싼 수정인 경우가 많다.
- **gitboard: "이 루프가 벡터화됐는가"를 검증된 사실로 노출한다.** gitboard가 서비스 성능을 추적한다면, 벡터화 여부를 가정하지 말고 빌드 최적화 리포트에서 가져와 지연 시간 옆에 함께 보여준다.
