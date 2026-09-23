# 21 · Interview — Don't draw yet. Ask what the box is for.
title_ko: 아직 그리지 마라. 그 상자가 무엇을 위한 것인지 물어라.
situation: A system design interview at a London fintech. The prompt is "design the settlement service for a prediction market." Jay has forty-five minutes and a whiteboard, and the interviewer is watching how he starts, not what he draws.
situation_ko: 런던 핀테크의 시스템 설계 면접. 문제는 "예측시장의 정산 서비스를 설계하라." Jay에게는 45분과 화이트보드가 있고, 면접관은 무엇을 그리는지가 아니라 어떻게 시작하는지를 본다.
why: The first five minutes decide the interview. Candidates who start drawing lose to candidates who scope, state assumptions out loud, and name the one constraint that shapes everything. This is that opening, sentence by sentence.
why_ko: 처음 5분이 면접을 결정한다. 바로 그리기 시작하는 후보는 범위를 정하고, 가정을 소리 내어 말하고, 모든 것을 결정하는 제약 하나를 짚는 후보에게 진다. 그 오프닝을 문장 단위로 담았다.
status: done
dones: 2026-09-21T23:07:39+09:00
done: 2026-09-21T23:07:39+09:00

## Dialogue
Interviewer: Design the settlement service for a prediction market. Take it wherever you like.
> 예측시장의 정산 서비스를 설계해 보세요. 원하는 방향으로 가져가셔도 됩니다.
Jay: Before I draw anything, three questions, so I solve your problem and not one I invented. Is settlement on-chain, off-chain, or both? What's the scale, roughly, markets per day and positions per market? And what's the cost of settling wrong versus settling late?
> 무엇을 그리기 전에 질문 셋을 하겠습니다. 제가 만든 문제가 아니라 당신의 문제를 풀기 위해서요. 정산은 온체인인가요, 오프체인인가요, 둘 다인가요? 규모는 대략 하루 마켓 수와 마켓당 포지션 수가 어느 정도죠? 그리고 잘못 정산하는 비용 대 늦게 정산하는 비용은요?
Interviewer: Both, custody on-chain and matching off-chain. Say a thousand markets a day, ten thousand positions each. Wrong is much worse than late.
> 둘 다요. 커스터디는 온체인, 매칭은 오프체인. 하루 마켓 천 개, 마켓당 포지션 만 개라고 하죠. 잘못이 늦은 것보다 훨씬 나쁩니다.
Jay: Then I'll say my key assumption out loud: correctness beats latency, so I'm designing a system that can stop. Every design choice from here follows from that. Push back if that's wrong.
> 그럼 핵심 가정을 소리 내어 말하겠습니다. 정확성이 지연보다 우선이니 멈출 수 있는 시스템을 설계합니다. 여기서부터 모든 설계 선택이 거기서 따라옵니다. 틀렸으면 반박해 주세요.
Interviewer: That's fine. Go on.
> 좋습니다. 계속하세요.
Jay: Three components. A resolution source that produces a signed outcome. A settlement engine that computes payouts as a pure function of positions plus outcome, idempotent per market. And an invariant checker that compares total payouts against escrowed collateral before anything moves, and halts on mismatch.
> 컴포넌트 셋입니다. 서명된 결과를 만드는 정산 소스. 포지션과 결과의 순수 함수로 지급을 계산하는, 마켓별로 멱등인 정산 엔진. 그리고 무엇이든 움직이기 전에 총 지급액과 에스크로 담보를 비교하고 불일치면 멈추는 인베리언트 검사기.
Interviewer: Why the halt? Users will hate a frozen market.
> 왜 중단이죠? 사용자는 얼어붙은 마켓을 싫어할 텐데요.
Jay: They will, for an hour. You told me wrong is much worse than late, and a halt is the only reversible failure. If I'd been told the opposite, I'd design fail-open with a dispute window instead. That's the trade, and it's yours to make, not mine.
> 한 시간 동안은요. 잘못이 늦은 것보다 훨씬 나쁘다고 하셨고, 중단은 되돌릴 수 있는 유일한 실패입니다. 반대로 들었다면 분쟁 창을 둔 fail-open으로 설계했을 겁니다. 그게 트레이드오프이고, 그 선택은 제 것이 아니라 당신 것입니다.
Interviewer: Good. Now let's talk about what happens at ten million positions.
> 좋습니다. 이제 포지션 천만 개에서 무슨 일이 일어나는지 이야기해 보죠.
Jay: Then the pure function is the thing I keep and the storage is the thing I change. Let me draw where it shards.
> 그러면 순수 함수는 유지하고 스토리지를 바꿉니다. 어디서 샤딩되는지 그려 보겠습니다.

## Techniques
1. **그리기 전에 세 질문.** "Before I draw anything, three questions, so I solve your problem and not one I invented." 범위·규모·실패 비용. 이 세 질문이 면접관의 머릿속 정답지를 열어 준다.
2. **가정을 소리 내어 말하고 반박을 초대한다.** "I'll say my key assumption out loud… Push back if that's wrong." 틀린 가정으로 20분을 쓰는 것이 시스템 설계 면접에서 떨어지는 가장 흔한 길이다.
3. **트레이드오프의 소유권을 돌려준다.** "That's the trade, and it's yours to make, not mine." 시니어 신호. 정답을 고집하지 않고 결정을 요구사항에 묶는다.





## Words
| reversible | /rɪˈvɝsəbəl/ | 되돌릴 수 있는 유일한 실패 |

## Expressions
| take it wherever you like | 원하는 방향으로 가져가라 |
| before I draw anything | 무엇을 그리기 전에 |
| a problem I invented | 내가 만들어낸 문제 |
| roughly | 대략 |
| wrong versus late | 잘못 대 늦음 |
| say my key assumption out loud | 핵심 가정을 소리 내어 말하다 |
| push back if that's wrong | 틀렸으면 반박하라 |
| a pure function of | ~의 순수 함수 |
| the only reversible failure | 되돌릴 수 있는 유일한 실패 |
| it's yours to make, not mine | 그 결정은 내 것이 아니라 당신 것이다 |
