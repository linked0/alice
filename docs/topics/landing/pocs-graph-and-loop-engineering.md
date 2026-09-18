## en
- **CI: replace any single do-everything agent prompt with a planner-worker-checker graph.** Before adding parallel agents to any Jayverse repo, require one typed handoff and one bounded retry per task, not a single prompt asked to plan, execute and verify at once.
- **Auditor: keep the evaluator and budget outside the graph being improved.** If agent workflows for Rabbit or Verex are ever allowed to propose their own changes, gate promotion through a fixed Auditor-run evaluation; never let the graph grade itself.
- **gitboard: surface retry counts and terminal-failure reasons per agent task.** A stuck or looping build should show up as a traced, bounded state on the dashboard, not silent spend.

## ko
- **CI: 모든 걸 한 프롬프트에 맡기는 에이전트를 planner-worker-checker 그래프로 바꾼다.** Jayverse 저장소 어디든 병렬 에이전트를 추가하기 전에, 계획·실행·검증을 한 프롬프트에 몰아넣지 말고 타입이 있는 핸드오프 하나와 상한이 있는 재시도 하나를 요구한다.
- **Auditor: 평가자와 예산을 개선 대상 그래프 바깥에 둔다.** Rabbit이나 Verex의 에이전트 워크플로우가 스스로 변경을 제안하게 하더라도, 승격은 고정된 Auditor 평가를 거치게 한다. 그래프가 자기 숙제를 채점하게 두지 않는다.
- **gitboard: 에이전트 작업별 재시도 횟수와 종료 실패 사유를 노출한다.** 멈추거나 도는 빌드가 조용한 지출이 아니라 추적 가능한, 범위가 정해진 상태로 대시보드에 나타나야 한다.
