## en
- **Verex: pick the aggregation scheme explicitly and defend against rogue keys.** If the CLOB ever batches many market-maker signatures, BLS pairing-based aggregation suits an open, validator-like set while Schnorr/MuSig fits a small fixed multisig — document which is used and require proof of possession so an attacker can't craft a key relative to someone else's.
- **Wallet: test that EIP-712 signature verification rejects the malleable counterpart, not just the canonical one.** Since ecrecover relies on ECDSA's public-key-recovery property, add a test that a Wallet-signed payload's (r, -s mod n) variant is rejected, not silently accepted as a second valid signature.

## ko
- **Verex: 집계 스킴을 명시적으로 고르고 rogue-key 공격을 방어한다.** CLOB이 여러 마켓메이커 서명을 배치로 묶는다면, 페어링 기반 BLS 집계는 개방적이고 검증자 집합 같은 상황에 맞고 Schnorr/MuSig는 소규모 고정 멀티시그에 맞는다. 어느 쪽을 쓰는지 문서화하고, 공격자가 남의 공개키에 상대적으로 키를 조작하지 못하도록 소유 증명을 요구한다.
- **Wallet: EIP-712 서명 검증이 정규 형태뿐 아니라 malleable한 변형도 거부하는지 테스트한다.** ecrecover는 ECDSA의 공개키 복구 속성에 의존하므로, Wallet이 서명한 페이로드의 (r, -s mod n) 변형이 두 번째 유효 서명으로 조용히 받아들여지지 않고 거부되는지 테스트를 추가한다.
