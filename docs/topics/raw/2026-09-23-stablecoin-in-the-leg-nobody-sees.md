Digital Asset Works article pasted by jay, 2026-09-23.

Headline: 마스터카드, 34조원 카드거래 스테이블코인으로 정산
Byline: 박재연 · 입력 2026.09.23 10:30
Primary source linked in the article:
https://s27.q4cdn.com/749715820/files/doc_news/SoFi-Becomes-First-National-Bank-to-Go-Live-with-Stablecoin-Settlement-across-Mastercards-Global-Payments-Network-2026.pdf

WHAT THIS FILE IS
jay's paste, kept as received. I did not open the linked press release and did not check any
figure against Mastercard's or SoFi's own filings. Everything below is the article's.

--- PASTED CONTENT (verbatim) ---

글로벌 결제기업 마스터카드(Mastercard)가 미국 인터넷은행 소파이(SoFi)와 손잡고 연환산 250억달러(약 34조원) 규모의 카드거래를 스테이블코인으로 정산한다.

22일(현지시간) 소파이와 마스터카드에 따르면 소파이은행의 직불·신용카드 프로그램에서 자체 달러 스테이블코인 SoFiUSD(소파이USD)를 활용한 정산이 시작됐다. 지난 3월 양사가 관련 협력을 발표한 지 약 6개월 만이다.

소파이는 전체 카드 프로그램을 소파이USD 기반 블록체인 정산으로 전환하고 있다. 이 프로그램의 연환산 거래액은 250억달러를 넘을 것으로 예상된다. 관련 거래는 현재 블록체인에서 실제 처리되고 있다.

핵심은 소비자가 스테이블코인으로 직접 카드대금을 결제하는 구조가 아니라 카드거래 이후 금융기관 사이에서 이뤄지는 정산 과정에 스테이블코인을 사용하는 것이다.

소파이USD는 미국 통화감독청(OCC)의 감독을 받는 국립은행인 소파이은행이 발행한다. 미국 달러와 1대1로 상환할 수 있고 준비자산은 주로 현금으로 구성된다. 기관과 소파이 이용자는 결제와 정산 등 금융 서비스에 소파이USD를 사용할 수 있다.

마스터카드는 이번 사례를 통해 기존 글로벌 카드 결제 인프라와 은행 발행 스테이블코인을 연결했다.

셰리 헤이먼드(Sherri Haymond) 마스터카드 디지털상용화 글로벌 총괄은 "소파이와 함께 실험을 넘어 규제된 스테이블코인 정산을 실제 운영 환경에 적용하고 있다"고 말했다. 이어 "마스터카드가 제공하는 신뢰와 규모, 안전장치를 유지하면서 기업들이 자금 이동 방식을 더 다양하게 선택할 수 있도록 하는 단계"라고 설명했다.

앤서니 노토(Anthony Noto) 소파이 최고경영자(CEO)는 "가맹점이 소파이의 기업금융 플랫폼을 통해 소파이은행 계좌로 정산금을 즉시 받고 이를 24시간 현금으로 인출할 수 있다"고 설명했다.

--- END PASTED CONTENT ---

NOTES ON SOURCING (written when the card was built, 2026-09-23)

Reported, from the article: the SoFi × Mastercard go-live on 22 Sept (US time), six months after
the March announcement; SoFiUSD as SoFi Bank's own dollar stablecoin; SoFi Bank as an
OCC-supervised national bank; 1:1 USD redemption with reserves mostly in cash; the whole card
program being converted, with an annualised program volume expected above $25bn; that consumers
do NOT pay in stablecoin and the token sits in the inter-institution settlement leg; the two
executive quotes.

NOT verified by me: every number and claim above. I did not open the linked press release, did
not check the $25bn figure or the "first national bank" claim, and do not know which chain the
settlement runs on — the article does not say, and the card does not guess.

The card's own arguments, labelled as such in the body:
 1. That the adoption path here is the opposite of the retail crypto-payments narrative: the
    layer that changed is the one no cardholder can see.
 2. That the consumer leg was never the slow part — authorisation is already ~1 second, and the
    delay lives in clearing and settlement — so this is where a faster rail has somewhere to go.
    Same shape as the Trueo speed argument in #77.
 3. That "$25bn settled in stablecoin" is very likely not $25bn moving on-chain, because card
    settlement is NET, not gross. This is an inference from how four-party card settlement
    generally works, NOT something the article or the release says. Flagged in the body as the
    card's reading and as the thing to check first.
 4. That the merchant-side "instant, 24/7" benefit is partly a closed-loop effect — the funds
    land in a SoFi Bank account, reached through SoFi's own corporate banking platform — and
    should not be attributed wholesale to the stablecoin leg. The article's own wording
    (가맹점이 소파이의 기업금융 플랫폼을 통해 소파이은행 계좌로) is what this reading rests on;
    it does not state whether merchants must bank with SoFi to get it.

Open questions worth answering before citing this item anywhere load-bearing:
 - Which chain, and is it public or permissioned?
 - Gross vs net: what amount actually moves on-chain per settlement cycle?
 - Is SoFiUSD a deposit token (a liability of SoFi Bank) or a reserve-backed stablecoin held off
   the bank's balance sheet? "Issued by the bank, redeemable 1:1, reserves mostly cash" is
   compatible with both, and the distinction decides whether depositor protections apply.
 - Do merchants need a SoFi Bank account for the instant-settlement claim?

Related items already in Jayverse: kb-kookmin-kinexys-deposit-rail (#65),
four-seats-and-the-empty-one (#74), one-bank-both-doors (#73),
reserve-that-makes-the-bank-fragile (#76), uniswap-hook-cannot-move (#77),
never-about-issuance (#81).
