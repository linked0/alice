# 400 · Term — Feature flag
title_ko: Feature flag — 배포하지 않고 기능을 끄는 스위치, 그리고 그게 없을 때의 대가
situation: Jay asks what "the flag" means in a postmortem he is reading. The answer is short — a feature flag is a software switch that turns a capability on or off — but the interesting part is the sentence the postmortem actually contains: the flag was cut from the release because it would have taken a day. When the bug arrived, the team stopped payouts by hand, from a runbook, in twelve minutes.
situation_ko: Jay가 읽고 있던 포스트모템에서 "the flag"가 무슨 뜻인지 묻는다. 답은 짧다. feature flag는 기능을 켜고 끄는 소프트웨어 스위치다. 그런데 정작 흥미로운 건 그 문서에 실제로 적힌 문장이다. 하루가 걸린다는 이유로 flag를 출시에서 뺐고, 버그가 터지자 팀은 runbook을 보고 손으로 12분 만에 지급을 멈췄다.
why: Ask **"What does 'the flag' mean here?"** — the `here` is what makes it a question about this text rather than about the English word, and it is the single most useful thing to append when you are asking about jargon in context. On the term itself: a feature flag is a **kill switch**, and the two words are not synonyms. A flag is the mechanism; kill switch is the role it plays when something is on fire. Learn it as a pair with the verbs it lives beside — to **halt** payouts, to **queue** them, to **roll back**, to **ship without** a flag. And keep the sentence that makes it a real engineering topic rather than a definition: **a flag is never just a Boolean.** Doing it safely means admin permissions, an audit trail, a decision about payments already in flight, tests, and a restart procedure — which is why "one day" was an honest estimate and why cutting it felt cheap.
why_ko: **"What does 'the flag' mean here?"** 라고 묻자. 문장 끝의 `here`가 이 질문을 영어 단어에 대한 것이 아니라 **이 문서에 대한 것**으로 만든다. 문맥 속 전문용어의 뜻을 물을 때 붙일 수 있는 가장 쓸모 있는 한 단어다. 용어 자체에 대해서는, feature flag가 곧 **kill switch**이지만 둘은 동의어가 아니다. flag는 메커니즘이고, kill switch는 불이 났을 때 그것이 맡는 **역할**이다. 옆에 붙어 사는 동사들과 함께 외우자 — 지급을 **halt**하다, **queue**에 넣다, **roll back**하다, flag 없이 **ship**하다. 그리고 이것을 정의가 아니라 진짜 엔지니어링 주제로 만드는 문장을 기억하자. **flag는 결코 Boolean 하나가 아니다.** 안전하게 만들려면 관리자 권한, 감사 로그, 이미 처리 중인 지급에 대한 판단, 테스트, 재시작 절차가 필요하다. "하루"가 정직한 추정이었던 이유이고, 그것을 뺀 것이 싸게 느껴졌던 이유다.
status: done
added: 2026-09-23
done: 2026-09-23T11:40:00+09:00

## Dialogue
Jay: What does "the flag" mean here? The postmortem keeps saying they wished they had it.
> 여기서 "the flag"가 무슨 뜻이야? 포스트모템에서 그게 있었으면 좋았을 거라고 계속 나오는데.
Mira: A feature flag. A switch in config that turns a capability on or off without shipping new code. In this case it gated payouts.
> feature flag. 새 코드를 배포하지 않고 기능을 켜고 끄는 설정 스위치야. 이 경우엔 지급을 제어했고.
Jay: So `payouts_enabled = false` and everything stops?
> 그럼 `payouts_enabled = false`면 전부 멈추는 거야?
Mira: Stops or queues — that's a design decision, and it's the one people forget. Either way you can halt payouts in seconds instead of cutting a release. That's why it's also called a kill switch.
> 멈추거나 대기열에 넣거나 — 그건 설계 결정이고, 다들 잊어버리는 부분이지. 어느 쪽이든 릴리스를 새로 내는 대신 몇 초 만에 지급을 중단할 수 있어. 그래서 kill switch라고도 부르고.
Jay: If it's that useful, why did they ship without it?
> 그렇게 유용한데 왜 그거 없이 출시했어?
Mira: It was scoped at a day and it got cut. And a day is about right — it's not a Boolean. You need admin permissions, an audit trail, a rule for payments already in flight, and tests.
> 하루로 산정됐다가 잘렸어. 그리고 하루는 꽤 맞는 추정이야. Boolean 하나가 아니거든. 관리자 권한, 감사 로그, 이미 처리 중인 지급에 대한 규칙, 테스트가 필요해.
Jay: So what did they do when it actually broke?
> 그래서 실제로 터졌을 때 어떻게 했어?
Mira: Jay had written a runbook for stopping payouts by hand. The team followed it and had them halted in twelve minutes. Good outcome — but twelve minutes is the price of the day they saved.
> Jay가 지급을 수동으로 멈추는 runbook을 써 뒀어. 팀이 그대로 따라서 12분 만에 중단했고. 좋은 결과지 — 다만 12분은 아낀 하루의 대가야.

