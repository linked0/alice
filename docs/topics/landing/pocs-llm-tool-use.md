## en
- **Rabbit: keep a deterministic validator between the tool call and the signature.** Any agent-initiated mandate execution should pass through a validator before the signed transaction is sent — the wrong-call case this card describes is exactly what simulate-before-sign exists to catch.
- **OFA: treat a solver's proposed fill as a tool call, not an execution.** The auction contract is the validation layer that must reject a bad solver call before it settles, the same intent-versus-execution gap this card flags for function calling.

## ko
- **Rabbit: 툴 콜과 서명 사이에 결정적 검증자를 둔다.** 에이전트가 시작한 mandate 실행은 서명된 트랜잭션이 나가기 전에 검증자를 거쳐야 한다. 이 카드가 설명하는 잘못된 호출 케이스는 정확히 simulate-before-sign이 잡아내기 위해 존재하는 것이다.
- **OFA: 솔버가 제안한 체결을 실행이 아니라 툴 콜로 취급한다.** 옥션 컨트랙트는 나쁜 솔버 호출이 정산되기 전에 거부해야 하는 검증 레이어다. 이 카드가 함수 호출에 대해 지적하는 의도-대-실행 간극과 같다.
