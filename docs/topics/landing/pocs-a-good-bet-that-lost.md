## en
- **Verex: add a break-even-probability column to every market-maker/agent trade log.** Derive it from the traded price (pot odds) and measure edge against that number, not against 50% — the honest edge check this page names.
- **Verex/OFA: size positions by Kelly fraction capped for survival, not by raw expected value.** Compare actual stake as a fraction of bankroll against the Kelly fraction implied by claimed edge, and cap the market maker's or solver's exposure by risk of ruin, not by expected return alone.
- **Auditor: compute required sample size before claiming an edge.** Given a claimed edge and observed variance, calculate how many resolutions are needed to distinguish it from zero at a stated confidence, and withhold the "it's working" claim until that N is reached.
- **Verex: re-validate market-maker edge against live trading, not a static backtest.** A backtest describes a world that no longer contains the market maker once it trades — schedule a recurring live-vs-backtest comparison instead of trusting one offline number.

## ko
- **Verex: 모든 마켓 메이커/에이전트 거래 로그에 손익분기 확률 열을 추가한다.** 거래된 가격에서 유도한 값(팟 오즈)을 쓰고, 50%가 아니라 그 숫자 대비 엣지를 측정한다. 이 페이지가 말하는 정직한 엣지 검증이다.
- **Verex/OFA: 원시 기대값이 아니라 생존을 위해 상한을 둔 켈리 비율로 포지션 크기를 정한다.** 실제 베팅 비중을 뱅크롤 대비 비율로 놓고 주장된 엣지가 내포하는 켈리 비율과 비교하며, 마켓 메이커나 솔버의 노출을 기대수익이 아니라 파산 확률로 제한한다.
- **Auditor: 엣지를 주장하기 전에 필요한 표본 크기를 계산한다.** 주장된 엣지와 관측된 분산이 주어지면 정해진 신뢰도에서 그 엣지를 0과 구별하는 데 필요한 정산 횟수를 계산하고, N에 도달하기 전에는 "작동하고 있다"는 주장을 유보한다.
- **Verex: 정적 백테스트가 아니라 실거래 대비로 마켓 메이커 엣지를 재검증한다.** 백테스트는 마켓 메이커가 거래를 시작하는 순간 더 이상 존재하지 않는 세계를 묘사한다. 오프라인 숫자 하나를 믿는 대신 실거래 대 백테스트 비교를 주기적으로 스케줄링한다.
