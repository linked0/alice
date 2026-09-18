## en
- **Rabbit: agents propose the exact mandate/UserOp, never sign it.** Any agentic flow over 7702/7715 session keys should have the LLM output an exact command artifact that a separate deterministic executor submits verbatim, with the write path never running through the model itself.
- **OFA: gate solver-proposed execution behind propose-then-approve.** The intent/solver auction should register the exact winning artifact for approval before a deterministic executor runs it, rather than letting agent output reach the chain directly.
- **Auditor: store agent action logs masked-and-hashed, not raw.** The audit trail of what an agent proposed versus what was approved must not itself become a leak path, the same discipline this card applies to its PII log.
- **gitboard: track the read/write split as a metric.** Show what share of Jayverse's agent-touching code is read-only analysis (safe to automate now) versus write actions still behind a human gate, so automation is shown to grow by adding verified executor paths, not by loosening agent permissions.

## ko
- **Rabbit: 에이전트는 정확한 mandate/UserOp를 제안할 뿐 직접 서명하지 않는다.** 7702/7715 세션키 위의 에이전트 흐름은 LLM이 정확한 커맨드 아티팩트를 출력하고, 별도의 결정론적 실행기가 그것을 그대로 제출해야 한다. 쓰기 경로가 모델을 거쳐서는 안 된다.
- **OFA: 솔버가 제안한 실행을 propose-then-approve로 게이트한다.** 인텐트/솔버 경매는 승인 대상 아티팩트를 정확히 등록해 승인받은 뒤 결정론적 실행기가 돌려야지, 에이전트 출력이 바로 체인에 닿게 해서는 안 된다.
- **Auditor: 에이전트 행동 로그를 원문이 아니라 마스킹+해시로 저장한다.** 에이전트가 무엇을 제안했고 무엇이 승인됐는지의 감사 트레일 자체가 유출 경로가 되어서는 안 된다. 이 카드가 PII 로그에 적용하는 것과 같은 원칙이다.
- **gitboard: read/write 비중을 지표로 추적한다.** Jayverse의 에이전트 관련 코드 중 지금 안전하게 자동화 가능한 읽기 전용 분석과, 여전히 사람 승인이 필요한 쓰기 작업의 비중을 보여준다. 자동화는 에이전트 권한을 완화해서가 아니라 검증된 실행 경로를 늘려서 커져야 한다.
