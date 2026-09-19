# 36 · Design review — That argument works for any conclusion
title_ko: 그 논증은 어떤 결론에도 통합니다
situation: Design review at a London fintech where Jay leads a small settlement team. A senior PM, Tomasz, proposes moving the risk engine to a third-party service now because "everyone will be on it in two years anyway" and "we can shape it better from inside their design partner programme". Jay has to disagree without making it personal.
situation_ko: 런던 핀테크의 설계 리뷰. Jay는 작은 결제 팀을 이끈다. 시니어 PM Tomasz가 "2년 뒤엔 다 그걸 쓸 테니" 그리고 "디자인 파트너 프로그램 안에서 우리가 더 잘 바꿀 수 있으니" 리스크 엔진을 지금 외부 서비스로 옮기자고 한다. Jay는 사람을 공격하지 않으면서 반대해야 한다.
why: Inevitability and doing-more-from-within are the two arguments a team lead hears most, and both sound like strategy. The skill is to name the shape of the argument, not the motive of the person, then ask for the one thing the argument cannot supply: a checkable condition.
why_ko: 불가피성과 안에서-더-많이는 팀 리드가 가장 자주 듣는 두 논증이고, 둘 다 전략처럼 들린다. 기술은 사람의 동기가 아니라 논증의 모양에 이름을 붙이고, 그 논증이 줄 수 없는 한 가지, 검사 가능한 조건을 요구하는 것이다.
status: important

## Dialogue
Tomasz: Everyone in the sector will be on their risk engine within two years. If we move now we get in early, and inside the design partner programme we can shape the roadmap.
> 업계 전부가 2년 안에 그 리스크 엔진을 쓸 겁니다. 지금 옮기면 일찍 들어가고, 디자인 파트너 프로그램 안에서 로드맵을 바꿀 수 있어요.
Jay: I want to separate two things you just said, because I react to them differently. The first is "it is going to happen anyway". The second is "we can steer it from inside".
> 지금 하신 말 두 가지를 나누고 싶습니다. 제가 다르게 반응하거든요. 첫째는 "어차피 일어날 일이다", 둘째는 "안에서 조종할 수 있다"입니다.
Tomasz: Fair. Take the first.
> 좋아요. 첫째부터.
Jay: "Everyone will be on it" would be just as good a reason to wait as to move. If it is inevitable, the price and the API will be better in two years and we lose nothing by being late. So the argument does not actually pick a side. What would pick a side is a cost we pay now by waiting. Do we have one?
> "다 쓸 것이다"는 옮길 이유만큼 기다릴 이유로도 똑같이 좋습니다. 불가피하다면 2년 뒤 가격과 API가 더 나을 테니 늦어도 잃는 게 없어요. 그러니 그 논증은 실제로 편을 고르지 않습니다. 편을 고르는 건 지금 기다려서 내는 비용이죠. 그런 게 있나요?
Tomasz: The partner discount, mainly. And influence.
> 주로 파트너 할인이요. 그리고 영향력.
Jay: The discount is a number, so let us put it on the slide and compare it with the migration cost. Influence is the second argument, and that one worries me more. "We can shape it from inside" is something every design partner says, and it is true regardless of whether the vendor ever changes a line for us.
> 할인은 숫자니까 슬라이드에 올려 이전 비용과 비교하죠. 영향력은 둘째 논증이고, 그쪽이 더 걱정됩니다. "안에서 바꿀 수 있다"는 모든 디자인 파트너가 하는 말이고, 벤더가 우리 때문에 한 줄이라도 바꾸는지와 상관없이 참이에요.
Tomasz: So you think it is empty?
> 그럼 빈말이라고 보시는 거예요?
Jay: I think it is unfalsifiable as stated, which is different. Make it falsifiable and I am in. For example: within six months they ship the per-counterparty limit we need, or we keep our engine and the pilot ends. Written into the contract. If they will not sign that, the influence was never real.
> 지금 표현으로는 반증할 수 없다고 봅니다. 빈말과는 달라요. 반증 가능하게 만들면 저도 찬성합니다. 예컨대 6개월 안에 우리에게 필요한 거래상대별 한도를 출시한다, 아니면 우리 엔진을 유지하고 파일럿을 끝낸다. 계약에 적어서요. 그걸 서명하지 않으면 영향력은 원래 없었던 겁니다.
Tomasz: That is a harder sell to them.
> 그쪽에 팔기 더 어렵겠네요.
Jay: It is. But it turns a story into a condition, and conditions are the only thing I can defend to the risk committee. I am not against the move. I am against making it for reasons that would have worked for any move.
> 그렇죠. 하지만 이야기를 조건으로 바꿉니다. 조건은 제가 리스크 위원회에서 지킬 수 있는 유일한 것이에요. 이전에 반대하는 게 아닙니다. 어떤 이전에도 통했을 이유로 이전하는 데 반대하는 겁니다.

## Techniques
1. **논증을 둘로 나누고 각각에 이름을 붙인다.** "I want to separate two things you just said." 사람이 아니라 논증의 모양을 다루면 반대가 개인 공격으로 들리지 않는다.
2. **논증이 반대 결론에도 통함을 보인다.** "would be just as good a reason to wait as to move." 반박이 아니라 정보량이 없다는 관찰이라서 상대가 방어할 것이 없다.
3. **빈말이라 하지 않고 반증 가능하게 만들어 달라고 한다.** "Make it falsifiable and I am in." 조건을 제안하는 쪽이 협력적으로 보이고, 조건을 거부하면 상대가 스스로 답한 셈이 된다.

## Expressions
| I react to them differently | 저는 그 둘에 다르게 반응합니다(나누어 다루겠다는 신호) |
| just as good a reason to wait as to move | 옮길 이유만큼 기다릴 이유로도 좋다 |
| does not actually pick a side | 실제로는 편을 고르지 않는다(결론을 정해 주지 않는다) |
| put it on the slide | 슬라이드에 올리다(숫자로 드러내다) |
| regardless of whether | ~인지 여부와 상관없이 |
| unfalsifiable as stated | 지금 표현으로는 반증 불가능한 |
| Make it falsifiable and I am in | 반증 가능하게 만들면 찬성합니다 |
| written into the contract | 계약에 명시된 |
| a harder sell | 팔기 더 어려운 것(설득이 더 어려운 제안) |
| turns a story into a condition | 이야기를 조건으로 바꾼다 |
| the only thing I can defend to | ~에게 지킬 수 있는 유일한 것 |
| reasons that would have worked for any move | 어떤 선택에도 통했을 이유 |
