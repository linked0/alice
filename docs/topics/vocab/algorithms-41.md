| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| cross the boundary | 경계를 넘나들다 · 매 시스템콜마다 유저-커널 경계를 넘는 오버헤드를 설명 · "crosses the user-kernel boundary on every system call" |
| dominate | (비용·시간에서) 압도적 비중을 차지하다 · 오버헤드가 전체 비용의 대부분을 차지함 · "that overhead dominates the total cost" |
| keep ~ from ~ing | ~가 ~하지 못하게 막다 · 데이터가 유저 공간을 거치지 않도록 막는 기법 · "keep data from passing through user space" |
| take on | (책임·역할을) 떠맡다 · 커널이 하던 프로토콜 처리를 애플리케이션이 대신 떠맡음 · "the application now has to take on the protocol handling" |
| at the cost of | ~을 대가로, ~을 희생하고 · 복잡도와 이식성을 대가로 경계 넘나듦을 줄임 · "at the cost of complexity and portability" |
| make progress | 진전을 이루다, 작업을 처리하다 · 시스템콜 없이도 처리를 이어갈 수 있음 · "make progress with no system calls at all" |
| concentrated in | ~에 집중되어 있다 · CPU 시간이 커널 시간에 몰려 있는 현상 · "shows CPU time concentrated in kernel time" |
| io_uring | 아이오유링(io_uring) · 커널·유저 공간이 링 버퍼를 공유해 시스템콜 없이도 비동기 I/O를 처리하는 리눅스 인터페이스. "io_uring provides an asynchronous interface built on two ring buffers" |
| NIC | 네트워크 인터페이스 카드(Network Interface Card, NIC) · 커널 바이패스가 큐를 유저공간 드라이버로 직접 매핑하는 하드웨어. "mapping NIC queues directly into a user-space driver" |
| epoll | 이폴(epoll) · 리눅스의 전통적 이벤트 기반 I/O 다중화 API, io_uring과의 비교 대상. "Implement the same echo server on epoll and on io_uring" |
| p99 | p99 레이턴시(99번째 백분위수 지연) · 전체 요청 중 99%가 이 값 이하로 끝났음을 나타내는 성능 지표. "compare p99 latency and system calls per second" |
<!-- acronyms 2026-09-18 -->
