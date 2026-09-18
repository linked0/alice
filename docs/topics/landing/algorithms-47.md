## en
- **Verex: reach for a one-line bpftrace script before adding app instrumentation.** When backend API tail latency shows up in gitboard but not in application logs, run a one-line bpftrace script against the Cloud Run/GKE host first, before adding more instrumentation code.
- **Devnet: use eBPF to isolate a stalling Anvil node's bottleneck.** When the hosted Anvil node stalls syncing from Sepolia, use eBPF to tell filesystem or network-stack bottlenecks apart from RPC-layer ones, without redeploying the node.
- **gitboard: point the runbook at eBPF for spikes that won't reproduce.** Add eBPF as the named escalation step in gitboard's runbook for a latency spike that won't reproduce elsewhere, no code change or redeploy needed to capture it.

## ko
- **Verex: 앱 계측을 늘리기 전에 한 줄짜리 bpftrace 스크립트부터 쓴다.** 백엔드 API 테일 레이턴시가 gitboard에는 나타나지만 애플리케이션 로그에는 안 보인다면, 계측 코드를 더 추가하기 전에 Cloud Run/GKE 호스트에 한 줄짜리 bpftrace 스크립트를 먼저 돌린다.
- **Devnet: 정체된 Anvil 노드의 병목을 eBPF로 가려낸다.** 호스팅된 Anvil 노드가 Sepolia 동기화 중 멈춘다면, 노드를 재배포하지 않고 eBPF로 파일시스템 병목과 네트워크 스택 병목, RPC 계층 병목을 구분한다.
- **gitboard: 재현 안 되는 스파이크의 런북에 eBPF를 명시한다.** 다른 곳에서 재현되지 않는 레이턴시 스파이크에 대해 gitboard 런북의 에스컬레이션 단계로 eBPF를 명시한다. 코드 변경이나 재배포 없이 포착할 수 있다.
