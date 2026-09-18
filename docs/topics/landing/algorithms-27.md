## en
- **Verex: add a gas-snapshot ceiling test.** Beyond the existing cost-ceiling awareness, add a Foundry gas-snapshot test on settlement and order-processing functions that fails the build if memory-word count crosses a set ceiling, catching the quadratic cost before mainnet.
- **DeFi: audit inline assembly for JUMPDEST assumptions.** If jayverse-defi's liquid-staking contracts use computed jumps, treat the JUMPDEST-bitmap scan as a code-review checklist item, since a wrong assumption there corrupts control flow silently rather than reverting.
- **Bridge/Token: flag large-calldata-copy paths in the relayer.** Lock-and-mint calldata handling is exactly the shape that pays the memory-expansion quadratic penalty most; review those functions specifically for the cost curve, not just the happy-path gas estimate.

## ko
- **Verex: 가스 스냅샷 상한 테스트를 추가한다.** 기존의 비용 상한 인식을 넘어, 정산·주문처리 함수에 Foundry 가스 스냅샷 테스트를 추가해 메모리 워드 수가 정해진 상한을 넘으면 빌드가 실패하게 만든다. 메인넷 전에 이차 비용 급증을 잡아낸다.
- **DeFi: 인라인 어셈블리의 JUMPDEST 가정을 감사한다.** jayverse-defi의 유동성 스테이킹 컨트랙트가 계산된 점프를 쓴다면, JUMPDEST 비트맵 스캔을 코드 리뷰 체크리스트 항목으로 다룬다. 이 가정이 틀리면 리버트가 아니라 조용히 제어 흐름이 깨진다.
- **Bridge/Token: 릴레이어의 대용량 calldata 복사 경로를 표시한다.** lock-and-mint calldata 처리는 메모리 확장의 이차 비용 페널티를 가장 많이 지불하는 형태다. 이런 함수는 해피패스 가스 추정치만이 아니라 비용 곡선 관점에서 따로 검토한다.
