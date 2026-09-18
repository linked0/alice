## en
- **gitboard: time-box the first invariant alert (e.g., Verex settlement mismatch, bridge mint over cap) — if self-hosted Prometheus setup is still stalled past 30 minutes, stand it up on a SaaS watcher instead and migrate later.** Coverage today beats a perfect stack next month.
- **Auditor: define the invariant to alert on before choosing a tool.** The check that halts on a real condition is what matters; the vendor is a second decision.
- **Devnet/CI: plan dual monitoring long-term — self-hosted Prometheus for the devnet/CI pipeline, plus a SaaS watcher for early coverage of Verex and Bridge contracts.** A vendor outage should not be the only blind spot in the system.

## ko
- **gitboard: 첫 불변식 알림(예: Verex 정산 불일치, 브리지 발행 한도 초과)에 시간 제한을 둔다. 셀프호스팅 Prometheus 설정이 30분을 넘겨 막혀 있다면 SaaS 워처로 먼저 세우고 나중에 옮긴다.** 오늘의 커버리지가 다음 달의 완벽한 스택보다 낫다.
- **Auditor: 도구를 고르기 전에 알림을 걸 불변식부터 정의한다.** 실제 조건에서 멈추는 체크가 중요하고, 벤더 선택은 그다음 결정이다.
- **Devnet/CI: 장기적으로 이중 모니터링을 계획한다. devnet/CI 파이프라인은 셀프호스팅 Prometheus로, Verex와 Bridge 컨트랙트의 초기 커버리지는 SaaS 워처로 확보한다.** 벤더 장애가 시스템의 유일한 사각지대가 되어서는 안 된다.
