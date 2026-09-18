## en
- **Number: distill any on-site prediction model from a larger reference model.** If Number ships an indicator or prediction model, train it on a narrow task from a bigger teacher's outputs, and publish capability-retained versus size-saved next to the indicator.
- **Verex: use a distilled model as the cheap first-pass resolution check.** Keep a larger model or a human as the escalation path when the small model's triage disagrees with the expected outcome.
- **Auditor: require the teacher, task and retained-capability note for any distilled model in production.** A distilled model's output should never be judged as if it came from the teacher without that methodology written down.

## ko
- **Number: 사내 예측 모델은 더 큰 참조 모델에서 증류한다.** Number가 지표나 예측 모델을 내놓는다면 더 큰 티처 모델의 출력으로 좁은 과업에 대해 학습시키고, 지표 옆에 보존된 능력 대비 절감된 크기를 공개한다.
- **Verex: 증류된 모델을 저비용 1차 정산 체크로 쓴다.** 작은 모델의 트리아지가 기대 결과와 어긋날 때 더 큰 모델이나 사람을 에스컬레이션 경로로 유지한다.
- **Auditor: 프로덕션에 쓰이는 증류 모델마다 티처, 과업, 보존된 능력을 문서로 요구한다.** 이 방법론을 적어두지 않은 채 증류 모델의 출력을 티처의 출력처럼 판단해서는 안 된다.