## Techniques
1. **문맥 속 용어를 물을 때는 문장 끝에 `here`를 붙인다.** "What does the flag mean?"은 사전적 의미를 묻는 질문으로 들리고, 상대는 일반론을 설명하기 시작한다. **"What does 'the flag' mean here?"** 는 "이 문서에서"라고 범위를 좁혀 주고, 따옴표는 그 단어를 인용하고 있다는 신호가 된다. 회의에서 모르는 약어가 나왔을 때 그대로 쓸 수 있는 형태다.
2. **정의를 들은 다음에는 예시가 아니라 경계를 묻는다.** Jay는 "So `payouts_enabled = false` and everything stops?"라고 되묻는다. 자기가 이해한 것을 구체적인 형태로 되돌려 주는 질문이라, 상대가 "멈추거나 대기열에 넣거나"라는 **실제로 중요한 차이**를 보탤 수 있다. "Can you give me an example?"보다 훨씬 많은 것을 끌어낸다.
3. **비용을 숫자 두 개의 교환으로 말한다.** "Twelve minutes is the price of the day they saved." 영어 회고에서 가장 설득력 있는 문장 형태다. 비난하지 않고, 추정치와 결과를 나란히 놓아 판단을 듣는 사람에게 맡긴다. 다음에 같은 결정을 할 때 쓸 수 있는 근거가 된다.

## Words
| flag | /flæɡ/ | 기능을 켜고 끄는 설정 스위치 — 이 문맥에서는 깃발이 아니다. `feature flag`의 줄임말로 그냥 "the flag"라고 부른다 |
| toggle | /ˈtɑːɡl̩/ | 켜고 끄는 두 상태 스위치, 또는 그렇게 전환하다 — 명사·동사 둘 다. flag의 더 일반적인 말 |
| kill switch | /ˈkɪl swɪtʃ/ | 긴급 정지 장치 — 강세는 KILL에. flag의 메커니즘이 아니라 위기 때의 역할을 가리킨다 |
| to halt | /hɔːlt/ | (진행 중인 것을) 중단시키다 — stop보다 격식 있고 단호하다. "halt payouts" |
| to queue | /kjuː/ | 대기열에 넣다 — 발음이 철자와 전혀 다르다. 알파벳 q 하나와 같은 소리, "큐" |
| payout | /ˈpeɪaʊt/ | 지급, 지급금 — 명사는 한 단어이고 강세는 앞(PAY-out). 동사는 두 단어 `pay out` |
| in flight | /ɪn ˈflaɪt/ | 이미 시작돼 처리 중인 — "payments already in flight". 비행기 말고 진행 중인 작업 |
| to gate | /ɡeɪt/ | (조건을 걸어) 통과를 제어하다 — "the flag gated payouts". 동사로 쓰는 것이 핵심 |
| to scope | /skoʊp/ | 작업량을 산정하다, 범위를 정하다 — "it was scoped at a day" |
| to cut | /kʌt/ | (일정·범위에서) 빼다, 잘라내다 — "it got cut". 자르다보다 "빼기로 했다"에 가깝다 |
| to roll back | /roʊl ˈbæk/ | 이전 버전으로 되돌리다 — flag를 끄는 것보다 무겁고 느린 대안 |
| audit trail | /ˈɔːdɪt treɪl/ | 감사 추적 기록, 누가 언제 무엇을 했는지 남는 로그 |
| runbook | /ˈrʌnbʊk/ | 장애 시 따라 하는 절차서 — 한 단어. "written a runbook for stopping payouts" |
| postmortem | /ˌpoʊstˈmɔːrtəm/ | 사후 분석, 장애 회고 — 강세는 MOR에. IT에서는 부검이 아니라 회고 문서 |

## Expressions
| What does "the flag" mean here? | 여기서 "the flag"가 무슨 뜻이야? · 문맥 속 용어를 물을 때. 끝의 here가 범위를 이 문서로 좁힌다 |
| a switch in config | 설정에 있는 스위치 · 코드가 아니라 설정으로 제어된다는 뜻을 한 마디로 |
| without shipping new code | 새 코드를 배포하지 않고 · flag의 존재 이유 전체가 이 구절에 들어 있다 |
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
| the price of the day they saved | 그들이 아낀 하루의 대가 · 비용을 비난 없이 교환으로 표현하는 문장 |
