## en
- **Bridge: model lock-and-mint as a durable-execution flow, not a status column.** The Anvil-to-Sepolia relayer's lock, wait-for-confirmations, mint sequence is exactly the long-running-with-external-waits shape; fix the nonce or request id outside the retried step so a retry can never double-mint.
- **Verex: give market resolution the same treatment.** Close, wait for oracle, dispute window, settle, withdraw should run as a journaled workflow that survives a worker crash, with all clock reads and RPC calls pushed into activities, not the workflow body.
- **Devnet: gate workflow-code changes with versioning before redeploying.** Any in-flight resolution or bridge run must not silently take a different history branch when the code changes underneath it — version the workflow, don't just ship.

## ko
- **Bridge: 락-앤-민트를 상태 컬럼이 아니라 durable-execution 흐름으로 모델링한다.** Anvil↔Sepolia 릴레이어의 락, 컨펌 대기, 민트 시퀀스는 정확히 장기 실행에 외부 대기가 낀 모양이다. 재시도되는 단계 밖에서 논스나 요청 ID를 고정해 재시도가 이중 민트로 이어지지 않게 한다.
- **Verex: 마켓 정산도 같은 방식으로 다룬다.** 종료, 오라클 대기, 분쟁 기간, 정산, 인출은 워커가 죽어도 살아남는 저널링된 워크플로우로 돌려야 하고, 시계 읽기와 RPC 호출은 워크플로우 본문이 아니라 액티비티로 넣는다.
- **Devnet: 워크플로우 코드를 바꾸기 전 버저닝으로 막는다.** 진행 중인 정산이나 브리지 실행이 코드가 바뀌었을 때 조용히 다른 히스토리 분기를 타면 안 된다. 그냥 배포하지 말고 워크플로우를 버전으로 관리한다.
