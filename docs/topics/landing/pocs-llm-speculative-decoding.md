## en
- **Number: if the research pipeline or the daily alice-tech report ever chains LLM calls, apply the draft-then-verify pattern.** A fast cheap pass drafts, a slower pass checks, cutting latency without changing output quality.
- **Auditor: an anomaly or resolution-check pipeline that runs a fast flag model and a careful verify model is the same shape as speculative decoding.** Measure the fast model's agreement rate before deciding it's worth running.

## ko
- **Number: 리서치 파이프라인이나 매일의 alice-tech 리포트가 LLM 호출을 체인으로 연결하게 되면, draft-then-verify 패턴을 적용한다.** 빠르고 저렴한 패스가 초안을 만들고 느린 패스가 검증해, 출력 품질을 바꾸지 않으면서 지연시간을 줄인다.
- **Auditor: 빠른 플래그 모델과 신중한 검증 모델을 함께 돌리는 이상 탐지나 정산 검증 파이프라인은 speculative decoding과 같은 구조다.** 이를 도입할 가치가 있는지 판단하기 전에 빠른 모델의 합의율을 먼저 측정한다.
