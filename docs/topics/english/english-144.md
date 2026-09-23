# 144 · Word — sloppy
title_ko: sloppy — 엉성한, 대충 한; 헐렁한
situation: Tom asks Jay for a quick review on a PR before he leaves for the day. The logic is right, but three catch blocks swallow every error and two debug logs are still in. Jay wants to name the carelessness without making it sound like a verdict on Tom.
situation_ko: Tom이 퇴근 전에 PR을 빨리 봐 달라고 Jay에게 부탁한다. 로직은 맞지만 catch 블록 셋이 모든 에러를 삼키고 디버그 로그 둘이 그대로 남아 있다. Jay는 Tom 자체에 대한 평가처럼 들리지 않게 그 허술함을 지적하고 싶다.
why: **Sloppy** means done carelessly, without attention to detail: sloppy code, a sloppy mistake, sloppy handwriting. Sloppy code can still work, so it is not the same as "wrong"; the complaint is about care, not correctness. It also means loose-fitting (a sloppy sweater) and, of kisses, wet and messy. In a review, aim it at the work ("the error handling is sloppy"), never at the person ("you're sloppy"), and in front of a manager reach for "could be tighter".
why_ko: **Sloppy**는 세부에 신경 쓰지 않고 대충 한 것을 말한다. sloppy code, a sloppy mistake, sloppy handwriting. 엉성한 코드도 돌아가기는 하므로 "wrong"과 같지 않다. 문제는 정확성이 아니라 정성이다. 헐렁한 옷(a sloppy sweater)이나 질펀한 키스에도 쓴다. 리뷰에서는 사람("you're sloppy")이 아니라 작업("the error handling is sloppy")을 겨냥하고, 매니저 앞에서는 "could be tighter" 쪽이 안전하다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, second export (2026-09-21), page 4 card 1 (word): 옥스퍼드 영한사전 "sloppy — 1. 엉성한, 대충 하는 2. 헐렁한 3. (애정 표현 등이) 질펀한[몹시 감상적인]". The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 두 번째 내보내기(2026-09-21), 4페이지 카드 1(단어): 옥스퍼드 영한사전 "sloppy — 엉성한, 대충 하는; 헐렁한; 질펀한". 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-79.txt

## Dialogue
Tom: Can you give my PR a quick look? I want to merge before I leave.
> 내 PR 빨리 한번 봐 줄래? 퇴근 전에 머지하고 싶어서.
Jay: The logic is right, but the error handling is sloppy. Three catch blocks swallow everything, and two console.logs are still in there.
> 로직은 맞는데 에러 처리가 엉성해. catch 블록 셋이 다 삼키고 있고, console.log도 둘 남아 있어.
Tom: Sloppy as in wrong?
> 엉성하다는 게 틀렸다는 뜻이야?
Jay: Sloppy as in careless. It works today; it just hides the next bug. Log the error and rethrow, and drop the debug lines.
> 부주의하다는 뜻이야. 오늘은 돌아가지만 다음 버그를 숨기게 돼. 에러를 로그하고 다시 던지고, 디버그 줄은 지워.
Tom: Ten minutes. Thanks for saying it plainly.
> 10분이면 돼. 돌려 말하지 않아서 고마워.
Jay: Sloppy is a word for the code, not for you. I'd rather say it now than debug it in prod.
> sloppy는 코드에 하는 말이지 너한테 하는 말이 아니야. 프로덕션에서 디버깅하는 것보단 지금 말하는 게 낫지.

## Techniques
1. **평가는 작업물에, 사람에게는 아니다.** "the error handling is sloppy"처럼 주어를 코드로 두면 같은 단어도 인신공격이 되지 않는다. "Sloppy is a word for the code, not for you."
2. **형용사를 되물으면 한 단어로 다시 정의한다.** "Sloppy as in wrong?" → "Sloppy as in careless." — "X as in Y" 패턴으로 뜻을 좁혀 준다.






## Words
| sloppy | /ˈslɑpi/ | 엉성한, 대충 한 |
| tighter | /ˈtaɪtɚ/ | 좀 더 다듬을 수 있겠다 |

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| sloppy | 엉성한, 대충 한 — 코드·글씨·실수에. "the error handling is sloppy" |
| X as in Y | X라는 게 Y라는 뜻이냐 — 단어 뜻을 확인하거나 좁힐 때. "Sloppy as in careless." |
| swallow an error | 에러를 삼키다(잡고 아무것도 안 하다) — 리뷰 용어 |
| could be tighter | 좀 더 다듬을 수 있겠다 — sloppy의 부드러운 대체 표현 |
