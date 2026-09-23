# 1 · Review — The function is fine. Who can call it?
title_ko: 함수는 괜찮다. 누가 호출하나?
situation: Priya's PR adds an admin pause to Verex settlement. The feature is needed; the PR never says who holds the switch or what turns it back on.
situation_ko: Priya의 PR이 Verex 정산에 관리자 일시정지를 추가한다. 기능은 필요하지만, 누가 스위치를 쥐는지와 무엇이 다시 켜는지가 PR에 없다.
why: The most useful review move in this genre: agree with the feature in two words, then ask for the paperwork without sounding like a block.
why_ko: 이 장르에서 가장 유용한 리뷰 기술. 두 단어로 기능에 동의한 뒤, 막는 것처럼 들리지 않게 문서를 요구한다.
status: done
dones: 2026-09-18T15:08+09:00, 2026-09-21T09:30:00+09:00, 2026-09-23T11:06:00+09:00
done: 2026-09-23T11:06:00+09:00

## Dialogue
Priya: This adds a pause so we can stop settlement if the oracle goes bad. I think it's uncontroversial.
> 오라클이 이상해지면 정산을 멈출 수 있게 일시정지를 추가했습니다. 논란의 여지가 없다고 봅니다.
Jay: The function is. What I can't find in the PR is who can call it, and what un-pauses it.
> 함수는 그렇습니다. PR에서 못 찾는 건 누가 호출할 수 있고 무엇이 해제하는가예요.
Priya: Owner only, for now. We'd un-pause by hand once we've looked.
> 지금은 오너만이요. 확인한 뒤 수동으로 풀 겁니다.
Jay: Reasonable start. I'd want those two sentences somewhere that isn't a code comment. "For now" and "by hand" are what an auditor asks about, not the modifier.
> 합리적인 출발입니다. 그 두 문장을 코드 주석이 아닌 곳에 두고 싶어요. 감사자가 묻는 건 modifier가 아니라 "지금은"과 "수동으로"거든요.
Priya: Where, then?
> 그럼 어디에요?
Jay: A three-column table in the repo: what a human can do, who and how, when we give it up. Even TBD in the third column beats the column not existing.
> 레포에 세 열짜리 표요. 사람이 할 수 있는 것, 누가 어떻게, 언제 내려놓는가. 세 번째 열이 미정이어도 열이 없는 것보다 낫습니다.
Priya: It'll be TBD for everything today.
> 오늘은 전부 미정일 텐데요.
Jay: That's honest. A table full of TBDs is a roadmap. A missing table is a question we answer under pressure later.
> 그게 정직한 거죠. 미정으로 가득한 표는 로드맵이고, 없는 표는 나중에 압박 속에서 답할 질문입니다.

## Techniques
1. **기능과 문서를 갈라서 말한다.** "The function is. What I can't find is…" 첫 두 단어로 기능에 동의한다고 못 박으면 뒤의 요구가 반대로 들리지 않는다.
2. **제3자의 눈으로 번역한다.** "what an auditor asks about" 상대가 사소하게 본 단어가 왜 중요한지 제3자 기준으로 말하면 취향 싸움이 되지 않는다.
3. **빈칸을 허용해 문턱을 낮춘다.** "Even TBD beats the column not existing." 완성도를 요구하면 아무도 시작하지 않는다. 표가 생기면 채워진다.
4. **생략으로 대비를 만든다 — `…, not X` 와 `The function is.`** 이 대화는 같은 생략을 두 번 쓴다. `"The function is."` 는 `"The function is uncontroversial."` 의 줄임이고, `"…what an auditor asks about, not the modifier."` 는 `"the modifier is not what an auditor asks about"` 의 줄임이다. 앞 문장의 구조를 반복하지 않고 쉼표 + `not X` 로 끝내면 대비가 날카로워지고, 동의가 마지못한 것이 아니라 확신 있게 들린다. `Bring the report, not the slides.` / `It's the timing that worries me, not the price.` 와 같은 형태다.





