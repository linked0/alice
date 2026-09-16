# 8 · Incident — "No answer" is not "broken"
title_ko: "무응답"은 "고장"이 아니다
situation: The status page shows three services as unreachable at 3 a.m. Sun-woo is about to page everyone. The services are Cloud Run instances that scaled to zero.
situation_ko: 새벽 3시, 상태 페이지에 서비스 셋이 무응답으로 뜬다. 선우가 모두를 호출하려 한다. 그 서비스들은 0으로 스케일된 Cloud Run 인스턴스다.
why: Incident English for the first five minutes: slow the escalation, separate signal from state, and fix the page so the next person doesn't have this conversation.
why_ko: 사고 첫 5분의 영어. 에스컬레이션을 늦추고, 신호와 상태를 구분하고, 다음 사람이 같은 대화를 하지 않게 페이지를 고친다.

## Dialogue
Sun-woo: Three services are down on the status page. I'm paging the on-call.
> 상태 페이지에 서비스 셋이 다운이에요. 온콜을 호출할게요.
Jay: Hold one minute. Which three?
> 1분만요. 어느 셋이죠?
Sun-woo: Exchange, DeFi, Game.
> Exchange, DeFi, Game이요.
Jay: Those scale to zero when nobody's using them. From outside, a sleeping service and a stopped one look identical. Hit each one once and see if it wakes.
> 그건 아무도 쓰지 않으면 0으로 줄어드는 것들이에요. 밖에서 보면 자는 서비스와 멈춘 서비스가 똑같아요. 각각 한 번 쳐보고 깨어나는지 봐요.
Sun-woo: Exchange is back. Cold start, four seconds. The other two as well.
> Exchange 돌아왔어요. 콜드 스타트 4초. 나머지 둘도요.
Jay: Good. So there's no incident, but there is a bug, and it's on our status page. "Unreachable" is the wrong word for "asleep."
> 좋아요. 그러니 사고는 없지만 버그는 있고, 우리 상태 페이지에 있어요. "무응답"은 "잠든"의 잘못된 표현이에요.
Sun-woo: Should the probe wake them up first?
> 프로브가 먼저 깨워야 할까요?
Jay: No. Waking three services every five seconds costs money for a page nobody reads at night. Label the state honestly, "no answer, may be sleeping," and leave paging to real signals.
> 아니요. 5초마다 서비스 셋을 깨우는 건 밤에 아무도 읽지 않는 페이지에 돈을 쓰는 거예요. 상태를 정직하게 "무응답, 잠들었을 수 있음"으로 표기하고 호출은 진짜 신호에 맡겨요.

## Techniques
1. **첫 문장은 속도를 늦춘다.** "Hold one minute. Which three?" 에스컬레이션을 막지 않고 정보를 하나 요구하면 1분을 벌 수 있다.
2. **신호와 상태를 가른다.** "a sleeping service and a stopped one look identical" 관측이 상태를 결정하지 않는다는 점을 한 문장으로 말한다.
3. **사고가 없어도 버그는 잡는다.** "there's no incident, but there is a bug" 야간 오경보를 낭비가 아니라 페이지 개선으로 끝맺는다.

## Expressions
| page the on-call | 온콜을 호출하다 |
| hold one minute | 1분만 기다려라 |
| scale to zero | 0으로 스케일되다 |
| look identical from outside | 밖에서는 똑같이 보인다 |
| see if it wakes | 깨어나는지 봐라 |
| cold start | 콜드 스타트 |
| no incident, but a bug | 사고는 없지만 버그는 있다 |
| the wrong word for | ~의 잘못된 표현 |
| label the state honestly | 상태를 정직하게 표기하라 |
| leave paging to real signals | 호출은 진짜 신호에 맡겨라 |
