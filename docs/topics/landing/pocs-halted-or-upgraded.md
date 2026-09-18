## en
- **Devnet/Bridge: classify any emergency fix by where the patch lands.** If Devnet or the bridge relayer ever needs an emergency change, diff it against the prior version to see whether it touches one contract or shared infrastructure, and name the incident accordingly in the postmortem.
- **Auditor: build the block-gap timeline before writing the incident summary.** For any outage, pull block heights and timestamps around the window first and let that number decide the wording, rather than starting from the announcement text.
- **gitboard: log response speed as a governance metric.** Record detection-to-patch and patch-to-adoption times for any emergency response across services, since how fast a fix reaches quorum is itself a measurement of who controls the system.

## ko
- **Devnet/Bridge: 패치가 어디에 떨어지는지로 긴급 수정을 분류한다.** Devnet이나 브리지 릴레이어에 긴급 변경이 필요하다면 이전 버전과 diff해서 컨트랙트 하나를 건드렸는지 공유 인프라를 건드렸는지 확인하고, 사후 보고서에서 그에 맞게 이름 붙인다.
- **Auditor: 사고 요약을 쓰기 전에 블록 갭 타임라인부터 만든다.** 어떤 장애든 먼저 해당 구간의 블록 높이와 타임스탬프를 뽑아 그 숫자가 표현을 결정하게 한다. 발표문에서 출발하지 않는다.
- **gitboard: 대응 속도를 거버넌스 지표로 기록한다.** 어떤 서비스든 긴급 대응의 탐지-패치, 패치-적용 시간을 기록한다. 수정이 쿼럼에 도달하는 속도 자체가 누가 시스템을 통제하는지를 보여주는 측정값이다.
