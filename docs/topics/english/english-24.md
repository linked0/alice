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
6. **"…even when the answer is no. What I can't work with is finding out in a hallway." — 이 대화에서 Jay가 거는 조건, 한 문장씩.**
   - **앞 문장 전체**: *"I'm going to make decisions you disagree with. When I do, I want to hear it directly from you, and I'll tell you what I decided and why, **even when the answer is no**."* → "제가 동의하지 않으실 결정을 내릴 겁니다. 그럴 때 저는 당신에게서 **직접** 듣고 싶고, 무엇을 왜 결정했는지 말하겠습니다. **답이 '안 된다'일 때도요.**"
   - **`even when the answer is no` — 먼저 누가 설명하는가.** 헷갈리기 쉬운 지점이라 못 박아둔다. **설명하는 쪽은 리더(Jay)다. 부하(Fiona)가 아니다.** 근거는 원문 자체에 있다 — `**I'll** tell you what I decided and why`. 주어가 `I`, 즉 Jay다. 그리고 `the answer`는 **Jay가 내리는 답**이지 Fiona의 답이 아니다. 앞 문장이 *"I'm going to make **decisions** you disagree with"*이므로, 결정하는 사람도 설명하는 사람도 Jay다. 이 대목을 "부하가 자기 제안을 설명한다"로 읽으면 문장이 통째로 뒤집힌다.
   - **그래서 왜 핵심인가.** 대부분의 리더는 **자기 결정의 이유를 답이 '예스'일 때만 말해준다.** 받아들일 때는 "좋습니다, 이래서 이렇게 갑시다"가 쉽게 나온다 — 상대가 이미 만족했으니 설명이 부담이 없다. 거절할 때는 반대다. 이유를 말하면 **반론을 부르기 때문에**, 이유 없이 "안 됩니다"로 끝내거나 "검토해 보겠습니다"로 덮고 다시 꺼내지 않는다. Jay는 정확히 **그 불편한 경우**를 콕 집어 약속한다. 설명이 쉬운 쪽(yes)이 아니라 어려운 쪽(no)을 약속해야 약속에 값이 붙는다. **이 다섯 단어를 빼면 문장 전체가 공짜가 된다.**
   - **`What I can't work with is ~` — 구문.** 이건 **의사분열문(pseudo-cleft, what-cleft)**이다. `What + 주어 + 동사 + is + X` 형태로 **X를 문장 끝으로 밀어 강조**한다. 그냥 *"I can't work with finding out in a hallway"*라고 해도 뜻은 같지만, `What I can't work with is…`로 시작하면 **듣는 사람이 "무엇?" 하고 기다리게 만든 뒤 답을 준다.**
   - **의미도 주의.** `I can't work with X`는 "나는 X를 못 한다"가 아니다. **"X는 내가 같이 일할 수 없게 만드는 조건이다"** — 능력이 아니라 **경계선**을 긋는 말이다. 한국어로는 "그것만은 안 됩니다" / "그 조건에서는 같이 일할 수 없습니다"에 가깝다.
   - **`finding out in a hallway`가 가리키는 장면.** 직역은 "복도에서 알게 되는 것". **누가 알게 되는가? Jay다.** 즉 *Fiona가 회의에서는 말하지 않고, 나중에 다른 사람들에게 말하고, 그 말이 돌고 돌아 Jay의 귀에 우연히 들어오는 상황.* 복도(hallway)는 **회의실에서 하지 않은 말이 실제로 오가는 장소**를 가리키는 영어권 사무실의 상투적 이미지다 — 우리로 치면 "탕비실에서 듣는다", "회식 자리에서 알게 된다"에 해당한다.
   - **situation 문장과 이어진다.** 맨 위 상황 설명의 `working around him`(→ 기법 4)이 **실제로 눈에 보이는 순간이 바로 복도다.** Jay가 두려워하는 건 갈등이 아니라 **우회**이고, 복도는 우회가 남기는 흔적이다.
   - **한 거래로 읽으면**: *직접 말해 달라* ↔ *나는 거절할 때도 이유를 말하겠다.* **양쪽 다 '불편한 쪽'을 맡는 교환**이고, 이게 이 대화에서 Jay가 내는 마지막 카드다. 자원도 인정도 아닌 **운영 규칙**.
