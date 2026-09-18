## en
- **Bridge/Token: name the settlement leg, not just the route.** For the JYVE Anvil⇄Sepolia bridge, write down explicitly whether a non-major asset ever settles as a first-class leg or every path is routed through ETH or a dollar-pegged token, the same fork Agorá has to resolve for the won.
- **Verex: KRW-adjacent markets need the same field.** Any market settling in or near won should state whether it settles via a direct FX path or is routed through a dollar leg in its resolution field, mirroring the reference-rate discipline from the Kaiko item.
- **Auditor: track Agorá's published design decision as a citable methodology.** Add it to the watch list so Jayverse's own bridge and settlement rules can point to an external precedent when they choose first-class-leg over routed.

## ko
- **Bridge/Token: 정산 레그를 지정한다, 경로만 말하지 않는다.** JYVE Anvil⇄Sepolia 브리지에서 비주요 자산이 1급 레그로 직접 정산되는지, 아니면 모든 경로가 ETH나 달러 페그 토큰을 거치는지 명시한다. Agorá가 원화에 대해 풀어야 하는 것과 같은 갈림길이다.
- **Verex: 원화 인접 마켓도 같은 필드가 필요하다.** 원화로 또는 원화에 가깝게 정산되는 마켓은 정산 필드에 직접 FX 경로로 정산되는지 달러 레그를 거쳐 라우팅되는지 명시해야 한다. Kaiko 항목의 참조 금리 원칙과 같다.
- **Auditor: Agorá의 공개된 설계 결정을 인용 가능한 방법론으로 추적한다.** 워치리스트에 추가해, Jayverse의 브리지·정산 규칙이 1급 레그 대 라우팅을 선택할 때 참고할 외부 선례로 삼는다.
