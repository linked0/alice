# 291 · Word — flaky
title_ko: flaky — (테스트가) 불안정한; (사람이) 못 미더운
situation: Monday morning triage. One integration test fails about once in ten runs and has been blocking merges all week. Sam wants to delete it; Jay wants it quarantined and fixed, and the same word ends up describing the vendor whose sandbox causes it.
situation_ko: 월요일 아침 트리아지. 통합 테스트 하나가 열 번에 한 번꼴로 실패하면서 한 주 내내 머지를 막고 있다. Sam은 지우자고 하고 Jay는 격리한 뒤 고치자고 하는데, 그 원인인 외부 업체의 샌드박스에도 같은 단어가 붙는다.
why: **Flaky** describes something that cannot be relied on to behave the same way twice: a flaky test passes or fails at random, and a flaky person cancels late and forgets what they promised. The literal sense is "coming off in flakes", as in flaky pastry. About a test or a vendor it is ordinary engineering vocabulary; said to a colleague's face it is an insult, so keep it for systems.
why_ko: **flaky**는 같은 조건에서 같게 동작한다고 믿을 수 없는 것을 가리킨다. flaky test는 무작위로 통과하거나 실패하고, flaky한 사람은 약속을 잊고 막판에 취소한다. 원래 뜻은 "얇게 벗겨지는"이다(flaky pastry). 테스트나 외부 업체에 쓰면 평범한 엔지니어링 어휘지만, 동료를 앞에 두고 쓰면 모욕이 된다. 사람이 아니라 시스템에 쓰는 편이 안전하다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, third export — the 전체 view (2026-09-21), card 116 of 228: "flaky [ˈfleɪki] — 1. 형용사 (조각조각으로) 얇게 벗겨지는 2. 괴짜인; 뭘 잘 잊어먹는" (옥스퍼드). The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장 세 번째 내보내기 — 전체 보기(2026-09-21), 228장 중 116번 카드: "flaky [ˈfleɪki] — 1. 형용사 (조각조각으로) 얇게 벗겨지는 2. 괴짜인; 뭘 잘 잊어먹는" (옥스퍼드). 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-183.txt

## Dialogue
Sam: That payment test failed again. Third time this week, and it passes on a rerun. Can we just delete it?
> 그 결제 테스트 또 실패했어. 이번 주에만 세 번인데 재실행하면 통과해. 그냥 지우면 안 돼?
Jay: It's flaky, not wrong. It's catching something real about one in ten times — deleting it hides the bug.
> 그건 틀린 게 아니라 불안정한 거야. 열 번에 한 번은 진짜 문제를 잡고 있어. 지우면 버그가 숨겨질 뿐이야.
Sam: So what do we do with it today?
> 그럼 오늘은 어떻게 하지?
Jay: Quarantine it so it stops blocking merges, and open a ticket. A flaky test everyone ignores is worse than no test.
> 머지를 막지 않게 격리하고 티켓을 열자. 다들 무시하는 flaky test는 없는 것보다 나빠.
Sam: The timeouts come from their sandbox, you know.
> 타임아웃은 그쪽 샌드박스에서 나는 거 알지.
Jay: I know. Their sandbox is flaky too, but I'll put that more diplomatically in the email.
> 알아. 그쪽 샌드박스도 flaky 하지. 메일에는 좀 더 외교적으로 쓸게.

## Techniques
1. **"It's X, not Y" 구문으로 오해를 먼저 끊는다.** "It's flaky, not wrong." 한 줄로 삭제하자는 주장의 전제를 무너뜨린다.
2. **같은 단어라도 상대가 바뀌면 표현을 바꾼다고 예고한다.** "I'll put that more diplomatically in the email." 내부 어휘와 외부 어휘를 구분하는 습관이다.



## Words
| flaky | /ˈfleɪki/ | 불안정한, 못 미더운 |
| quarantine a test | /ˈkwɔrənˌtin ə tɛst/ | 테스트를 격리하다 |

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| flaky | 불안정한, 못 미더운 — 테스트·외부 서비스에. "It's flaky, not wrong." |
| quarantine a test | 테스트를 격리하다 — 실패해도 머지를 막지 않게 분리 |
| it passes on a rerun | 재실행하면 통과한다 — flaky의 전형적 증상 |
| put it more diplomatically | 더 완곡하게 표현하다 — 사내 표현을 사외용으로 바꿀 때 |
