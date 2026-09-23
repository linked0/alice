# 133 · Line — I'd rather not hold this one hostage to a refactor we'll do properly in two weeks.
title_ko: I'd rather not hold this one hostage to a refactor we'll do properly in two weeks. — 2주 뒤에 제대로 할 리팩터링 때문에 이 PR까지 묶어 두고 싶지는 않다
situation: Aoife reviews Jay's PR that fixes a fee-calculation bug and asks him to also untangle the module's layering while he is in there. Jay agrees the refactor is needed, but it is already scheduled, and he wants the bounded fix merged now without sounding like he is dodging the cleanup.
situation_ko: Aoife가 수수료 계산 버그를 고치는 Jay의 PR을 리뷰하면서, 손댄 김에 모듈의 계층 구조도 정리하라고 한다. Jay는 리팩터링이 필요하다는 데 동의하지만 그건 이미 일정에 잡혀 있고, 정리를 피하는 것처럼 들리지 않게 범위가 한정된 수정만 지금 머지하고 싶다.
why: **Hold X hostage to Y** means Y decides whether X can move at all: nothing merges until the refactor lands. It is a vivid metaphor, and the plain engineering phrase is **block X on Y** ("I don't want to block this PR on the refactor"). The sentence works because it concedes the refactor is real ("we'll do properly in two weeks") while separating scope: merge the bounded fix now, do the structural cleanup later. "Properly" quietly warns that a refactor squeezed into this PR would be half-baked. Do not use it to dodge work you have no plan for; it needs a real date behind it.
why_ko: **hold X hostage to Y**는 Y가 X의 진행 자체를 결정한다는 뜻이다. 리팩터링이 끝날 때까지 아무것도 머지되지 않는다. 생생한 비유이고, 개발자 영어의 평범한 표현은 **block X on Y**("I don't want to block this PR on the refactor")다. 이 문장은 리팩터링의 필요성을 인정하면서("we'll do properly in two weeks") 범위를 분리하기 때문에 통한다. 한정된 수정은 지금 머지하고 구조 정리는 나중에. "properly"는 이 PR에 리팩터링을 끼워 넣으면 어설프게 될 거라는 조용한 경고다. 계획도 없는 일을 피하려고 쓰면 안 된다. 뒤에 실제 날짜가 있어야 한다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, second export (2026-09-21), page 3 card 15 (sentence): memo Original "I'd rather not hold this one hostage to a refactor we'll do properly in two weeks." / Korean "2주 뒤에 제대로 할 리팩터링 때문에 이번 작업까지 발목 잡히게 하고 싶지는 않아요." / Recommended "I'd rather not block this change on a refactor we're planning to do properly in two weeks." The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 두 번째 내보내기(2026-09-21), 3페이지 15번 카드(문장): 메모 원문 "I'd rather not hold this one hostage to a refactor we'll do properly in two weeks." / 번역 "2주 뒤에 제대로 할 리팩터링 때문에 이번 작업까지 발목 잡히게 하고 싶지는 않아요." / 권장 "I'd rather not block this change on a refactor…". 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-79.txt

## Dialogue
Aoife: The fix is fine, but while you're in there, can you pull the fee logic out of the handler? The layering is a mess.
> 수정은 괜찮은데, 손댄 김에 수수료 로직을 핸들러에서 빼 줄 수 있어? 계층이 엉망이야.
Jay: Agreed on the layering. But I'd rather not hold this one hostage to a refactor we'll do properly in two weeks. The fix is three lines, and it's live for users today.
> 계층 문제는 동의해. 그런데 2주 뒤에 제대로 할 리팩터링 때문에 이 PR을 묶어 두고 싶지는 않아. 수정은 세 줄이고, 지금 사용자한테 영향이 있어.
Aoife: Two weeks is real? Not "someday"?
> 2주가 진짜야? "언젠가"가 아니라?
Jay: It's ticketed for the next sprint, and I own it. If I squeeze the refactor into this PR, you'd get a rushed version of it and a bigger diff to review.
> 다음 스프린트에 티켓으로 잡혀 있고 내가 맡았어. 이 PR에 리팩터링을 끼워 넣으면 급하게 만든 버전이랑 리뷰할 diff만 커질 거야.
Aoife: Fine. Merge the fix, and link the refactor ticket in the description.
> 알겠어. 수정은 머지하고, 설명란에 리팩터링 티켓 링크해 줘.

## Techniques
1. **큰 요청은 인정부터 하고 범위를 분리한다.** "Agreed on the layering. But I'd rather not hold this one hostage to…" — 필요성은 받아들이되 이 PR의 범위 밖이라고 선을 긋는다.
2. **"나중에"에는 날짜와 담당자를 붙여 신뢰를 만든다.** "It's ticketed for the next sprint, and I own it." — 상대의 "Not 'someday'?"에 구체적으로 답해야 분리가 회피로 들리지 않는다.





## Words
| ticketed | /ˈtɪkətɪd/ | 다음 스프린트 티켓으로 잡혀 있다 |

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| hold X hostage to Y | Y 때문에 X를 진행하지 못하게 묶어 두다 — 강한 비유. "I'd rather not hold this one hostage to a refactor" |
| block X on Y | X를 Y에 종속시켜 막다 — 같은 뜻의 평범한 개발자 표현. "I don't want to block this PR on the refactor." |
| while you're in there | 손댄 김에 — 리뷰어가 추가 작업을 부탁할 때 |
| ticketed for the next sprint | 다음 스프린트 티켓으로 잡혀 있다 — "나중에"를 구체화하는 말 |
