## en
- **CI: diff optimizer-on vs optimizer-off bytecode for DeFi and Verex contracts.** Flag unexpectedly large SSTORE removals for manual review before merge, not just to explain gas after the fact.
- **Auditor: check what dead-code elimination removed near any side-effect-bearing branch.** A slash or liquidation path is exactly where a wrongly-elided store would be costly, so verify the "no side effects" assumption actually holds there.
- **DeFi: compare optimized vs unoptimized assembly specifically on the slash/reward paths.** These are the highest-cost places for constant propagation or DCE to have removed something it shouldn't have.

## ko
- **CI: DeFi와 Verex 컨트랙트의 옵티마이저 on/off 바이트코드를 diff한다.** 예상치 못하게 큰 SSTORE 제거를 병합 전에 수동 검토 대상으로 표시한다. 가스를 사후에 설명하는 용도로만 쓰지 않는다.
- **Auditor: 부작용이 있는 분기 근처에서 dead-code elimination이 무엇을 제거했는지 확인한다.** slash나 청산 경로가 바로 잘못 제거된 store가 비용을 초래할 곳이므로, "부작용 없음" 가정이 실제로 성립하는지 검증한다.
- **DeFi: slash/보상 경로에서 최적화 전후 어셈블리를 구체적으로 비교한다.** constant propagation이나 DCE가 제거해서는 안 될 것을 제거했을 때 비용이 가장 큰 지점이다.
