| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| tail latency | 꼬리 지연(가장 느린 요청들의 지연) · 평균과 대비되는 성능 지표. "the slowest one percent matters" |
| p99 | 99번째 백분위수(요청 100개 중 느린 1개의 값) · 지연 SLO의 표준 단위. "measure p99 on the CLOB round trip" |
| throughput | 처리량(단위 시간당 처리한 양) · 대역폭·지연과 함께 세 가지 기본 지표. "bandwidth mattered" |
| clean-slate | 백지에서 새로 설계한 · 기존 프로토콜 호환을 버린 설계를 부르는 말. "a clean-slate protocol for the second" |
| RDMA / RoCE | Remote Direct Memory Access / RDMA over Converged Ethernet(이더넷 위의 RDMA) · 데이터센터 고속 전송의 표준 이름. "TCP or RoCE good enough" |
| incast | 인캐스트(다수 송신자가 한 수신자에게 동시에 보내는 패턴) · 데이터센터 혼잡의 대표 원인. "Incast and queue build-up" |
| top-of-rack (ToR) switch | 랙 상단 스위치(서버 랙마다 하나씩 있는 첫 홉 스위치) · 데이터센터 토폴로지 용어. "the egress buffer of the top-of-rack switch" |
| egress | 출구(나가는 방향) · ingress(입구)와 짝. "egress queues per port" |
| congestion control | 혼잡 제어(네트워크가 막힐 때 속도를 조절하는 규칙) · TCP의 핵심 메커니즘. "Sender-driven congestion control" |
| ECN | Explicit Congestion Notification(명시적 혼잡 알림, 패킷에 표시를 남기는 방식) · 손실 없이 혼잡을 알리는 신호. "through ECN marks or loss" |
| control lag | 제어 시차(신호와 반응 사이의 지연) · 제어 이론 용어, 진동의 원인. "The feedback loop has a control lag" |
| head-of-line (HOL) blocking | 선두 차단(앞의 것이 막혀 뒤가 못 나가는 현상) · 큐·스트림 설계의 고전적 병목. "Byte streams and head-of-line blocking" |
| message boundary | 메시지 경계(어디서 한 메시지가 끝나는지) · 스트림 프로토콜의 결함을 설명할 때. "no notion of where one message ends" |
| RPC | Remote Procedure Call(원격 함수 호출, 요청-응답 쌍) · 분산 시스템의 기본 통신 단위. "Messages and RPCs, not streams" |
| SRPT | Shortest Remaining Processing Time first(잔여 처리 시간이 짧은 것 먼저) · 스케줄링 이론의 최적 정책. "a short message can overtake a long one" |
| grant (packet) | 허가(수신자가 보내도 된다고 알리는 패킷) · Homa 고유 용어, 수신자 주도 제어의 도구. "the receiver issues grant packets" |
| unscheduled / scheduled packets | 허가 없이 보내는 앞부분 / 허가를 받아 보내는 나머지 · Homa의 두 패킷 종류. "the first part of a message immediately, the unscheduled packets" |
| barrier synchronization | 배리어 동기화(모든 노드가 한 지점에 모일 때까지 기다리는 것) · 병렬 계산의 기본 동기화. "a barrier synchronization at the end of a compute step" |
| KV cache | key-value 캐시(트랜스포머 추론에서 이전 토큰의 키·값을 저장) · LLM 추론 인프라 용어. "a lookup in a distributed KV cache" |
| run-to-completion | 완료까지 실행(작업을 중간에 끊지 않고 끝까지 처리하는 모델) · 커널·네트워크 스택 설계 용어. "Homa's run-to-completion processing model" |
| upstream (v.) | 업스트림에 병합하다(패치를 원 프로젝트, 여기서는 리눅스 커널에 넣다) · 오픈소스 관용어. "working toward upstreaming it" |
| an order of magnitude | 한 자릿수(10배) 규모 · 크기 비교의 관용구. "by an order of magnitude" |
