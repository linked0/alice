## en
- **Bridge: split the lock-and-mint relayer's signing key with k-of-n Shamir sharing instead of one key.** This directly fixes the single-relayer risk this batch's zkEVM PoC flags — compromising fewer than k shares reveals nothing.
- **Verex: use threshold signing for any oracle or resolution-source key, not a single signer.** A k-of-n scheme means no single compromised party can forge a resolution or a price feed.
- **Number: if readings are ever redundantly distributed, use Reed-Solomon erasure coding instead of plain replication.** It gets the same durability at lower storage cost, per this PoC's structure.

## ko
- **Bridge: lock-and-mint 릴레이어의 서명 키를 단일 키가 아니라 k-of-n Shamir 분산으로 나눈다.** 이는 이 배치의 zkEVM PoC가 지적한 단일 릴레이어 위험을 직접 해결한다 — k개 미만의 조각이 유출돼도 아무 정보도 드러나지 않는다.
- **Verex: 단일 서명자가 아니라 오라클이나 정산 소스 키에 threshold 서명을 쓴다.** k-of-n 방식이면 단일 당사자가 침해당해도 정산이나 가격 피드를 위조할 수 없다.
- **Number: 읽기가 언젠가 중복 배포된다면 단순 복제 대신 Reed-Solomon 소거 코딩을 쓴다.** 이 PoC의 구조에 따라 같은 내구성을 더 낮은 저장 비용으로 얻는다.
