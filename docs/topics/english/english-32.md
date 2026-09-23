# 32 · Interview — How do you use AI, and what do you refuse to hand it?
title_ko: AI를 어떻게 쓰고, 무엇은 넘기지 않나요?
situation: A panel interview for a team lead role at a Copenhagen fintech. Sofie, the head of engineering, asks the question every 2026 interview now contains: "How do you use AI in your work?" The wrong answers are "for everything" and "I don't trust it." Jay has to show judgement, not enthusiasm.
situation_ko: 코펜하겐 핀테크 팀 리드 패널 면접. 엔지니어링 헤드 Sofie가 2026년 모든 면접에 들어 있는 질문을 한다. "일에서 AI를 어떻게 쓰나요?" 틀린 답은 "전부에"와 "믿지 않습니다". Jay는 열의가 아니라 판단력을 보여야 한다.
why: This question is a proxy for whether you will let a team's fundamentals rot. The answer that works names what you delegate, what you keep, and why the line is where it is, with one example where the line saved you.
why_ko: 이 질문은 팀의 기본기를 썩게 둘 사람인지의 대리 지표다. 되는 답은 무엇을 위임하고 무엇을 지키는지, 왜 선이 거기 있는지를 말하고, 그 선이 자신을 구한 사례 하나를 붙인다.
status: important

## Dialogue
Sofie: How do you use AI in your work? Be specific.
> 일에서 AI를 어떻게 쓰나요? 구체적으로요.
Jay: I split tasks into errands and walks. Errands go to the agent: literature and API surveys, refactoring inside a module whose interface I've fixed, test scaffolding, proofreading, and code review for the things a linter misses. Walks I do by hand: the design of a boundary, the first invariant test on anything that moves money, and any bug I don't yet understand. The line is there because the walks are where I learn the system, and a lead who stops learning the system can't review anything.
> 작업을 심부름과 걷기로 나눕니다. 심부름은 에이전트에게요. 문헌과 API 조사, 제가 인터페이스를 고정한 모듈 내부의 리팩터링, 테스트 스캐폴딩, 교정, 린터가 놓치는 것에 대한 코드 리뷰. 걷기는 손으로 합니다. 경계 설계, 돈을 움직이는 모든 것의 첫 불변식 테스트, 그리고 아직 이해하지 못한 모든 버그. 선이 거기 있는 이유는 걷기가 시스템을 배우는 곳이고, 시스템 배우기를 멈춘 리드는 아무것도 리뷰할 수 없기 때문입니다.
Sofie: Give me a time the line mattered.
> 그 선이 중요했던 때를 말해 주세요.
Jay: Last spring an agent proposed a settlement change that passed every test we had. I made myself trace the payout path by hand before approving, which took an hour I resented. The change double-counted fees on refunds, a case no test covered. If I had treated that as an errand, it would have shipped. So now, for anything touching payouts, the first review is a walk, and I write the missing test before I write the approval.
> 지난봄 에이전트가 우리가 가진 모든 테스트를 통과하는 정산 변경을 제안했습니다. 승인 전에 지급 경로를 손으로 따라가게 스스로 강제했고, 짜증나는 한 시간이었습니다. 그 변경은 환불 시 수수료를 이중 계산했고, 어떤 테스트도 다루지 않는 케이스였습니다. 심부름으로 취급했다면 출시됐을 겁니다. 그래서 지금은 지급을 건드리는 모든 것에 첫 리뷰는 걷기이고, 승인을 쓰기 전에 빠진 테스트를 씁니다.
Sofie: Doesn't that slow your team down?
> 그러면 팀이 느려지지 않나요?
Jay: It slows the ten percent that can lose money and speeds up the ninety that can't. And for juniors I'm stricter the other way: they walk more than I do, because the routine bugs are how they become the people who can review the agent later. If the agent takes all of those, in three years I have a team that can prompt and can't judge.
> 돈을 잃을 수 있는 10퍼센트는 느려지고 그럴 수 없는 90퍼센트는 빨라집니다. 그리고 주니어에게는 반대로 더 엄격합니다. 저보다 더 많이 걷게 합니다. 일상적 버그가 나중에 에이전트를 리뷰할 수 있는 사람이 되는 방법이니까요. 에이전트가 그것을 전부 가져가면 3년 뒤 프롬프트는 할 수 있고 판단은 못 하는 팀이 생깁니다.
Sofie: What do you do when the agent is confidently wrong?
> 에이전트가 자신 있게 틀리면 어떻게 하나요?
Jay: Treat it like a well-read colleague who's had two drinks. Ask for the reasoning step by step, run the step that can be run, and never accept a claim about money without a number I can reproduce. It's a useful colleague. It's not a witness.
> 잘 읽었지만 두 잔 마신 동료처럼 대합니다. 추론을 단계별로 요구하고, 실행할 수 있는 단계는 실행하고, 재현할 수 있는 숫자 없이는 돈에 대한 주장을 절대 받지 않습니다. 유용한 동료입니다. 증인은 아닙니다.

## Techniques
1. **이분법을 거절하고 배분을 보여준다.** "I split tasks into errands and walks." 전부/전무 대신 분류. 그리고 선의 이유("the walks are where I learn the system").
2. **선이 구한 사례는 비용도 함께.** "an hour I resented… it would have shipped." 자기 규율의 비용을 인정할 때 사례가 진짜로 들린다.
3. **팀 관점으로 끝낸다.** "in three years I have a team that can prompt and can't judge." 리드 면접에서 개인 습관은 팀 정책으로 번역되어야 점수가 된다.



## Words
| errands and walks | /ˈɛrəndz ənd wɔks/ | 심부름과 걷기(위임할 일과 직접 할 일) |
| hour I resented | /ˈaʊɚ aɪ riˈzɛntɪd/ | 짜증났던 한 시간 |
| confidently wrong | /ˈkɑnfədəntli rɔŋ/ | 자신 있게 틀린 |

## Expressions
| errands and walks | 심부름과 걷기(위임할 일과 직접 할 일) |
| whose interface I've fixed | 내가 인터페이스를 고정한 |
| a bug I don't yet understand | 아직 이해하지 못한 버그 |
| an hour I resented | 짜증났던 한 시간 |
| a case no test covered | 어떤 테스트도 다루지 않은 케이스 |
| it would have shipped | 출시됐을 것이다 |
| stricter the other way | 반대 방향으로 더 엄격한 |
| can prompt and can't judge | 프롬프트는 할 수 있고 판단은 못 하는 |
| confidently wrong | 자신 있게 틀린 |
| a number I can reproduce | 내가 재현할 수 있는 숫자 |
| it's not a witness | 그것은 증인이 아니다 |
