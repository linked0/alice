# 182 · Line — What's the one question a PoC would have to answer for this to move forward?
title_ko: What's the one question a PoC would have to answer for this to move forward? — 이게 다음 단계로 가려면 PoC가 반드시 답해야 할 단 하나의 질문은 뭔가요?
situation: A steering meeting. Mateo's partner team asks for two months to run a PoC of an intent-based bridge. Jay has to decide on budget and wants the single make-or-break question pinned down, with a number, before anyone starts.
situation_ko: 스티어링 회의. Mateo의 파트너 팀이 인텐트 기반 브리지의 PoC를 위해 두 달을 요청한다. Jay는 예산을 결정해야 하고, 누구든 시작하기 전에 성패를 가르는 단 하나의 질문을 숫자와 함께 못 박고 싶다.
why: **PoC** (proof of concept) is a short test of whether an idea works before real budget; **move forward** means going to the next stage, full build, funding, launch. The shape of the question, "the one question X would have to answer for Y to move forward", forces a make-or-break criterion instead of a list of nice-to-haves, and pairs with gate metrics fixed up front (fill rate, p95 latency) so the PoC ends as a yes or a no without sunk-cost arguments. "For this to move forward" means "in order for this to proceed". The casual meeting form is "What's the make-or-break question this PoC needs to answer?"
why_ko: **PoC**(개념 증명)는 진짜 예산을 넣기 전에 아이디어가 작동하는지 짧게 검증하는 것이고, **move forward**는 본개발, 예산 투입, 출시 같은 다음 단계로 가는 것이다. "the one question X would have to answer for Y to move forward"라는 질문의 꼴은 있으면 좋은 것들의 목록 대신 성패를 가르는 기준 하나를 강제하며, 미리 정한 게이트 지표(체결률, p95 지연)와 짝을 이뤄 PoC가 매몰 비용 논쟁 없이 예/아니오로 끝나게 한다. "For this to move forward"는 "이것이 진행되려면"이다. 회의체는 "What's the make-or-break question this PoC needs to answer?"다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, second export (2026-09-21), last card (sentence): Original "What's the one question a PoC would have to answer for this to move forward?" / Corrected "What is the one question a PoC must answer for this to move forward?" / Korean "이 프로젝트가 진전되기 위해 PoC(개념 증명)를 통해 반드시 검증해야 하는 단 하나의 핵심 질문은 무엇인가요?" / Meeting Casual "What's the make-or-break question this PoC needs to solve?" The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 두 번째 내보내기(2026-09-21), 마지막 카드(문장): 원문 "What's the one question a PoC would have to answer for this to move forward?" / 수정 "What is the one question a PoC must answer for this to move forward?" / 한국어 "이 프로젝트가 진전되기 위해 PoC(개념 증명)를 통해 반드시 검증해야 하는 단 하나의 핵심 질문은 무엇인가요?" / 회의 캐주얼 "What's the make-or-break question this PoC needs to solve?" 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-79.txt

## Dialogue
Mateo: We're asking for two months to run a PoC on the intent-based bridge.
> 인텐트 기반 브리지 PoC에 두 달을 요청드립니다.
Jay: Before we talk budget: what's the one question a PoC would have to answer for this to move forward?
> 예산 얘기 전에요. 이게 다음 단계로 가려면 PoC가 반드시 답해야 할 단 하나의 질문이 뭔가요?
Mateo: Whether solvers actually fill cross-chain intents in under ten seconds at our volumes.
> 솔버들이 우리 물량에서 크로스체인 인텐트를 실제로 10초 안에 체결하느냐죠.
Jay: Good, that's a make-or-break question. Now put numbers on it, fill rate and p95 latency, fixed up front, so the PoC ends as a yes or a no.
> 좋아요, 그게 성패를 가르는 질문이네요. 이제 거기에 숫자를 붙이세요. 체결률과 p95 지연을 미리 정해서 PoC가 예 아니면 아니오로 끝나게요.
Mateo: Say 95% filled under ten seconds at 500 intents an hour.
> 시간당 인텐트 500건에서 95%가 10초 안에 체결, 이 정도로요.
Jay: Then two weeks should show it, not two months. If it clears the gate, we move forward; if not, we stop without arguing about sunk cost.
> 그럼 두 달이 아니라 2주면 보일 거예요. 게이트를 통과하면 진행하고, 아니면 매몰 비용 논쟁 없이 멈추죠.

## Techniques
1. **예산 논의 전에 "단 하나의 질문"을 요구한다.** "What's the one question a PoC would have to answer for this to move forward?" — 목록이 아니라 기준 하나를 받아 내는 질문의 꼴이다.
2. **질문이 나오면 숫자와 기한으로 바꾼다.** "put numbers on it, fill rate and p95 latency, fixed up front" → "two weeks should show it, not two months" — 게이트 지표가 정해지면 기간도 줄어든다.





## Words
| gate | /ɡeɪt/ | 게이트(사전 정의 기준)를 통과하다 |
| forward | /ˈfɔrwɚd/ | 이것이 다음 단계로 가려면 |

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| the one question a PoC would have to answer | PoC가 반드시 답해야 할 단 하나의 질문 — 검증 범위를 좁힐 때 |
| for this to move forward | 이것이 다음 단계로 가려면 — 예산·본개발 결정의 조건 |
| a make-or-break question | 성패를 가르는 질문 — 회의 캐주얼 버전 |
| clear the gate | 게이트(사전 정의 기준)를 통과하다 — PoC를 예/아니오로 끝낼 때 |
