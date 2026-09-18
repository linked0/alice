## en
- **Verex: check dispute-resolution rewards against the VCG payment rule.** Model the oracle-dispute payment so each participant's payment equals the welfare their report costs everyone else, and check whether the current or planned design still makes truthful reporting a dominant strategy before shipping it.
- **Verex: guard against Sybil and budget-balance failures explicitly.** Since dispute participants can create multiple identities, add a staking or Sybil-cost requirement rather than assuming VCG's truthfulness guarantee survives fake identities unmodified.
- **OFA: apply the same dominant-strategy test to solver bids.** The ATLAS-style solver auction is a mechanism-design problem too — check whether solver bidding is truthful under the chosen rule before assuming competition alone aligns incentives.

## ko
- **Verex: 분쟁 정산 보상을 VCG 지불 규칙으로 검증한다.** 오라클 분쟁 지불이 각 참여자가 나머지 모두에게 끼친 복지 비용과 같도록 모델링하고, 현재 또는 계획된 설계가 출시 전에도 진실한 보고를 여전히 우월 전략으로 만드는지 확인한다.
- **Verex: 시빌과 예산 균형 실패를 명시적으로 방어한다.** 분쟁 참여자가 여러 신원을 만들 수 있으므로, VCG의 진실성 보장이 가짜 신원에도 그대로 유지된다고 가정하지 말고 스테이킹이나 시빌 비용 요건을 추가한다.
- **OFA: 솔버 입찰에도 같은 우월 전략 테스트를 적용한다.** ATLAS식 솔버 경매도 메커니즘 설계 문제다. 경쟁만으로 인센티브가 정렬된다고 가정하기 전에, 선택한 규칙 아래 솔버 입찰이 진실한지 확인한다.
