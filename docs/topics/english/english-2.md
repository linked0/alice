# 2 · Design — Fail closed or fail open
title_ko: 막고 실패할까, 통과시키고 실패할까
situation: The Chainlink feed is late. Marek wants to settle on the last known price; Jay would rather freeze. Neither option is good, and only one is reversible.
situation_ko: Chainlink 피드가 늦다. Marek은 마지막 가격으로 정산하자고 하고 Jay는 얼리자고 한다. 둘 다 좋지 않고, 되돌릴 수 있는 건 하나뿐이다.
why: Naming the two options with their standard names cuts the argument in half, and the reversibility test usually ends it.
why_ko: 두 선택지에 표준 이름을 붙이면 논쟁이 절반으로 줄고, 되돌릴 수 있는가 기준이 대개 논쟁을 끝낸다.

## Dialogue
Marek: If the oracle is late, settle on the last known price. Freezing makes us look broken.
> 오라클이 늦으면 마지막 가격으로 정산해요. 얼리면 고장 난 것처럼 보입니다.
Jay: So we're choosing between failing closed and failing open. I'd name it that way, because both are bad and only one is reversible.
> 그러니까 fail-closed와 fail-open 중에 고르는 거네요. 그렇게 이름 붙이고 싶어요. 둘 다 나쁘고 되돌릴 수 있는 건 하나라서요.
Marek: Reversible how?
> 되돌릴 수 있다는 게 어떤 뜻이죠?
Jay: Freeze and be wrong, people are annoyed for an hour. Settle on a stale price and be wrong, someone got paid and someone didn't, and we can't take it back without touching balances.
> 얼렸는데 틀리면 사람들이 한 시간 짜증 납니다. 오래된 가격으로 정산했는데 틀리면 누군가는 받고 누군가는 못 받았고, 잔고를 건드리지 않고는 되돌릴 수 없어요.
Marek: Unless the resolution is disputable for a window.
> 정산에 분쟁 제기 창을 두지 않는 한요.
Jay: That's a real third option, and better than either of mine. Then the question isn't open or closed. It's how long the window is and who can raise a dispute.
> 그건 진짜 세 번째 선택지고 제 둘보다 낫습니다. 그러면 질문이 open이냐 closed냐가 아니라, 창이 얼마나 길고 누가 제기할 수 있느냐가 되죠.
Marek: And if nobody disputes, it settles quietly.
> 아무도 제기하지 않으면 조용히 정산되고요.
Jay: Which is what we want. It's a parameter now, not an argument. Let's write both numbers down before we build.
> 그게 우리가 원하는 거죠. 이제 논쟁이 아니라 파라미터입니다. 만들기 전에 두 숫자를 적어둡시다.

## Techniques
1. **선택지에 표준 이름을 붙인다.** "failing closed and failing open" 이름이 붙으면 남들이 이미 끝낸 논쟁을 다시 하지 않는다.
2. **되돌릴 수 있는가로 저울질한다.** "only one is reversible" 어느 쪽이 더 나쁜지 다투면 끝나지 않는다. 되돌릴 수 있는 실수와 없는 실수로 가르면 한 줄에 끝난다.
3. **상대의 반례를 3안으로 승격시킨다.** "That's a real third option, and better than either of mine." 이 문장이 상대를 설계자로 만들고, 실제로 더 나은 답이 나오는 방식이다.

## Expressions
| the last known price | 마지막으로 알려진 가격 |
| makes us look broken | 고장 난 것처럼 보이게 한다 |
| fail closed / fail open | 막고 실패 / 통과시키고 실패 |
| only one is reversible | 되돌릴 수 있는 건 하나뿐 |
| a stale price | 갱신되지 않은 가격 |
| without touching balances | 잔고를 건드리지 않고 |
| disputable for a window | 일정 기간 분쟁 제기 가능한 |
| a real third option | 진짜 세 번째 선택지 |
| a parameter, not an argument | 논쟁이 아니라 파라미터 |
| it settles quietly | 조용히 정산된다 |
