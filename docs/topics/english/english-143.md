# 143 · Line — Marek — flagging a correction to my own review.
title_ko: Marek — flagging a correction to my own review. — Marek, 제 리뷰에 정정할 게 있어 알립니다
situation: Yesterday Jay told Marek in review that the retry wrapper must be moved out of the handler. Overnight he re-read the code and saw he had traced the call path wrong; the wrapper is fine where it is. Marek has already started the move, so Jay messages him before more time goes into it.
situation_ko: 어제 Jay는 리뷰에서 Marek에게 재시도 래퍼를 핸들러 밖으로 옮겨야 한다고 말했다. 밤사이 코드를 다시 읽다가 호출 경로를 잘못 추적했다는 걸 알았다. 래퍼는 지금 자리가 맞다. Marek이 이미 이동 작업을 시작했으니 Jay는 시간이 더 들어가기 전에 메시지를 보낸다.
why: **Flagging** is the work-English verb for bringing something to someone's attention; "flagging a correction" says in two words that this message exists to fix something. The preposition is **correction to** (a correction to my review, a correction to the spec), not "correction on". The memo's line then names the mistake ("what I said yesterday was wrong"), states the motive ("before it costs you more time"), and leaves the apology out. One refinement: **catch** is for the moment you spot an error; once you already know what was wrong, **correct** is the precise verb. No "so sorry" is needed; the speed of the message is the courtesy.
why_ko: **flagging**은 상대의 주의를 어떤 사항으로 돌리는 업무 영어 동사다. "flagging a correction"은 이 메시지가 무언가를 바로잡기 위해 존재한다는 걸 두 단어로 말한다. 전치사는 **correction to**(a correction to my review, a correction to the spec)이지 "correction on"이 아니다. 메모의 문장은 잘못을 명시하고("what I said yesterday was wrong"), 동기를 밝히고("before it costs you more time"), 사과는 뺀다. 한 가지 다듬을 점은, **catch**는 오류를 발견하는 순간의 동사이고, 무엇이 틀렸는지 이미 알면 **correct**가 정확하다. "so sorry"는 필요 없다. 메시지의 빠르기가 곧 예의다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, second export (2026-09-21), page 3 card 20 (sentence): memo Original "Marek — flagging a correction on my own review. What I said yesterday was wrong, and I want to catch it before it costs you more time." / Corrected "… a correction to my own review …" / Korean "Marek — 제가 직접 작성한 리뷰에서 수정할 부분이 있어 알려드립니다. 어제 제가 말씀드린 내용은 틀렸고, 그 때문에 시간을 더 쓰시기 전에 바로잡고 싶습니다."; note: correct rather than catch once the error is known. The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 두 번째 내보내기(2026-09-21), 3페이지 20번 카드(문장): 메모 원문 "Marek — flagging a correction on my own review. What I said yesterday was wrong, and I want to catch it before it costs you more time." / 수정 "… a correction to my own review …" / 번역 "Marek — 제가 직접 작성한 리뷰에서 수정할 부분이 있어 알려드립니다. …"; 오류를 이미 알면 catch보다 correct. 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-79.txt

## Dialogue
Marek: Morning. I'm about halfway through moving the retry wrapper. Should have it up by lunch.
> 좋은 아침. 재시도 래퍼 옮기는 거 절반쯤 했어요. 점심 전에 올릴 수 있을 거예요.
Jay: Stop there for a second. Marek — flagging a correction to my own review. What I said yesterday about moving the wrapper was wrong, and I want to correct it before it costs you more time.
> 잠깐 멈춰 주세요. Marek, 제 리뷰에 정정할 게 있어 알립니다. 어제 래퍼를 옮기라고 한 말은 틀렸고, 시간을 더 쓰시기 전에 바로잡고 싶어요.
Marek: What changed?
> 뭐가 바뀌었어요?
Jay: My reading of the call path. I had the handler invoking the wrapper twice; it doesn't. The wrapper is fine where it is, so the move buys nothing.
> 제가 호출 경로를 읽은 방식이요. 핸들러가 래퍼를 두 번 호출한다고 봤는데 아니었어요. 래퍼는 지금 자리가 맞고, 옮겨 봤자 얻는 게 없어요.
Marek: Good to know now rather than after the PR. Should I revert the half I've done?
> PR 뒤가 아니라 지금 알아서 다행이네요. 절반 한 거 되돌릴까요?
Jay: Yes, revert it. I'll leave a note on the review thread so the record shows the correction came from me.
> 네, 되돌려 주세요. 리뷰 스레드에 메모를 남겨서 정정이 제 쪽에서 나왔다는 게 기록에 남게 할게요.

## Techniques
1. **정정 메시지는 목적 → 무엇이 틀렸나 → 왜 지금인가 순서로, 사과 없이.** "flagging a correction to my own review. What I said yesterday … was wrong, and I want to correct it before it costs you more time." — 상대가 첫 줄에서 용건을 안다.
2. **틀린 원인을 한 문장으로 특정한다.** "My reading of the call path. I had the handler invoking the wrapper twice; it doesn't." — 원인이 구체적이어야 상대가 남은 판단을 신뢰한다.



## Words
| correct | /kɚˈɛkt/ | 이미 아는 오류를 바로잡다 vs 오류를 발견하다 |
| move buys nothing | /muv baɪz ˈnʌθɪŋ/ | 옮겨도 얻는 게 없다 |

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| flagging a correction to X | X에 대한 정정을 알립니다 — 업무 메시지 첫 줄, 전치사는 to. "flagging a correction to my own review" |
| correct vs catch | 이미 아는 오류를 바로잡다 vs 오류를 발견하다 — 알고 있으면 correct. "I want to correct it before it costs you more time." |
| cost you more time | 당신의 시간을 더 쓰게 하다 — 시간을 돈처럼 소모하게 만들다 |
| the move buys nothing | 옮겨도 얻는 게 없다 — buy = 이득을 가져오다, 변경의 가치를 말할 때 |
