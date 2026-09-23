# 162 · Line — Not wait — wrap. One module owns how an account authorizes a transaction, and everything else calls it.
title_ko: Not wait — wrap. One module owns how an account authorizes a transaction, and everything else calls it. — "wait"가 아니라 "wrap"; 승인 로직은 모듈 하나가 전담하고 나머지는 그걸 호출한다
situation: On a noisy architecture call, Ken hears "wait" when Jay says "wrap" and objects to added latency. Jay corrects the word and lays out the module boundary he wants for account authorization.
situation_ko: 소음이 심한 아키텍처 통화에서 Ken이 Jay의 "wrap"을 "wait"로 듣고 지연 시간이 늘어난다며 반대하기 시작한다. Jay는 단어를 세 음절로 바로잡고, 계정 승인에 대해 실제로 원하는 모듈 경계를 설명한다.
why: Two moves in one line. "Not wait — wrap" corrects a misheard word by setting the wrong one and the right one side by side; it is the fastest repair in conversation. Then **wrap** in architecture means putting scattered existing calls behind one abstraction, and "a module owns X" means that module holds all the logic and responsibility for X. "Everything else calls it" closes the boundary: no other code touches signers directly. Wrap is not "package" or "finish" here.
why_ko: 한 줄에 두 가지 동작이 들어 있다. "Not wait — wrap"은 잘못 들은 단어와 맞는 단어를 나란히 놓아 바로잡는 말로, 대화에서 가장 빠른 수정이며 아무도 기분 나빠하지 않는다. 그다음 아키텍처에서 **wrap**은 흩어진 기존 호출을 추상화 하나 뒤로 감싼다는 뜻이고, "a module owns X"는 그 모듈이 X의 로직과 책임을 전부 가진다는 뜻이다. "Everything else calls it"이 경계를 닫는다. 다른 코드는 서명자나 세션 키를 직접 건드리지 않는다. 여기서 wrap은 "포장하다"나 "마무리하다"가 아니다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, second export (2026-09-21), page 4 card 11 (sentence): Original "Not wait — wrap. I want one module that owns 'how an account authorizes a transaction,' and everything else calls it." / Korean "'wait'가 아니라 'wrap'이야. 계정이 트랜잭션을 어떻게 승인하는지에 대한 로직은 하나의 모듈이 전담하고, 나머지 모든 코드는 그 모듈을 호출하게 하고 싶어." The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 두 번째 내보내기(2026-09-21), 4페이지 11번 카드(문장): 원문 "Not wait — wrap. I want one module that owns …, and everything else calls it." / 번역 "'wait'가 아니라 'wrap'이야. 계정이 트랜잭션을 어떻게 승인하는지에 대한 로직은 하나의 모듈이 전담하고, 나머지 모든 코드는 그 모듈을 호출하게 하고 싶어." 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-79.txt

## Dialogue
Ken: If we wait on every authorization, we add latency to every call. I don't love that.
> 승인마다 기다리면 모든 호출에 지연이 붙어. 그건 별로야.
Jay: Not wait — wrap. I said wrap. One module owns how an account authorizes a transaction, and everything else calls it.
> wait가 아니라 wrap. wrap이라고 했어. 계정이 트랜잭션을 어떻게 승인하는지는 모듈 하나가 전담하고, 나머지는 전부 그걸 호출하는 거야.
Ken: Oh. Wrap the existing signer calls, you mean.
> 아. 기존 서명 호출을 감싸자는 거구나.
Jay: Right. Today the API, the scheduler, and the agent each talk to the signer and the session-key logic directly. I want one entry point, authorize(tx), and nobody else knows the details.
> 맞아. 지금은 API, 스케줄러, 에이전트가 각각 서명자와 세션 키 로직을 직접 건드리잖아. 진입점 하나, authorize(tx)만 두고 나머지는 세부 사항을 모르게 하고 싶어.
Ken: So if we add delegation later, it's one change.
> 그럼 나중에 위임을 추가해도 한 군데만 바꾸면 되겠네.
Jay: One change, in the module that owns it. That's the whole point.
> 한 군데, 그걸 전담하는 모듈에서. 그게 핵심이야.

## Techniques
1. **잘못 들은 단어는 "Not A — B"로 즉시 바로잡고 바로 본론으로 간다.** "Not wait — wrap. I said wrap." — 사과나 설명 없이 틀린 단어와 맞는 단어만 나란히 놓으면 충분하다.
2. **경계를 설명할 때는 "누가 소유하고 누가 호출하는가"로 말한다.** "One module owns … and everything else calls it." — 클래스 이름이 아니라 책임의 방향으로 구조를 전달한다.



## Words
| wrap | /ræp/ | 흩어진 호출을 추상화 하나 뒤로 감싸다 |
| module owns X | /ˈmɑdʒul oʊnz ɛks/ | 모듈 하나가 X의 로직과 책임을 전담한다 |

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| Not wait — wrap. | wait가 아니라 wrap — 잘못 들은 단어를 나란히 놓아 바로잡는 형식 |
| wrap | 흩어진 호출을 추상화 하나 뒤로 감싸다 — "Wrap the existing signer calls" |
| a module owns X | 모듈 하나가 X의 로직과 책임을 전담한다 — "One module owns how an account authorizes a transaction" |
| everything else calls it | 나머지 코드는 그 모듈을 통해서만 접근한다 — 경계를 닫는 말 |
