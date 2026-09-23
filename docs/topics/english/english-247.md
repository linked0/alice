# 247 · Word — extrapolate
title_ko: extrapolate — (기존 데이터를 근거로) 추정[외삽]하다
situation: On a video call with a customer's infrastructure team, Jay is asked how the service will behave at ten times today's traffic. He only has a week of load-test data, and he wants to give a useful number while flagging how far the guess is stretched.
situation_ko: 고객사 인프라 팀과의 화상 회의에서 Jay는 트래픽이 지금의 열 배가 되면 서비스가 어떻게 될지 질문을 받는다. 가진 것은 일주일치 부하 테스트 데이터뿐이라, 쓸모 있는 숫자를 주되 그 추정이 얼마나 늘려 잡은 것인지도 함께 밝히려 한다.
why: To **extrapolate** is to take what you already measured and extend the pattern beyond it — from a week to a year, from 1,000 users to 100,000. It carries a built-in warning: the further you extrapolate, the weaker the claim, which is why English speakers say "if I extrapolate" or "extrapolating from a week of data" to stay honest. Do not confuse it with "interpolate", which is filling a gap inside the measured range, and do not use it to mean a simple guess with no data behind it.
why_ko: **extrapolate**는 이미 측정한 것을 그 범위 밖으로 연장해 추정하는 것이다. 일주일치로 1년을, 사용자 1,000명으로 10만 명을 말하는 식이다. 단어 자체에 경고가 들어 있어서, 멀리 연장할수록 주장은 약해진다. 그래서 영어 화자는 정직하게 "if I extrapolate", "extrapolating from a week of data"라고 단서를 붙인다. 측정 범위 안의 빈칸을 메우는 interpolate와 혼동하지 말고, 근거 없는 막연한 추측을 가리키는 데 쓰지도 말아야 한다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, third export — the 전체 view (2026-09-21), card 70 of 228: 옥스퍼드 영한사전 "extrapolate [ɪkˈstræpəleɪt] — 동사 (…을 기반으로) 추론[추정]하다". The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장 세 번째 내보내기 — 전체 보기(2026-09-21), 228장 중 70번 카드: 옥스퍼드 영한사전 "extrapolate [ɪkˈstræpəleɪt] — 동사 (…을 기반으로) 추론[추정]하다". 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-183.txt

## Dialogue
Ken: Give us a number. What happens at ten times the traffic?
> 숫자를 주세요. 트래픽이 열 배가 되면 어떻게 됩니까?
Jay: If I extrapolate from a week of load tests, the write path hits its limit around eight times. Beyond that I'm extrapolating well past what we measured.
> 일주일치 부하 테스트로 추정하면 쓰기 경로가 8배쯤에서 한계에 부딪힙니다. 그 이상은 측정한 범위를 한참 벗어난 추정이에요.
Ken: So eight is the honest answer.
> 그럼 정직한 답은 8배군요.
Jay: Eight is measured-ish. Ten is a curve I drew myself. Give me two weeks at double load and I'll replace the curve with data.
> 8배는 거의 측정값이고, 10배는 제가 그린 곡선입니다. 2배 부하로 2주만 주시면 그 곡선을 데이터로 바꿔 드리겠습니다.

## Techniques
1. **추정에는 근거의 범위를 붙인다.** "If I extrapolate from a week of load tests"처럼 from 뒤에 데이터의 크기를 밝히면 숫자의 신뢰도까지 함께 전달된다.
2. **측정값과 추정값을 말로 구분한다.** "Eight is measured-ish. Ten is a curve I drew myself" — 어디까지가 사실인지 선을 그으면 신뢰를 잃지 않고 숫자를 줄 수 있다.



## Words
| extrapolate from something | /ɛkˈstræpəˌleɪt frʌm ˈsʌmθɪŋ/ | ~을 근거로 범위 밖까지 추정하다 |
| write path | /raɪt pæθ/ | 쓰기 경로 |

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| extrapolate from something | ~을 근거로 범위 밖까지 추정하다 — 용량 산정·예측. "If I extrapolate from a week of load tests" |
| past what we measured | 측정한 범위를 벗어나서 — 추정의 한계를 밝힐 때 |
| the write path | 쓰기 경로 — 성능 병목을 지목할 때 |
