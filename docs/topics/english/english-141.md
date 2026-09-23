# 141 · Line — If a diff needs context from another PR to be reviewable, I'll say so up front.
title_ko: If a diff needs context from another PR to be reviewable, I'll say so up front. — 다른 PR의 맥락이 있어야 리뷰가 되는 diff라면 처음부터 그렇게 말하겠다
situation: In a retro, Lena says she spent an hour on Jay's PR before realising half the logic had landed in an earlier one. Jay has already owned that; now he wants to state the one habit he will carry over so it does not happen again.
situation_ko: 회고에서 Lena가 Jay의 PR에 한 시간을 썼는데 로직의 절반이 이전 PR에서 이미 들어갔다는 걸 나중에야 알았다고 말한다. Jay는 그 책임을 이미 인정했고, 이제 재발하지 않도록 앞으로 가져갈 습관 하나를 말하고 싶다.
why: The sentence is a rule Jay sets for himself, in three engineering-native pieces. **Reviewable** is stronger than "visible": a diff can be on screen and still not reviewable if the reviewer lacks the context to judge it. **Up front** means at the start, before anyone spends time; "I'll say so up front" uses "so" to stand for the whole condition. **Carry over from this** is how you frame the lesson: a practice you take from this incident into the next one. It is not an apology (that came earlier, as "that's on me") and not a promise to avoid split PRs; splitting is fine, hiding the split is not.
why_ko: 이 문장은 Jay가 스스로 정하는 규칙이고, 개발자다운 조각 셋으로 되어 있다. **reviewable**은 "visible"보다 강하다. diff가 화면에 떠 있어도 리뷰어에게 판단할 맥락이 없으면 reviewable하지 않다. **up front**는 처음부터, 누가 시간을 쓰기 전에라는 뜻이고, "I'll say so up front"의 so는 앞의 조건 전체를 받는다. **carry over from this**는 교훈을 담는 틀이다. 이번 일에서 다음 일로 가져가는 습관. 사과는 아니고(그건 앞서 "that's on me"로 했다), PR 분할을 피하겠다는 약속도 아니다. 나누는 건 괜찮고, 나눴다는 걸 숨기는 게 문제다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, second export (2026-09-21), page 3 card 19 (sentence): memo Original "And one thing I want to carry over from this — if a diff needs context from another PR to be reviewable, I'll say so up front." / Korean "어떤 diff를 제대로 리뷰하려면 다른 PR의 맥락이 필요할 경우, 앞으로는 그 사실을 처음부터 미리 밝히겠습니다." / Natural "One takeaway for me: if a diff needs context from another PR, I'll flag it up front." The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 두 번째 내보내기(2026-09-21), 3페이지 19번 카드(문장): 메모 원문 "And one thing I want to carry over from this — if a diff needs context from another PR to be reviewable, I'll say so up front." / 번역 "어떤 diff를 제대로 리뷰하려면 다른 PR의 맥락이 필요할 경우, 앞으로는 그 사실을 처음부터 미리 밝히겠습니다." / 자연스러운 표현 "One takeaway for me: … I'll flag it up front." 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-79.txt

## Dialogue
Lena: I lost an hour on that PR before I found the earlier one with the actual state machine in it.
> 그 PR에서 한 시간을 날렸어, 실제 상태 머신이 들어 있는 이전 PR을 찾기 전까지.
Jay: That's on me. And one thing I want to carry over from this: if a diff needs context from another PR to be reviewable, I'll say so up front. First line of the description, with the link.
> 그건 내 책임이야. 그리고 이번 일에서 가져가고 싶은 게 하나 있어. 다른 PR의 맥락이 있어야 리뷰가 되는 diff라면 처음부터 그렇게 말할게. 설명란 첫 줄에, 링크랑 같이.
Lena: Splitting it was fine, by the way. I just couldn't tell it was split.
> 참고로 나눈 건 괜찮았어. 나눴다는 걸 알 수가 없었을 뿐이야.
Jay: Right, that's the distinction. The diff was visible but not reviewable. A one-line "depends on #412 for the state machine" would have saved you the hour.
> 맞아, 그게 차이야. diff는 보였지만 리뷰할 수는 없었지. "상태 머신은 #412에 의존함" 한 줄이면 네 한 시간을 아꼈을 거야.
Lena: Let's make that the template. Context line first, then the summary.
> 그걸 템플릿으로 하자. 맥락 줄 먼저, 그다음 요약.

## Techniques
1. **책임 인정 → 재발 방지 습관 순으로 말한다.** "That's on me. And one thing I want to carry over from this: …" — 사과에 머물지 않고 앞으로의 규칙을 한 문장으로 세운다.
2. **조건절 규칙은 "if … , I'll …"로 짧게 세우고 so로 받는다.** "if a diff needs context … , I'll say so up front" — so가 조건 전체를 대신하므로 반복하지 않는다.



## Words
| carry | /ˈkæri/ | 이번 일에서 앞으로 가져가다 |
| depends | /dɪˈpɛndz/ | #412에 의존함 |

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| say so up front | 처음부터 그렇게 말하다 — 남이 시간을 쓰기 전에 밝힘. "I'll say so up front." |
| carry over from this | 이번 일에서 앞으로 가져가다 — 교훈·습관을 말할 때. "one thing I want to carry over from this" |
| reviewable | 리뷰어가 판단할 맥락을 갖춘 상태 — visible과 구별. "visible but not reviewable" |
| depends on #412 | #412에 의존함 — PR 설명 첫 줄의 맥락 표시 |
