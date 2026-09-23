# 23 · Interview — Tell me about a time you disagreed with your manager
title_ko: 매니저와 의견이 갈렸던 때를 말해 보세요
situation: A behavioural interview for a team lead role at an Amsterdam payments company. The interviewer asks the question every candidate is warned about. Jay has a real story: he argued against shipping a settlement feature without a kill switch, lost the argument, and was proven right two weeks later. The trap is telling it as "I was right."
situation_ko: 암스테르담 결제 회사 팀 리드 면접의 행동 질문. 모든 후보가 경고받는 그 질문이다. Jay에게는 실제 이야기가 있다. 킬 스위치 없이 정산 기능을 출시하는 데 반대했고, 논쟁에서 졌고, 2주 뒤 옳았음이 증명됐다. 함정은 이것을 "내가 옳았다"로 말하는 것이다.
why: This question is not about the disagreement. It tests whether you can disagree without contempt, commit to a decision you lost, and describe your manager as a reasonable person. Non-native speakers often win the argument in the story and lose the interview.
why_ko: 이 질문은 의견 차이에 대한 것이 아니다. 경멸 없이 반대할 수 있는지, 진 결정에 커밋할 수 있는지, 매니저를 합리적인 사람으로 묘사하는지를 본다. 비원어민은 이야기 속 논쟁에서 이기고 면접에서 지는 일이 많다.
status: done
added: 2026-09-19
done: 2026-09-23T12:10:00+09:00

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
4. **모르는 용어는 문장 끝에 `here`를 붙여 묻는다.** "What does 'the flag' mean here?" — `here`가 사전적 뜻이 아니라 **이 이야기 안에서의 뜻**으로 질문의 범위를 좁힌다. 따옴표는 그 단어를 인용하고 있다는 신호다. 면접에서도 회의에서도 모르는 약어가 나왔을 때 그대로 쓸 수 있고, 모른다고 인정하는 대신 정확히 묻는 것으로 들린다.





## Words
| flag | /flæɡ/ | 이 이야기에서는 깃발이 아니라 **feature flag** — 배포 없이 기능을 켜고 끄는 설정 스위치. 줄여서 그냥 "the flag" |
| feature flag | /ˈfitʃər flæɡ/ | 기능 플래그. `payouts_enabled = true` 면 지급 실행, `false` 면 중단하거나 대기열 보관 |
| kill switch | /ˈkɪl swɪtʃ/ | 긴급 정지 장치 — 강세는 KILL에. flag의 **메커니즘**이 아니라 불이 났을 때의 **역할**을 가리킨다 |
| toggle | /ˈtɑɡl̩/ | 두 상태 스위치, 또는 그렇게 전환하다 — 명사·동사 둘 다. flag의 더 일반적인 말 |
| to gate | /ɡeɪt/ | (조건을 걸어) 통과를 제어하다 — "the flag gated payouts". 동사로 쓰는 것이 핵심 |
| to halt | /hɔlt/ | (진행 중인 것을) 중단시키다 — stop보다 격식 있고 단호하다. "halt payouts" |
| to queue | /kju/ | 대기열에 넣다 — 철자가 발음에 전혀 도움이 안 된다. 알파벳 q 하나와 같은 소리, "큐" |
| payout | /ˈpeɪaʊt/ | 지급, 지급금 — 명사는 한 단어, 강세는 앞(PAY-out). 동사는 두 단어 `pay out` |
| in flight | /ɪn ˈflaɪt/ | 이미 시작돼 처리 중인 — "payments already in flight". 비행기가 아니라 진행 중인 작업 |
| to scope | /skoʊp/ | 작업량을 산정하다, 범위를 정하다 — "it was scoped at a day" |
| to cut | /kʌt/ | (일정·범위에서) 빼다 — "it got cut". 자르다보다 "빼기로 했다"에 가깝다 |
| to roll back | /roʊl ˈbæk/ | 이전 버전으로 되돌리다 — flag를 끄는 것보다 무겁고 느린 대안 |
| audit trail | /ˈɔdɪt treɪl/ | 감사 추적 기록 — 누가 언제 무엇을 했는지 남는 로그 |
| runbook | /ˈrʌnbʊk/ | 장애 시 그대로 따라 하는 절차서 — 한 단어 |
| postmortem | /ˌpoʊstˈmɔrtəm/ | 사후 분석, 장애 회고 — 강세는 MOR에. IT에서는 부검이 아니라 회고 문서 |
| exposure | /ɪkˈspoʊʒər/ | (금융) 손실 가능액, 노출 — "total exposure". s가 /ʒ/ 소리 |
| reasoning | /ˈrizənɪŋ/ | 논리, 근거 — "her reasoning was fair" |
| to relitigate | /riˈlɪtəɡeɪt/ | 이미 끝난 논쟁을 다시 꺼내다 — 강세는 LI에 |
| to sulk | /sʌlk/ | 삐지다, 토라져 있다 — 면접에서 절대 보이면 안 되는 태도의 이름 |
| noon | /nun/ | 정오 — "a decision by noon" |

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
| What does "the flag" mean here? | 여기서 "the flag"가 무슨 뜻인가요? · 문맥 속 용어를 묻는 형태. 끝의 here가 범위를 이 이야기로 좁힌다 |
| a switch in config | 설정에 있는 스위치 · 코드가 아니라 설정으로 제어된다는 뜻을 한 마디로 |
| without shipping new code | 새 코드를 배포하지 않고 · feature flag의 존재 이유 전체가 이 구절에 있다 |
| it gated payouts | 지급 통과 여부를 제어했다 · gate를 동사로 쓰는 용법 |
| stops or queues | 멈추거나 대기열에 넣거나 · 설계 결정이 갈리는 지점을 두 단어로 |
| that's a design decision | 그건 설계 결정이다 · "정답이 없고 우리가 골라야 한다"를 정중하게 말하는 법 |
| halt payouts in seconds | 몇 초 만에 지급을 중단하다 · flag가 파는 것은 속도다 |
| cutting a release | 릴리스를 새로 내는 것 · cut a release = 배포본을 만들어 내보내다 |
| it was scoped at a day | 하루짜리로 산정됐다 · 추정치를 말하는 수동태 |
| it got cut | (범위에서) 빠졌다 · 누가 뺐는지 말하지 않고 사실만 남기는 형태 |
| it's not a Boolean | Boolean 하나가 아니다 · 단순해 보이는 일이 실제로는 아니라고 반박할 때 |
| payments already in flight | 이미 처리 중인 결제 · 중단 설계에서 가장 자주 빠지는 경우 |
| had them halted in twelve minutes | 12분 만에 중단시켰다 · have + 목적어 + 과거분사, "~되게 했다" |
| the price of the day they saved | 아낀 하루의 대가 · 비용을 비난 없이 교환으로 표현하는 문장 |
