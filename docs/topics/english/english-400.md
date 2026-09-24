# 400 · Grammar — might be ~ing, would: one case, not a guess
title_ko: might be ~ing … would — 추측이 아니라 "가령"
situation: In a design review Jay keeps reaching for "For example, let's say a user uploads a large file…" and it lands flat every time — too many words before the point, and the conditional makes it sound like he is unsure the case exists. Reading Toni Morrison's Beloved the night before, he hits a sentence that does the same job in one move: `She might be hurrying across a field… Nothing else would be in her mind.` It is not a guess about Sethe. It is one representative instance, narrated. Jay wants that move in his own English.
situation_ko: 디자인 리뷰에서 Jay는 자꾸 "For example, let's say a user uploads a large file…"로 시작하는데 매번 힘이 빠진다. 요점까지 말이 너무 길고, 조건절 때문에 그런 경우가 있는지조차 확신이 없어 보인다. 전날 밤 토니 모리슨의 『빌러비드』를 읽다가 같은 일을 한 수로 해내는 문장을 만난다. `She might be hurrying across a field… Nothing else would be in her mind.` 세스에 대한 추측이 아니다. **대표적인 한 경우를 골라서 서술한 것**이다. Jay는 그 수를 자기 영어에 넣고 싶다.
why: The trap is reading `might` as 추측. Here it is not epistemic at all — Morrison is not wondering whether Sethe was in a field. She is picking one typical occasion and running it, and the giveaway is the `would` that follows: `might` sets the case up, `would` states what holds inside it. A real guess would stay in `might` or switch to `probably`. Once Jay sees the pair he can use it at work, where the same construction replaces the clumsy "let's say" frame and sounds like someone who has watched the system behave. Second point: `devious` with a non-human subject is not 교활한 — a devious brain is one that does not go straight, the same root as `deviate`.
why_ko: 함정은 `might`를 추측으로 읽는 것이다. 여기서는 인식적 추측이 전혀 아니다. 모리슨은 세스가 들판에 있었는지 궁금해하고 있지 않다. **전형적인 경우 하나를 골라 굴리고 있고**, 표지는 뒤따르는 `would`다. `might`가 상황을 세우고 `would`가 그 안에서 성립하는 것을 진술한다. 진짜 추측이라면 `might`에 머물거나 `probably`로 바꿨을 것이다. 이 짝이 보이면 회사에서 쓸 수 있다. 어설픈 "let's say" 틀을 대체하고, **시스템이 그렇게 움직이는 걸 실제로 본 사람처럼** 들린다. 두 번째 요점: 사람이 아닌 주어의 `devious`는 교활한이 아니다. **곧장 가지 않는** 머리라는 뜻이고, `deviate`와 같은 어원이다.
status: new
added: 2026-09-25
source: Toni Morrison, *Beloved* (Alfred A. Knopf, 1987) — three sentences quoted for commentary on the grammar, kept short and attributed; the novel's text is not otherwise reproduced here. The grammatical reading of `might … would` as exemplification, and the argument for adding "가령" in Korean, were pasted by jay on 2026-09-25 from another assistant and are that assistant's, not mine. What this item adds is the name for the move, the `would` diagnostic, and the transfer to working English. I did not check the quotation against a copy of the novel, and I have not read the sentences that follow it — which the pasted explanation itself says would settle why `might` was chosen. That stays open.
source_ko: 토니 모리슨, 『빌러비드』(Alfred A. Knopf, 1987) — 문법 논평을 위해 세 문장을 짧게 인용하고 출처를 밝혔다. 소설 본문은 그 외에 이 저장소에 옮기지 않았다. `might … would`를 예시로 읽는 문법 해석과 한국어에 "가령"을 넣자는 논거는 jay가 2026-09-25에 다른 어시스턴트에게서 받아 붙여넣은 것이고 **그쪽의 것이지 내 것이 아니다.** 이 항목이 더한 것은 그 수의 이름, `would` 진단법, 그리고 실무 영어로의 이전이다. 인용문을 소설 원본과 대조하지 않았고, 뒤따르는 문장들도 읽지 않았다 — 붙여넣은 설명 자신이 그것이 `might`가 쓰인 이유를 확정해줄 거라고 말한 부분이다. **열린 채로 둔다.**
raw: 2026-09-25-english-400.md

## Dialogue
Hana: Walk me through the failure. Start with when it actually happens.
> 실패 경로를 설명해줘. 실제로 언제 일어나는지부터.
Jay: A user might be uploading a two-gigabyte export over hotel wifi, with the tab in the background. Nothing else would be competing for that socket.
> 사용자가 호텔 와이파이로 2기가짜리 내보내기 파일을 올리고 있다고 하자. 탭은 백그라운드에 있고. 그 소켓을 두고 경쟁하는 건 아무것도 없을 거야.
Hana: So the connection looks idle to the proxy.
> 그럼 프록시 입장에서는 연결이 놀고 있는 것처럼 보이겠네.
Jay: It does. The proxy would reap it at sixty seconds, the client would retry from zero, and the user would watch the bar reset for the third time.
> 그래. 프록시는 60초에 그걸 회수하고, 클라이언트는 처음부터 다시 시도하고, 사용자는 진행 바가 세 번째로 초기화되는 걸 보게 되는 거지.
Hana: Is that hypothetical or did you see it?
> 그거 가정이야, 아니면 본 거야?
Jay: I watched it happen twice last week. I'm describing the typical case, not guessing at one.
> 지난주에 두 번 봤어. **추측하는 게 아니라 전형적인 경우를 서술하는 거야.**
Hana: Good — say that next time. "I'm describing the typical case" is worth ten minutes of argument.
> 좋네 — 다음엔 그렇게 말해. "전형적인 경우를 서술하는 중"이라는 한마디가 10분짜리 논쟁을 아껴줘.

