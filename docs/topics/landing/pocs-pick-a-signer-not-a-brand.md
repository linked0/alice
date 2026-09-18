## en
- **Wallet: require the five-item checklist before recommending or supporting any hardware signer.** Audit date and scope, deterministic-nonce evidence, entropy-path audit, fulfilment/logistics disclosure, and algorithm-upgradeability — score the device, not the brand.
- **Rabbit: verify deterministic nonces wherever a mandate/session key signs off-device.** Confirm RFC 6979 or hedged determinism is actually used, and add the two-signature byte-comparison as a CI smoke test on any signing path Rabbit depends on.
- **Auditor: score any signer or custody vendor's disclosure, not its incident count.** Rate time-to-patch, root-cause specificity, and stated affected range — the same rubric Jayverse's own incident-disclosure practice should meet if something in Wallet or Rabbit ever breaks.
- **Devnet/Wallet: any Jayverse multisig or treasury key should span independent implementations, not just independent devices of one brand.** Correlated layers inside a single vendor share the same failure surface, which defeats the point of a quorum.

## ko
- **Wallet: 하드웨어 서명기를 추천하거나 지원하기 전에 다섯 항목 체크리스트를 요구한다.** 감사 날짜와 범위, 결정론적 논스 증거, 엔트로피 경로 감사, 물류·이행 공개, 알고리즘 업그레이드 가능성 — 브랜드가 아니라 기기를 채점한다.
- **Rabbit: mandate/세션키가 오프디바이스에서 서명하는 모든 지점에서 결정론적 논스를 검증한다.** RFC 6979나 hedged determinism이 실제로 쓰이는지 확인하고, Rabbit이 의존하는 서명 경로에 두 번 서명해 바이트를 비교하는 테스트를 CI 스모크 테스트로 추가한다.
- **Auditor: 서명·커스터디 벤더를 사고 건수가 아니라 공개 문서로 채점한다.** 패치까지 걸린 시간, 근본 원인의 구체성, 명시된 영향 범위를 평가한다. Wallet이나 Rabbit에서 무언가 터졌을 때 Jayverse 자체 공개 관행도 이 기준을 충족해야 한다.
- **Devnet/Wallet: Jayverse의 멀티시그나 트레저리 키는 한 브랜드의 서로 다른 기기가 아니라 독립된 구현에 걸쳐야 한다.** 한 벤더 안의 계층들은 서로 상관돼 있어 같은 실패 표면을 공유하며, 이는 쿼럼의 취지를 무너뜨린다.
