# 145 · Line — The outer handler may not see each failed attempt the way a reader expects.
title_ko: The outer handler may not see each failed attempt the way a reader expects. — 바깥 핸들러는 읽는 사람이 예상하는 대로 실패한 시도를 하나하나 보지 못할 수 있다
situation: Lena is reviewing Jay's PR that wraps an API call in a retry helper. The outer try/catch looks like it covers the whole operation, yet the log shows one failure after three actual attempts. She asks whether that is a bug; Jay explains where the retries really happen and agrees to write the reasoning into the PR.
situation_ko: Lena가 API 호출을 재시도 헬퍼로 감싼 Jay의 PR을 리뷰한다. 바깥 try/catch가 전체 작업을 덮는 것처럼 보이는데, 실제로 세 번 실패했는데도 로그에는 실패 하나만 찍힌다. 버그냐고 묻자 Jay는 재시도가 실제로 어디서 일어나는지 설명하고 그 이유를 PR에 적기로 한다.
why: The line is the core claim of a paragraph Jay wrote about retry behaviour: an outer try/handler may look as if it **encompasses** the operation, but the retries can run inside another callback, task, or control-flow boundary, and if the exception is caught or transformed there, the outer handler never sees the individual attempts. "The way a reader expects" names the gap between what the code looks like and what it does, and "may not" keeps it hedged rather than accusatory. The original was correct but dense ("in the way someone reading the surrounding code would expect"); the shorter form says the same. The practical move is to record that reasoning in the PR so future reviewers get the architectural context, not merely the final code.
why_ko: 이 문장은 Jay가 재시도 동작에 대해 쓴 단락의 핵심 주장이다. 바깥 try/handler가 작업 전체를 **encompass**하는 것처럼 보여도 실제 재시도는 다른 콜백, 태스크, 제어 흐름 경계 안에서 일어날 수 있고, 예외가 거기서 잡히거나 변환되면 바깥 핸들러는 개별 시도를 보지 못한다. "the way a reader expects"는 코드가 보이는 모습과 실제 동작 사이의 간극을 가리키고, "may not"은 비난이 아니라 기술적 가능성으로 톤을 유지한다. 원문은 정확하지만 길었고("in the way someone reading the surrounding code would expect"), 짧은 판도 같은 뜻이다. 실전 요령은 그 이유를 PR에 기록해서 나중 리뷰어가 최종 코드만이 아니라 아키텍처 맥락을 얻게 하는 것이다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, second export (2026-09-21), page 4 card 1 (sentence): Original "…the outer handler may not see each failed attempt in the way someone reading the surrounding code would expect. Recording that reasoning in the PR gives future reviewers the missing architectural context…", Corrected unchanged, Level 10/10, notes on encompass and control-flow boundary. The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 두 번째 내보내기(2026-09-21), 4페이지 카드 1(문장): 원문 "…the outer handler may not see each failed attempt in the way someone reading the surrounding code would expect…", 수정 없음, Level 10/10, encompass와 control-flow boundary 해설. 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-79.txt

## Dialogue
Lena: Your outer try/catch wraps the whole call, so why does the log show one failure when the API actually failed three times?
> 바깥 try/catch가 호출 전체를 감싸는데, API는 실제로 세 번 실패했는데 왜 로그엔 실패가 하나만 찍혀?
Jay: Because the retries happen inside the client library, across a different control-flow boundary. The outer handler may not see each failed attempt the way a reader expects; it only sees the last one.
> 재시도가 클라이언트 라이브러리 안에서, 다른 제어 흐름 경계 너머에서 일어나기 때문이야. 바깥 핸들러는 읽는 사람이 예상하는 대로 실패한 시도를 하나하나 보지 못할 수 있어. 마지막 것만 보지.
Lena: So the outer block looks like it encompasses the operation, but it doesn't.
> 그러니까 바깥 블록이 작업 전체를 감싸는 것처럼 보이지만 실제로는 아니라는 거네.
Jay: Right. The exceptions are caught and transformed inside the retry loop before they reach us. I'll document that reasoning in the PR so the next reviewer gets the architectural context, not just the final code.
> 맞아. 예외가 우리한테 오기 전에 재시도 루프 안에서 잡히고 변환돼. 다음 리뷰어가 최종 코드만이 아니라 아키텍처 맥락을 얻도록 그 이유를 PR에 적어 둘게.
Lena: Please do. I'd have flagged it as a bug otherwise.
> 그렇게 해 줘. 안 그랬으면 버그로 표시했을 거야.
Jay: That reaction is exactly why it's worth writing down.
> 그 반응이 바로 적어 둘 가치가 있는 이유야.

## Techniques
1. **"보이는 것"과 "실제"를 한 문장에 나란히 놓는다.** "looks like it encompasses the operation, but it doesn't" — 리뷰어의 오해를 부정하지 않고 오해가 생기는 이유를 먼저 말한다.
2. **설명으로 끝내지 않고 기록을 약속한다.** "I'll document that reasoning in the PR" — 코드 선택만이 아니라 이유를 남기겠다는 말이 리뷰를 닫는다.



## Words
| encompass | /ɛnˈkʌmpəs/ | 완전히 포함하다, 감싸다 |
| outer | /ˈaʊtɚ/ | 바깥 핸들러가 실패한 시도를 하나하나 못 볼 수 있다 |
| handler | /ˈhændlɚ/ | 바깥 핸들러가 실패한 시도를 하나하나 못 볼 수 있다 |
| failed | /feɪld/ | 바깥 핸들러가 실패한 시도를 하나하나 못 볼 수 있다 |
| attempt | /əˈtɛmpt/ | 바깥 핸들러가 실패한 시도를 하나하나 못 볼 수 있다 |
| boundary | /ˈbaʊndɚi/ | 제어 흐름 경계 |

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| the outer handler may not see each failed attempt | 바깥 핸들러가 실패한 시도를 하나하나 못 볼 수 있다 — 재시도가 안쪽에서 일어날 때 |
| encompass | 완전히 포함하다, 감싸다 — "looks like it encompasses the operation" |
| control-flow boundary | 제어 흐름 경계 — 콜백·태스크·추상화 계층으로 실행이 넘어가는 지점 |
| document the reasoning in the PR | 이유를 PR에 기록하다 — 최종 코드만이 아니라 왜 그렇게 했는지 |
