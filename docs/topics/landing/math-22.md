## en
- **Verex: eigendecompose the covariance matrix across correlated markets before aggregating position risk.** Check for a dominant common factor rather than treating markets as independent when sizing combined risk.
- **OFA: check the spectral radius of any iterative solver used in the clearing/matching step.** If it isn't below 1 the iteration won't converge — test this on devnet before it ships, not after a stuck auction in production.
- **Number: run PCA on the readings/indicator set before publishing one as an indicator.** A component only earns a slot in the catalogue once it's checked against being just an artifact of input scaling.

## ko
- **Verex: 포지션 리스크를 합산하기 전에 상관된 마켓들의 공분산 행렬을 고유분해한다.** 마켓들을 독립적인 것으로 취급하지 말고, 합산 리스크를 사이즈할 때 지배적인 공통 팩터가 있는지 확인한다.
- **OFA: 클리어링/매칭 단계에서 쓰는 반복 솔버의 스펙트럼 반경을 확인한다.** 1보다 작지 않으면 반복이 수렴하지 않는다 — 운영 중 경매가 멈춘 뒤가 아니라 출시 전에 devnet에서 테스트한다.
- **Number: 지표로 발행하기 전에 읽기/지표 집합에 PCA를 돌린다.** 컴포넌트가 단순히 입력 스케일링의 산물이 아님을 확인한 뒤에야 카탈로그에 지표로 올릴 자격을 얻는다.
