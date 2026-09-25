ETHGlobal partner-spotlight post pasted by jay on 2026-09-25. No URL was given, so the item carries
no --src-url: the paste is the source, which is the case the article-source rule covers.

--- PASTED CONTENT (verbatim) ---

ETHGlobal Tokyo Partner Spotlight: @curvegridinc

Curvegrid helps developers build blockchain apps faster with MultiBaas, giving developers APIs and
tools to connect applications, smart contracts, and onchain data.

Excited to have them with us through the weekend!

--- END PASTED CONTENT ---

WHAT I CHECKED (2026-09-25)

The post is a sponsor announcement and says almost nothing about the product, so I searched for what
MultiBaas actually does. From Curvegrid's documentation and blog, plus ethereum.org's tools listing
and a sample-app repo — all read as SEARCH SUMMARIES, not opened directly:

- MultiBaas is a SaaS platform for building on EVM chains, with a web UI and a REST API. Described
  as a hosted control plane for deploying and operating multi-chain EVM backends when you want
  managed keys, indexing hooks and dashboards without building the ops in-house.
- Smart contract management: deploy and interact with any contract from the UI or the REST API.
- Cloud Wallets: sign and submit transactions and messages using your own hardware or software keys,
  with a Transaction Manager (TXM) that monitors those transactions and automatically resubmits when
  required.
- Webhooks: event-driven updates instead of polling or holding connections open. Customisable to
  track ETH, ERC20, ERC721 and ERC1155 transfers, and mined or dropped transactions.
- Chain indexing.
- Authentication, role-based access control, and integration with existing systems.
- A 2024 release added a new UI, broader network support and webhooks; Optimism was added the same
  year.

NOT verified: I did not use MultiBaas, did not open the documentation directly, did not read the
sample app, and cannot confirm the current feature set, pricing, network list, or what "your own
hardware or software keys" means operationally — specifically, whether the signing material is ever
present on Curvegrid's side. That last question is the one the card says matters most and it is the
one I could not answer.

The card's own arguments, labelled as such in the body:
 1. That the three burdens this category removes are node/RPC operation, indexing, and transaction
    lifecycle management, and that the third is both the most underestimated and the only one that
    requires holding signing authority — so the value and the risk come from the same feature.
 2. That the question to ask any hosted signer is not "is it secure" but "what can it sign without
    me", which is answerable from the docs and is the thing to check before a hackathon weekend
    becomes a production dependency.
 3. That hackathon sponsorship selects for time-to-first-transaction, which is exactly what
    middleware optimises and is not what production selects for — a real dynamic that cuts both
    ways, since it is also how good tools get found.

Related items: agent-payments-korea-control-plane (#3, REVISIT) and its Kora section — a hosted
fee-payer with an allowed_programs policy is the same category of object; consumed-authorization;
admin-rights-protect-the-evidence; third-party-blast-radius;
supported-market-not-supported-merchant (borrowed infrastructure, one domain over);
the-bottleneck-moved-downstream (abstraction and comprehension).
