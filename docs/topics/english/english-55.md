# 55 · Word — pettifogging
title_ko: pettifogging — 좀스러운, 사소한 것에 트집 잡는
situation: Ken tells Jay that a security-fix PR has been blocked for two days over a trailing comma and a variable name. Jay wants a word for that kind of trivial nitpicking, and a fix that stops it from happening again.
situation_ko: Ken이 Jay에게 보안 수정 PR이 후행 쉼표 하나와 변수 이름 때문에 이틀째 막혀 있다고 말한다. Jay는 그런 사소한 트집을 가리키는 단어와, 다시는 안 생기게 할 해법을 원한다.
why: **Pettifogging** means fussing over trivial details or technicalities as if they mattered. It comes from "pettifogger", an old word for a small-time lawyer who argued over technicalities, so it carries contempt: petty plus pointless. It is not "detail-oriented", which is praise, and it is not "strict"; a strict reviewer blocks on bugs, a pettifogging one blocks on commas. It is a strong, slightly bookish word, fine for describing a process, rude if aimed at a person to their face.
why_ko: **Pettifogging**은 사소한 세부 사항이나 형식적 조항을 마치 중요한 것처럼 붙들고 늘어진다는 뜻이다. 사소한 법 조항으로 다투던 삼류 변호사를 가리키는 옛말 "pettifogger"에서 왔기 때문에 경멸이 담긴다. 좀스럽고 쓸모없다는 뜻이다. 칭찬인 "detail-oriented"와 다르고 "strict"와도 다르다. 엄격한 리뷰어는 버그로 막고, pettifogging한 리뷰어는 쉼표로 막는다. 강하고 약간 책 냄새 나는 단어라 과정을 묘사할 때는 괜찮지만 사람 면전에서 쓰면 무례하다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, card 9 of 20 (word), pasted 2026-09-21: 옥스퍼드 영한사전 "pettifogging — 형용사 좀스러운; 사소한". The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 카드 20장 중 9번(단어), 2026-09-21 붙여넣음: 옥스퍼드 영한사전 "pettifogging — 형용사 좀스러운; 사소한". 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-39.txt

## Dialogue
Ken: The signature-check PR has been blocked for two days. Over a trailing comma and a variable name.
> 서명 검증 PR이 이틀째 막혀 있어. 후행 쉼표 하나랑 변수 이름 때문에.
Jay: That's pettifogging. Those are Prettier's job, not a reviewer's. Blocking a security fix over them is just petty.
> 그건 좀스러운 트집이야. 그런 건 Prettier가 할 일이지 리뷰어가 할 일이 아니야. 그런 걸로 보안 수정을 막는 건 그냥 옹졸한 거지.
Ken: Pettifogging? I've never heard that one.
> pettifogging? 처음 듣는데.
Jay: Fussing over trivial details as if they mattered. It comes from an old word for a lawyer who argued over technicalities. Good for describing the process, not something you say to the reviewer's face.
> 사소한 세부 사항을 중요한 것처럼 붙들고 늘어지는 거. 법 조항으로 다투던 변호사를 가리키던 옛말에서 왔어. 과정을 묘사할 땐 좋은데, 리뷰어 면전에서 할 말은 아니야.
Ken: So what do we actually do?
> 그럼 실제로 어떻게 해?
Jay: Add the lint rule so the machine argues about commas, and ask reviewers to tag style comments "nit" and approve anyway.
> 린트 규칙을 넣어서 쉼표 싸움은 기계가 하게 하고, 리뷰어들한테는 스타일 코멘트에 "nit"를 붙이고 그래도 승인하라고 부탁하자.

## Techniques
1. **강한 단어를 쓰면 바로 어디까지 써도 되는지 선을 긋는다.** "Good for describing the process, not something you say to the reviewer's face" — 단어의 뜻과 함께 사용 범위를 말하면 동료가 잘못 옮기지 않는다.
2. **불평 뒤에는 절차로 답한다.** "Add the lint rule… and ask reviewers to tag style comments 'nit'" — 사람을 탓하는 대신 도구와 규칙으로 옮기면 팀 리드의 말이 된다.



## Words
| petty | /ˈpɛˌti/ | 옹졸한, 쩨쩨한 |
| technicality | /ˌtɛknɪˈkælɪti/ | 형식적인 세부 조항 |
| nit | /nɪt/ | 사소한 지적(nitpick의 줄임) |

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| pettifogging | 좀스러운, 사소한 것에 트집 잡는 — 과정·태도를 묘사할 때, 면전에서는 무례. "That's pettifogging." |
| petty | 옹졸한, 쩨쩨한 — pettifogging의 일상 버전. "Blocking a security fix over them is just petty." |
| a technicality | 형식적인 세부 조항 — 본질과 상관없는 규정. "a lawyer who argued over technicalities" |
| nit | 사소한 지적(nitpick의 줄임) — 코드 리뷰에서 "고쳐도 안 고쳐도 됨" 표시. "tag style comments 'nit' and approve anyway" |
