## en
- **Number: reproduce the accuracy-vs-bit-width curve on hardware jay actually owns before trusting a vendor's "retains a lot of accuracy."** If Number ever runs local inference for research, measure perplexity and top-token agreement at each bit-width rather than citing the quantization vendor's numbers.
- **Devnet: budget RAM+VRAM against the quant size rule of thumb before calling anything "local."** A model that needs 450GB is only local for a server Devnet owns, not a claim to repeat for a smaller box, and disk offloading past that line quietly changes the real throughput number.
- **Auditor/gitboard: record which dtype and measured accuracy delta backed any agent-facing decision.** "Sub-2-bit, still good enough" should be a logged number tied to a specific decision, not a marketing phrase carried into the pipeline.

## ko
- **Number: 벤더의 "정확도를 많이 유지한다"는 말을 믿기 전에 jay가 실제로 가진 하드웨어에서 정확도 대 비트폭 곡선을 재현한다.** Number가 연구용으로 로컬 추론을 돌린다면, 양자화 벤더의 수치를 인용하는 대신 각 비트폭에서 perplexity와 top-token 일치율을 직접 측정한다.
- **Devnet: 무언가를 "로컬"이라고 부르기 전에 quant 크기 어림 규칙(RAM+VRAM ≈ quant 크기)으로 예산을 잡는다.** 450GB가 필요한 모델은 Devnet이 소유한 서버에서만 로컬이지 더 작은 머신에 그대로 옮길 수 있는 주장이 아니며, 그 선을 넘어가는 디스크 오프로딩은 실제 처리량 숫자를 조용히 바꿔버린다.
- **Auditor/gitboard: 에이전트 관련 결정을 뒷받침한 dtype과 측정된 정확도 차이를 기록한다.** "sub-2-bit인데도 충분히 좋다"는 파이프라인에 그대로 들어가는 마케팅 문구가 아니라 특정 결정에 묶인 기록된 숫자여야 한다.
