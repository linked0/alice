# 25 · Interview — The reviewer found a bug in your take-home
title_ko: 리뷰어가 과제에서 버그를 찾았다
situation: Take-home debrief for a senior engineer role at a Berlin exchange. Jay submitted an order-matching service. Tomasz, the reviewer, opens with a race condition Jay missed: two cancels for the same order can both succeed. Forty minutes left, and the first two matter most.
situation_ko: 베를린 거래소 시니어 엔지니어 과제 디브리프. Jay는 주문 매칭 서비스를 제출했다. 리뷰어 Tomasz가 Jay가 놓친 레이스 컨디션으로 시작한다. 같은 주문에 대한 취소 둘이 모두 성공할 수 있다. 40분이 남았고, 처음 2분이 가장 중요하다.
why: The take-home debrief is not graded on the code you sent. It is graded on what you do when someone shows you it is wrong. Defending, over-apologising, and "I would have fixed that with more time" all lose. Diagnosing out loud wins.
why_ko: 과제 디브리프는 제출한 코드로 채점되지 않는다. 누군가 틀렸다고 보여줄 때 무엇을 하는지로 채점된다. 방어, 과한 사과, "시간이 더 있었으면 고쳤을 것"은 모두 진다. 소리 내어 진단하는 것이 이긴다.
status: planned

## Dialogue
Tomasz: I ran two concurrent cancels against the same order id. Both returned 200 and the order book went negative. Talk me through that.
> 같은 주문 id에 취소 둘을 동시에 보냈습니다. 둘 다 200을 돌려주고 오더북이 마이너스가 됐어요. 설명해 보세요.
Jay: You're right, and I can see why. The cancel reads the order, checks it's open, then writes the cancelled state in a separate statement. Between the read and the write there's no lock and no version check, so two readers both see "open." That's a bug I should have caught; it's the same shape as a double-spend.
> 맞습니다, 이유도 보입니다. 취소가 주문을 읽고, 열려 있는지 확인하고, 별도 문장으로 취소 상태를 씁니다. 읽기와 쓰기 사이에 락도 버전 체크도 없어서 두 읽기가 모두 "열림"을 봅니다. 제가 잡아야 했던 버그고, 이중 지출과 같은 모양입니다.
Tomasz: How would you fix it?
> 어떻게 고치겠어요?
Jay: Smallest change: make the cancel a single conditional update, "set state to cancelled where id equals X and state equals open," and treat zero rows affected as "already cancelled," returning 409 instead of 200. That's atomic in Postgres without a transaction. If we later move the book in-memory, the same rule becomes a compare-and-swap on the order's version.
> 가장 작은 변경: 취소를 단일 조건부 업데이트로 만듭니다. "id가 X이고 state가 open인 곳의 state를 cancelled로." 영향 받은 행이 0이면 "이미 취소됨"으로 보고 200 대신 409를 반환합니다. Postgres에서는 트랜잭션 없이 원자적입니다. 나중에 오더북을 인메모리로 옮기면 같은 규칙이 주문 버전에 대한 compare-and-swap이 됩니다.
Tomasz: Why did your tests not catch it?
> 왜 테스트가 못 잡았죠?
Jay: Because I tested the cancel path, not the cancel race. All my tests are sequential. The honest answer is that I didn't write a single concurrency test, and for a matching engine that's the wrong place to save time. If I were adding one now, it'd be a test that fires N cancels in parallel and asserts exactly one 200.
> 취소 경로를 테스트했고 취소 레이스는 테스트하지 않았으니까요. 제 테스트는 전부 순차적입니다. 정직한 답은 동시성 테스트를 하나도 쓰지 않았다는 것이고, 매칭 엔진에서 그건 시간을 아낄 자리가 아니었습니다. 지금 하나 추가한다면 N개의 취소를 병렬로 쏘고 정확히 하나만 200인지 검증하는 테스트입니다.
Tomasz: Anything else in there you'd flag before we do?
> 우리가 찾기 전에 먼저 지적할 게 있나요?
Jay: Two. The fee calculation uses floats; that should be integer minor units. And the matching loop is O(n) per incoming order because I used a list, which is fine for the exercise and wrong for production; a price-level map with FIFO queues is the standard fix. I chose to spend the time on the API and the tests instead, and I'd make that call again for a take-home, but I'd want those two fixed before anything real ran on it.
> 둘요. 수수료 계산이 float를 씁니다. 정수 최소 단위여야 합니다. 그리고 리스트를 써서 매칭 루프가 들어오는 주문마다 O(n)인데, 과제에는 괜찮고 프로덕션에는 틀렸습니다. 가격 레벨 맵과 FIFO 큐가 표준 해법입니다. 대신 API와 테스트에 시간을 쓰기로 했고 과제라면 다시 그렇게 하겠지만, 실제로 무엇이든 돌리기 전엔 그 둘을 고치고 싶습니다.

## Techniques
1. **동의하고, 즉시 진단한다.** "You're right, and I can see why. The cancel reads… then writes… no lock and no version check." 방어도 사과도 아닌, 원인을 한 문장으로. 리뷰어가 보는 것은 당신이 프로덕션 장애 회의에서 어떻게 행동할지다.
2. **가장 작은 수정과 다음 수정을 함께.** "Smallest change… If we later move the book in-memory, the same rule becomes a compare-and-swap." 지금 고칠 것과 아키텍처가 바뀌어도 살아남는 원칙을 같이 말하면 시니어로 읽힌다.
3. **묻기 전에 먼저 꺼낸다.** "Anything else you'd flag?" 에 "Two." 자기 코드의 약점을 리뷰어보다 먼저 아는 후보는 채용된다. 그리고 트레이드오프의 이유("I chose to spend the time on…")를 붙여 실수와 선택을 구분한다.

## Expressions
| talk me through that | 그것을 설명해 달라 |
| I can see why | 이유가 보인다 |
| the same shape as | ~와 같은 모양(구조)이다 |
| smallest change | 가장 작은 변경 |
| zero rows affected | 영향 받은 행 0 |
| the honest answer is | 정직한 답은 |
| the wrong place to save time | 시간을 아낄 자리가 아니다 |
| anything you'd flag | 지적할 것이 있는가 |
| integer minor units | 정수 최소 단위(센트 등) |
| I'd make that call again | 다시 그렇게 결정하겠다 |
| before anything real ran on it | 실제로 무엇이든 그 위에서 돌기 전에 |
