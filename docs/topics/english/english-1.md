# 1 · Review — The function is fine. Who can call it?
title_ko: 함수는 괜찮다. 누가 호출하나?
situation: Priya's PR adds an admin pause to Verex settlement. The feature is needed; the PR never says who holds the switch or what turns it back on.
situation_ko: Priya의 PR이 Verex 정산에 관리자 일시정지를 추가한다. 기능은 필요하지만, 누가 스위치를 쥐는지와 무엇이 다시 켜는지가 PR에 없다.
why: The most useful review move in this genre: agree with the feature in two words, then ask for the paperwork without sounding like a block.
why_ko: 이 장르에서 가장 유용한 리뷰 기술. 두 단어로 기능에 동의한 뒤, 막는 것처럼 들리지 않게 문서를 요구한다.

## Dialogue
Priya: This adds a pause so we can stop settlement if the oracle goes bad. I think it's uncontroversial.
> 오라클이 이상해지면 정산을 멈출 수 있게 일시정지를 추가했습니다. 논란의 여지가 없다고 봅니다.
Jay: The function is. What I can't find in the PR is who can call it, and what un-pauses it.
> 함수는 그렇습니다. PR에서 못 찾는 건 누가 호출할 수 있고 무엇이 해제하는가예요.
Priya: Owner only, for now. We'd un-pause by hand once we've looked.
> 지금은 오너만이요. 확인한 뒤 수동으로 풀 겁니다.
Jay: Reasonable start. I'd want those two sentences somewhere that isn't a code comment. "For now" and "by hand" are what an auditor asks about, not the modifier.
> 합리적인 출발입니다. 그 두 문장을 코드 주석이 아닌 곳에 두고 싶어요. 감사자가 묻는 건 modifier가 아니라 "지금은"과 "수동으로"거든요.
Priya: Where, then?
> 그럼 어디에요?
Jay: A three-column table in the repo: what a human can do, who and how, when we give it up. Even TBD in the third column beats the column not existing.
> 레포에 세 열짜리 표요. 사람이 할 수 있는 것, 누가 어떻게, 언제 내려놓는가. 세 번째 열이 미정이어도 열이 없는 것보다 낫습니다.
Priya: It'll be TBD for everything today.
> 오늘은 전부 미정일 텐데요.
Jay: That's honest. A table full of TBDs is a roadmap. A missing table is a question we answer under pressure later.
> 그게 정직한 거죠. 미정으로 가득한 표는 로드맵이고, 없는 표는 나중에 압박 속에서 답할 질문입니다.

## Techniques
1. **기능과 문서를 갈라서 말한다.** "The function is. What I can't find is…" 첫 두 단어로 기능에 동의한다고 못 박으면 뒤의 요구가 반대로 들리지 않는다.
2. **제3자의 눈으로 번역한다.** "what an auditor asks about" 상대가 사소하게 본 단어가 왜 중요한지 제3자 기준으로 말하면 취향 싸움이 되지 않는다.
3. **빈칸을 허용해 문턱을 낮춘다.** "Even TBD beats the column not existing." 완성도를 요구하면 아무도 시작하지 않는다. 표가 생기면 채워진다.

## Expressions
| it's uncontroversial | 논란의 여지가 없다 |
| who can call it | 누가 호출할 수 있나 |
| what un-pauses it | 무엇이 해제하나 |
| owner only, for now | 지금은 오너만 |
| a reasonable start | 합리적인 출발점 |
| somewhere that isn't a code comment | 코드 주석이 아닌 어딘가에 |
| when we give it up | 언제 내려놓는가 |
| TBD (to be determined) | 미정 |
| beats the column not existing | 열이 없는 것보다 낫다 |
| answer it under pressure later | 나중에 압박 속에서 답하다 |
