# 34 · Design — Which price are we settling on?
title_ko: 우리는 어느 가격으로 정산하나?
situation: Design review at a Paris fintech, Jay's sixth week as lead. The new market type resolves on "the ETH price at 16:00 UTC". Camille, the product manager, thinks that sentence is the spec. Jay knows it is the start of a dispute, and he has to say so without sounding like the engineer who blocks everything.
situation_ko: 파리 핀테크의 설계 리뷰, Jay의 리드 6주 차. 새 마켓 타입은 "16:00 UTC의 ETH 가격"으로 정산된다. PM Camille은 그 문장이 스펙이라고 생각한다. Jay는 그것이 분쟁의 시작임을 알고, 모든 것을 막는 엔지니어처럼 들리지 않으면서 말해야 한다.
why: The gap between a price and a reference rate is where settlement disputes live, and it is invisible to product until the first angry customer. A lead's job is to turn "the price" into a named source, a fixing time and a fallback before launch, in a way the product manager can own.
why_ko: 가격과 참조 금리 사이의 틈이 정산 분쟁이 사는 곳이고, 첫 화난 고객이 오기 전까지 제품 쪽에는 보이지 않는다. 리드의 일은 런칭 전에 "그 가격"을 이름 붙은 출처, 픽싱 시각, 폴백으로 바꾸되 PM이 소유할 수 있는 방식으로 하는 것이다.
status: planned

## Dialogue
Camille: Resolution is simple: the ETH price at 16:00 UTC. What's the engineering concern?
> 정산은 단순해요. 16:00 UTC의 ETH 가격. 엔지니어링 쪽 우려가 뭔가요?
Jay: Not an engineering concern, a customer one. At 16:00 there are about forty ETH prices, one per exchange, and on a normal day they differ by a few dollars. On a bad day one venue prints a wick that's 5 percent off for eleven seconds. Whichever number we pick, the customer on the losing side will point at another one.
> 엔지니어링 우려가 아니라 고객 우려예요. 16:00에 ETH 가격은 거래소마다 하나씩 마흔 개쯤 있고, 평범한 날에도 몇 달러씩 달라요. 나쁜 날에는 한 거래소가 11초 동안 5퍼센트 벗어난 꼬리를 찍어요. 어느 숫자를 골라도 지는 쪽 고객은 다른 숫자를 가리킬 거예요.
Camille: So we pick the biggest exchange.
> 그럼 가장 큰 거래소로 하죠.
Jay: We could, and then our settlement depends on one company's uptime and one company's wash trading. The alternative is a reference rate: a benchmark administrator takes a vetted set of venues, throws out outliers by a published rule, aggregates over a window, and publishes one number with a methodology behind it. Kaiko does this under EU benchmark regulation, and it's available on-chain through an oracle. It costs us a licence and a day of integration.
> 그럴 수 있고, 그러면 우리 정산이 한 회사의 가동률과 한 회사의 워시 트레이딩에 달리게 돼요. 대안은 참조 금리예요. 벤치마크 관리자가 심사된 거래소 집합을 가져다 공개된 규칙으로 이상치를 버리고, 창에 걸쳐 집계해서, 방법론이 뒤에 있는 숫자 하나를 발표해요. Kaiko가 EU 벤치마크 규정 아래 이걸 하고, 오라클로 온체인에서 받을 수 있어요. 비용은 라이선스 하나와 통합 하루예요.
Camille: A day, and a licence fee, for a number that's almost the same.
> 하루와 라이선스 비용을, 거의 같은 숫자에.
Jay: Almost the same on the days nobody complains. The licence buys us the sentence "we settled on a regulated benchmark, here's the methodology" on the day somebody does. Without it, the sentence is "we settled on Binance," and then we are the ones defending Binance's print.
> 아무도 불평 안 하는 날엔 거의 같죠. 라이선스가 사주는 건 누군가 불평하는 날 "우리는 규제된 벤치마크로 정산했고, 방법론은 여기 있습니다"라는 문장이에요. 없으면 문장은 "우리는 바이낸스로 정산했습니다"가 되고, 그러면 바이낸스의 체결가를 방어하는 게 우리예요.
Camille: Fine. What do you need from me?
> 좋아요. 제가 뭘 해야 하죠?
Jay: Three lines in the spec, and they're yours to write, not mine: the source by name, the fixing time to the second, and what happens if the source is down at 16:00. I'll propose the fallback; you decide it.
> 스펙에 세 줄이고, 제가 아니라 당신이 쓸 것이에요. 이름 붙은 출처, 초 단위의 픽싱 시각, 16:00에 출처가 죽어 있으면 어떻게 하는지. 폴백은 제가 제안하고, 결정은 당신이 해요.
Camille: Send me the fallback options today.
> 폴백 옵션을 오늘 보내주세요.

## Techniques
1. **우려의 주인을 바꾼다.** "Not an engineering concern, a customer one." 엔지니어의 반대를 고객의 결과로 재프레임하면 PM이 방어하지 않고 듣는다.
2. **싼 대안이 실제로 사는 것을 말한다.** "The licence buys us the sentence… on the day somebody does." 비용을 정당화할 때 기능이 아니라 나쁜 날의 문장을 판다.
3. **결정을 스펙 세 줄로 돌려준다.** "Three lines in the spec, and they're yours to write, not mine." 리뷰가 지적으로 끝나지 않고 PM이 소유하는 산출물로 끝난다.

## Expressions
| resolves on | ~로 정산된다(결과가 결정된다) |
| a customer concern | 고객 쪽 우려 |
| prints a wick | 꼬리(순간 급변)를 찍다 |
| point at another one | 다른 것을 가리키다(반박하다) |
| a vetted set of venues | 심사된 거래소 집합 |
| by a published rule | 공개된 규칙으로 |
| almost the same on the days nobody complains | 아무도 불평 안 하는 날엔 거의 같다 |
| buys us the sentence | 그 문장을 살 수 있게 해준다 |
| defending someone's print | 남의 체결가를 방어하다 |
| to the second | 초 단위로 |
| yours to write, not mine | 내가 아니라 당신이 쓸 것 |
