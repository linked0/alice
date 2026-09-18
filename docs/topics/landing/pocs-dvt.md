## en
- **DeFi: model the native-DVT question for the staking design, even schematically.** Since the EtherFi-style liquid-staking build sits on top of validator operators, sketch what m-of-n registered keys without a DKG ceremony would mean for "operator set change" and "operator slashing" in the pool design, even before any protocol ships it.
- **DeFi/Devnet: design any operator-registry logic as swappable middleware.** Apply the same absorption pattern as 4337-bundlers-vs-native-AA: if the staking contracts include operator aggregation or grouping logic now, keep it behind an interface the protocol could later absorb, rather than baking it in as permanent.
- **Auditor: log the four open questions as a watch item before DeFi commits.** Track slashing attribution, latency budget, the m<n collusion trade-off and the n≤16 rationale, and revisit them before DeFi's staking design locks in any validator-set assumption.

## ko
- **DeFi: 스테이킹 설계에서 네이티브 DVT 질문을 개략적으로라도 모델링한다.** EtherFi식 유동성 스테이킹 빌드는 검증자 운영자들 위에 서 있으므로, DKG 세레모니 없이 m-of-n으로 등록된 키가 풀 설계에서 "운영자 집합 변경"과 "운영자 슬래싱"에 어떤 의미인지 어떤 프로토콜이 이를 출시하기 전에 미리 스케치해 둔다.
- **DeFi/Devnet: 운영자 레지스트리 로직은 교체 가능한 미들웨어로 설계한다.** 4337 번들러가 네이티브 AA에 흡수되는 것과 같은 패턴을 적용한다. 지금 스테이킹 컨트랙트에 운영자 집계나 그룹핑 로직이 들어간다면 영구적으로 굳히지 말고 나중에 프로토콜이 흡수할 수 있는 인터페이스 뒤에 둔다.
- **Auditor: DeFi가 확정 짓기 전에 네 가지 미해결 질문을 감시 항목으로 기록한다.** 슬래싱 귀속, 지연 예산, m<n 공모 트레이드오프, n≤16 근거를 추적하고, DeFi 스테이킹 설계가 검증자 집합 가정을 확정하기 전에 다시 검토한다.
