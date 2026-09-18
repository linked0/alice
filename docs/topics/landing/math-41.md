## en
- **Verex: bound LMSR divergence from the CLOB with an explicit threshold.** Compare the LMSR quoted price against the CLOB best quote at varying liquidity parameter b, and trigger a maker-parameter review when divergence crosses a set number rather than drifting silently.
- **Verex: put the liquidity parameter's max-loss bound into the market-maker config.** LMSR's finite max-possible-loss is a direct function of b; that number belongs alongside slippage tuning as an operating loss budget, not just a code comment.
- **Auditor: test the fixed-point log-sum-exp for accumulated rounding error.** The same "was this computed under the invariant" question from the Liquid issuance case applies here — add a numerical-stability test over a long trade sequence, not just a single-call unit test.

## ko
- **Verex: LMSR과 CLOB의 괴리에 명시적 임계값을 둔다.** 유동성 파라미터 b를 바꿔가며 LMSR 호가와 CLOB 최우선 호가를 비교하고, 조용히 드리프트하게 두는 대신 괴리가 정해진 숫자를 넘으면 메이커 파라미터 검토를 트리거한다.
- **Verex: LMSR의 최대 손실 상한을 마켓메이커 설정에 넣는다.** LMSR의 유한한 최대 가능 손실은 b의 직접적 함수다. 이 숫자는 코드 주석이 아니라 슬리피지 튜닝 옆에 운영 손실 예산으로 있어야 한다.
- **Auditor: 고정소수점 log-sum-exp의 누적 반올림 오차를 테스트한다.** Liquid 발행 사고에서 나온 "이것이 불변식 아래에서 계산되었는가"라는 질문이 여기에도 적용된다. 단발 호출 유닛 테스트가 아니라 긴 거래 시퀀스에 걸친 수치 안정성 테스트를 추가한다.
