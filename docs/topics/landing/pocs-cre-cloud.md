## en
- **Verex: treat market resolution as this exact pattern — a private source, a verified bridge, on-chain settlement.** Since the chain can't check the venue/admin data itself, document per market what the resolution oracle's attestation actually covers, not just that a resolution happened.
- **Auditor: write, per CRE-style integration, what the bridge's attestation is worth and by what rule.** This is the Auditor row's exact job — the private data never gets published, so the methodology note is the only thing a consumer can check.
- **Number: readings sourced from private/licensed data should enforce access on-chain and remember data off-chain.** Same split Jayverse keeps arriving at elsewhere — a permission token on-chain, the actual reading kept off-chain until the permission is checked.

## ko
- **Verex: 마켓 정산을 정확히 이 패턴으로 다룬다. 비공개 소스, 검증된 브리지, 온체인 정산.** 체인이 거래소/관리자 데이터를 직접 확인할 수 없으므로, 정산이 일어났다는 사실뿐 아니라 정산 오라클의 증명이 실제로 무엇을 보장하는지를 마켓별로 문서화한다.
- **Auditor: CRE 방식 연동마다 브리지의 증명이 어떤 가치가 있고 어떤 규칙에 따르는지 적는다.** 이것이 정확히 Auditor 행의 역할이다. 비공개 데이터는 절대 공개되지 않으므로, 소비자가 확인할 수 있는 것은 방법론 노트뿐이다.
- **Number: 비공개/라이선스 데이터에서 온 읽기는 접근을 온체인에서 강제하고 데이터는 오프체인에 둔다.** Jayverse가 다른 곳에서도 계속 도달하는 것과 같은 분리다. 권한 토큰은 온체인에, 실제 읽기는 권한이 확인될 때까지 오프체인에 남는다.
