# 23 · Interview — Tell me about a time you disagreed with your manager
title_ko: 매니저와 의견이 갈렸던 때를 말해 보세요
situation: A behavioural interview for a team lead role at an Amsterdam payments company. The interviewer asks the question every candidate is warned about. Jay has a real story: he argued against shipping a settlement feature without a kill switch, lost the argument, and was proven right two weeks later. The trap is telling it as "I was right."
situation_ko: 암스테르담 결제 회사 팀 리드 면접의 행동 질문. 모든 후보가 경고받는 그 질문이다. Jay에게는 실제 이야기가 있다. 킬 스위치 없이 정산 기능을 출시하는 데 반대했고, 논쟁에서 졌고, 2주 뒤 옳았음이 증명됐다. 함정은 이것을 "내가 옳았다"로 말하는 것이다.
why: This question is not about the disagreement. It tests whether you can disagree without contempt, commit to a decision you lost, and describe your manager as a reasonable person. Non-native speakers often win the argument in the story and lose the interview.
why_ko: 이 질문은 의견 차이에 대한 것이 아니다. 경멸 없이 반대할 수 있는지, 진 결정에 커밋할 수 있는지, 매니저를 합리적인 사람으로 묘사하는지를 본다. 비원어민은 이야기 속 논쟁에서 이기고 면접에서 지는 일이 많다.
status: planned

## Dialogue
Interviewer: Tell me about a time you disagreed with your manager. What happened?
> 매니저와 의견이 갈렸던 때를 말해 주세요. 어떻게 됐나요?
Jay: Last spring we were shipping a settlement feature two days before a partner demo. I wanted a kill switch, a flag that could halt payouts, before it went live. My manager wanted to ship without it and add it the following sprint. Her reasoning was fair: the demo mattered, and the flag was a day of work we didn't have.
> 지난봄 파트너 데모 이틀 전에 정산 기능을 출시하고 있었습니다. 저는 라이브 전에 킬 스위치, 지급을 멈출 수 있는 플래그를 원했습니다. 매니저는 그것 없이 출시하고 다음 스프린트에 추가하길 원했습니다. 그분 논리는 타당했습니다. 데모가 중요했고, 플래그는 우리에게 없는 하루치 일이었습니다.
Interviewer: How did you make your case?
> 어떻게 주장하셨나요?
Jay: Once, clearly, in writing. I wrote a half-page: what could go wrong, what it would cost per hour without a switch, and what I'd need to build it in half a day instead of one. Then I asked for a decision by noon so we'd stop debating and start building either way.
> 한 번, 명확하게, 글로요. 반 페이지를 썼습니다. 무엇이 잘못될 수 있는지, 스위치 없이 시간당 얼마의 비용이 드는지, 하루 대신 반나절에 만들려면 무엇이 필요한지. 그리고 정오까지 결정을 요청했습니다. 어느 쪽이든 토론을 멈추고 만들기 시작하려고요.
Interviewer: And she said no.
> 그리고 안 된다고 했군요.
Jay: She said ship without it. So I shipped without it, and I made sure the team heard me support the decision, because a lead who loses an argument and then sulks costs more than a missing flag. I also quietly wrote the runbook for a manual halt, so if we needed one, it would take ten minutes instead of an hour.
> 그것 없이 출시하라고 했습니다. 그래서 그것 없이 출시했고, 팀이 제가 그 결정을 지지하는 것을 듣게 했습니다. 논쟁에서 지고 삐진 리드는 빠진 플래그보다 비용이 크니까요. 그리고 조용히 수동 중단 런북을 썼습니다. 필요해지면 한 시간 대신 10분이 걸리도록요.
Interviewer: Did you need it?
> 필요했나요?
Jay: Two weeks later, yes. A pricing bug overpaid about forty users. We halted manually in twelve minutes using the runbook, and the flag went in that afternoon. Total exposure was a few hundred euros.
> 2주 뒤에, 네. 가격 버그가 약 40명에게 과지급했습니다. 런북으로 12분 만에 수동 중단했고, 플래그는 그날 오후에 들어갔습니다. 총 노출은 몇백 유로였습니다.
Interviewer: So you were right.
> 그러니까 당신이 옳았군요.
Jay: About the flag, yes. About the decision, I'm less sure. The demo went well and it led to the contract we're still running on. If I'd been the manager with her information, I might have made the same call. What I took from it is that when I lose an argument, I should reduce the cost of being right later, not keep relitigating.
> 플래그에 대해서는요. 결정에 대해서는 덜 확신합니다. 데모는 잘 됐고 지금도 우리가 굴러가는 계약으로 이어졌습니다. 제가 그분의 정보를 가진 매니저였다면 같은 결정을 했을지도 모릅니다. 거기서 배운 것은, 논쟁에서 지면 계속 재론하는 대신 나중에 옳을 때의 비용을 줄여야 한다는 것입니다.

## Techniques
1. **상대의 논리를 먼저 타당하게 만든다.** "Her reasoning was fair: the demo mattered." 매니저를 합리적으로 그리면 내 반대가 판단력으로 읽히고, 어리석게 그리면 내 반대가 성격으로 읽힌다.
2. **한 번, 글로, 결정 기한과 함께.** "Once, clearly, in writing… I asked for a decision by noon." 반대의 형식이 곧 시니어 신호다. 반복해서 설득하는 것은 주니어, 한 번 명확히 쓰고 결정을 요청하는 것은 리드.
3. **"내가 옳았다"를 거절한다.** "About the flag, yes. About the decision, I'm less sure." 면접관이 미끼를 던졌을 때 그것을 물지 않는 문장. 여기서 채용이 결정된다.

## Expressions
| the question every candidate is warned about | 모든 후보가 경고받는 질문 |
| her reasoning was fair | 그분 논리는 타당했다 |
| make your case | 주장을 펼치다 |
| once, clearly, in writing | 한 번, 명확하게, 글로 |
| a decision by noon | 정오까지 결정 |
| either way | 어느 쪽이든 |
| a lead who loses an argument and then sulks | 논쟁에서 지고 삐지는 리드 |
| total exposure | 총 노출(손실 가능액) |
| I'm less sure | 덜 확신한다 |
| relitigate | 이미 끝난 논쟁을 다시 꺼내다 |
| reduce the cost of being right later | 나중에 옳을 때의 비용을 줄이다 |
