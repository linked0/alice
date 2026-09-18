## en
- **Devnet: run the load harness against the hosted Anvil node.** Since Jayverse already runs on GCP Cloud Run, deploy this k6/vegeta harness against the devnet or Rabbit's Cloud Run service and record p50/p99 vs RPS, instance-count lag, and cost per 1k requests before assuming it survives a spike.
- **Wallet/Rabbit: measure cold-start time on the simulate-before-sign endpoint.** Cold starts directly hit the wallet's simulate call; measure it explicitly and decide whether paying for min-instances there is worth it, rather than assuming Cloud Run's default is fine.
- **gitboard: turn the four curves into a recurring check.** Add latency knee, autoscaler lag, cost/1k requests, and cold-start time as a per-service panel gitboard tracks continuously, not a one-off study that goes stale.

## ko
- **Devnet: 호스팅된 Anvil 노드에 로드 하네스를 돌린다.** Jayverse가 이미 GCP Cloud Run에서 돌아가므로, 이 k6/vegeta 하네스를 devnet이나 Rabbit의 Cloud Run 서비스에 대해 실행해 p50/p99 대 RPS, 인스턴스 수 지연, 요청 1천 건당 비용을 스파이크를 버틸 거라 가정하기 전에 기록한다.
- **Wallet/Rabbit: 서명 전 시뮬레이션 엔드포인트의 콜드 스타트 시간을 측정한다.** 콜드 스타트는 지갑의 시뮬레이션 호출에 직접 영향을 준다. 이를 명시적으로 측정하고, Cloud Run 기본값이 괜찮다고 가정하는 대신 그 엔드포인트에 min-instances 비용을 지불할 가치가 있는지 판단한다.
- **gitboard: 네 개의 곡선을 반복 체크로 만든다.** 레이턴시 무릎점, 오토스케일러 지연, 요청 1천 건당 비용, 콜드 스타트 시간을 gitboard가 서비스별로 계속 추적하는 패널로 추가한다. 한 번 하고 낡아버리는 단발성 연구로 두지 않는다.
