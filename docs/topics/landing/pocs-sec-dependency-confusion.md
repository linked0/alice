## en
- **CI: add a scoped-registry check across every Jayverse repo.** On top of the existing frozen-lockfile policy, confirm every internal-looking package name across rabbit, verex, jayverse-wallet, jayverse-token, jayverse-personas and jayverse-number is either scoped to a private registry or intentionally public, so a public namesquat can't win resolution.
- **gitboard: surface the last dependency-confusion audit date per repo.** This class stays silent until exploited and won't show up in ordinary CI green checks — track the audit date on the dashboard so it's visibly stale rather than invisibly skipped.

## ko
- **CI: 모든 Jayverse 저장소에 스코프 레지스트리 체크를 추가한다.** 기존 락파일 고정 정책에 더해, rabbit, verex, jayverse-wallet, jayverse-token, jayverse-personas, jayverse-number 전체에서 내부용처럼 보이는 패키지명이 프라이빗 레지스트리에 스코프되어 있거나 의도적으로 공개된 것인지 확인해, 공개 네임스쿼팅이 해석에서 이기지 못하게 한다.
- **gitboard: 저장소별 마지막 dependency-confusion 감사 날짜를 노출한다.** 이 취약점 클래스는 악용되기 전까지 조용하며 일반 CI 초록불로는 드러나지 않는다. 감사 날짜를 대시보드에 추적해 보이지 않게 건너뛰는 대신 눈에 띄게 오래된 상태로 만든다.
