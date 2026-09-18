## en
- **Bridge/Token: batch-and-net gets a concrete test, not just a rule.** Add a CI check asserting the Intra Jayverse Bridge relayer never emits a Sepolia mint per single internal transfer, and that per-user transfer cadence cannot be read off mint-tx timestamps.
- **Wallet: flag the moment an action crosses the ledger boundary.** The simulate-before-sign screen should mark when a signed action leaves the internal vault and becomes a public-chain transaction, since that is exactly where a graph edge gets published.
- **Auditor: add graph exposure as a checked field.** Alongside resolution methodology, record which Jayverse settlement paths publish sender, receiver and timestamp and which stay netted internally, so "confidential" claims can be verified rather than assumed.

## ko
- **Bridge/Token: 배치-넷팅을 규칙이 아니라 구체적 테스트로.** Intra Jayverse Bridge 릴레이어가 내부 전송 하나마다 Sepolia 민팅을 발행하지 않는지, 사용자별 전송 주기가 민팅 트랜잭션 타임스탬프로 역산되지 않는지 확인하는 CI 체크를 추가한다.
- **Wallet: 액션이 원장 경계를 넘는 순간을 표시한다.** simulate-before-sign 화면은 서명한 액션이 내부 볼트를 벗어나 퍼블릭 체인 트랜잭션이 되는 순간을 표시해야 한다. 바로 그 지점에서 그래프 엣지가 공개되기 때문이다.
- **Auditor: 그래프 노출을 점검 항목에 추가한다.** 정산 방법론 옆에, 어떤 Jayverse 정산 경로가 송신자·수신자·타임스탬프를 공개하고 어떤 경로가 내부에서 넷팅되어 남는지 기록해, "기밀"이라는 주장을 가정이 아니라 검증 대상으로 만든다.
