## en
- **Number: choose an MoE shape, not a bigger dense model, for any locally hosted research assistant.** If Number ever self-hosts inference for readings or indicators, active parameters set the speed and total parameters set the capacity — pick the model by the ceiling that division gives, not by parameter count in a headline.
- **Rabbit: benchmark tokens/sec with the context filled, before committing to local infra for the agent loop.** An agent's context is never short, and attention cost grows with it — measure throughput with a realistic session length, not a fresh prompt, before deciding whether the AA agent's reasoning runs local or cloud.
- **Devnet/infra: decide local vs cloud by utilisation, not by sticker price.** Cost per token is hardware divided by tokens generated over its life — only a continuously looping workload (an always-on agent) makes local inference pencil out; an idle dev box does not.

## ko
- **Number: 로컬로 서빙할 리서치 어시스턴트가 있다면 더 큰 dense 모델이 아니라 MoE 형태를 고른다.** Number가 읽기나 지표를 위해 언젠가 추론을 직접 호스팅한다면, 활성 파라미터가 속도를 정하고 전체 파라미터가 용량을 정한다. 헤드라인의 파라미터 수가 아니라 이 나눗셈이 주는 상한으로 모델을 고른다.
- **Rabbit: 로컬 인프라를 확정하기 전에 컨텍스트가 채워진 상태로 초당 토큰 수를 측정한다.** 에이전트의 컨텍스트는 절대 짧지 않고 어텐션 비용은 컨텍스트와 함께 커진다. AA 에이전트의 추론을 로컬로 돌릴지 클라우드로 돌릴지 결정하기 전에 신선한 프롬프트가 아니라 실제 세션 길이로 처리량을 잰다.
- **Devnet/인프라: 정가가 아니라 사용률로 로컬 대 클라우드를 결정한다.** 토큰당 비용은 하드웨어를 수명 동안 생성한 토큰 수로 나눈 값이다. 계속 도는 워크로드(상시 가동 에이전트)만 로컬 추론이 남고, 유휴 상태인 개발용 박스는 그렇지 않다.
