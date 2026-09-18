| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| cache stampede | 캐시 쏠림(인기 키 만료 시 요청이 한꺼번에 몰리는 현상) · 캐시 장애의 대표적 원인. "A cache stampede happens when a popular key expires" |
| single-flight | (동시 요청을) 하나로 묶어 처리하는 기법 · 중복 요청 중 하나만 원본에 보내는 방어 기법. "single-flight (letting only one request query the origin)" |
| jitter | 지터(무작위로 섞은 편차) · 만료 시각을 흩뿌려 동시 만료를 막는 기법. "adding random jitter to expiration times" |
| stale-while-revalidate | 갱신 중에는 오래된 값을 잠시 보여주는 기법 · 최신화 동안 지연을 감추는 캐시 전략. "stale-while-revalidate (serving the stale value briefly" |
| take down | (서버 등을) 다운시키다·마비시키다 · 몰린 요청이 원본 서버를 멈추게 하는 상황. "can momentarily take the origin down" |
| exposed load | (캐시가 사라져) 그대로 노출된 부하 · 백엔드가 감당 못 하는 트래픽을 가리킴. "the backend collapsing under the exposed load" |
| acceptable staleness | 허용 가능한 데이터 지연(오래됨) 정도 · 캐시 전략을 고르기 전에 먼저 정의해야 하는 기준. "how much staleness is acceptable" |
| TTL | 생존 시간(Time To Live) · 캐시 정책 중 만료 시간 기반 방식을 가리킴. "policies broadly split into expiration-based (TTL)" |
<!-- acronyms 2026-09-18 -->
