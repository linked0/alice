# 62 · Line — Just 'cause you're a novelist doesn't mean you're free.
title_ko: Just 'cause you're a novelist doesn't mean you're free. — 소설가라고 해서 자유로운 건 아니야
situation: In a code review, Sam points at a green pipeline and 100% coverage on a new module and asks to merge. Jay has read the tests and knows they only freeze today's behaviour, so he needs to push back without dismissing the work Sam did.
situation_ko: 코드 리뷰에서 Sam이 초록불 파이프라인과 새 모듈의 커버리지 100%를 가리키며 머지하자고 한다. Jay는 테스트를 읽어 봤고 그것들이 오늘의 동작을 그대로 굳혀 놓았을 뿐이라는 걸 알기에, Sam이 한 일을 깎아내리지 않으면서 반박해야 한다.
why: **Just because A doesn't mean B** says A is true but the conclusion people draw from it does not follow: "Just because it's tested doesn't mean it's correct." The whole "just because…" clause is the subject of "doesn't mean", so careful speech adds no extra "it" before "doesn't". 'Cause is the spoken shortening of because; say it, but write "because" in a review comment. The pattern is a polite way to block a shortcut, because it grants the premise before rejecting the inference.
why_ko: **Just because A doesn't mean B**는 A는 사실이지만 사람들이 거기서 끌어내는 결론은 따라오지 않는다는 말이다. "Just because it's tested doesn't mean it's correct." "just because…" 절 전체가 "doesn't mean"의 주어이므로 정확히 말할 때는 "doesn't" 앞에 it을 따로 넣지 않는다. 'cause는 because의 구어 축약이라 말로는 쓰되 리뷰 코멘트에는 because로 적는다. 전제를 인정한 뒤 추론만 거부하기 때문에 지름길을 막는 정중한 방법이 된다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, card 12 of 20 (sentence), pasted 2026-09-21: Original "Just 'cause you're a novelist doesn't mean you're free." / Corrected "Just because you're a novelist doesn't mean you're free." / Korean Translation "소설가라고 해서 자유로운 건 아니야." The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 카드 20장 중 12번(문장), 2026-09-21 붙여넣음: Original "Just 'cause you're a novelist doesn't mean you're free." / Corrected "Just because you're a novelist doesn't mean you're free." / 한국어 번역 "소설가라고 해서 자유로운 건 아니야." 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-39.txt

## Dialogue
Sam: All green, 100% coverage on the new module. Can we merge?
> 다 통과했고 새 모듈 커버리지 100%야. 머지해도 돼?
Jay: Just because it's fully covered doesn't mean it's correct. The tests assert whatever the function returns today; two of them would still pass if it returned an empty list.
> 커버리지가 다 찼다고 해서 맞다는 건 아니야. 테스트가 함수가 오늘 돌려주는 값을 그대로 단정하고 있어서, 두 개는 빈 리스트를 돌려줘도 통과할 거야.
Sam: Ouch. So what would convince you?
> 아프네. 그럼 뭘 보면 납득하겠어?
Jay: One test with an expected value worked out by hand from the spec. Coverage tells me the code ran, not that it did the right thing.
> 스펙에서 직접 계산한 기대값을 넣은 테스트 하나. 커버리지는 코드가 실행됐다는 것만 알려 주지, 맞게 동작했다는 건 아니야.
Sam: Fair. Just 'cause it's green doesn't mean it's done, I get it.
> 알았어. 초록불이라고 끝난 건 아니다, 이해했어.
Jay: Exactly. Add that one test and I'll approve.
> 바로 그거야. 그 테스트 하나 추가하면 승인할게.

## Techniques
1. **전제는 인정하고 추론만 끊는다.** "Just because it's fully covered doesn't mean it's correct." — A가 사실임은 받아들이므로 상대가 방어적으로 되지 않고, 바로 뒤에 근거(빈 리스트 예)를 붙인다.
2. **거절에는 통과 조건을 붙인다.** "One test with an expected value worked out by hand… Add that one test and I'll approve." — 무엇이면 되는지를 구체적으로 말해야 리뷰가 막히지 않는다.

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| Just because A doesn't mean B | A라고 해서 B인 건 아니다 — 지름길 결론에 반박할 때; 절 전체가 주어. "Just because it's fully covered doesn't mean it's correct." |
| 'cause / cuz | because의 구어 — 말할 때만; 리뷰 코멘트엔 because. "Just 'cause it's green doesn't mean it's done." |
| assert whatever it returns today | 현재 반환값을 그대로 단정하다 — 스냅샷식 테스트를 비판할 때 |
| Coverage tells me the code ran, not that it did the right thing. | 커버리지의 한계를 한 문장으로 — "X tells me A, not B" 대조 구문 |
