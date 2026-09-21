# 124 · Word — cull
title_ko: cull — 솎아내다, 도태시키다 (수를 줄이려고 골라 없애다)
situation: The backlog has passed 400 tickets and nobody can find anything in it. In grooming, Jay proposes a ruthless pass, and Mateo, who is newer to the team, asks what he means by the word.
situation_ko: 백로그가 400건을 넘어 아무도 그 안에서 뭘 찾지 못한다. 그루밍에서 Jay가 가차 없는 정리를 제안하자, 팀에 온 지 얼마 안 된 Mateo가 그 단어가 무슨 뜻인지 묻는다.
why: **Cull** originally means to kill selected animals to keep a population down, which is why it appears in farming and disease news ("additional culling"). Engineers borrow it for any deliberate thinning of a set: cull the backlog, cull stale feature flags, cull dependencies. It implies choosing what goes and removing it for good, so it is stronger than "clean up" or "tidy" and more selective than "delete everything". Use it as a verb or a noun ("a backlog cull"); avoid it when the animals sense would land badly, for instance about people or teams.
why_ko: **Cull**은 본래 개체 수를 줄이려고 골라서 죽인다는 뜻이라 축산이나 전염병 뉴스에 나온다("additional culling"). 개발자들은 어떤 집합이든 의도적으로 솎아내는 일에 이 말을 빌려 쓴다. cull the backlog, cull stale feature flags, cull dependencies. 무엇을 없앨지 고른 뒤 영구히 제거한다는 뜻이라 "clean up"이나 "tidy"보다 세고, "전부 삭제"보다 선별적이다. 동사로도 명사로도 쓴다("a backlog cull"). 동물을 도살한다는 원래 뜻이 거슬릴 자리, 예컨대 사람이나 팀에 대해서는 피한다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, second export (2026-09-21), page 3 card 11 (word): 옥스퍼드 영한사전 "cull — 1. 동사 (특정 동물을 그 수를 제한하기 위해) 도태시키다 2. 명사 (특정 동물의 수를 제한하기 위한) 도태". The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 두 번째 내보내기(2026-09-21), 3페이지 11번 카드(단어): 옥스퍼드 영한사전 "cull — 1. 동사 (특정 동물을 그 수를 제한하기 위해) 도태시키다 2. 명사 (특정 동물의 수를 제한하기 위한) 도태". 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-79.txt

## Dialogue
Mateo: Four hundred and twelve tickets. I searched for the rate-limit bug and got thirty hits.
> 412건이에요. 레이트 리밋 버그를 검색했더니 30개가 나와요.
Jay: Time to cull the backlog. Anything untouched for six months gets closed, and the owner has a week to object.
> 백로그를 솎아낼 때야. 6개월 동안 손 안 댄 건 닫고, 담당자한테 이의 제기할 일주일을 줘.
Mateo: "Cull" — like, delete?
> "cull"이 삭제한다는 거예요?
Jay: Delete selectively. The word comes from farming: you cull a herd to keep the numbers down. Same idea here — pick what goes, remove it for good, keep the rest healthy.
> 골라서 삭제하는 거. 축산에서 온 말이야. 개체 수를 줄이려고 무리를 솎아내지. 여기도 같은 생각이야. 없앨 걸 고르고, 영구히 없애고, 나머지를 건강하게 유지하는 거.
Mateo: Some of the old ones are still real bugs, though.
> 그래도 오래된 것 중에 진짜 버그도 있는데요.
Jay: Then they get reopened with a fresh report. If nobody can reproduce it in a week, it wasn't real enough to keep.
> 그럼 새 리포트로 다시 열면 돼. 일주일 안에 아무도 재현 못 하면 남겨 둘 만큼 진짜가 아니었던 거야.

## Techniques
1. **낯선 단어는 어원 한 줄로 설명한다.** "The word comes from farming: you cull a herd to keep the numbers down." — 뜻과 뉘앙스(선별, 영구 제거)가 함께 전달된다.
2. **가차 없는 정리에는 되돌릴 길을 붙인다.** "the owner has a week to object" / "they get reopened with a fresh report" — 반대 의견이 나오기 전에 안전장치를 말해 둔다.

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| cull the backlog | 백로그를 솎아내다 — 선별해 영구 제거. "Time to cull the backlog." |
| keep the numbers down | 수를 억제하다 — cull의 목적을 말할 때 |
| have a week to object | 이의 제기할 일주일이 있다 — 일괄 조치에 유예를 줄 때 |
| reproduce a bug | 버그를 재현하다 — 오래된 리포트를 살릴지 판단할 때 |