7. **그러면 부하인 Fiona는 언제 `no`라고 하는가 — 이 장면의 실제 결말.** 기법 6에서 `the answer`가 **Jay의 답**이라고 못 박았는데, 그러면 Fiona의 거절은 어디 있느냐는 질문이 남는다. **있다. 두 번 있고, 종류가 다르다.**
   - **첫 번째 — 협상의 no.** *"That's a lot of unpaid consulting."* ("그건 무급 컨설팅이 많네요.") 요청 자체를 거절하는 게 아니라 **가격을 지적한다.** 영어권 협상에서 아주 흔한 형태다 — **거절하지 않고 비용을 테이블에 올려놓는 것.** 이 한마디가 Jay에게 "대가를 내놓으라"고 요구하고, 실제로 Jay는 바로 다음 턴에 자원과 공개 인정을 내놓는다. **이 no가 없었으면 Jay는 공짜로 얻었을 것이다.**
   - **두 번째 — 기술적 no, 그리고 이게 진짜다.** *"All right. First thing, then: the deploy plan you sent yesterday runs migrations during the Bacs window. **Don't.**"* — **`Don't.` 한 단어.** 이유도 완충도 사과도 없다. Bacs는 영국의 은행 자동이체 정산 시스템이고, **그 처리 창(window)에 DB 마이그레이션을 돌리면 결제가 깨진다.** 9년치 맥락이 있어야만 나오는 지적이다.
   - **여기서 구조를 보라.** Jay가 *"I want to hear it directly from you"*라고 요청한 **바로 두 턴 뒤에 Fiona가 그걸 실행한다.** 복도가 아니라, 회의에서가 아니라, **지금 이 방에서 직접.** 약속이 추상으로 끝나지 않고 **그 자리에서 한 번 작동해 보인 것**이고, 그래서 Jay가 *"That's exactly what I meant. Walk me through it."*로 받는다. **대화가 닫히는 방식이 곧 거래가 성립했다는 증거다.**
   - **다만 정확히 해둘 것 — Jay의 약속은 아직 시험되지 않았다.** 이 장면에서 Jay의 답은 사실상 **예스**다(그는 지적을 받아들이고 설명을 청한다). `even when the answer is no`가 진짜로 값을 치르는 순간은 **Jay가 Fiona의 지적을 듣고도 뒤집지 않기로 하고, 그 이유를 말해야 하는 날**이다. 그 날은 이 대화 밖에 있다. **약속은 쉬운 경우에 맺어지고 어려운 경우에 검증된다** — 이 장면이 보여주는 건 전자까지다.
   - **정리하면 no가 세 종류다.** Fiona의 **협상 no**("비싼데요") · Fiona의 **기술 no**("하지 마세요") · Jay의 **결정 no**("그래도 이렇게 갑니다, 이유는 —"). **앞의 둘은 대사에 나오고, 세 번째는 약속으로만 존재한다.**






## Words
| narrower | /ˈnɛroʊɚ/ | 더 좁은 것 |
| hallway | /ˈhɔlˌweɪ/ | 복도 — 회의에서 안 한 말이 오가는 곳 |
| unpaid | /ənˈpeɪd/ | 무급 컨설팅 |
| obstacle | /ˈɑbstəkəl/ | 장애물 — work around가 원래 상대하는 것 |
| reconciliation | /ˌrɛkənˌsɪliˈeɪʃən/ | 대사(對査) · 화해 |
| reconcile | /ˈrɛkənˌsaɪl/ | 맞추다, 대사하다 · 화해시키다 |
| audit | /ˈɔdɪt/ | 감사 |
| ledger | /ˈlɛdʒɚ/ | 원장, 장부 |
| migration | /maɪˈgreɪʃən/ | (DB) 마이그레이션, 스키마 변경 |
| consulting | /kənˈsʌltɪŋ/ | 자문 (unpaid consulting = 무급 자문) |

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
| finding out in a hallway | 복도에서 (우연히) 알게 되다 — 당사자가 아니라 남을 통해 |
| even when the answer is no | (내가 내리는) 답이 '안 된다'일 때도 — 말하는 사람은 리더 |
| I'll tell you what I decided and why | 무엇을 왜 결정했는지 말하겠다 (주어가 리더인 것이 핵심) |
| What I can't work with is ~ | 내가 같이 일할 수 없는 건 ~다 (경계선 긋기 · what-cleft) |
| hear it directly from you | 당신에게서 직접 듣다 |
| That's a lot of unpaid consulting | 그건 무급 컨설팅이 많네요 (거절 대신 비용을 올려놓는 no) |
| Don't. | 하지 마세요 — 이유 없이 한 단어로 끊는 기술적 no |
| Walk me through it | 차근차근 설명해 주세요 (지적을 받아들였다는 신호) |
| the Bacs window | Bacs 처리 창 — 영국 은행 자동이체 정산이 도는 시간대 |
| walk me through it | 차근차근 설명해 달라 |
