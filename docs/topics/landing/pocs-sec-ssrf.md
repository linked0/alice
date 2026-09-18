## en
- **Verex: allowlist any URL a market creator supplies for resolution.** Before shipping a resolution source that fetches a user-provided URL, add an allowlist and egress control, since that is exactly the attacker-chosen-fetch this card describes.
- **All services on Cloud Run: block the GCP metadata endpoint explicitly.** Add an explicit check that no backend fetch path can reach 169.254.169.254, rather than relying on network defaults, given SSRF's history of reaching cloud credentials through metadata services.

## ko
- **Verex: 마켓 생성자가 제공한 URL은 화이트리스트로 제한한다.** 사용자가 제공한 URL을 가져오는 정산 소스를 배포하기 전에 화이트리스트와 아웃바운드 제어를 추가한다. 이것이 정확히 이 카드가 말하는 공격자 지정 요청이기 때문이다.
- **Cloud Run의 모든 서비스: GCP 메타데이터 엔드포인트를 명시적으로 차단한다.** 백엔드의 어떤 요청 경로도 169.254.169.254에 닿지 못하도록 네트워크 기본값에 기대지 않고 명시적으로 차단한다. SSRF가 메타데이터 서비스를 통해 클라우드 자격증명에 도달한 전례가 많기 때문이다.
