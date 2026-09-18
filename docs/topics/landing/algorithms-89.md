## en
- **Verex: write the one rounding-convention document and link every module to it.** LMSR's cost function, the CLOB and the settlement path each do their own fixed-point division; a single round-down-what-user-receives, round-up-what-user-pays rule, stated once, is what stops them drifting apart.
- **Auditor: turn the buy-then-sell cycle test into a standing CI check, not a one-time exercise.** Simulating thousands of rapid trade cycles and asserting pool balance never leaks is the concrete test the Auditor row should require before any change to Verex's fixed-point math ships.

## ko
- **Verex: 반올림 규칙 문서 하나를 작성하고 모든 모듈이 그것을 참조하게 한다.** LMSR의 비용 함수, CLOB, 정산 경로가 각자 고정소수점 나눗셈을 한다. 사용자가 받는 것은 내림, 지불하는 것은 올림이라는 규칙 하나를 한 번만 적어두는 것이 서로 어긋나는 것을 막는다.
- **Auditor: 매수-매도 사이클 테스트를 일회성 연습이 아니라 상시 CI 체크로 만든다.** 수천 번의 빠른 거래 사이클을 시뮬레이션해 풀 잔액이 새지 않는지 검증하는 것이, Verex의 고정소수점 수학이 바뀔 때마다 Auditor 행이 요구해야 할 구체적인 테스트다.
