## en
- **Bridge/Token/Personas: name the verification model explicitly, don't inherit a default.** When the JYVE bridge or relayer ever adds a second chain beyond Anvil⇄Sepolia, write down who actually secures each message — today's multisig relayer or a future DVN-style set — rather than letting a default configuration become the trust decision by accident.
- **Devnet: write down which chain's finality is the weakest link.** Since devnet forks Sepolia today and targets an OP-Stack L2 later, any cross-chain flow through it inherits the slowest, most reorg-prone chain it touches — record that explicitly instead of treating multi-chain state as one uniform network.
- **OFA: add a lock-in check before a solver ever routes across chains.** If the intent/solver auction spans more than one chain, test whether switching the settlement path is a config change or an app rewrite, since that answer decides how much runtime dependency the auction has taken on.
- **Auditor: standing question — "who can halt or censor a message?"** Apply it to every interop or bridge component, not only Bridge/Token, since a compromise or pause of a shared messaging layer takes down everything routed through it at once.

## ko
- **Bridge/Token/Personas: 기본값을 그냥 물려받지 말고 검증 모델을 명시한다.** JYVE 브리지나 릴레이어가 Anvil⇄Sepolia를 넘어 두 번째 체인을 추가하게 되면, 오늘의 멀티시그 릴레이어든 향후 DVN 방식이든 각 메시지를 실제로 누가 담보하는지 적어둔다. 기본 설정이 의도치 않게 신뢰 결정이 되게 두지 않는다.
- **Devnet: 어느 체인의 파이널리티가 가장 약한 고리인지 적어둔다.** devnet은 지금 Sepolia를 포크하고 이후 OP-Stack L2를 목표로 하므로, 이를 거치는 모든 크로스체인 흐름은 가장 느리고 리오그에 취약한 체인의 위험을 그대로 물려받는다. 멀티체인 상태를 하나의 균일한 네트워크로 취급하지 말고 이를 명시한다.
- **OFA: 솔버가 체인을 넘나들기 전에 락인 점검을 추가한다.** 인텐트/솔버 경매가 둘 이상의 체인에 걸치면, 정산 경로를 바꾸는 것이 설정 변경인지 앱 재작성인지 테스트한다. 이 답이 경매가 얼마나 런타임 종속을 떠안았는지를 결정한다.
- **Auditor: "누가 메시지를 멈추거나 검열할 수 있는가"를 상시 질문으로 둔다.** Bridge/Token뿐 아니라 모든 인터롭·브리지 컴포넌트에 적용한다. 공유 메시징 레이어 하나가 손상되거나 멈추면 그것을 거치는 모든 것이 동시에 멈추기 때문이다.
