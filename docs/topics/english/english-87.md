# 87 · Word — pejorative
title_ko: pejorative — (낱말·발언이) 경멸적인, 비난투의
situation: In code review, Jay wrote "legacy billing module" in a PR description. Tom, who wrote that module, asks whether "legacy" is a dig at his code. Jay wants to say the word was descriptive, not contemptuous, and then remove the ambiguity.
situation_ko: 코드 리뷰에서 Jay가 PR 설명에 "legacy billing module"이라고 썼다. 그 모듈을 만든 Tom이 "legacy"가 자기 코드를 비꼰 것이냐고 묻는다. Jay는 그 단어가 경멸이 아니라 설명이었다고 말한 뒤, 애매함을 없애고 싶다.
why: **Pejorative** describes a word or remark that carries contempt or disapproval; it is a formal word about language itself ("I didn't mean it as pejorative"). It works as an adjective and as a noun ("'legacy' can be a pejorative"). Trap: it is not a synonym for "rude person" and not "prerogative", which sounds similar. Jay needs it in reviews and docs whenever a label like legacy, hack, or workaround could be read as an insult and he wants to say it was not.
why_ko: **Pejorative**는 경멸이나 못마땅함을 담은 낱말이나 발언을 가리키며, 언어 자체를 두고 말하는 격식 단어다("I didn't mean it as pejorative"). 형용사로도 명사로도 쓴다("'legacy' can be a pejorative"). 함정: "무례한 사람"의 동의어가 아니고, 발음이 비슷한 "prerogative"(특권)와도 다르다. Jay는 legacy, hack, workaround 같은 딱지가 모욕으로 읽힐 수 있어 그게 아니었다고 말할 때 리뷰와 문서에서 이 단어가 필요하다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, second export (2026-09-21), page 2 card 10 (word): 옥스퍼드 영한사전 "pejorative — 형용사 (낱말·발언이) 경멸적인[비난투의]". The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 두 번째 내보내기(2026-09-21), 2페이지 10번 카드(단어): 옥스퍼드 영한사전 "pejorative — 형용사 (낱말·발언이) 경멸적인[비난투의]". 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-79.txt

## Dialogue
Tom: You called the billing module "legacy" in the PR description. Is that a dig at my code?
> PR 설명에서 빌링 모듈을 "legacy"라고 했던데. 내 코드 비꼰 거야?
Jay: Not at all. I didn't mean it as pejorative — it just means the code predates the current architecture, not that it's bad.
> 전혀 아니야. 경멸적인 뜻으로 쓴 게 아니라, 그 코드가 지금 아키텍처보다 먼저 있었다는 뜻이지 나쁘다는 게 아니야.
Tom: Pejorative?
> Pejorative?
Jay: A word that carries contempt. "Legacy" can be neutral or pejorative depending on tone, so I'll change it to "pre-v2 billing module" to be safe.
> 경멸을 담은 말. "legacy"는 어조에 따라 중립일 수도 경멸일 수도 있으니까, 안전하게 "pre-v2 billing module"로 바꿀게.
Tom: Appreciated. Some people do use it as a polite insult.
> 고마워. 어떤 사람들은 그걸 점잖은 모욕으로 쓰거든.
Jay: Which is exactly why the description should say what the code is, not how I feel about it.
> 바로 그래서 설명에는 내 감정이 아니라 코드가 뭔지를 써야 하는 거지.

## Techniques
1. **오해를 부인하고 곧바로 단어를 바꾼다.** "I didn't mean it as pejorative … so I'll change it to 'pre-v2 billing module' to be safe." — 의도를 설명하는 데 그치지 않고 애매한 딱지를 사실 서술로 교체한다.
2. **격식 단어는 상대가 되물으면 한 구로 정의한다.** "A word that carries contempt." — 정의 뒤에 "can be neutral or pejorative depending on tone"으로 왜 그 단어가 필요했는지 보여 준다.

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| pejorative | (말이) 경멸적인 — 언어에 대한 격식 단어. "I didn't mean it as pejorative" |
| a dig at | ~를 비꼬는 말 — 가벼운 공격을 가리킬 때. "Is that a dig at my code?" |
| predate | ~보다 먼저 있다 — legacy를 중립적으로 풀 때. "the code predates the current architecture" |
| to be safe | 안전하게, 혹시 몰라서 — 애매한 표현을 바꾸는 이유 |
