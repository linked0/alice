# 33 · Planning — Grill me before you plan
title_ko: 계획하기 전에 나를 심문하라
situation: Jay's first sprint planning as lead of a distributed team in Berlin. Nadia, a senior engineer, has written a plan for the new payout service in twenty minutes with an agent and wants to start. Jay suspects the plan encodes assumptions nobody agreed on. He has to slow it down without insulting the work.
situation_ko: 베를린 분산 팀 리드로서 첫 스프린트 계획. 시니어 엔지니어 Nadia가 에이전트와 20분 만에 새 지급 서비스 계획을 썼고 시작하길 원한다. Jay는 그 계획이 아무도 합의하지 않은 가정을 담고 있다고 의심한다. 작업을 깎아내리지 않고 속도를 늦춰야 한다.
why: The most common failure of agent-assisted teams is a plan that looks finished before the team shares a picture. A lead's job is to make the questions happen before the code does, and to do it in a way that makes the author look thorough, not careless.
why_ko: 에이전트 보조 팀의 가장 흔한 실패는 팀이 그림을 공유하기 전에 완성된 것처럼 보이는 계획이다. 리드의 일은 코드 전에 질문이 일어나게 하는 것이고, 저자가 부주의한 게 아니라 철저해 보이게 하는 방식으로 하는 것이다.
status: important

## Dialogue
Nadia: The plan's in the doc. Agent and I went through it this morning. Can we start after standup?
> 계획은 문서에 있어요. 오늘 아침 에이전트와 같이 봤어요. 스탠드업 뒤에 시작할까요?
Jay: It's a good plan, and I want to try something before we start. Give me ten minutes to grill you on it, out loud, and if I can't find a decision we haven't actually made, we start at eleven.
> 좋은 계획이에요. 시작하기 전에 하나 해보고 싶어요. 10분만 소리 내어 심문하게 해주고, 우리가 실제로 내리지 않은 결정을 제가 못 찾으면 11시에 시작합시다.
Nadia: Fine. Go.
> 좋아요. 하세요.
Jay: When a payout fails halfway, does the merchant see a pending balance or the old balance?
> 지급이 중간에 실패하면 가맹점은 보류 잔고를 보나요, 이전 잔고를 보나요?
Nadia: Pending. The agent suggested optimistic updates.
> 보류요. 에이전트가 낙관적 업데이트를 제안했어요.
Jay: Did we decide that, or did the agent? Because Finance told me last week they reconcile against what the merchant saw. If we show pending and roll back, their books don't match ours.
> 그건 우리가 결정한 건가요, 에이전트가? 지난주 재무팀이 가맹점이 본 것을 기준으로 대사한다고 했거든요. 보류를 보여주고 롤백하면 그들 장부와 우리 장부가 안 맞아요.
Nadia: I didn't know that. Then it's the old balance until settlement confirms.
> 그건 몰랐어요. 그럼 정산 확인까지 이전 잔고요.
Jay: Second one. The plan says "idempotency key in Redis." Who owns the key when two services retry the same payout?
> 둘째. 계획에 "Redis의 멱등성 키"라고 있어요. 두 서비스가 같은 지급을 재시도하면 키는 누가 소유하나요?
Nadia: ...The ledger should. Redis is a cache in front of it.
> …원장이요. Redis는 그 앞의 캐시.
Jay: Agreed, and that's a sentence that isn't in the doc. Two decisions in six minutes. I'm not saying the plan was careless; I'm saying the agent can't know what Finance told me. Add those two, and let's make this the rule: any plan gets ten minutes of questions from someone who didn't write it, before the first line of code.
> 동의하고, 그건 문서에 없는 문장이에요. 6분에 결정 둘. 계획이 부주의했다는 게 아니에요. 에이전트는 재무팀이 제게 한 말을 알 수 없다는 거예요. 그 둘을 추가하고, 이걸 규칙으로 합시다. 어떤 계획이든 첫 코드 줄 전에 쓰지 않은 사람에게서 10분의 질문을 받는다.
Nadia: Eleven, then. And you're doing this to your own plans too.
> 그럼 11시. 그리고 당신 계획에도 이걸 하는 거죠.
Jay: Especially mine.
> 제 것에 특히요.

## Techniques
1. **시간을 걸고 검증 가능한 조건을 붙인다.** "Give me ten minutes… if I can't find a decision we haven't actually made, we start at eleven." 지연이 아니라 내기. 못 찾으면 바로 시작이므로 저자가 받아들일 수 있다.
2. **"누가 결정했나"를 묻는다.** "Did we decide that, or did the agent?" 계획 속 가정을 드러내는 가장 짧은 질문. 에이전트는 회의실에 없었던 정보를 알 수 없다.
3. **개인 지적을 팀 규칙으로 바꾼다.** "let's make this the rule… Especially mine." 저자 한 사람에 대한 비판이 아니라 모두에게 적용되는 절차로 닫아, 관계와 규칙을 동시에 지킨다.





## Words
| grill | /ɡrɪl/ | 그것에 대해 당신을 심문하다 |
| halfway | /ˌhæfˈweɪ/ | 중간에 |

## Expressions
| grill you on it | 그것에 대해 당신을 심문하다 |
| out loud | 소리 내어 |
| a decision we haven't actually made | 우리가 실제로 내리지 않은 결정 |
| halfway | 중간에 |
| did we decide that, or did the agent | 그건 우리가 결정했나, 에이전트가 했나 |
| their books don't match ours | 그들 장부와 우리 장부가 안 맞다 |
| who owns the key | 키는 누가 소유하나 |
| a sentence that isn't in the doc | 문서에 없는 문장 |
| I'm not saying… I'm saying… | ~라는 게 아니라 ~라는 것이다 |
| someone who didn't write it | 그것을 쓰지 않은 사람 |
| especially mine | 제 것에 특히 |
