| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| sandboxed | 샌드박스 처리된, 격리된 · 커널 안에서 안전하게 격리되어 실행되는 환경을 가리킬 때. "a sandboxed VM that runs safely inside the kernel" |
| statically check | 정적으로 검사하다 · 실행 전에 코드를 분석해 안전성을 검증할 때. "a verifier statically checks termination and memory-access safety" |
| attach to | ~에 연결되다, 붙다 · 프로그램이 특정 커널 지점(훅)에 걸릴 때. "attached to kprobes, uprobes, tracepoints, perf events" |
| wrap ... down to | ~로 간단히 축약해주다 · 복잡한 과정을 한 줄 스크립트 수준으로 압축할 때. "wrap this whole process down to a one-line script" |
| narrow down | 범위를 좁혀가다 · 원인을 후보군에서 하나씩 줄여나갈 때. "this lets you narrow down the cause with evidence" |
| reaches layers that ... never touch | ~가 닿지 못하는 층까지 도달하다 · 애플리케이션 로그로는 볼 수 없는 곳까지 관찰할 때. "it reaches layers that application logs never touch" |
| tail latency | 테일 레이턴시(상위 퍼센타일의 느린 응답) · 대부분은 빠르지만 일부 요청이 느릴 때 쓰는 성능 용어. "tail latency in Verex's backend API" |
| eBPF | 확장 버클리 패킷 필터(extended Berkeley Packet Filter) · 커널 안에서 안전하게 실행되는 관찰·트레이싱 기술, 이 카드의 주제. "eBPF is a sandboxed VM that runs safely inside the kernel" |
| bpftrace | eBPF를 한 줄 스크립트로 쓸 수 있게 해주는 고수준 트레이싱 도구 · 프로덕션에서 지연시간을 즉석에서 관찰할 때 쓰는 실제 도구. "Use a one-line bpftrace script to pull a histogram of disk I/O latency" |
| BCC | BPF 컴파일러 컬렉션(BPF Compiler Collection) · eBPF 프로그램 작성을 감싸주는 고수준 툴킷. "Higher-level tools like bpftrace and BCC wrap this whole process" |
| JIT | 즉시 컴파일(Just-In-Time compilation) · 검증을 통과한 eBPF 프로그램이 커널 훅에 붙기 전 거치는 컴파일 단계. "only programs that pass are JIT-compiled and attached to kprobes" |
<!-- acronyms 2026-09-18 -->
