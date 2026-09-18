## en
- **Verex: use mulDiv-style 512-bit intermediates for every LMSR and settlement calculation.** Never multiply and divide as two separate operations, and pick a rounding direction that favors the protocol over the user.
- **Verex: fuzz-test Q64.96 math for intermediate overflow before any mainnet-bound deployment.** Deliberately search for overflow inputs in the price and settlement math, mirroring the exercise, and fix them with the mulDiv approach.
- **Auditor: require the rounding direction to be a reviewable, explicit line.** For every fixed-point calculation in Verex or DeFi, a wrong rounding direction is a silent balance-leak vulnerability, so it should never be implicit.

## ko
- **Verex: 모든 LMSR·정산 계산에 mulDiv 방식의 512비트 중간값을 사용한다.** 곱셈과 나눗셈을 두 개의 분리된 연산으로 절대 처리하지 않고, 사용자보다 프로토콜에 유리한 반올림 방향을 선택한다.
- **Verex: 메인넷 배포 전에 Q64.96 수학의 중간 오버플로를 퍼즈 테스트한다.** 연습문제처럼 가격·정산 수학에서 오버플로를 유발하는 입력을 의도적으로 찾아내고 mulDiv 방식으로 고친다.
- **Auditor: 반올림 방향을 검토 가능한 명시적 라인으로 요구한다.** Verex나 DeFi의 모든 고정소수점 계산에서 잘못된 반올림 방향은 조용한 잔고 유출 취약점이므로 암묵적이어서는 안 된다.
