## en
- **Verex/CI: build the two regression gates the practical connection names.** An exact-value gate for contract gas snapshots, and a percentile/variance-based gate (p95/p99 vs a noise band) for matching-engine and API latency.
- **gitboard: report p50/p95/p99 for any latency dashboard row, not the average.** Per this page, that's closer to what users actually feel.
- **CI: exclude a warm-up period from any benchmark used as a regression gate, and widen the noise threshold or use relative in-run comparison on shared runners.** A fixed absolute threshold on noisy CI either lets regressions through or cries wolf until nobody trusts it.

## ko
- **Verex/CI: 실무 연결이 언급하는 두 가지 회귀 게이트를 만든다.** 컨트랙트 가스 스냅샷용 정확값 게이트와, 매칭 엔진·API 지연용 퍼센타일/분산 기반 게이트(노이즈 밴드 대비 p95/p99).
- **gitboard: 지연 대시보드의 모든 행에 평균이 아니라 p50/p95/p99를 보고한다.** 이 페이지에 따르면 그것이 사용자가 실제로 체감하는 것에 더 가깝다.
- **CI: 회귀 게이트로 쓰는 모든 벤치마크에서 워밍업 구간을 제외하고, 공유 러너에서는 노이즈 임계값을 넉넉히 잡거나 같은 실행 내 상대 비교를 쓴다.** 노이즈가 있는 CI에 고정된 절대 임계값을 쓰면 회귀를 통과시키거나, 아무도 신뢰하지 않을 때까지 늑대가 왔다고 계속 외치게 된다.
