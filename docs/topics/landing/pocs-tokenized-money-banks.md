## en
- **Token/Bridge: classify JYVE's claim before shipping it.** JYVE is closer to family (2) — a redemption claim against the bridge's locked reserve — than a deposit; write that down in the bridge contract docs so users know what class of claim they hold, not just what chain it moved on.
- **Verex: name which family backs any stablecoin collateral.** If Verex accepts a stablecoin for margin or settlement, the resolution/collateral field should say whether it is a first-party redemption claim or a third-party token, since the two carry different counterparty risk the exchange is implicitly underwriting.
- **Auditor: add the deposit-to-stablecoin conversion cost as a watch item.** The LCR 25%→100% jump is exactly the kind of structural trigger the Auditor row should track for any Jayverse asset that might someday convert claim types, so the cost of that conversion is documented before it happens.
- **Devnet: model the three claim types as a small PoC.** A tokenized-deposit-style wrapper, a redemption-claim token and a pass-through are three different contracts, and Devnet is cheap enough to prototype the gap directly rather than assume they behave the same.

## ko
- **토큰/브릿지: JYVE의 청구권을 출시 전에 분류한다.** JYVE는 예금이라기보다 브릿지의 락업 준비금에 대한 상환 청구권(패밀리 2)에 가깝다. 브릿지 컨트랙트 문서에 이를 명시해 사용자가 어느 체인으로 이동했는지가 아니라 어떤 종류의 청구권을 보유하는지 알게 한다.
- **Verex: 스테이블코인 담보가 어느 패밀리인지 명시한다.** Verex가 마진이나 정산에 스테이블코인을 받는다면, 정산/담보 필드는 그것이 퍼스트파티 상환 청구권인지 서드파티 토큰인지 밝혀야 한다. 둘은 거래소가 암묵적으로 떠안는 거래상대방 리스크가 다르다.
- **Auditor: 예금-스테이블코인 전환 비용을 감시 항목으로 추가한다.** LCR 25%→100% 도약은 Jayverse의 어떤 자산이든 언젠가 청구권 종류를 바꿀 때 Auditor 행이 추적해야 할 전형적인 구조적 트리거이므로, 그 전환 비용을 일이 벌어지기 전에 문서화한다.
- **Devnet: 세 청구권 유형을 작은 PoC로 모델링한다.** 토큰화 예금형 래퍼, 상환 청구권 토큰, 패스스루는 서로 다른 컨트랙트다. Devnet은 셋이 같다고 가정하지 않고 그 차이를 직접 프로토타입할 만큼 저렴하다.
