# 289 · Word — expletive
title_ko: expletive — (화나거나 아파서 내뱉는) 욕설
situation: In a code review the afternoon before a release, Jay finds a debug log line that a tired teammate left in with a swear word in the message. He has to ask for it to go without making a lecture out of it.
situation_ko: 릴리스 전날 오후 코드 리뷰에서, Jay는 지친 동료가 남겨 둔 디버그 로그 한 줄에 욕설이 섞여 있는 것을 발견한다. 설교처럼 들리지 않게 그 줄을 빼 달라고 말해야 한다.
why: An **expletive** is a swear word — the formal, journalistic label for one, as in "expletive deleted" or "he muttered an expletive under his breath". The word itself is perfectly polite, which is its whole use: you can report the swearing without repeating it. Grammar borrows the same term for a dummy subject like the "it" in "it is raining", so a style guide may mean something quite different by it.
why_ko: **expletive**는 욕설을 가리키는 격식 있는, 신문 기사 같은 말이다. "expletive deleted"(욕설 삭제), "he muttered an expletive under his breath"처럼 쓴다. 단어 자체는 점잖고, 바로 그 점이 쓸모다. 욕을 그대로 옮기지 않고도 욕이 있었다고 보고할 수 있다. 문법에서는 "it is raining"의 it 같은 허사를 같은 이름으로 부르기 때문에, 문체 안내서에서는 전혀 다른 뜻일 수 있다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, third export — the 전체 view (2026-09-21), card 114 of 228: "ex·ple·tive [ˈeksplətɪv] — 명사 (화가 나거나 아파서 내뱉는) 욕설" (옥스퍼드). The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장 세 번째 내보내기 — 전체 보기(2026-09-21), 228장 중 114번 카드: "ex·ple·tive [ˈeksplətɪv] — 명사 (화가 나거나 아파서 내뱉는) 욕설" (옥스퍼드). 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-183.txt

## Dialogue
Jay: Line 214 has an expletive in the log message. Could you take it out before we tag the release?
> 214번 줄 로그 메시지에 욕설이 하나 들어 있어. 릴리스 태그 달기 전에 빼 줄 수 있어?
Marek: Which word? I wrote that at two in the morning.
> 어느 단어? 새벽 두 시에 쓴 거라서.
Jay: I'd rather not type it into the review thread. That's why I said "an expletive".
> 리뷰 스레드에 그 단어를 치고 싶지는 않아. 그래서 "an expletive"라고 한 거야.
Marek: Fair. Does it really matter in a debug line?
> 그럴 만하네. 디버그 줄인데 그게 그렇게 문제야?
Jay: Support copies logs into tickets, and customers read the tickets. Anything shipped gets read by someone we haven't met.
> 지원팀이 로그를 티켓에 붙여 넣고, 고객이 그 티켓을 읽어. 나간 건 결국 우리가 모르는 사람이 읽게 돼.
Marek: Removing it now. Thanks for not quoting me.
> 지금 지울게. 그대로 인용 안 해 줘서 고마워.

## Techniques
1. **욕설을 옮기지 않고 보고하는 방법이 이 단어다.** "I'd rather not type it into the review thread. That's why I said 'an expletive'."
2. **사소해 보이는 지적에는 이유를 한 문장으로 붙인다.** "Anything shipped gets read by someone we haven't met." — 규칙이 아니라 결과로 설득한다.





## Words
| expletive | /ˈɛksplətɪv/ | 욕설 |
| deleted | /dɪˈlitəd/ | 욕설 삭제 |
| rather | /ˈræðɚ/ | ~하고 싶지는 않다 |

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| an expletive | 욕설 — 욕을 옮기지 않고 가리키는 격식어. "Line 214 has an expletive in the log message." |
| expletive deleted | 욕설 삭제 — 기사·기록에 쓰는 관용 표기 |
| take something out | ~을 빼다 — 코드 리뷰의 기본 요청 |
| I'd rather not ~ | ~하고 싶지는 않다 — 부드러운 거절 |
