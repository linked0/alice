## en
- **Verex: measure real finalized-status latency and set the confirmation threshold from it.** Run the exercise on Sepolia/devnet blocks and use the actual inclusion-to-finalized time, not an assumed constant, revisiting it if devnet's chain config or finality model changes.
- **Bridge: derive the Anvil-to-Sepolia mint confirmation requirement the same way.** A too-low threshold is a reorg risk specifically on the mint side, so measure finality latency before fixing the bridge's confirmation count.
- **gitboard: track finalization latency live.** Expose inclusion-to-justified-to-finalized timing as a gitboard metric so a chain-config change is visible before it silently shifts Verex's or the Bridge's effective safety margin.

## ko
- **Verex: 실제 확정 상태 지연시간을 측정해서 확정 임계값을 거기서 도출한다.** Sepolia/devnet 블록에 연습을 실행해서 가정한 상수가 아니라 실제 포함부터 확정까지의 시간을 사용한다, devnet의 체인 설정이나 확정 모델이 바뀌면 다시 측정한다.
- **Bridge: Anvil-to-Sepolia 발행 확인 요건도 같은 방식으로 도출한다.** 너무 낮은 임계값은 특히 발행 쪽에서 리오그 위험이므로, 브리지의 확인 수를 고정하기 전에 확정 지연시간을 측정한다.
- **gitboard: 확정 지연시간을 실시간으로 추적한다.** 포함부터 justified, finalized까지의 타이밍을 gitboard 지표로 노출해서 체인 설정 변경이 Verex나 Bridge의 실효 안전 마진을 조용히 바꾸기 전에 보이게 한다.
