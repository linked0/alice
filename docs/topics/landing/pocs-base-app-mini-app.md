## en
- **Rabbit: benchmark the AA funnel against Base App's numbers.** Take jaylabs.xyz's connect → funded → first-transaction rates and compare them with what a passkey-smart-account arrival would look like; that gap is the actual case for tightening Rabbit's session-key onboarding.
- **Verex: write the geofencing rule before any Mini App wrapper exists.** If a Verex market ever opens inside a mainstream client, eligibility and jurisdiction checks have to ship before the manifest, since the market inherits the host's regulatory posture, not Rabbit's or Verex's own.
- **Wallet: treat "already funded on arrival" as the target state.** Wallet's simulate-before-sign screen should be judged by the same three ratios (open → funded → first transaction) Base App uses, not by whether the signature step itself is smooth.

## ko
- **Rabbit: AA 퍼널을 Base App 수치와 비교 측정한다.** jaylabs.xyz의 연결→충전→첫 거래 전환율을 패스키 스마트 계정이 이미 도착해 있는 경우와 비교하고, 그 격차가 Rabbit 세션 키 온보딩을 다듬어야 할 실제 근거가 된다.
- **Verex: Mini App 래퍼가 생기기 전에 지역 제한 규칙부터 적는다.** Verex 마켓이 주류 클라이언트 안에서 열리게 되면 매니페스트보다 먼저 적격성과 관할 검사가 있어야 한다. 마켓은 Rabbit이나 Verex 자체가 아니라 호스트의 규제 태도를 물려받기 때문이다.
- **Wallet: "도착 즉시 충전 완료"를 목표 상태로 삼는다.** Wallet의 서명 전 시뮬레이션 화면은 서명 단계 자체의 매끄러움이 아니라 Base App과 같은 세 가지 비율(열람→충전→첫 거래)로 평가해야 한다.
