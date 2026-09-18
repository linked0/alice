## en
- **Devnet: treat every read as unverified by definition.** A single-node hosted Anvil fork has no second independent view, so any finality-confidence logic must actually be tested against Sepolia, or later the OP-Stack L2, where a second provider exists.
- **Bridge: gate mint or release on a confidence tag, not "latest."** Lock-and-mint should require a finalized (or explicit safe) block hash from at least two independent providers before releasing funds; failing to reach that tag should pause release, not retry against a fresh latest.
- **Verex: define per-action risk explicitly.** Cheap, reversible reads can use failover; market resolution and payout should require agreement-by-hash across independent RPC providers before being treated as final.

## ko
- **Devnet: 모든 읽기를 정의상 미검증으로 취급한다.** 호스팅된 단일 노드 Anvil 포크에는 독립된 두 번째 시야가 없으므로, 파이널리티 신뢰도 로직은 실제로 두 번째 프로바이더가 존재하는 Sepolia나 이후의 OP-Stack L2에서 검증해야 한다.
- **Bridge: "latest"가 아니라 신뢰도 태그로 민팅/방출을 통제한다.** lock-and-mint은 자금을 방출하기 전 최소 두 독립 프로바이더로부터 finalized(또는 명시적 safe) 블록 해시를 요구해야 한다. 그 태그에 도달하지 못하면 새 latest로 재시도하지 말고 방출을 멈춘다.
- **Verex: 액션별 위험도를 명시적으로 정의한다.** 저렴하고 가역적인 읽기는 페일오버를 써도 되지만, 마켓 정산과 정산금 지급은 독립 RPC 프로바이더 간 해시 일치를 확인한 뒤에야 확정으로 취급한다.
