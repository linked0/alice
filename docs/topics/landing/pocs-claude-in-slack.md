## en
- **alice-tech report: build the Slack-to-Notion summarization by hand before automating it.** Route a Slack thread through Claude's existing Slack and Notion MCP connectors into the daily alice-tech report manually first, and only consider a tagged bot once that manual step is run often enough to be missed.
- **gitboard: treat a future tagged presence as an ops commitment, not a convenience.** If gitboard ever gets an @-mentionable Claude, budget for it having to always be running, handle being tagged in the wrong channel, and fail visibly — the availability promise is the expensive half.
- **Auditor: apply the same "run it manually, see if it's missed" test before automating.** Before building any automated auditor bot, run the manual publish-and-log workflow for a few weeks; if nobody misses it when it stops, the automation was not needed.

## ko
- **alice-tech 리포트: 자동화 전에 Slack→Notion 요약을 수동으로 먼저 만든다.** Claude의 기존 Slack·Notion MCP 커넥터로 Slack 스레드를 일일 alice-tech 리포트로 수동 연결해 먼저 돌려보고, 그 수동 단계가 자주 그리워질 만큼 쓰인 뒤에야 태그형 봇을 고려한다.
- **gitboard: 미래의 태그형 프레즌스는 편의가 아니라 운영 책임으로 다룬다.** gitboard에 @멘션 가능한 Claude가 생긴다면, 항상 실행 중이어야 하고, 엉뚱한 채널에서 태그되는 상황을 처리하고, 눈에 보이게 실패해야 한다는 비용까지 예산에 넣는다. 가용성 약속이 비싼 쪽이다.
- **Auditor: 자동화 전에 "수동으로 돌려보고 그리운지 본다"는 같은 테스트를 적용한다.** 자동화된 auditor 봇을 만들기 전에 수동 게시·기록 워크플로를 몇 주 돌려본다. 멈췄을 때 아무도 그리워하지 않으면 자동화는 필요 없던 것이다.
