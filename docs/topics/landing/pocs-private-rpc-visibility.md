## en
- **Wallet: never collapse accepted-by-provider, included, and final into one status.** The simulate-before-sign screen should show all three distinctly and use an explicit timeout with a provider-side cancel path, since a private submission removes the public-mempool heartbeat the UI might otherwise assume.
- **Verex: reconcile private-submission status from an unrelated public node.** If order or settlement transactions ever route through a protected RPC to avoid frontrunning, the submitting provider's own acknowledgement is the least independent witness — check inclusion and finality separately.
- **Auditor: log which channel a critical transaction used.** "Accepted by provider" is one party's view, not consensus; mark it as such in any audit trail rather than treating it as equivalent to a receipt.

## ko
- **Wallet: provider 수락, 포함, 파이널을 한 상태로 뭉치지 않는다.** 서명 전 시뮬레이션 화면은 세 가지를 구분해서 보여줘야 하고, provider 쪽 취소 경로가 있는 명시적 타임아웃을 둬야 한다. 프라이빗 제출은 UI가 무심코 전제하는 공개 멤풀 신호를 없애기 때문이다.
- **Verex: 프라이빗 제출 상태를 무관한 퍼블릭 노드에서 대조 확인한다.** 프론트러닝을 피하려고 주문이나 정산 트랜잭션이 보호된 RPC를 거친다면, 제출을 받은 provider 자신의 확인은 가장 독립성이 낮은 증인이다. 포함과 파이널리티를 별도로 확인한다.
- **Auditor: 중요한 트랜잭션이 어느 채널을 썼는지 기록한다.** "provider가 수락함"은 한쪽의 시각일 뿐 합의가 아니다. 영수증과 동등하게 취급하지 말고 감사 추적에 그렇게 표시한다.
