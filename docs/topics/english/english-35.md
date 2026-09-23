# 35 · Interview — The mean is fine. Which percentile hurts?
title_ko: 평균은 괜찮아요. 어느 백분위수가 아픈가요?
situation: System-design interview for a staff engineer role at a Berlin payments company. The interviewer, Lena, describes a notification service whose dashboard shows 40 ms average latency and asks Jay what he would check first. Jay has ten minutes and a whiteboard.
situation_ko: 베를린 결제 회사의 스태프 엔지니어 시스템 설계 면접. 면접관 Lena가 대시보드에 평균 지연 40ms가 찍히는 알림 서비스를 설명하고 무엇을 먼저 확인할지 묻는다. Jay에게는 10분과 화이트보드가 있다.
why: The strongest system-design answers start by rejecting the metric on the table and naming the one that matters. Doing it without sounding like a know-it-all is the skill: ask for the number, explain why it decides the user's experience, then propose the smallest change that would show it.
why_ko: 가장 강한 시스템 설계 답은 테이블 위의 지표를 거부하고 중요한 지표를 이름 붙이는 데서 시작한다. 아는 척으로 들리지 않게 하는 것이 기술이다. 숫자를 요청하고, 그것이 왜 사용자 경험을 결정하는지 설명하고, 그것을 보여 줄 가장 작은 변경을 제안한다.
status: important

## Dialogue
Lena: Average latency is 40 milliseconds and the error rate is under 0.1 percent. Users still complain that payment confirmations arrive late. Where would you start?
> 평균 지연은 40밀리초, 에러율은 0.1퍼센트 미만입니다. 그런데도 사용자는 결제 확인이 늦게 온다고 불평해요. 어디서 시작하시겠어요?
Jay: With a different number. The mean is fine; I would ask for the p99, and the p99 per region. A confirmation that arrives at 40 milliseconds ninety-nine times and at four seconds once is a service that feels slow, because the one is what people remember.
> 다른 숫자로요. 평균은 괜찮습니다. p99, 그리고 지역별 p99를 요청하겠습니다. 아흔아홉 번은 40밀리초에, 한 번은 4초에 오는 확인은 느리게 느껴지는 서비스예요. 사람들이 기억하는 건 그 한 번이니까요.
Lena: Suppose the p99 is 3.8 seconds. What is your hypothesis?
> p99가 3.8초라고 해 보죠. 가설은요?
Jay: Two candidates, and I would check them in this order. First, a queue somewhere is serving in arrival order, so a burst of large payloads, say end-of-day statements, sits in front of the small confirmations. Second, a downstream call with a retry and a fixed timeout, where the timeout is the 3.8 seconds. Both show up as a flat shelf in the latency histogram rather than a smooth tail.
> 후보 둘이고, 이 순서로 확인하겠습니다. 첫째, 어딘가의 큐가 도착 순서대로 처리해서 큰 페이로드 묶음, 예컨대 일말 명세서가 작은 확인 앞에 앉아 있는 것. 둘째, 재시도와 고정 타임아웃이 있는 하위 호출로 그 타임아웃이 3.8초인 것. 둘 다 지연 히스토그램에서 부드러운 꼬리가 아니라 평평한 턱으로 나타납니다.
Lena: And if it is the queue?
> 큐라면요?
Jay: Then the fix is not more capacity, it is ordering. Give small messages their own lane, or serve by remaining size so a confirmation overtakes a statement. That is the same idea as receiver-driven transports in datacenters: let the side that can see the congestion decide who goes next.
> 그러면 해법은 용량 추가가 아니라 순서입니다. 작은 메시지에 별도 차선을 주거나, 남은 크기 순으로 처리해 확인이 명세서를 추월하게 하세요. 데이터센터의 수신자 주도 전송과 같은 아이디어예요. 혼잡을 볼 수 있는 쪽이 다음을 정하게 하는 것.
Lena: You are confident about the diagnosis before seeing the data.
> 데이터를 보기 전에 진단에 확신이 있으시네요.
Jay: Confident about the order of checks, not the answer. If the histogram has no shelf, I am wrong about both and I would look at GC pauses next. I would rather name my hypothesis and be corrected in ten minutes than be vague and right in a week.
> 답이 아니라 확인 순서에 확신이 있는 겁니다. 히스토그램에 턱이 없으면 둘 다 틀린 것이고, 다음엔 GC 멈춤을 보겠습니다. 일주일 뒤에 모호하게 맞는 것보다 10분 안에 가설을 말하고 교정받는 쪽이 낫습니다.
Lena: What would you put on the dashboard tomorrow?
> 내일 대시보드에 뭘 올리시겠어요?
Jay: p99 next to the mean, split by message size, with the SLO drawn as a line. If the team cannot see the tail, they will keep optimising the average, and the average is already fine.
> 평균 옆에 p99를, 메시지 크기별로 나누고, SLO를 선으로 그려서요. 팀이 꼬리를 볼 수 없으면 계속 평균을 최적화할 텐데, 평균은 이미 괜찮으니까요.

## Techniques
1. **지표를 거부하되 대안을 즉시 이름 붙인다.** "The mean is fine; I would ask for the p99." 반박이 아니라 더 좋은 질문으로 들린다.
2. **가설을 순서와 함께 말한다.** "Two candidates, and I would check them in this order." 확신의 대상을 답이 아니라 절차로 옮기면 틀려도 신뢰가 남는다.
3. **틀릴 조건을 먼저 말한다.** "If the histogram has no shelf, I am wrong about both." 면접관이 물기 전에 반증 조건을 내놓으면 자만이 아니라 엄밀함으로 읽힌다.



## Words
| mean is fine | /min ɪz faɪn/ | 평균은 괜찮다(문제는 다른 곳에 있다) |
| in this order | /ɪn ðɪs ˈɔrdɚ/ | 이 순서로 |
| own lane | /oʊn leɪn/ | 자기 차선(별도 처리 경로) |
| overtakes | /ˈoʊvɚˌteɪks/ | 추월한다 |

## Expressions
| the mean is fine | 평균은 괜찮다(문제는 다른 곳에 있다) |
| the one is what people remember | 그 한 번이 사람들이 기억하는 것이다 |
| in this order | 이 순서로 |
| sits in front of | ~의 앞에 앉아 있다(막고 있다) |
| a flat shelf in the histogram | 히스토그램의 평평한 턱(특정 값에 몰린 구간) |
| its own lane | 자기 차선(별도 처리 경로) |
| overtakes | 추월한다 |
| confident about the order of checks, not the answer | 답이 아니라 확인 순서에 확신이 있다 |
| I would rather … than … | …보다 …하는 쪽이 낫다 |
| drawn as a line | 선으로 그려진(기준선으로 표시된) |
| keep optimising the average | 계속 평균을 최적화하다 |
