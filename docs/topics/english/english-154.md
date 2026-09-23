# 154 · Line — Building is a one-way door on our time; adopting is a two-way door on our stack.
title_ko: Building is a one-way door on our time; adopting is a two-way door on our stack. — 직접 만드는 건 시간에서 되돌릴 수 없는 문, 도입하는 건 스택에서 되돌릴 수 있는 문
situation: Marek would rather build the team's workflow engine in house than take on a dependency. Jay argues the opposite in a design meeting: the dependency could be removed in a week because the business logic stays in their own functions, while four weeks of building can never be recovered.
situation_ko: Marek은 의존성을 들이기보다 워크플로 엔진을 팀에서 직접 만들고 싶어 한다. Jay는 설계 회의에서 반대로 주장한다. 비즈니스 로직이 자체 함수에 남으니 의존성은 일주일이면 걷어 낼 수 있지만, 직접 만드는 데 쓴 4주는 되돌릴 수 없다고.
why: **One-way door** and **two-way door** are decision vocabulary: a one-way door is irreversible or very costly to reverse, a two-way door you can walk back out of. "On our time" and "on our stack" name the dimension each door is about: time spent building is gone for good, while a dependency can be removed later. The **asymmetry** is the point: the two options differ in kind, not degree, so building only looks safer. The practical rule that follows is to spend long deliberation on one-way doors and decide two-way doors quickly. The corrected version joins the two halves with a semicolon.
why_ko: **One-way door**와 **two-way door**는 의사결정 어휘다. 일방향 문은 되돌릴 수 없거나 되돌리는 비용이 매우 큰 결정, 양방향 문은 다시 나올 수 있는 결정이다. "On our time"과 "on our stack"은 각 문이 어느 차원에 관한 것인지 말한다. 만드는 데 쓴 시간은 영영 사라지고, 의존성은 나중에 제거할 수 있다. 핵심은 **asymmetry**다. 두 선택은 정도가 아니라 종류가 달라서, 직접 만드는 쪽이 안전해 보일 뿐이다. 따라오는 실전 규칙은 일방향 문에 오래 고민하고 양방향 문은 빨리 결정하는 것이다. 수정본은 두 절을 세미콜론으로 잇는다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, second export (2026-09-21), page 4 card 6 (sentence): Original "…That asymmetry is my whole argument — building is a one-way door on our time, adopting is a two-way door on our stack." / Corrected with a semicolon between the halves / Korean "직접 구축하는 것은 시간 측면에서 되돌릴 수 없는 선택이고, 외부 솔루션을 도입하는 것은 기술 스택 측면에서 되돌릴 수 있는 선택입니다." / Level 9/10, one-way vs two-way door as reversibility. The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 두 번째 내보내기(2026-09-21), 4페이지 카드 6(문장): 원문 "building is a one-way door on our time, adopting is a two-way door on our stack" / 수정본은 세미콜론 / 한국어 "직접 구축하는 것은 시간 측면에서 되돌릴 수 없는 선택이고, 도입하는 것은 스택 측면에서 되돌릴 수 있는 선택입니다." / one-way·two-way door 해설. 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-79.txt

## Dialogue
Marek: I'd still rather build the workflow engine ourselves. A dependency is a risk.
> 난 그래도 워크플로 엔진을 우리가 직접 만들고 싶어. 의존성은 위험이야.
Jay: It's a risk we can undo. The business logic stays in our own functions either way, so we could remove the dependency in about a week.
> 되돌릴 수 있는 위험이지. 어느 쪽이든 비즈니스 로직은 우리 함수에 남으니까 의존성은 일주일이면 걷어 낼 수 있어.
Marek: And building?
> 직접 만들면?
Jay: Four weeks we never get back. That asymmetry is my whole argument. Building is a one-way door on our time; adopting is a two-way door on our stack.
> 절대 돌려받지 못하는 4주. 그 비대칭이 내 주장의 전부야. 직접 만드는 건 시간에서 되돌릴 수 없는 문이고, 도입하는 건 스택에서 되돌릴 수 있는 문이야.
Marek: One-way meaning irreversible.
> one-way가 되돌릴 수 없다는 뜻이지.
Jay: Right. Walk through and you can't walk back. A two-way door you can come back out of if you don't like the room, so let's not spend a one-way-door amount of deliberation on it. Adopt, keep the logic ours, revisit in a quarter.
> 맞아. 들어가면 못 돌아와. 양방향 문은 방이 마음에 안 들면 다시 나올 수 있으니까, 여기에 일방향 문만큼의 고민을 쓰지 말자. 도입하고, 로직은 우리 것으로 두고, 한 분기 뒤에 다시 보자.

## Techniques
1. **선택지를 되돌릴 수 있느냐로 다시 분류한다.** "It's a risk we can undo." — 위험의 크기가 아니라 가역성으로 프레임을 바꾸면 논쟁의 축이 이동한다.
2. **비유를 말한 뒤 곧바로 결정 규칙으로 잇는다.** "let's not spend a one-way-door amount of deliberation on it" — 문 비유가 "얼마나 고민할지"의 규칙이 된다.



## Words
| one-way door | /ˌwʌnˈweɪ dɔr/ | 되돌릴 수 없는 결정 / 되돌릴 수 있는 결정 |
| two-way | /ˈtuˌweɪ/ | 되돌릴 수 없는 결정 / 되돌릴 수 있는 결정 |
| asymmetry | /ˌeɪˈsɪmətri/ | 그 비대칭이 내 주장의 전부다 |
| argument | /ˈɑrɡjəmənt/ | 그 비대칭이 내 주장의 전부다 |
| undo | /ənˈdu/ | 되돌릴 수 있는 위험 |
| revisit | /riˈvɪzɪt/ | 한 분기 뒤에 다시 검토하다 |

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| a one-way door / a two-way door | 되돌릴 수 없는 결정 / 되돌릴 수 있는 결정 — "Building is a one-way door on our time." |
| that asymmetry is my whole argument | 그 비대칭이 내 주장의 전부다 — 논점을 한 단어로 모을 때 |
| a risk we can undo | 되돌릴 수 있는 위험 — 의존성·실험을 옹호할 때 |
| revisit in a quarter | 한 분기 뒤에 다시 검토하다 — 가역적 결정의 마감 |
