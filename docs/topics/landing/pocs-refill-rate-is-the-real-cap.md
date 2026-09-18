## en
- **Bridge/Token: compute max loss = limit × (time-to-detect ÷ refill period) for JYVE's mint/burn rate limit, using Jayverse's real detection time, not the headline limit.** Record that number as the actual cap the team can survive, not the rate limit alone.
- **Bridge/Token: choose the refill period as an explicit safety/availability trade and write down the honest-user queue it implies.** A faster refill approaches the whole reserve as the real cap; a slower one throttles legitimate bridge users.
- **Auditor: require every rate-limited contract (bridge mint, relayer) to publish its refill period next to its limit.** A quoted rate limit without a refill period is an incomplete spec and should be treated as one.

## ko
- **Bridge/Token: JYVE의 발행/소각 레이트 리밋에 대해 최대 손실 = 한도 × (탐지 시간 ÷ 리필 주기)를 Jayverse의 실제 탐지 시간으로 계산한다.** 레이트 리밋 자체가 아니라 이 숫자를 팀이 감당할 수 있는 실제 상한으로 기록한다.
- **Bridge/Token: 리필 주기를 안전성/가용성 트레이드오프로 명시적으로 선택하고 그로 인한 정상 사용자 대기열을 적어둔다.** 리필이 빠를수록 실질 상한은 전체 준비금에 가까워지고, 느릴수록 정상 브리지 사용자가 막힌다.
- **Auditor: 레이트 리밋이 걸린 모든 컨트랙트(브리지 발행, 릴레이어)가 한도 옆에 리필 주기를 공개하도록 요구한다.** 리필 주기 없이 제시된 레이트 리밋은 불완전한 스펙으로 취급한다.
