## en
- **Verex: put single-flight in front of the order-book snapshot and oracle price cache specifically.** A stampede there directly degrades the price accuracy users see, which is the highest-stakes case the PoC names.
- **Number: use stale-while-revalidate for distributed readings.** A popular reading's cache expiry shouldn't hammer the origin computation when many licensed consumers hit it at once.
- **gitboard: track p99 latency and origin-query count per cached key as a standard test.** Run the exercise's load test against any new cache added to a service, not just Verex's, before it ships.

## ko
- **Verex: 오더북 스냅샷과 오라클 가격 캐시 앞에 구체적으로 single-flight를 둔다.** 여기서의 스탬피드는 사용자가 보는 가격 정확도를 바로 떨어뜨린다. 이 PoC가 지목하는 가장 위험도 높은 경우다.
- **Number: 배포되는 읽기에 stale-while-revalidate를 쓴다.** 인기 있는 읽기의 캐시가 만료될 때 다수의 라이선스 소비자가 동시에 몰려 원본 계산을 두들기지 않게 한다.
- **gitboard: 캐시된 키마다 p99 지연과 원본 조회 횟수를 표준 테스트로 추적한다.** 이 연습문제의 부하 테스트를 Verex뿐 아니라 어떤 서비스에 새 캐시를 추가하든 출시 전에 돌린다.
