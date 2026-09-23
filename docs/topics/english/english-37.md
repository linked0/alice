# 37 · Interview — Start with the latency budget, then the fail-safe
title_ko: 지연 예산부터, 그다음 안전장치
situation: Final-round system-design interview at a Zurich medtech company building remote-operated devices. The interviewer, Anneke, asks Jay to sketch how he would run a control loop between a console in one city and a robot 500 km away, over a link he does not fully control. Whiteboard, twenty minutes.
situation_ko: 원격 조작 장비를 만드는 취리히 메드테크 회사의 최종 시스템 설계 면접. 면접관 Anneke가 한 도시의 콘솔과 500km 떨어진 로봇 사이의 제어 루프를, 완전히 통제할 수 없는 링크 위에서 어떻게 운영할지 스케치해 달라고 한다. 화이트보드, 20분.
why: A remote-control design lives or dies on two numbers and one person: the end-to-end latency budget, the tail of that latency, and who takes over when the link fails. Saying those three things first, before drawing boxes, is what separates a senior answer from a diagram.
why_ko: 원격 제어 설계는 두 숫자와 한 사람에 달려 있다. 종단 간 지연 예산, 그 지연의 꼬리, 그리고 링크가 끊길 때 넘겨받을 사람. 상자를 그리기 전에 이 셋을 먼저 말하는 것이 시니어의 답과 다이어그램을 가른다.
status: important

## Dialogue
Anneke: Console here, robot 500 kilometres away, a link you rent rather than own. Where do you start?
> 콘솔은 여기, 로봇은 500킬로미터 밖, 링크는 소유가 아니라 임대. 어디서 시작하시겠어요?
Jay: With the budget, not the boxes. Light covers 500 kilometres in under three milliseconds, so distance is not the problem. The loop is: capture, encode, transport, decode, render, the surgeon's reaction, then the command back and the actuator. I would set a budget of around 150 milliseconds end to end and allocate it across those stages before choosing any component.
> 상자가 아니라 예산부터요. 빛은 500킬로미터를 3밀리초 안에 가니 거리는 문제가 아닙니다. 루프는 캡처, 인코딩, 전송, 디코딩, 렌더, 집도의의 반응, 그다음 명령의 복귀와 액추에이터입니다. 종단 간 150밀리초 정도로 예산을 정하고, 부품을 고르기 전에 단계별로 배분하겠습니다.
Anneke: Why 150?
> 왜 150이죠?
Jay: It is the band where published telesurgery cases still report direct-feeling control. The Japanese Starlink trial ran at about 130. Above 200, operators start to lead their movements. I would treat 150 as the mean target and then ask the question that matters more: what does the 99th percentile look like?
> 공개된 원격수술 사례들이 아직 직접 조작하는 느낌이라고 보고하는 구간입니다. 일본의 Starlink 시험은 약 130이었어요. 200을 넘으면 조작자가 움직임을 앞질러 예측하기 시작합니다. 150을 평균 목표로 두고, 더 중요한 질문을 하겠습니다. 99번째 백분위수는 어떤가요?
Anneke: Suppose the link is satellite. Mean 40, but it spikes.
> 링크가 위성이라고 해 보죠. 평균 40인데 튄다면요?
Jay: Then the mean is fine and the spikes are the design. Three things. A jitter buffer sized to the p99, so the video is steady even when the network is not. A dead-man rule: if the command stream is silent for more than, say, 300 milliseconds, the robot holds position, it does not complete the last motion. And a hard floor: below a measured link quality, the console loses authority and cannot get it back until the link has been stable for a full minute.
> 그럼 평균은 괜찮고 스파이크가 설계 대상입니다. 셋입니다. p99에 맞춘 지터 버퍼, 네트워크가 흔들려도 영상은 안정되게. 데드맨 규칙, 명령 스트림이 예컨대 300밀리초 이상 침묵하면 로봇은 마지막 동작을 마치지 않고 자세를 유지합니다. 그리고 하한선, 측정된 링크 품질이 기준 아래면 콘솔은 권한을 잃고 링크가 1분 내내 안정되기 전까지 되찾지 못합니다.
Anneke: Who has authority when the console loses it?
> 콘솔이 권한을 잃으면 누가 갖죠?
Jay: The person standing next to the patient. This is the part I would put on the slide before any architecture: there is a qualified surgeon in the room in Abuja, and the system is designed so that handing over to them is one action, not a negotiation. Remote control is a privilege the link grants and the room can revoke.
> 환자 옆에 서 있는 사람입니다. 어떤 아키텍처보다 먼저 슬라이드에 올릴 부분이에요. Abuja의 수술실에 자격 있는 외과의가 있고, 그에게 넘기는 것이 협상이 아니라 한 동작이 되게 설계합니다. 원격 조작은 링크가 부여하고 수술실이 회수할 수 있는 특권입니다.
Anneke: You have not drawn anything yet.
> 아직 아무것도 안 그리셨네요.
Jay: On purpose. If we agree on 150, the p99 rule and the handover, the boxes almost draw themselves. If we do not, the boxes will be wrong however neat they are.
> 의도적입니다. 150, p99 규칙, 인수인계에 합의하면 상자는 거의 저절로 그려집니다. 합의하지 않으면 아무리 깔끔해도 상자는 틀립니다.

## Techniques
1. **숫자를 먼저 걸고 근거를 짧게 댄다.** "I would set a budget of around 150 milliseconds… It is the band where published cases still report direct-feeling control." 숫자 뒤에 한 문장 근거를 붙이면 자신감이 아니라 준비로 읽힌다.
2. **평균을 인정하고 꼬리로 옮긴다.** "Then the mean is fine and the spikes are the design." 반박이 아니라 초점 이동. Eng #35와 같은 수.
3. **사람을 아키텍처보다 먼저 놓는다.** "The person standing next to the patient." 안전장치를 사람으로 말하면 설계가 책임을 알고 있다고 들린다.






## Words
| revoke | /rɪˈvoʊk/ | 링크가 주고 수술실이 회수할 수 있는 특권 |
| allocate | /ˈæləˌkeɪt/ | 그 단계들에 배분하다 |
| spikes | /spaɪks/ | 평균은 괜찮고 스파이크가 설계 대상이다 |
| buffer | /ˈbʌfɚ/ | p99에 맞춘 지터 버퍼 |
| negotiation | /nɪˌɡoʊʃiˈeɪʃən/ | 협상이 아니라 한 동작 |

## Expressions
| the budget, not the boxes | 상자(구성 요소)가 아니라 예산부터 |
| allocate it across those stages | 그 단계들에 배분하다 |
| the band where … still report | ~라고 아직 보고되는 구간 |
| operators start to lead their movements | 조작자가 움직임을 앞질러 예측하기 시작한다 |
| the mean is fine and the spikes are the design | 평균은 괜찮고 스파이크가 설계 대상이다 |
| a jitter buffer sized to the p99 | p99에 맞춘 지터 버퍼 |
| a dead-man rule | 데드맨 규칙(신호가 끊기면 안전 상태로) |
| holds position | 자세를 유지한다(동작을 멈춘다) |
| loses authority | 권한을 잃는다 |
| one action, not a negotiation | 협상이 아니라 한 동작 |
| a privilege the link grants and the room can revoke | 링크가 주고 수술실이 회수할 수 있는 특권 |
| the boxes almost draw themselves | 상자가 거의 저절로 그려진다 |
