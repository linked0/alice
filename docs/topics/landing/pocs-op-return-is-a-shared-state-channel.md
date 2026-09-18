## en
- **Verex: inscribe the resolution basis on-chain and prove oracle-before-settlement by block height.** Record the source and timestamp the market resolved on, so "why this paid" is shared, verifiable state rather than a claim only the UI makes.
- **Token/Bridge: pair the relayer's agreed facts with an on-chain trigger, not just a message.** An unforgeable record that a mint or burn event happened is not enforcement — write the code that fires automatically when the counterparty side doesn't follow through.
- **Auditor: require every cross-party settlement to name its default trigger.** For any bridge or market resolution, the audit should ask what code executes if the counterparty defaults; an empty answer means a gentlemen's agreement, not a protocol.

## ko
- **Verex: 정산 근거를 온체인에 새기고 오라클이 정산보다 먼저였음을 블록 높이로 증명한다.** 마켓이 어떤 소스와 시각을 기준으로 정산됐는지 기록해, "왜 이렇게 지급됐는지"가 UI만의 주장이 아니라 공유되고 검증 가능한 상태가 되게 한다.
- **Token/Bridge: 릴레이어가 합의한 사실을 메시지뿐 아니라 온체인 트리거와 짝짓는다.** 민트나 번 이벤트가 일어났다는 위조 불가능한 기록은 집행이 아니다. 상대방이 이행하지 않을 때 자동으로 발동하는 코드를 작성한다.
- **Auditor: 당사자 간 모든 정산에 기본값(default) 트리거를 명시하도록 요구한다.** 모든 브리지나 마켓 정산에 대해, 상대방이 이행하지 않을 때 어떤 코드가 실행되는지 감사에서 묻는다. 답이 없다면 프로토콜이 아니라 신사협정이다.
