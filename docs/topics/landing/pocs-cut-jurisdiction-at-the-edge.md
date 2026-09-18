## en
- **Verex: put jurisdiction blocking in one edge layer, never in settlement logic.** Front every Verex endpoint with a single geo-check function, return 451, and treat its log as the compliance artifact rather than a codebase audit.
- **Auditor: point to the log stream, not the code.** When asked how a jurisdiction is blocked, the Auditor row answers with the edge function's log, matching the "publish what was checked" instinct it already has.
- **Rabbit: run the false-positive measurement on jaylabs.xyz traffic.** Replay real portal traffic through the geo decision and count VPN/satellite/roaming misses before trusting IP-geo alone; pair with KYC wherever session-key mandates move real funds.
- **CI: gate the edge layer's latency once it exists.** Add the p50/p99 before/after check to CI so a future refactor can't silently push the country branch out of the TLS-terminating isolate.

## ko
- **Verex: 관할권 차단은 하나의 엣지 레이어에만 둔다, 정산 로직에는 절대 두지 않는다.** 모든 Verex 엔드포인트 앞에 단일 지역 확인 함수를 두고 451을 반환하며, 그 로그를 코드베이스 감사가 아니라 컴플라이언스 증거물로 다룬다.
- **Auditor: 코드가 아니라 로그 스트림을 가리킨다.** 어떤 관할권이 왜 차단되는지 물으면 Auditor 행은 엣지 함수의 로그로 답한다, 이미 가진 '확인한 것을 공개한다'는 본능과 일치한다.
- **Rabbit: jaylabs.xyz 트래픽에 오탐 측정을 실행한다.** 실제 포털 트래픽을 지역 판정에 통과시켜 VPN/위성/로밍으로 인한 오판을 센 다음에야 IP 기반 지역 판정만 믿는다, 세션 키 위임이 실제 자금을 옮기는 곳에서는 KYC와 짝짓는다.
- **CI: 엣지 레이어가 생기면 지연시간을 게이트로 건다.** 전후 p50/p99 체크를 CI에 추가해서 이후 리팩터링이 country 분기를 TLS 종단 아이솔레이트 밖으로 조용히 밀어내지 못하게 한다.
