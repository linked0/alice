X/Twitter posts pasted by jay, 2026-09-23.

--- PASTED CONTENT (verbatim, the relevant part) ---

StarkWare 🥷 님이 재게시함
Eli Ben-Sasson | Starknet.io  @EliBenSasson · 17시간

This is what I've been dreaming about for more than a decade:

As Zcash co-founder I've been saying for more than a decade that the real problem of privacy is
making it usable with good UX for end-users, for doing more than just transferring a single asset
(for that case, ZEC rocks!).

Great job @sendmoodz @EkuboProtocol !

  인용
  Ekubo @EkuboProtocol · 17시간
  You can now swap privately via Ekubo Protocol on Starknet!
  Try it out here:
  https://ekubo.org/swap?inputCurrency=0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7&amount=1&chainId=0x534e5f4d41494e&outputCurrency=0x33068f6539f8e6e6b131e6b2b814e6c34a5224bc66947c47dab9dfee93b35fb&privacy=private

--- END PASTED CONTENT ---

Also in the same paste, unrelated and NOT made into an item: an ntv Nachrichten post about German
heating and electricity prices this winter (n-tv.de/mediathek/videos/wirtschaft/…id31334561).
Recorded here only so the paste is preserved whole.

NOTES ON SOURCING (written when the card was built, 2026-09-23)

Reported: the two posts above, and the shape of the linked URL. That is all. I did not open
ekubo.org, did not execute a swap, did not read Ekubo's or Starknet's documentation, and did not
look up @sendmoodz. I do not know what mechanism provides the privacy, what the fee is, what the
latency is, or whether the feature is on mainnet for everyone — the chainId in the URL
(0x534e5f4d41494e) decodes as the ASCII string "SN_MAIN", which is Starknet mainnet, but that is a
property of the link, not confirmation that the feature is generally available.

Verified only in the trivial sense that anyone can check: the URL carries `privacy=private` as a
query parameter alongside `inputCurrency`, `outputCurrency`, `amount` and `chainId`.

The card's own arguments, labelled as such in the body:
 1. That the news is the URL. Privacy appearing as a query parameter on an ordinary swap page
    means it has been reduced to an option inside a tool people already use, rather than a
    separate venue, asset and ritual. That is exactly the UX claim Ben-Sasson makes, stated as a
    fact about the interface rather than as a wish.
 2. That a private swap is a strictly harder problem than a shielded transfer, and why: a
    transfer's invariant is closed inside one asset's shielded pool, while a swap touches a public
    AMM whose reserves move. The pool can leak what the transaction hides.
 3. That the anonymity set is the whole security property, and on launch day it is smallest — so
    the correct reading of a day-one privacy feature is "promising mechanism, no privacy yet".
 4. That an opt-in privacy toggle is itself a disclosure: choosing it separates you from everyone
    who did not. Default-off is good for adoption and bad for the anonymity set, and this tension
    is not a flaw anyone has solved.

Explicitly NOT claimed by this card: how Ekubo implements the feature. Batching, a shielded pool
with aggregate settlement, encrypted orders and intent-style designs are all plausible and the
card names them as the space of options, not as a description of this product.

Related items: zama-blockchain-https (raw file 2026-09-23-zama-blockchain-https.md),
https-won-because-it-got-cheap, consumed-authorization, uniswap-hook-cannot-move.
