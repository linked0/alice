# 63 · Word — knock-on
title_ko: knock-on — 연쇄적인, 파급 효과를 일으키는
situation: In sprint planning, Ken wants to bump the monorepo to Node 22 this sprint because it is "a one-line change". Jay knows the line is the easy part and that the base image, the CI runners, and a pinned lambda will all move with it, so he wants the team to size the chain, not the line.
situation_ko: 스프린트 플래닝에서 Ken이 "한 줄짜리 변경"이라며 이번 스프린트에 모노레포를 Node 22로 올리고 싶어 한다. Jay는 그 한 줄이 쉬운 부분이고 베이스 이미지, CI 러너, 버전이 고정된 람다가 모두 같이 움직인다는 걸 알기에, 팀이 한 줄이 아니라 연쇄를 산정하길 바란다.
why: **Knock-on** describes an effect caused indirectly by something else that then sets off further effects in a chain: "the knock-on effects of a version bump". It is mainly British ("knock-on effect" is the fixed collocation) and works as an adjective before a noun; you do not "knock on" a change. Americans more often say ripple effect or downstream impact. The trap: it is not a side effect in the programming sense, a function mutating state; it is about consequences spreading through a system or a plan.
why_ko: **Knock-on**은 다른 무엇에 의해 간접적으로 생겨서 다시 연쇄적으로 다음 효과를 일으키는 영향을 말한다. "the knock-on effects of a version bump" 주로 영국식이고("knock-on effect"가 굳은 표현), 명사 앞 형용사로 쓰이며 변경을 "knock on"한다고는 하지 않는다. 미국식으로는 ripple effect나 downstream impact를 더 많이 쓴다. 함정은 프로그래밍의 side effect(함수가 상태를 바꾸는 것)와 다르다는 점이다. 시스템이나 계획 전체로 번져 가는 결과를 말한다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, card 13 of 20 (word), pasted 2026-09-21: 옥스퍼드 영한사전 "|knock-|on — 형용사 연쇄 반응을 일으키는, 연쇄적인". The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 카드 20장 중 13번(단어), 2026-09-21 붙여넣음: 옥스퍼드 영한사전 "knock-on — 형용사 연쇄 반응을 일으키는, 연쇄적인". 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-39.txt

## Dialogue
Ken: Bumping Node to 22 is a one-line change in the engines field, right? Let's just do it this sprint.
> Node 22로 올리는 건 engines 필드 한 줄이잖아? 이번 스프린트에 그냥 하자.
Jay: The line is easy. It's the knock-on effects I'm worried about: the base image changes, the CI runners need the new toolchain, and the signing lambda still pins 18.
> 한 줄은 쉬워. 내가 걱정하는 건 연쇄 효과야. 베이스 이미지가 바뀌고, CI 러너에 새 툴체인이 필요하고, 서명 람다는 아직 18에 고정돼 있어.
Ken: Knock-on effects?
> 연쇄 효과?
Jay: One change that sets off a chain of further changes. Knock one domino over and the rest follow. In American English you'd hear "ripple effect" or "downstream impact"; same idea.
> 하나를 바꾸면 줄줄이 다른 변경이 따라오는 거. 도미노 하나를 넘어뜨리면 나머지가 따라 넘어지는 것처럼. 미국식으로는 "ripple effect"나 "downstream impact"라고도 하는데 같은 뜻이야.
Ken: So how do we size it?
> 그럼 규모를 어떻게 잡지?
Jay: I'll list every knock-on item tomorrow, and we plan the bump as three tickets, not one.
> 내일 연쇄 항목을 전부 나열할게. 그리고 버전 업은 티켓 하나가 아니라 세 개로 계획하자.

## Techniques
1. **"쉬운 변경"에는 파급 범위로 답한다.** "The line is easy. It's the knock-on effects I'm worried about:" — 분열문(It's X I'm worried about)으로 걱정의 대상을 짚고 콜론 뒤에 목록을 붙인다.
2. **단어를 설명할 때 동의어의 지역 차이를 곁들인다.** "In American English you'd hear 'ripple effect'" — 청자가 미국인이면 그쪽 표현을 함께 주는 것이 친절하다.



## Words
| ripple effect | /ˈrɪpəl ɪˈfɛkt/ | 파급 효과 |
| pin | /pɪn/ | 버전을 고정하다 |

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| knock-on (effect) | 연쇄적인, 파급 — 주로 영국식, 명사 앞 형용사. "It's the knock-on effects I'm worried about." |
| ripple effect / downstream impact | 파급 효과 — 미국식 동의어 |
| set off a chain of ~ | ~의 연쇄를 일으키다 — "One change that sets off a chain of further changes." |
| pin (a version) | 버전을 고정하다 — "the signing lambda still pins 18" |
