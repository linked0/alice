# 140 · Word — writ large
title_ko: writ large — 더 크고 뚜렷한 형태로 드러난; 대대적인
situation: In an architecture review, Priya says the trouble with one small helper module is not worth a redesign. Jay thinks the helper is a miniature of the whole monolith's problem, and wants a phrase that says "the same thing, bigger and plainer".
situation_ko: 아키텍처 리뷰에서 Priya는 작은 헬퍼 모듈 하나의 문제는 재설계할 만한 가치가 없다고 말한다. Jay는 그 헬퍼가 모놀리스 전체 문제의 축소판이라고 보고, "같은 것이 더 크고 더 뚜렷하게"라는 표현을 원한다.
why: **Writ large** follows the noun it describes and means the same thing shown on a bigger, more obvious scale: "the monolith is this helper writ large". "Writ" is an old past participle of "write", so the image is something written in large letters, easy to read. It is formal and slightly literary, common in essays and design documents, and it works in a meeting when you want to sound precise. The dictionary senses 뚜렷한, 역력한 and 대대적인 come from the same picture. Do not put it before the noun ("a writ-large problem" is wrong), and do not confuse it with "in large part".
why_ko: **writ large**는 꾸미는 명사 뒤에 오고, 같은 것이 더 크고 더 뚜렷한 규모로 드러났다는 뜻이다. "the monolith is this helper writ large". writ는 write의 옛 과거분사라, 큰 글자로 써서 읽기 쉽게 만든 이미지다. 격식 있고 약간 문어적이라 에세이와 설계 문서에 흔하고, 회의에서 정확하게 들리고 싶을 때 쓸 수 있다. 사전의 "뚜렷한, 역력한", "대대적인"은 같은 그림에서 나온다. 명사 앞에 두면 안 되고("a writ-large problem"은 틀림), "in large part"(대부분)와 혼동하면 안 된다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, second export (2026-09-21), page 3 card 19 (word): 옥스퍼드 영한사전 "writ large — 1. 뚜렷한, 역력한 2. 엄연한[대대적인] …". The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 두 번째 내보내기(2026-09-21), 3페이지 19번 카드(단어): 옥스퍼드 영한사전 "writ large — 1. 뚜렷한, 역력한 2. 엄연한[대대적인] …". 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-79.txt

## Dialogue
Priya: It's one helper module with too many callers. That's a cleanup ticket, not a redesign.
> 호출자가 너무 많은 헬퍼 모듈 하나잖아. 그건 정리 티켓이지 재설계가 아니야.
Jay: On its own, sure. But look at the shape: every service imports it, it reaches into three databases, and nobody owns it. That's the whole monolith writ large.
> 그것만 보면 그렇지. 그런데 모양을 봐. 모든 서비스가 임포트하고, DB 세 개에 손을 뻗고, 주인이 없어. 그게 모놀리스 전체를 크게 써 놓은 거야.
Priya: Writ large?
> writ large?
Jay: The same problem, bigger and easier to see. The helper is a small, readable copy of what the monolith does everywhere. If we fix the helper properly, we've written the rule for the rest.
> 같은 문제가 더 크고 더 잘 보이게 된 거. 이 헬퍼는 모놀리스가 곳곳에서 하는 짓의 작고 읽기 쉬운 복사본이야. 헬퍼를 제대로 고치면 나머지에 대한 규칙을 쓴 셈이지.
Priya: So the cleanup ticket becomes the pilot for the redesign.
> 그럼 정리 티켓이 재설계의 파일럿이 되는 거네.
Jay: Exactly. Small fix, same pattern writ large afterwards.
> 맞아. 작은 수정, 그다음엔 같은 패턴을 크게.

## Techniques
1. **작은 사례를 큰 문제의 축소판으로 연결할 때 명사 뒤에 붙인다.** "That's the whole monolith writ large." — 명사(the monolith) + writ large 순서. 앞에 두지 않는다.
2. **문어적 표현을 쓰면 되물음에 일상어로 바꿔 준다.** "The same problem, bigger and easier to see." — 격식어와 풀이를 한 쌍으로 말하면 회의에서 잘난 척으로 들리지 않는다.






## Words
| writ | /rɪt/ | X가 더 크고 뚜렷하게 드러난 것 |
| large | /lɑrdʒ/ | X가 더 크고 뚜렷하게 드러난 것 |
| redesign | /ˌridɪˈzaɪn/ | 재설계의 시범 사례 |

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| X writ large | X가 더 크고 뚜렷하게 드러난 것 — 명사 뒤, 격식·문어. "That's the whole monolith writ large." |
| on its own | 그것만 놓고 보면 — 부분 인정 후 반론으로 넘어갈 때. "On its own, sure. But…" |
| nobody owns it | 담당자가 없다 — 코드·모듈의 소유권을 말할 때 |
| the pilot for the redesign | 재설계의 시범 사례 — 작은 수정을 큰 변화의 첫 단계로 자리매김 |
