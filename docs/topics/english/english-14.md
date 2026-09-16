# 14 · Design — It looks like a stablecoin. It isn't one.
title_ko: 스테이블코인처럼 보인다. 아니다.
situation: Dana, from marketing, wants to call USDCX "our stablecoin" on the landing page. USDCX is a ledger credit in Verex's database, funded by Stripe test mode.
situation_ko: 마케팅의 Dana가 랜딩 페이지에서 USDCX를 "우리 스테이블코인"이라 부르고 싶어 한다. USDCX는 Stripe 테스트 모드로 충전되는 Verex 데이터베이스의 장부 크레딧이다.
why: Correcting a category error with a non-engineer: give the accurate word, explain the one property that matters, and offer the sentence they can use.
why_ko: 비개발자와의 범주 오류 교정. 정확한 단어를 주고, 중요한 속성 하나를 설명하고, 상대가 쓸 수 있는 문장을 준다.

## Dialogue
Dana: Can we call USDCX our stablecoin? It's a dollar, it's on the site, people know the word.
> USDCX를 우리 스테이블코인이라고 부를 수 있을까요? 달러이고, 사이트에 있고, 사람들이 아는 단어예요.
Jay: People know the word, which is exactly why we can't. A stablecoin is a token anyone can hold in any wallet, backed by an issuer's reserve. USDCX is a row in our database.
> 사람들이 아는 단어라서 오히려 쓸 수 없어요. 스테이블코인은 누구나 어떤 지갑에든 보유할 수 있고 발행자의 준비금이 뒷받침하는 토큰이에요. USDCX는 우리 데이터베이스의 행이죠.
Dana: Users don't see the difference.
> 사용자는 차이를 못 봐요.
Jay: They see it the day they try to withdraw and can't. There's no off-ramp yet. That's the one property that matters, and the word "stablecoin" promises the opposite.
> 출금하려다 못 하는 날 보게 돼요. 아직 오프램프가 없어요. 그게 중요한 속성 하나이고, "스테이블코인"이라는 단어는 그 반대를 약속하죠.
Dana: So what do I write?
> 그럼 뭐라고 쓰죠?
Jay: "USDCX is your Verex balance, credited when you pay with a card. Test mode, not withdrawable." Shorter than a disclaimer and it's true.
> "USDCX는 카드로 결제하면 충전되는 Verex 잔액입니다. 테스트 모드, 출금 불가." 면책 문구보다 짧고 사실이에요.
Dana: That's less exciting.
> 덜 흥미롭네요.
Jay: It is. The exciting version comes when we wire a real off-ramp and swap the row for USDC. Then you get to say "stablecoin" and mean it.
> 그렇죠. 흥미로운 버전은 실제 오프램프를 연결하고 행을 USDC로 바꿀 때 와요. 그때는 "스테이블코인"이라고 말해도 진짜가 되죠.

## Techniques
1. **상대의 근거를 뒤집어 쓴다.** "People know the word, which is exactly why we can't." 같은 사실에서 반대 결론을 끌어낸다.
2. **속성 하나로 압축한다.** "the one property that matters" 정의 논쟁 대신 사용자가 겪을 순간 하나를 말한다.
3. **쓸 문장을 준다.** "So what do I write?" 에 완성된 문장으로 답하면 교정이 협업이 된다.

## Expressions
| people know the word | 사람들이 그 단어를 안다 |
| which is exactly why | 바로 그래서 |
| backed by an issuer's reserve | 발행자의 준비금이 뒷받침하는 |
| a row in our database | 우리 데이터베이스의 행 |
| the day they try to withdraw | 출금하려는 날 |
| off-ramp | 오프램프, 현금화 경로 |
| promises the opposite | 반대를 약속한다 |
| shorter than a disclaimer | 면책 문구보다 짧다 |
| less exciting | 덜 흥미롭다 |
| say it and mean it | 말하고 그것이 진짜이다 |
