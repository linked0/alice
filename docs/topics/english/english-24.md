# 24 · First weeks — The senior who has been here nine years
title_ko: 9년 있었던 시니어
situation: Jay's second week as team lead at a Dublin fintech. Fiona has been on the team for nine years, knows every system, and was passed over for the lead role Jay now holds. Their first one-on-one. If this goes wrong, Jay leads a team whose most important engineer is working around him.
situation_ko: 더블린 핀테크에서 팀 리드 2주 차. Fiona는 이 팀에 9년 있었고, 모든 시스템을 알고, Jay가 지금 맡은 리드 자리에서 밀렸다. 첫 일대일. 이게 틀어지면 Jay는 가장 중요한 엔지니어가 자기를 우회하는 팀을 이끌게 된다.
why: The first one-on-one with a passed-over senior decides the next year. The winning move is not authority and not flattery; it is naming the situation plainly, asking for a specific kind of help, and giving something real in return.
why_ko: 밀린 시니어와의 첫 일대일이 다음 1년을 결정한다. 이기는 수는 권위도 아첨도 아니다. 상황을 있는 그대로 부르고, 특정한 종류의 도움을 요청하고, 실질적인 무엇을 돌려주는 것.
status: important

## Dialogue
Jay: Thanks for making time. I want to start with the obvious thing rather than pretend it isn't there: you've been here nine years, you went for this role, and they gave it to someone from outside. I'd understand if that's frustrating.
> 시간 내주셔서 감사합니다. 없는 척하는 대신 분명한 것부터 시작하고 싶습니다. 9년 여기 계셨고, 이 자리에 지원하셨고, 회사는 외부 사람에게 줬습니다. 답답하셔도 이해합니다.
Fiona: It was. I've moved on. Mostly.
> 그랬어요. 넘어갔어요. 대체로.
Jay: Fair. I'm not going to ask you to be happy about it. What I'd like to ask is something narrower: for the next three months, would you be the person who tells me when I'm about to break something? Not in the meeting. Before the meeting.
> 그렇죠. 기뻐하시라고 하지 않겠습니다. 부탁드리고 싶은 건 더 좁은 것입니다. 앞으로 석 달, 제가 무언가를 망가뜨리려 할 때 말해주는 사람이 되어 주시겠어요? 회의에서가 아니라, 회의 전에.
Fiona: That's a lot of unpaid consulting.
> 그건 무급 컨설팅이 많네요.
Jay: It is, so here's my side. Two things. First, the settlement redesign everyone's been putting off: I'd like you to own the design, and I'll get you the two engineers and the quarter to do it. Second, when I give my first architecture presentation to the CTO next month, I'll say that the reconciliation system that got us through the audit was yours, because it was.
> 맞습니다, 그래서 제 쪽 이야기입니다. 둘이요. 첫째, 모두가 미뤄온 정산 재설계요. 설계를 맡아주시길 바라고, 엔지니어 둘과 한 분기를 제가 확보하겠습니다. 둘째, 다음 달 CTO에게 첫 아키텍처 발표를 할 때 감사를 통과시킨 대사(對査, reconciliation) 시스템이 당신 것이었다고 말하겠습니다. 실제로 그랬으니까요.
Fiona: You read the audit report.
> 감사 보고서를 읽으셨군요.
Jay: And the commit history. Look, I'm going to make decisions you disagree with. When I do, I want to hear it directly from you, and I'll tell you what I decided and why, even when the answer is no. What I can't work with is finding out in a hallway.
> 그리고 커밋 이력도요. 제가 동의하지 않으실 결정을 내릴 겁니다. 그럴 때 당신에게서 직접 듣고 싶고, 무엇을 왜 결정했는지 말하겠습니다. 답이 아니오일 때도요. 제가 같이 일할 수 없는 건 복도에서 알게 되는 겁니다.
Fiona: All right. First thing, then: the deploy plan you sent yesterday runs migrations during the Bacs window. Don't.
> 좋아요. 그럼 첫 번째요. 어제 보내신 배포 계획은 Bacs 윈도우 중에 마이그레이션을 돌려요. 하지 마세요.
Jay: That's exactly what I meant. Walk me through it.
> 정확히 그 얘기예요. 설명해 주세요.

