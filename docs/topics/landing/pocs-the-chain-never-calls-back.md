## en
- **Wallet: tier payment notifications at inclusion and finality, with a retraction path.** Any incoming-transfer alert in Wallet should send tentative at inclusion, upgrade to confirmed at finality, and carry a message id so a reorg drill on Devnet can prove the retraction actually fires.
- **Rabbit: build the same event-queue-notify pipeline for session-key actions.** Agentic executions (a mandate firing, a session key spending) need dedup across watcher restarts and websocket reconnects, not a fire-and-forget send.
- **Verex: match settlement notifications to the dispute window.** A trader should be told "detected" at inclusion and "settled" only after the dispute window closes, and a market that gets disputed must retract any tentative "you won" message it already sent.

## ko
- **Wallet: 결제 알림을 인클루전과 파이널리티로 나누고 철회 경로를 둔다.** Wallet의 입금 알림은 인클루전 시점에 잠정 알림을 보내고 파이널리티에서 확정으로 올리며, 메시지에 id를 붙여 Devnet 리오르그 드릴로 철회가 실제로 발동하는지 증명할 수 있게 한다.
- **Rabbit: 세션 키 액션에도 같은 이벤트-큐-알림 파이프라인을 만든다.** 에이전트 실행(만데이트 발동, 세션 키 지출)은 와처 재시작과 웹소켓 재연결에도 중복 발송되지 않아야 하며, 그냥 던지고 잊는 방식이면 안 된다.
- **Verex: 정산 알림을 분쟁 기간에 맞춘다.** 트레이더에게는 인클루전 시점에 "감지됨", 분쟁 기간이 끝난 뒤에만 "정산됨"을 알려야 하고, 분쟁이 걸린 마켓은 이미 보낸 잠정 "승리" 메시지를 철회해야 한다.
