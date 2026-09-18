## en
- **Verex: tag every external settlement input with its trust class.** Beyond "settlement is as safe as its weakest input," each data feed or bridged asset Verex accepts should be labeled bridge-trust, light-client-trust, or solver-collateral-trust, with the worst-case loss bound written next to it.
- **Bridge: state Anvil↔Sepolia's actual trust model explicitly.** The relayer-based lock-and-mint bridge is closer to an externally-verified bridge than a light client; write down who can lie, what they lose, and whether a dispute window exists, rather than assuming it.
- **OFA: classify the solver auction's own trust assumption.** An intent/solver design shifts trust from message-passing authenticity to the solver's collateral and settlement dispute process — OFA's design should state that collateral size and dispute window explicitly.

## ko
- **Verex: 외부 정산 입력마다 신뢰 등급을 붙인다.** "정산은 가장 약한 입력만큼만 안전하다"는 것을 넘어, Verex가 받는 각 데이터 피드나 브리지된 자산에 브리지-신뢰, 라이트클라이언트-신뢰, 솔버-담보-신뢰 중 하나를 표시하고 그 옆에 최악의 손실 한도를 적는다.
- **Bridge: Anvil↔Sepolia의 실제 신뢰 모델을 명시적으로 적는다.** 릴레이어 기반 락앤민트 브리지는 라이트클라이언트보다 외부 검증형 브리지에 가깝다. 누가 거짓말할 수 있는지, 그러면 무엇을 잃는지, 분쟁 윈도우가 존재하는지를 가정이 아니라 문서로 적어둔다.
- **OFA: 솔버 경매 자체의 신뢰 가정을 분류한다.** 의도/솔버 설계는 신뢰를 메시지 전달의 진위성에서 솔버의 담보와 정산 분쟁 절차로 옮긴다. OFA 설계는 그 담보 크기와 분쟁 윈도우를 명시해야 한다.
