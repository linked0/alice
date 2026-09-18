## en
- **Verex: enforce injectable time, seed and integer-only math specifically in the off-chain settlement/matching replica.** No wall-clock reads, no floating point, no unsorted map iteration in any code path that must match an on-chain result.
- **CI: add the 1000-run same-seed replay test as a merge gate for Verex's off-chain settlement code.** If the output hashes don't all match, block the merge — that's this PoC's exercise applied directly.
- **DeFi: apply the same fixed-point, injectable-time discipline to jayverse-defi's yield and rebasing calculations,** since they recompute state the same way Verex's settlement engine does.

## ko
- **Verex: 오프체인 정산·매칭 레플리카에는 시간, 시드, 정수 전용 수학을 명시적으로 주입 가능하게 만든다.** 온체인 결과와 일치해야 하는 어떤 코드 경로에서도 wall-clock 읽기, 부동소수점, 정렬되지 않은 맵 순회를 쓰지 않는다.
- **CI: 같은 시드로 1000번 재생하는 테스트를 Verex 오프체인 정산 코드의 머지 게이트로 추가한다.** 출력 해시가 모두 일치하지 않으면 머지를 막는다 — 이 PoC의 연습문제를 그대로 적용한 것이다.
- **DeFi: 같은 고정소수점, 주입 가능한 시간 원칙을 jayverse-defi의 수익률·리베이스 계산에도 적용한다.** Verex의 정산 엔진과 같은 방식으로 상태를 재계산하기 때문이다.