## Words
| modifier | /ˈmɑdəfaɪər/ | 영어 단어가 아니라 **Solidity 키워드**. 함수에 붙여 호출 자격을 검사하는 재사용 가능한 가드 — `function pause() external onlyOwner`. 여기서 "the modifier"는 `onlyOwner` 그 자체를 가리킨다 |
| onlyOwner | /ˈoʊnli ˈoʊnər/ | 가장 흔한 modifier 이름. "Owner only, for now" 중 **"Owner only" 부분이 곧 modifier**이고, 감사자가 묻지 않는 쪽이다 |
| guard | /ɡɑrd/ | (코드에서) 조건이 맞지 않으면 실행을 막는 장치 — "a modifier is a reusable guard" |
| to pause | /pɔz/ | 일시정지시키다 · **to un-pause** /ʌnˈpɔz/ 는 그것을 해제하다. 하이픈이 붙는 즉석 조어이고, 회의에서 그대로 쓴다 |
| settlement | /ˈsɛtl̩mənt/ | 정산, 결제의 최종 처리 — "stop settlement if the oracle goes bad" |
| oracle | /ˈɔrəkl̩/ | 외부 데이터를 체인에 넣어 주는 장치 — 강세는 앞(OR-a-cle) |
| to go bad | /ɡoʊ ˈbæd/ | (장비·데이터가) 맛이 가다, 망가지다 — 음식에 쓰는 말을 시스템에 쓴 것이라 가볍고 구어적이다 |
| auditor | /ˈɔdɪtər/ | 감사자 — 강세는 앞(AU-di-tor). 여기서는 제3자의 시선을 대표하는 인물 |
| uncontroversial | /ˌʌnkɑntrəˈvɜrʃl̩/ | 논란의 여지가 없는 — 강세는 VER에(un-con-tro-VER-sial). 여섯 음절이라 끊어 연습할 것 |
| TBD | /ˌti bi ˈdi/ | to be determined, 미정 — 세 글자를 따로 읽고 강세는 마지막 D |
| to give something up | /ɡɪv ˈʌp/ | (권한을) 내려놓다 — "when we give it up". 포기하다보다 "쥐고 있던 것을 넘기다"에 가깝다 |
| roadmap | /ˈroʊdmæp/ | 앞으로의 계획표 — 한 단어 |
| under pressure | /ˈprɛʃər/ | 압박 속에서 — "answer it under pressure later". pressure의 ss는 /ʃ/ 소리 |
| elliptical | /ɪˈlɪptɪkl̩/ | (말이) 생략된 — 듣는 사람이 복원할 수 있는 말을 빼는 것. 기법 4의 이름 |

## Expressions
| it's uncontroversial | 논란의 여지가 없다 |
| who can call it | 누가 호출할 수 있나 |
| what un-pauses it | 무엇이 해제하나 |
| owner only, for now | 지금은 오너만 |
| a reasonable start | 합리적인 출발점 |
| somewhere that isn't a code comment | 코드 주석이 아닌 어딘가에 |
| when we give it up | 언제 내려놓는가 |
| TBD (to be determined) | 미정 |
| beats the column not existing | 열이 없는 것보다 낫다 |
| answer it under pressure later | 나중에 압박 속에서 답하다 |
| not the modifier | modifier가 아니라 · 앞 문장 전체를 반복하지 않고 쉼표 + not X 로 대비를 끝내는 형태 |
| the function is | (그 말은) 함수에 대해서는 맞다 · uncontroversial을 생략한 동의. 두 단어로 동의하고 바로 본론으로 간다 |
| bring the report, not the slides | 슬라이드 말고 보고서를 가져와 · 같은 생략 구조를 연습할 예문 |
| it's the timing that worries me, not the price | 걱정되는 건 가격이 아니라 타이밍이다 · it's X that … 강조 구문 + not Y 꼬리 |
| who holds the switch | 누가 그 스위치를 쥐고 있나 · 권한의 소재를 묻는 가장 짧은 형태 |
| what an auditor asks about | 감사자가 묻는 것 · 취향 싸움을 제3자 기준으로 바꾸는 장치 |
| it's already in the code | 그건 이미 코드에 있다 · 검증 가능한 쪽과 약속뿐인 쪽을 가르는 말 |
| a promise, not a control | 강제되지 않는 약속일 뿐 · 보안·감사 대화의 핵심 대비 |
| the easy half | 쉬운 절반 · 이미 풀린 쪽을 짚어 어려운 쪽을 드러낼 때 |
| when do you stop being able to | 언제부터 그럴 수 없게 되나 · 권한의 종료 시점을 묻는 문장 |
