## en
- **Verex: name the credit relationship before adding netting.** If portfolio margin or a hybrid credit pool is ever added to the CLOB, track required collateral ÷ net exposure as an explicit number — 1.0 means no netting exists, and the gap below it is what was bought and from whom.
- **Verex: if matching ever moves off the CLOB, buy back the audit trail on purpose.** Sequencer log commitments or Merkle proofs of the order lifecycle should cover amendments and cancellations, not just fills, and the provable share of the lifecycle should be a published number.
- **OFA: price the routing obligation, don't remove it.** The solver auction should measure realized slippage against the executable side of the book (ask when buying, bid when selling), and slashable solver commitments are what makes the MEV cost explicit rather than hidden.
- **Auditor / Devnet: the oracle-failure row is a surveillance job, not a feature.** Write the invariant checks, circuit breakers and rate limits as code that runs without anyone watching, and track time-to-resolution when the primary oracle is unavailable as a standing number.

## ko
- **Verex: 네팅을 추가하기 전에 되살아나는 신용 관계를 명시한다.** CLOB에 포트폴리오 마진이나 하이브리드 신용 풀이 추가된다면, 필요 담보 ÷ 순노출을 명시적 숫자로 추적한다. 1.0이면 네팅이 없다는 뜻이고, 그 아래 격차가 무엇을 누구에게서 사왔는지를 말해준다.
- **Verex: 매칭이 CLOB 밖으로 나간다면 감사 추적을 의도적으로 되사온다.** 시퀀서 로그 커밋이나 주문 생애주기의 머클 증명은 체결뿐 아니라 정정과 취소도 커버해야 하고, 생애주기 중 증명 가능한 비율을 공개 숫자로 둔다.
- **OFA: 라우팅 의무를 없애지 말고 가격을 매긴다.** 솔버 경매는 실행 가능한 호가창 기준 실현 슬리피지(매수 시 ask, 매도 시 bid)를 측정해야 하고, 슬래시 가능한 솔버 커밋이야말로 MEV 비용을 숨기지 않고 드러내는 장치다.
- **Auditor / Devnet: 오라클 실패 행은 기능이 아니라 감시 업무다.** 불변식 체크, 서킷 브레이커, 레이트 리밋을 아무도 지켜보지 않아도 돌아가는 코드로 작성하고, 주 오라클 불가 시 해결까지 걸리는 시간을 상시 숫자로 추적한다.
