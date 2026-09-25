Korean thread pasted by jay on 2026-09-25 with the instruction "summarize and add and more info for
Korean startup also". No URL was given and the item therefore carries no --src-url: the primary
source is the paste itself, which is the case the article-source rule covers.

--- PASTED CONTENT (verbatim) ---

한국이 해외진출을 원하는 스타트업의 무덤이 된 것은 Stripe가 한국을 지원하지 않는다는 것도 큰 이유
중 하나인데.

Stripe가 왜 그런 결정을 했냐면 그지같은 전자금융거래법(전금법)상 PG업 등록 규제 때문.

'천송이 코트'로 널리 알려진 사건과 맥락을 같이 하는데, 별 그지같은 규제를 만들어 놓았더니 이제 더
그지같은 과점 카르텔이 형성되어 철옹성같은 규제가 더 촘촘해졌다.

요런 서비스를 MoR(Merchant of Record)라고 한다. Paddle이 그 중에 제일 잘나가지만 수수료율이
높다거나 특정 서비스를 받지 않는거나(내 경우 맥클리너가 거부 카테고리에 들어가서 제외) 하는 경우가
있으므로 잘 비교해보고 선택할 것.

모든 MoR은 결제 뿐만 아니라 판매사업자 대행 용역을 포함하고 있으므로 수수료가 꽤 높은 편(Paddle의
경우 거래당 5% + $0.50).

Dodo Payments의 경우에는 그나마 수수료율은 낮지만 환불율에 굉장히 민감하다던가. 결국 내 경우
Polar를 추천받고 정착했는데 나쁘지 않은 듯.

[두 번째 글]
바이브코딩으로 앱 만드시는 분들! 결제 시스템 넣기 전에 이거 꼭 보세요.
(실제로 제가 사업자 없을 때, 미국 법인 설립도 안해도 돼서 stripe 대신 썼고 지금도 잘 쓰고 있습니다.)
1. 미국 법인 설립 없이 (Stripe 등은 미국 법인 설립이 필수)
2. 사업자등록증 제출 없이
3. 전세계에서 결제 가능
4. 전세계 각각의 결제 세금 계산도 대신해주는..
개인으로 신청해 바로 앱에 붙일 수 있는 결제 서비스가 있습니다. --> 바로 Paddle 입니다.
그런데 Paddle의 진짜 좋은 장점이 하나 더 있는데..
1. 네이버페이 됩니다. 2. 카카오페이 됩니다. 3. 국내 카드 결제도 됩니다.
또 당연히 "매달 자동 결제되는 구독"까지 만들 수 있습니다.
현재 일반 Stripe 결제 서비스는 한국을 직접 지원하지 않지만..
--> Paddle은 한국에서도 개인 판매자로 신청할 수 있습니다.
왜 Stripe는 안되고 Paddle에서는 가능하냐면요..
Paddle이 직접 고객에게 제품을 판매하는 주체가 되어 결제와 판매 단계의 부가세, 판매세 처리를 맡는
방식이기 때문입니다.

--- END PASTED CONTENT ---

WHAT I CHECKED, AND WHAT IT CHANGED (2026-09-25)

I ran two web searches rather than taking the thread at face value.

1. Stripe's Korea status. The thread's headline claim — "Stripe가 한국을 지원하지 않는다" — is now
   imprecise and the distinction matters. Search results (Stripe's own Korea payment-method page,
   plus several Korean write-ups) indicate Stripe has supported Korean payment methods since late
   2024: KRW, Korean cards, Naver Pay and Kakao Pay, accepted WITHOUT a local entity. What has not
   changed is that Korea is not a Stripe *merchant country*, so a Korean corporation still cannot
   open a Stripe account. One Threads post puts it exactly: existing foreign-entity accounts can now
   charge Korean customers; Korean entities still cannot open accounts.
   NOT verified by me against Stripe's own documentation — I read search summaries, not the docs.
2. MoR pricing. Paddle 5% + $0.50 per checkout, described as all-in with no surcharge for
   international cards or subscriptions. Lemon Squeezy matches the headline rate but reportedly
   carries surcharges for international cards, PayPal and subscriptions. Polar 5% + $0.50 on the
   free plan, with paid plans ($20–$400/mo) reducing it to roughly 3.8%–3.4% + $0.30–$0.40,
   international cards +1.5%, and organisations created before May 2026 keeping an earlier
   4% + $0.40. Paddle is described as covering the most tax jurisdictions.
   NOT verified against the providers' own pricing pages. Rates change; check before choosing.

Also corrected: the thread says "Stripe 등은 미국 법인 설립이 필수". A US entity is not required —
any supported merchant country works, and Singapore is a common choice for Korean founders.

The card's own arguments, labelled as such in the body:
 1. That "supported market" and "supported merchant country" are different things, and conflating
    them sends people to the wrong fix.
 2. That the MoR premium is not a payment fee but the price of someone else being the legal seller,
    and that global VAT/GST/sales-tax compliance is what you are actually buying.
 3. That the real cost is dependency, not the percentage: the MoR owns the customer contract, the
    refunds and the right to drop your category, so the prohibited-business list is a pre-build
    check, not a post-launch surprise.
 4. That the thread's regulation-to-cartel observation names a real mechanism — registration
    requirements create fixed compliance costs, only large players clear them, and the cleared
    players then become the constituency defending the requirement.
 5. That the Korean-side tax and FX tail is missing from the thread and needs an accountant rather
    than a card.

Related items: four-seats-and-the-empty-one (#74), agent-payments-korea-control-plane (#3, REVISIT),
issuer-holds-the-switch, never-about-issuance, stablecoin-in-the-leg-nobody-sees, the-excuse-expired.
