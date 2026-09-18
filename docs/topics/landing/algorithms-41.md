## en
- **Devnet: profile syscalls before scaling Anvil's RPC layer.** If the hosted devnet's RPC node ever shows CPU time concentrated in kernel time under many small JSON-RPC requests, run the strace -c comparison this card describes before adding instances — batched submission or reduced copying may be the actual fix.
- **Bridge: the relayer processing many small lock/mint/burn events across Anvil and Sepolia is the same workload shape.** If relayer throughput or latency ever becomes the bottleneck, the epoll-vs-io_uring comparison applies there too, not just to a generic RPC gateway.

## ko
- **Devnet: Anvil RPC 계층을 확장하기 전에 시스템콜부터 프로파일링한다.** 호스팅되는 devnet의 RPC 노드가 수많은 작은 JSON-RPC 요청 아래에서 CPU 시간이 커널 시간에 집중되는 모습을 보인다면, 인스턴스를 늘리기 전에 이 카드가 설명하는 strace -c 비교부터 돌린다. 배치 제출이나 복사 축소가 실제 해법일 수 있다.
- **Bridge: Anvil와 Sepolia 사이의 락/민트/번 이벤트를 처리하는 릴레이어도 같은 형태의 워크로드다.** 릴레이어의 처리량이나 지연이 병목이 된다면, epoll 대 io_uring 비교는 일반 RPC 게이트웨이뿐 아니라 여기에도 적용된다.