## Techniques
1. **코끼리를 먼저 부른다.** "I want to start with the obvious thing rather than pretend it isn't there." 상황을 명명하면 그 뒤의 요청이 조작처럼 들리지 않는다. 피하면 첫 일대일이 연극이 된다.
2. **좁고 기한 있는 요청.** "for the next three months… tell me when I'm about to break something. Not in the meeting. Before the meeting." "도와 달라"는 거절할 수 없어 무의미하고, 구체적인 요청은 수락할 수 있어 의미가 있다.
3. **대가를 먼저 낸다, 구체적으로.** "I'll get you the two engineers and the quarter… I'll say the reconciliation system was yours." 권한(자원)과 공개적 인정. 둘 다 리드만 줄 수 있는 것이고, 아첨은 아무도 못 사는 것.
4. **`work around` + 사람 — 이 상황 전체의 이름.** situation의 마지막 문장 "a team whose most important engineer is **working around him**"은 "그의 주변에서 일한다"가 아니다. **Jay를 거치지 않고 우회해서 일을 처리한다**는 뜻이다. 구체적으로는 Jay에게 보고하지 않고 직접 결정하고, 다른 사람들과 따로 협의하고, Jay의 의사결정 구조를 피해 일을 진행하는 상황. 보통 `work around`의 목적어는 문제나 장애물이다 — "We found a way to **work around the bug**"(그 버그를 우회할 방법을 찾았다). 그런데 여기서는 목적어가 **사람**이다. 그래서 날카롭다: Jay가 "거쳐야 할 리더"가 아니라 "피해서 지나가야 할 장애물"이 되어버렸다는 뉘앙스가 실린다. 그러니 "Jay 없이 일한다"가 아니라 **"Jay를 우회해서 일한다" / "Jay를 제쳐놓고 일을 처리한다"**가 정확한 번역이다. 이 한 구절이 왜 첫 일대일이 1년을 결정하는지를 설명한다 — 실패의 결과가 갈등이 아니라 *우회*이기 때문이다.
5. **`reconciliation` / `reconciliation system` — 이 대화에서 Jay가 내미는 카드의 정체.** 일반 영어에서 `reconciliation`은 **화해**다(사람 사이의 관계 회복). 그런데 **회계·금융에서는 전혀 다른 뜻**으로 굳어져 있다 — **대사(對査)**, 즉 **서로 독립적으로 관리되는 두 기록을 맞춰보고, 어긋나는 항목을 찾아내 원인을 설명하고 해소하는 작업**이다. 은행 계좌 명세와 내부 원장, 카드사 정산 파일과 자체 거래 로그, 두 시스템의 잔액 — 이 둘이 한 푼까지 일치하는지 매일 확인하는 일. 어원은 같다: *다시(re) 하나로(concile) 맞춘다.* 사람을 맞추면 화해, 숫자를 맞추면 대사.
   - `a reconciliation system`은 그 작업을 자동으로 돌리는 시스템이다. **핀테크에서 가장 지루하고 가장 중요한 축**에 속한다. 화려한 기능이 아니라 **틀리면 회사가 죽는 쪽**이라서다.
   - 그래서 `the reconciliation system that got us through the audit`이 무게를 갖는다. **감사(audit)에서 가장 먼저 무너지는 지점이 정확히 대사**다. 숫자가 안 맞으면 변명이 통하지 않는다. Fiona가 만든 것이 회사를 감사에서 통과시켰다는 말은 **"당신이 회사를 구한 적이 있다"의 회계 버전**이고, Jay는 그걸 CTO 앞에서 말하겠다고 제안한다.
   - **대화 설계상의 의미**: Jay가 내놓는 대가 둘 중 두 번째가 바로 이것이다. 첫째(엔지니어 둘 + 한 분기)는 **자원**, 둘째는 **공개적 귀속(public attribution)**. 아첨은 공짜지만 귀속은 리드만 줄 수 있고 되돌릴 수 없다. **`reconciliation`이라는 단어를 몰라도 대화는 읽히지만, 알면 Jay가 얼마나 구체적으로 준비했는지가 보인다** — 그는 감사 보고서와 커밋 이력을 읽고 왔다.






## Words
| narrower | /ˈnɛroʊɚ/ | 더 좁은 것 |
| hallway | /ˈhɔlˌweɪ/ | 복도에서 알게 되다 |
| unpaid | /ənˈpeɪd/ | 무급 컨설팅 |
| obstacle | /ˈɑbstəkəl/ | 장애물 — work around가 원래 상대하는 것 |
| reconciliation | /ˌrɛkənˌsɪliˈeɪʃən/ | 대사(對査) · 화해 |
| reconcile | /ˈrɛkənˌsaɪl/ | 맞추다, 대사하다 · 화해시키다 |
| audit | /ˈɔdɪt/ | 감사 |
| ledger | /ˈlɛdʒɚ/ | 원장, 장부 |

## Expressions
| working around him | 그를 우회해서 일하다 (사람을 장애물 취급) |
| reconciliation | 대사(對査) — 두 기록을 맞춰 차이를 해소하는 회계 작업. 일상어로는 '화해' |
| the reconciliation system | 대사 시스템. 그 작업을 자동으로 돌리는 것 |
| got us through the audit | 우리를 감사에서 통과시켜 줬다 |
| the ledger doesn't match | 원장이 안 맞는다 (대사 실패를 말하는 실무 표현) |
| work around the bug | 버그를 우회하다 (원래 용법: 목적어가 문제) |
| the obvious thing | 뻔한 것, 모두 아는 것 |
| passed over for a role | 자리에서 밀리다 |
| I'd understand if that's frustrating | 답답하셔도 이해한다 |
| mostly | 대체로 |
| something narrower | 더 좁은 것 |
| unpaid consulting | 무급 컨설팅 |
| here's my side | 내 쪽 이야기는 이렇다 |
| everyone's been putting off | 모두가 미뤄온 |
| I can't work with | 같이 일할 수 없는 것 |
| finding out in a hallway | 복도에서 알게 되다 |
| walk me through it | 차근차근 설명해 달라 |
