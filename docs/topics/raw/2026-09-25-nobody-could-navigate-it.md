Article pasted by jay on 2026-09-25. No URL was given, so the item carries no --src-url.

"Lovable says two-thirds of the Fortune 500 use it and revenue hit $600m"
By Ana Maria Constantin. Published 24 September 2026, 1:45 pm UTC.
Reporting on a HumanX Amsterdam session: Lovable co-founder and CTO Fabian Hedin interviewed on
stage by Forbes senior editor Iain Martin, Wednesday 23 September 2026.

--- THE ARTICLE'S CLAIMS, as pasted ---

Scale and money
- Revenue $600m, per Hedin. Martin said it was about $200m when he visited the Stockholm company
  last summer. In August a $400m round valued Lovable at $13.3bn.
- Two-thirds of the Fortune 500 use Lovable, "often because staff found it on their own." Those
  companies "then come to Lovable with thousands of apps and ask what to do."
- Deutsche Telekom has built more than 2,000 applications on Lovable for load-bearing uses.
  Microsoft and Nvidia named among large companies Lovable works with.
- Users sit in finance, HR, engineering, product and design.
- Apps built on Lovable get close to a billion visits a month, an order of magnitude more than
  Lovable itself.
- Lovable creates more than a million projects a week.

The Uber Eats example
- A sales leader who knew the restaurant pitch process end to end. A tool built on Lovable created
  a pitch customised for each restaurant. First version: a few hours or a day. Later changes: about
  10 minutes. Such changes used to wait months on an engineering backlog.
- Companies are also replacing costly internal software that offered little customisation. Users
  own what they build and can take it and run it themselves.

Security
- Security teams sometimes worry about all the new code, "rightfully so," Hedin said. Lovable works
  with CIOs on who should build what, which data each app can reach and who can edit it, "since
  editors indirectly gain access to that data." No-code tools allowed more deterministic guardrails.
- "You're kind of giving everyone a lot more power to create, which is great. But it comes with this
  flip side of, okay, but how do you actually make sure that they create things in a safe way?"
- On agents changing enterprise security: "I think before, a lot of people have been able to rely on
  kind of security by obscurity, where like the permission system internally in a large enterprise
  has not been perfect, but no one knows how to navigate it. Now you can have an agent navigate it."
- More than a million projects a week is too many to review by hand. Lovable uses AI to scan all of
  them and keeps scanning after users stop building. It fixes critical flaws in dependencies and
  proposes fixes for the rest. Free for all users; Hedin said it was the first in its category.
- Martin raised a pattern of vibe-coded apps that took off and then leaked user data. Hedin said
  builders have to assume vulnerabilities will exist, and pointed to a flaw recently found in the
  curl command-line tool.

Models
- Lovable has never offered a model picker. For a single task it may use more than 100 models,
  weighing cost, speed and quality. Asked whether that means routing to a cheaper open-source model
  rather than the most expensive Anthropic model, Hedin said Lovable can pass the savings on to
  users, and a cheaper model is often faster.
- "Customers ask for the routing after the industry's talk of token maxing turned into bills."
  Lovable is increasingly tuning its own models to cut cost and raise quality on some tasks.

Product
- Martin asked why users would not go straight to Codex or Claude. Hedin: "The difference, if you
  compare that with what Lovable does, is that Lovable does not output code. The output is a
  product." Increasingly, that product is a business.
- Security is an ongoing job, because an app that is secure today may not be secure in a month.
  Lovable handles hosting, deployment and scaling.
- 80% of the ideas users bring are about creating a business. Lovable Cloud now adds payments,
  email, SEO and ads. Example: Rafael, a founder in Brazil, built an AI education platform on
  Lovable; his 50 employees use Lovable for all internal processes and the company is on track for
  about $20m in ARR this year.

Framing and geography
- Hedin prefers "agentic coding" to "vibe coding" (Karpathy's term, coined more than two years ago);
  CEO Anton Osika said last week the company is "way past vibes."
- On staying in Sweden: he and Osika visited San Francisco early and did their due diligence; Europe
  gave competitive advantages including access to talent. Lovable mixes Y Combinator ways of working
  with Sweden's team-first mentality. In June, Osika spoke about Europe's confidence problem. "So I
  don't look back from building from Europe."

--- END ---

NOTES ON SOURCING (2026-09-25)

NOT verified: every figure and claim is the article reporting Hedin, who is the company's
co-founder speaking on a conference stage about his own company. Revenue, the Fortune 500 share,
the Deutsche Telekom count, the visit numbers, the Rafael example and the security-scanning claims
are all first-party and none is audited or independently checked here. I did not open the article's
source page (no URL was given), did not check the August round, and did not verify the "first in
its category" claim about the scanning tool.

One arithmetic note the card states: $600m revenue against a $13.3bn August valuation is roughly a
22x multiple. That is the article's own two numbers put together, not a judgement.

The card's own arguments, labelled as such in the body:
 1. That the security-by-obscurity quote is the most important sentence in the interview and has
    nothing to do with Lovable — enterprise permission systems have been protected by human
    unwillingness to navigate them, and that protection is gone whoever's agent it is.
 2. That "two-thirds of the Fortune 500" measures presence, not procurement, and the article says
    so: staff found it themselves and the companies arrive with thousands of apps asking what to do.
    That is shadow IT discovered after the fact, which is a more interesting fact than the share.
 3. That "the output is a product, not code" plus hosting, deployment, scaling, payments and a
    billion monthly visits means Lovable is infrastructure rather than a tool, and that the
    dependency question changes accordingly.
 4. That the model-routing story is the generation-cost problem arriving from the vendor side, and
    that removing the model picker also removes the user's ability to diagnose a bad day.
 5. That the curl comparison flatters: a curl flaw is found by decades of global review, and a
    vibe-coded app leaking a database has had none — true in substance, deflecting in form.

Related items: value-and-risk-are-one-feature (added the same day),
supported-market-not-supported-merchant (same day), the-bottleneck-moved-downstream,
admin-rights-protect-the-evidence, agent-data-flywheel-or-grinder, third-party-blast-radius,
machine-native-economy-blackrock, an-invariant-is-a-stop-not-an-alarm (#67).
