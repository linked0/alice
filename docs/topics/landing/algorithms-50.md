## en
- **Verex: run a staging chaos experiment injecting latency/errors into RPC and oracle separately.** Record whether either dependency alone halts the settlement pipeline — a steady-state hypothesis worth falsifying before mainnet volume.
- **Devnet: use the hosted Anvil as the controlled blast-radius environment.** Start with one dependency, widen gradually, and define abort conditions in advance, since Devnet is already the shared target every service points at.
- **Auditor: record the before/after improvement number after fixing a timeout/retry policy.** That pair belongs in the methodology notes, not just a changelog line, the same "write it down" instinct as the Kaiko-style rule.

## ko
- **Verex: RPC와 오라클에 각각 지연/오류를 주입하는 스테이징 카오스 실험을 돌린다.** 둘 중 하나의 의존성만으로 정산 파이프라인이 멈추는지 기록한다 — 메인넷 물량이 늘기 전에 반증해볼 가치가 있는 정상 상태 가설이다.
- **Devnet: 호스팅되는 Anvil을 통제된 blast radius 환경으로 쓴다.** 의존성 하나부터 시작해 점차 넓히고 중단 조건을 미리 정한다. Devnet은 이미 모든 서비스가 향하는 공유 대상이기 때문이다.
- **Auditor: 타임아웃/재시도 정책을 고친 뒤 전후 개선 숫자를 기록한다.** 그 짝은 체인지로그 한 줄이 아니라 방법론 노트에 있어야 한다. Kaiko 스타일 규칙과 같은 "적어둔다"는 본능이다.
