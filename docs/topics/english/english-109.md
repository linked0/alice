# 109 · Line — That's on me.
title_ko: That's on me. — 그건 내 책임이야, 내가 잘못했어
situation: A hotfix Jay approved on Friday broke the staging deploy, and on Monday Lena is trying to work out who missed the failing check. Jay wants to own it in one line and move straight to the fix, without a long apology that would make everyone uncomfortable.
situation_ko: Jay가 금요일에 승인한 핫픽스가 스테이징 배포를 깨뜨렸고, 월요일에 Lena는 누가 실패한 체크를 놓쳤는지 찾고 있다. Jay는 모두를 불편하게 만드는 긴 사과 대신 한 줄로 책임을 지고 바로 수정으로 넘어가고 싶다.
why: **That's on me** means "that is my responsibility" or "that was my mistake". It claims the fault cleanly and then stops, which is exactly the register Western teams expect: ownership without grovelling. The trap is stacking apologies on top ("I'm so sorry, I really should have…"), which shifts the meeting from fixing the problem to comforting the speaker. Its opposite is "that's on them / on the vendor", also a plain statement of who owns what. It is not "that's on my tab", which is about paying for drinks.
why_ko: **That's on me**는 "그건 내 책임이다", "내 실수였다"는 뜻이다. 잘못을 깔끔하게 인정하고 거기서 멈추는데, 그것이 서구 팀이 기대하는 등급이다. 굽신거리지 않는 책임 인정. 함정은 그 위에 사과를 쌓는 것("I'm so sorry, I really should have…")으로, 그러면 회의가 문제 해결에서 말한 사람 달래기로 옮겨 간다. 반대말은 "that's on them / on the vendor"로, 역시 누구 소관인지 담담히 밝히는 말이다. 술값을 낸다는 "that's on my tab"과는 다르다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, second export (2026-09-21), page 3 card 1 (memo): term note only — "🔥 That's on me — 아주 흔하고 유용. That's on me. = 그건 내 책임이야 / 그건 내가 잘못했어." No sentence analysis in the memo. The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 두 번째 내보내기(2026-09-21), 3페이지 1번 카드(메모): 용어 메모만 있음 — "🔥 That's on me — 아주 흔하고 유용. That's on me. = 그건 내 책임이야 / 그건 내가 잘못했어." 문장 분석은 없다. 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-79.txt

## Dialogue
Lena: Staging has been red since Friday night. The hotfix went out with a failing integration check. Who approved it?
> 스테이징이 금요일 밤부터 빨간불이야. 통합 체크가 실패한 채로 핫픽스가 나갔어. 누가 승인했어?
Jay: That's on me. I saw the check was flaky last week and assumed this was the same flake. It wasn't.
> 그건 내 책임이야. 지난주에 그 체크가 불안정한 걸 봐서 이번에도 같은 거라고 넘겨짚었어. 아니었지.
Lena: Okay. What do we do about it?
> 알겠어. 그럼 어떻게 하지?
Jay: Revert is already up for review. Then I'll add a rule that a flaky check can't be skipped without a second approver.
> 되돌리기는 이미 리뷰에 올려 뒀어. 그다음에 불안정한 체크는 두 번째 승인자 없이는 건너뛸 수 없다는 규칙을 넣을게.
Lena: Good. And the missing alert? Staging was red for two days and nobody got paged.
> 좋아. 그리고 빠진 알림은? 스테이징이 이틀 동안 빨간불이었는데 아무도 호출을 못 받았어.
Jay: That one's on the alerting config, not on any person. I'll open a ticket, but it needs an owner.
> 그건 알림 설정 문제지 사람 문제가 아니야. 티켓은 내가 열 텐데, 담당자가 필요해.

## Techniques
1. **책임 인정은 한 줄, 그다음은 바로 원인과 조치.** "That's on me. I saw the check was flaky… It wasn't." 사과를 늘어놓지 않고 판단 오류를 사실로 말한 뒤 "Revert is already up"으로 넘어간다.
2. **"on"으로 소유를 배분한다.** "That one's on the alerting config, not on any person" — 같은 구조로 내 책임과 시스템 문제를 구분할 수 있다.



## Words
| That's on me | /ðæts ɑn mi/ | 그건 내 책임이야 |
| that's on X | /ðæts ɑn ɛks/ | 그건 X 소관이다 |
| flaky | /ˈfleɪki/ | 불안정한, 간헐적으로 실패하는 |
| get paged | /ɡɛt peɪdʒd/ | 호출을 받다 |

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| That's on me. | 그건 내 책임이야 — 실수를 인정할 때, 뒤에 조치를 붙인다 |
| that's on X (the vendor / the config) | 그건 X 소관이다 — 책임 소재를 담담히 말할 때. "That one's on the alerting config" |
| flaky (check / test) | 불안정한, 간헐적으로 실패하는 — CI 대화 |
| get paged | 호출을 받다 — 온콜 알림. "nobody got paged" |
