## en
- **Devnet: check whether the OP-Stack L2 plan separates availability from ordering.** As devnet moves toward an OP-Stack L2, note whether the sequencer follows the Narwhal/Bullshark split, since that split is what determines the confirmation latency Verex can promise on order settlement.
- **Verex: benchmark peak order rate against actual devnet/Sepolia block bandwidth.** Don't assume a single-leader chain's throughput ceiling; a DAG-based L2 changes it, a single-leader L1 fork doesn't.
- **OFA: note whether the chosen L2 exposes pre-finality DAG state.** If propagated-but-uncommitted data is visible before ordering finishes, that's a surface a solver could exploit, and the intent/solver design should account for it.

## ko
- **Devnet: OP-Stack L2 계획이 가용성과 순서 결정을 분리하는지 확인한다.** devnet이 OP-Stack L2로 나아가면서, 시퀀서가 Narwhal/Bullshark식 분리를 따르는지 확인한다, 그 분리가 Verex가 주문 정산에서 약속할 수 있는 확정 지연시간을 결정하기 때문이다.
- **Verex: 최대 주문 처리량을 실제 devnet/Sepolia 블록 대역폭과 대조한다.** 단일 리더 체인의 처리량 한계를 가정하지 않는다. DAG 기반 L2는 그 한계를 바꾸지만 단일 리더 L1 포크는 바꾸지 않는다.
- **OFA: 선택한 L2가 확정 이전의 DAG 상태를 노출하는지 확인한다.** 전파됐지만 아직 커밋되지 않은 데이터가 순서 결정이 끝나기 전에 보인다면, 그것은 솔버가 악용할 수 있는 표면이므로 인텐트/솔버 설계가 이를 고려해야 한다.