## Techniques
1. **`might be ~ing`는 추측이 아니라 예시일 수 있다.** 모리슨의 `She might be hurrying across a field`는 세스가 들판에 있었는지에 대한 의문이 아니다. **전형적인 경우 하나를 골라 그 안으로 들어간 것**이다. 한국어로는 "~하고 있을 수도 있었다"가 아니라 **"가령 ~하고 있다고 하자"** 또는 **"~하고 있을 때면"** 이 맞는다.
2. **표지는 뒤따르는 `would`다.** `Nothing else would be in her mind.` 진짜 추측이라면 `might`에 머물거나 `probably`로 갔을 것이다. **`might`가 무대를 세우고 `would`가 그 무대 위에서 성립하는 것을 말한다.** 이 짝이 보이면 문장 전체의 성격이 정해진다. 회의에서도 같은 짝을 쓰면 된다. "A user **might be** uploading… Nothing else **would be** competing."
3. **회의에서 "For example, let's say…"를 버려라.** 요점까지 단어가 너무 많고, 조건절이 **그런 경우가 실제로 있는지조차 모른다는 인상**을 준다. `might be ~ing … would`로 바로 들어가면 짧고, **그 장면을 본 사람처럼 들린다.** 진짜로 봤다면 한 줄 덧붙여라. "I'm describing the typical case, not guessing at one."
4. **사람이 아닌 주어의 `devious`는 교활한이 아니다.** `her brain was devious`는 **곧장 가지 않고 옆길로 새는** 머리라는 뜻이고, `deviate`(벗어나다)와 같은 어원이다. 사람에게 쓰면 교활한이 맞지만 brain, route, path, argument 같은 주어에는 **"에두르는, 빙 도는"** 이다.

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| might be ~ing … would … | 가령 ~하고 있다고 하자, 그러면 ~할 것이다 — 추측이 아니라 **전형적인 한 경우를 세우는** 짝 |
| I'm describing the typical case | 전형적인 경우를 서술하는 겁니다 — 가정이냐고 물을 때의 답. **추측과 선을 긋는 한마디** |
| not guessing at one | 추측하는 게 아니라 — 위 문장 뒤에 붙여 대비를 세운다 |
| Is that hypothetical or did you see it? | 그거 가정이에요, 본 거예요? — 리뷰에서 상대가 던지는 표준 질문. 미리 답을 준비해둘 것 |
| to run a case | 한 경우를 굴려보다 — 시나리오를 처음부터 끝까지 따라가는 것 |
| a representative instance | 대표적인 한 사례 — "하나만 예로 들면"의 격식 있는 표현 |
| a devious route | 에두르는 경로 — 사람이 아닌 주어에서는 교활함이 아니라 **곧장 가지 않음** |
| to deviate from | ~에서 벗어나다 — `devious`와 같은 어원 |
| practically (= almost) | 거의 — `running practically`는 "실질적으로"가 아니라 **"거의 뛰다시피"** |
| to reap a connection | 연결을 회수하다 — 유휴 연결을 서버가 끊는 것 |
| to compete for a socket | 소켓을 두고 경쟁하다 — 같은 연결을 여러 요청이 쓰려 할 때 |
| to retry from zero | 처음부터 다시 시도하다 — 이어받기가 없을 때 |
| to watch the bar reset | 진행 바가 초기화되는 걸 보다 — 사용자 입장에서의 증상 |
| to land flat | (말이) 힘없이 떨어지다 — 설명이 먹히지 않을 때 |
| worth ten minutes of argument | 10분짜리 논쟁을 아껴주는 — 한마디의 값을 매길 때 |

## Words
| devious | /ˈdiviəs/ | (사람) 교활한 / (길·생각) 곧장 가지 않는, 에두르는 |
| to deviate | /ˈdiviˌeɪt/ | (경로·기준에서) 벗어나다 |
| sap | /sæp/ | (식물의) 수액, 즙 |
| chamomile | /ˈkæməˌmaɪl/ | 캐모마일 (국화과 허브) |
| to rinse | /rɪns/ | 헹구다, 씻어내다 |
| practically | /ˈpræktɪkli/ | 거의 (= almost); "실질적으로"의 뜻도 있으니 문맥으로 가른다 |
| hypothetical | /ˌhaɪpəˈθɛtɪkəl/ | 가정의, 가설적인 |
| epistemic | /ˌɛpɪˈstimɪk/ | 인식적인 — 화자가 얼마나 확신하는가에 관한 |
| to exemplify | /ɪɡˈzɛmpləˌfaɪ/ | 예시하다, 전형적으로 보여주다 |
| a tell | /tɛl/ | (숨기려 해도 드러나는) 표지, 단서 |
| representative | /ˌrɛprɪˈzɛntətɪv/ | 대표적인 |
| an instance | /ˈɪnstəns/ | 사례, 한 경우 |
| to reap | /rip/ | 거둬들이다 — 서버가 유휴 연결을 회수할 때도 씀 |
| intrusive | /ɪnˈtrusɪv/ | 침입하는 — 기억이 불쑥 밀고 들어올 때 |
