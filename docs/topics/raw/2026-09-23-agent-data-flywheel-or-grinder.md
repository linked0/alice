X/Twitter posts pasted by jay, 2026-09-23, in two messages. Merged into one item because they are
one announcement.

--- PASTED CONTENT (verbatim) ---

[headline of the first paste]
Trade stocks through the Coinbase MCP
We're bringing the everything exchange to agents.

  인용
  Coinbase Developer Platform🛡️ @CoinbaseDev · 12시간
  You can now trade stocks through Coinbase for Agents.
  Crypto. Derivatives. And now 6,000+ stocks.
  Need analytics or data on those stocks? x402 payments let your agents pay for live market data
  mid-task, from your USDC balance on Coinbase. No subscriptions needed.
  The most …

Brian Armstrong @brian_armstrong · 8시간
Connect your favorite AI Agent to Coinbase to trade, pay, and manage your finances.
Shown here on Muse but works on just about all of them.

  인용
  lincoln.base.eth @MurrLincoln · 12시간
  make x402 micropayments from your coinbase balance!
  i think there's a potential flywheel around:
  1. agent wants to make a trade
  2. agent pays for premium trading data
  3. agent makes more well-informed trade
  4. agent pays for more data to make more money

--- END PASTED CONTENT ---

NOTES ON SOURCING (written when the card was built, 2026-09-23)

Reported: the posts above, and nothing else. The CoinbaseDev post is truncated in the paste ("The
most …"), so part of it is missing. I did not open Coinbase's developer documentation, did not
connect an agent, did not look at the MCP server's tool list or its authorization model, and do
not know what "Muse" is beyond Armstrong naming it as the client shown in his demo.

NOT verified: the 6,000+ stock figure, what derivatives are included, which jurisdictions can use
it, what the x402 data providers are, what the per-call prices are, and — the important one —
what spending limits, scopes, approval steps or revocation mechanisms exist. None of that is in
the paste.

The card's own arguments, labelled as such in the body:
 1. That the four-step "flywheel" is only a flywheel if the expected gain from the data exceeds
    its cost, consistently. Otherwise the same architecture is a grinder: it converts a balance
    into data spend at machine speed. The loop's compounding is assumed; its spending is
    guaranteed.
 2. That "no subscriptions needed" removes a cap as well as a friction. A subscription is a
    bounded cost. Per-call pricing moves the bound from the contract to the agent's behaviour,
    which is the actual risk surface of agentic payments and the inverse of how it is marketed.
 3. That this is the first-party demand for a protocol its own publisher wrote — x402 is
    Coinbase's — which is a strong signal about intent and a weak one about adoption.
 4. That the control-plane point from agent-payments-korea-control-plane applies directly: the MCP
    server is where the relationship sits, and "the everything exchange for agents" is a claim
    about owning that surface rather than about asset coverage.
 5. That step 2 → step 3 is the highest-risk composition in the design: an agent with trade
    authority ingesting purchased market data is ingesting untrusted content into a loop that can
    spend. Paying for data does not make it trusted input.

Related items: machine-native-economy-blackrock (added the same day — this is its thesis shipped
as a product), agent-payments-korea-control-plane (#3, REVISIT), consumed-authorization,
stablecoin-in-the-leg-nobody-sees, mcp-three-sides.
