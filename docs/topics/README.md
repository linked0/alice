# Knowledge Notes (formerly Tech Notes, renamed 2026-09-18) — how items are added

`docs/notes.html` is hand-maintained HTML with four sections: **Tech** (formerly "Blockchain & Tech"),
**Theory** (renamed from Fundamentals 2026-09-18; ids `sec-fundamentals` / `--section fundamentals` unchanged), **Life**, **English** (formerly "Dev English"). `docs/topics/_nav.js` is the source of truth for numbering and
status; `docs/topics/_progress.js` paints the rail badges from it. Each item has a detail page in
`docs/topics/`.

## Anything jay mentions is a candidate item (jay, 2026-09-18)

- When jay mentions or pastes an item, a note, an article, a talk, or a number in conversation, treat it
  as an item for Knowledge Notes without waiting for the words "add this item": pick the section
  (Tech, Theory, Life), draft it, and say so in the reply. jay still decides whether it
  stays; the default is to add, not to ask. Questions clearly marked "just asking" are the
  exception: answer them, and offer the item in one line.

## Gemini YouTube briefings — check twice a week (jay, 2026-09-18)

- `/Users/jay/Documents/Gemini` receives Gemini's YouTube weekly briefing files (`YouTube-YYYY-MM-DD-*.md`,
  sections Blockchain / Tech / Life / Culture). Twice a week, Monday and Thursday KST or at the first
  request after three days without a check, compare the folder with
  [gemini-checked.md](gemini-checked.md): every file not logged is new. Add each of its entries to the
  related section (Blockchain and Tech → Tech, Life → Life) as a normal item with
  `--source gemini`, then log the file. **Fallback (jay, 2026-09-18): an entry that fits no section
  goes to Life** (first case: the Tokyo travel vlog, Life #4, type Vlog).
- First check 2026-09-18: `YouTube-2026-09-18-v2.md`.

## Where new Blockchain items come from (jay, 2026-09-16)

- **Daily source file:** `alice-tech-YYYY-MM-DD.md` in
  `~/Library/Mobile Documents/com~apple~CloudDocs/Claude/morning-blockchain-report/` (mirrored at
  `~/temp/morning-blockchain-report`). The morning-report skill writes it every morning (KST). It
  contains the day's "Note 후보" entries — `[오늘 · <source>] <title>` with 사실 / 각도 / 잴 것 /
  주의·대안 — a carry-over list, and Sources.
- **Read today's and yesterday's files once a day**, at jay's first "add tech item" request. A day
  can be missed, so yesterday's candidates stay in play until used. Pool: today's `[오늘 · …]`
  entries first, then yesterday's that no history entry has claimed. Take the next unused one in
  file order as the item's subject; its lines are the seed, its Sources are where
  verification starts. Content jay pastes directly wins for that item.
- Record which candidate became which item number in that day's
  `docs/history/YYYY-MM-DD-dev-notes-history.md`, so later requests the same day skip it.

## Tech (Blockchain) conventions

- **Tooling:** `python3 scripts/add-tech-item.py --key <key> --slot <N> --en en.md --ko ko.md [--status new] [--date] [--source chat|file]`
  Theory items use the same script with `--section fundamentals --tag Math|Algorithms|Economics`;
  they append at the end of the section (numbering there is curriculum order, not done-first) and get
  the same date and source tag (jay, 2026-09-18, first item #193).
  does the whole insert (nav data, card with date, detail page, renumbering, pager, counters).
  Re-run with the same key to replace an item in place.

- Done items first. The newest report takes the first not-done slot; items after it shift by one.
  Detail pages' `#N` kicker and prev/next pager are rebuilt after every insert.
- Dot colors: `#22c55e` DONE, `#38bdf8` RECENTLY DONE, `#ef4444` IMPORTANT, `#64748b` PLANNED,
  `#eab308` NEW, `#a855f7` REVISIT (done, come back later — see below). Mark done only when jay says so.
- **Added date (jay, 2026-09-16, from #54 on):** the KST date the item was added appears on the
  card head (`<span class="topic-date">YYYY-MM-DD</span>`, right-aligned after the title) and in
  the detail page kicker after the type (`#N · PoC · YYYY-MM-DD`). Older items carry no date.
- **Source tag (jay, 2026-09-18):** next to the date, a small pill says where the subject came from:
  `chat` when jay pasted or pointed at the content, `file` when it was taken from the alice-tech
  file, `gemini` when it came from the Gemini briefing folder (2026-09-18). Content jay pastes that is itself a candidate from that day's alice-tech file is tagged
  `file` (its subject came from the file; the paste is how it was pointed at). Card: `<span class="topic-src">`; kicker: `#N · PoC · YYYY-MM-DD · chat`. Pass `--source`.
- Every item: English and Korean copy text as JSON on the card and the page; page body generated
  from the copy text so they cannot diverge; a "Verified and unverified" closing section with
  sources.
- Counters agree in three places: rail pill, section meta, `_nav.js` jump. On a new KST day,
  append the previous day's closing totals to `progress` in `_nav.js` before changing counts.

## Life (jay, 2026-09-18; named Life until later that day — ids `sec-mindset` / `--section mindset` unchanged)

- The third knowledge section: ways of thinking and psychological insight for doing good work and
  living well with it — talks, interviews, essays, books, distilled. Not tooling, not news; the
  test is whether the item still applies when the tools change.
- Added with the same script: `--section mindset --type Talk` (or Essay / Book / Interview).
  Numbering is chronological and append-only, like Dev English. Same date and source tag, same
  EN + KO copy text, same "Why / How it works / Where it lands in Jayverse" body.
- Sits before Dev English in the page so `scripts/english-notes.py`, which re-appends its own
  section last, keeps working unchanged. English conversations follow the once-a-day rule, not one per Life item.

## English (Dev English)

One conversation per day (jay, 2026-09-18; until then it was one per new item): the first item request of a KST day also adds one English conversation, later items that day do not. Rules and format in [english/README.md](english/README.md).

## Key expressions on every detail page (jay, 2026-09-18)

- Every Tech, Theory and Life detail page ends with a **Key expressions** table (Korean
  article: **핵심 표현**): the words and phrases from its English text worth learning, with the
  Korean meaning, a note on where the expression is used, and the sentence it comes from. Example that
  started it: *treasury desk* on the S&P Global / OpenZeppelin page. English conversation pages already
  have their own expressions table and are left as they are.
- Source of truth: `docs/topics/vocab/<page>.md`, a two-column markdown table
  (`| Expression | 뜻 · 쓰이는 자리 |`). Rendering: `python3 scripts/add-vocab.py <page>` (or `--all`).
  The block sits between `<!-- vocab:start -->` and `<!-- vocab:end -->` in both articles and is
  replaced on re-run, so a regenerated page just needs the script run again.
- New items: write the table while writing the item and pass `--vocab <file>` to
  `add-tech-item.py`; it copies the file into `vocab/` and renders it. Size: 8–12 rows for a full
  item, fewer for short curriculum stubs. Pick what a fluent non-native developer would stop at
  (domain terms, idioms, collocations, phrasal verbs, prepositions), **and every acronym, regulation,
  standard or institution name the page assumes** (jay, 2026-09-18: "add the unusual words like BMR or
  MiFID II or ETP NAV, not only words and phrases") — for an acronym the Korean meaning is followed by
  the full English form in parentheses. Skip only everyday EVM vocabulary (EVM, RPC, ERC-20, L1/L2,
  NFT, DeFi) and words that are the same in Korean transliteration.
- Backfill on 2026-09-18 covered all 426 pages that existed that day.

## Entering the notes lands on a detail page (jay, 2026-09-18)

- The list page `notes.html` shows nothing the left rail does not, so entry goes straight to an item:
  the **Knowledge Notes** card on `index.html` links to the first NEW or IMPORTANT item in rail order
  (`add-tech-item.py` rewrites that link on every run), and `notes.html` opened without a hash redirects
  the same way from its own rail. `notes.html?list` or any `#sec-…` hash still shows the list; the
  "All Knowledge Notes" links use `?list`.
- Rail items on `notes.html` link to `topics/<page>.html` directly, not to the in-page anchor
  (`add-tech-item.py` and `english-notes.py` write them that way). The body list stays as the data the
  scripts read.
- Detail-page rails have the same Important / New / All buttons as the list page, defaulting to All so
  the current item is always visible. The 148 curriculum pages (algorithms-N, math-N) and the three
  hand-written pages have no rail, so they are unchanged.

## "Where it lands in Jayverse" on every detail page (jay, 2026-09-18)

- Every Tech, Theory and Life page closes its body with **Where it lands in Jayverse** (Korean:
  **Jayverse에서의 위치**): two to four bullets, each a bold lead naming a service and a decision, then one
  or two sentences concrete enough to act on. New items carry it in their own markdown and
  `add-tech-item.py` refuses an item without it. The 410 older pages were backfilled on 2026-09-18 from
  `docs/topics/landing/<page>.md` via `scripts/add-landing.py` (idempotent `<!-- landing:start/end -->`
  block, placed before "Verified and unverified" or before Key expressions). Curriculum pages keep their
  "Practical Connection" paragraph and add this section after it.

## Health items in Life (jay, 2026-09-18)

- The Life list ends with password-locked items numbered **1, 2, 3 …** (jay: first "from 1000 decreasing", then "I want the health number start from 1") and titled only `Health 1`, `Health 2`, … The real title is inside the ciphertext. jay: never use the
  word *private* in a file name, URL or title — "the word private makes people want to know"; *health* is the neutral
  name everywhere (`_health.js`, `health-N.html`, `health-*` ids and classes, `HEALTH_PASS`).
- Each card has **Detail →** (page `topics/health-N.html`: same rail with the Life items plus the Health items,
  password field on the page) and **Open here** (password field inside the card). Text decrypts in the browser and the
  tab stays unlocked until **Lock all** or the tab closes. A `♥ Health` link in every rail foot jumps to the first one.
  These pages are exempt from the Key-expressions and "Where it lands in Jayverse" rules: their text is not in the repo.
- **Since 2026-09-21 the ciphertext is not in the repo either.** It lives in the Firestore document `health/bundle` in project `doubletree-498007`, and the page fetches it after Google sign-in, then decrypts with the password as before. `docs/topics/_health.js` keeps only the labels (`Health 1` …), which say nothing. Both layers are kept on purpose: security rules govern browsers, not service accounts, and this project has ones with project-wide access — so sign-in decides who may *fetch* the bytes and the password decides who may *read* them. Reading a Health item now needs sign-in **and** the password. Note the old ciphertext stays in git history; jay (2026-09-21): "the already put files I don't care".
- Their text is not in the repo: the plaintext lives outside it at `~/Documents/Private/life-health-rules.md`
  (one `## Health N — title` heading per item, `### en` / `### ko` blocks), and
  `HEALTH_PASS='…' node scripts/health-encrypt.mjs <that file>` writes only ciphertext (AES-256-GCM, PBKDF2-SHA256
  600k) to `docs/topics/_health.js` and then runs `scripts/health-cards.py`, which rewrites the cards and rail links
  in `notes.html` between `<!-- health-nav -->` / `<!-- health-cards -->` markers and regenerates the `health-N.html`
  pages. The password is never written to a file; `add-tech-item.py` leaves these cards alone (no key in `_nav.js`,
  numbers are not renumbered).

## RECENTLY DONE — one fresh done state (jay, 2026-09-23)

- When an item is marked done it becomes **RECENTLY DONE** (blue, `#0284c7`) and stays so for the newest
  done-day **and the one before it**; after that it is plain **DONE** (`#22c55e`). A day starts at **06:00 KST**
  (jay: "done from the 6 a.m. today before the new day's first one is done"), and "the day before" means the
  previous day on which something was done, which is not always the calendar yesterday.
- **Why one state and not two** (jay, 2026-09-23: "too many colors are confusing so Merge Yesterday and Today as
  Recently and remove blue that could be used later for more important mark"). From 2026-09-18 this was two states,
  TODAY DONE (midnight blue `#191970`) and YESTERDAY DONE (sky blue `#38bdf8`). They cost two hues to express a
  distinction the `done YYYY-MM-DD` chip already makes precisely, and the rail read as noise. One state in one blue
  says the same thing.
- **One blue, not two** (jay, 2026-09-23: "How about use blue for recently except the revisit"). The merged state was
  first drawn deep green `#15803d`, to keep recency inside the DONE hue and leave blue free for a future mark stronger
  than IMPORTANT; jay then picked blue for it instead, so RECENTLY DONE is `#0284c7` and REVISIT keeps its purple
  `#a855f7`. The palette still lost a colour, because two blues became one. `#191970` and `#38bdf8` remain unused.
  Note `rtd-shell.mjs` uses `#38bdf8` as the dark-theme *accent* — page chrome, not a status — so RECENTLY DONE and
  that accent are deliberately different blues.
- **DONE is one colour in every section.** Theory and Invest used `#0284c7` for plain DONE; it is `#22c55e` everywhere
  now, which is what keeps `#0284c7` unambiguous as "recently".
- **One colour per label, enforced.** `roll-done-states.py` now rewrites any item whose colour has drifted from
  `PALETTE` on every run. Six Theory items were still `#0284c7` and one Invest item `#f59e0b` — invisible on any one
  page, and exactly what makes a palette feel noisy.
- Mechanics: `add-tech-item.py --status recent` (alias `today`; `--done-at` to override the time) stamps `done`
  (ISO, +09:00) on the `_nav.js` item; English items take `status: recent` + `done: <ISO +09:00>` in
  `docs/topics/english/english-N.md`, which `english-notes.py` carries into `_nav.js`. Both scripts then run
  `scripts/roll-done-states.py`, which buckets every stamped item by `(done − 6h).date()`, keeps the newest bucket
  and the one before it as RECENTLY DONE, relabels the rest DONE, syncs every rail dot in `notes.html`
  with `_nav.js`, and collapses duplicate rail entries. The roll script is safe to run alone.
- **Done date in the kicker (jay, 2026-09-21: "From now on, you should add the done date in a detail page").** Every
  item with a `done` stamp shows `<span title="done">done YYYY-MM-DD</span>` at the end of its detail-page kicker (the
  word "done" is visible, so it cannot be mistaken for the added date) and a `done YYYY-MM-DD` chip in its dot colour
  at the right of the card head on `notes.html` (jay, 2026-09-21: "Add Done data to One employee, one agent …").
  `add-tech-item.py` writes it for a new `recent` / `revisit` page; `roll-done-states.py` adds, updates or removes it on
  every page from the `_nav.js` stamp, so it never drifts. Items done before stamps existed (pre-2026-09-18) have no
  stamp and therefore no date. `index.md` has a Done column.
- Rail buttons in two rows — **Important · New · All** / **Revisit · Repeated · Recently** (Done button removed 2026-09-21; Today and Yesterday merged into Recently 2026-09-23) (a `.tier-break` span forces the
  break; list page, every detail page, template `rtd-shell.mjs`): Recently = RECENTLY DONE only, Repeated = items
  finished on more than one day (`data-times`), **Important = IMPORTANT only** (jay,
  2026-09-18: "make the important button only shows important"; the 2026-09-08/09 rule that Important also showed new
  and recently done items is retired). Each button shows exactly one state, inside the selected category (see the pills rule below). The state labels changed everywhere, including the page template `scripts/rtd-shell.mjs`.

## REVISIT — done, but come back to it (jay, 2026-09-21)

- A sixth state for items that are **already done and still matter enough to be reminded of later**: label
  **REVISIT**, purple dot `#a855f7`, status key `revisit` (jay: "one more category before Done which is already done
  but that I should remind later … filled with very important thing"; the name was Claude's suggestion, accepted).
  First two, marked the same day: Tech #1 learning greed (bin `deep`) and #2 the agent-team workflow.
- **REVISIT is the IMPORTANT of the done group** (jay, 2026-09-23: "the Revisit means the important things
  between DONEs so the Revisit could have the numbers"). IMPORTANT marks what still has to be done; REVISIT marks
  what is already done **and still matters**. That is why it sorts above DONE instead of below it, and why it is a
  separate colour rather than a flag on DONE: the top of a section should read as "the done work worth returning to",
  not as the oldest finished items.
- **It carries repeat counts like any other done state.** `revisit` is in `set-status.py`'s `DONE_LIKE`, so marking an
  item REVISIT appends to `dones` through `add_pass`, and `roll-done-states.py` writes `data-times` from
  `len(dones) > 1` without looking at the label. A REVISIT item read three times shows the purple dot, the rays and
  the numeral 3 — which is the combination that makes the rail say "done, important, and I keep coming back".
- **Counts as done** everywhere a done total is computed (section pill, section meta, `_nav.js` jump, overall badge):
  `add-tech-item.py`, `english-notes.py`, `roll-done-states.py` all include it. It never rolls: the RECENTLY DONE
  rule leaves REVISIT alone.
- **Sorts before Done.** `reorder-by-status.py` ranks it −1, so in Tech, Theory and Invest the order is **REVISIT <
  done < IMPORTANT < NEW < PLANNED**. Marking an item REVISIT therefore moves it to the top of its section.
- **Rail button:** row 2 is now **Revisit · Repeated · Recently** (the Done button was removed on 2026-09-21, jay: "I don't think I need the Done button"; plain DONE items are reached through All), the Revisit button first — on the list page, on
  every detail page that has the rail buttons (411 of 558; the older Theory pages never had them), and in the
  template `scripts/rtd-shell.mjs`. It shows REVISIT only.
- **REVISIT is sticky under a done pass** (jay, 2026-09-23: "If I set the done again for the number 3 but it should
  remain revisit … so it should be the same format to the done like set the number like DONE items that is done
  several times"). Pressing **Done** on an item that is already REVISIT means "I read it again", not "it stopped
  mattering": the label, the purple and the position all stay, and the pass count goes up. `set-status.py` applies
  the rule when the queue is drained and `_status.js` mirrors it so the dot does not turn green in the browser and
  purple again after the rebuild. To genuinely drop a REVISIT item to plain DONE, pass `--clear-revisit`.
- **From the Edit buttons, on a phone or another browser.** The status overlay (`docs/topics/_status.js`) offers
  `CHOICES = ['done', 'revisit', 'important', 'planned']`, so REVISIT is one tap on the detail page. **A pass is
  recorded per done-day, not per tap** — pressing Revisit twice in one sitting keeps one entry and only moves its
  time; pressing it on a later done-day is what makes the count 2. Two things to expect: the overlay only **queues**
  the change in Firestore, and the built pages stay the truth, so the new numeral appears once the queue is drained
  into the repo (see the weekly drain rule); and the overlay repaints colour, title and number but deliberately does
  **not** recompute `data-times`, because it cannot know the previous done-day from the page alone. So the dot changes
  immediately, the count changes at the drain.
- **How to mark one:** `add-tech-item.py --key <k> --status revisit …` (re-run in place), or `status: revisit` in an
  English item's markdown; then `reorder-by-status.py`. An item older than 2026-09-18 has no "Where it lands in Jayverse"
  section and the script refuses to rebuild it — for those, set `color` `#a855f7`, `label` `REVISIT` and a `done` stamp
  on its `_nav.js` entry by hand, then run `reorder-by-status.py` and `roll-done-states.py`; the roll syncs the rail
  dots, the counts, the overall badge on every page and the `index.html` landing card. There is no cap.
- **The stamp is a done day.** Marking an item REVISIT stamps `done`, and that stamp counts when `roll-done-states.py`
  picks the RECENTLY DONE days (jay, 2026-09-21: "today is KST 09-21"). The item keeps its purple dot and REVISIT
  label, and the roll adds `day: recent` to its `_nav.js` entry, rendered as `data-day` on the rail dot, so the
  **Recently button shows it too** (the filter matches the label *or* `data-day`). It is still never relabelled.

## The explanation goes in the item, not in the reply (jay, 2026-09-25)

jay: "You should add also the explanation into the item. And make it as a rule."

When jay asks for something to be added **and explained**, the explanation belongs **inside the item**. The
chat reply is not the deliverable; it disappears. The item is the record, and it has to stand on its own for
a reader who never saw the conversation — including jay in six months.

- **The test.** Read the item with the reply deleted. If anything jay was told is missing, the item is not
  finished. Nothing may exist only in chat.
- **Where it goes.** Tech / Theory / Invest / Life items: `## Why`, the `### …` sections, and `### Where it
  lands in Jayverse`. English items: `why` / `why_ko` for the frame and `## Techniques` for the moves, with
  `## Expressions` and `## Words` carrying the language itself.
- **The reply may be shorter than the item. It may never be richer.** If a point was worth making in chat it
  was worth writing down; if it was not worth writing down it was padding. Summarising the item in the reply
  is correct. Putting a point only in the reply is the error.
- **Including the caveats.** What was not verified, what is from memory, what is someone else's reasoning
  rather than mine — all of it goes in the item too, not only in the message. A caveat that lives in chat
  protects nobody.
- **Why.** Every item already separates what was reported from what it argues. That separation is worthless
  if the argument itself was delivered somewhere that is not kept. See
  [`raw/README.md`](raw/README.md) and the article-source rule below — same principle, one layer up: the
  record has to hold everything a reader needs to check the claim.

## Every item carries its article source (jay, 2026-09-24)

jay: "whenever you add new items, you should add the article source also." Every new item that has a public
source — an article, a paper, a thread, a repo, a video, a press release — must link to **that source**, not only
to the raw copy of it.

- **How.** `add-tech-item.py --src-url <url> [--src-name <label>]`. It renders a link in the page kicker, next to
  the added date and the channel. `--src-name` is a short label; leave it out and the URL's host is used
  (`hbr.org`, `news.hada.io`, `github.com`).
- **`--source` is not this.** `--source chat | file | gemini` records the **channel it reached jay through**, which
  is a different fact and stays. An item can be `chat` and still have an `hbr.org` source URL; most do.
- **`--raw` is not this either.** The raw file is *our copy* of the source, so it can be reopened after the original
  moves or disappears. `--src-url` is *the original*, so a reader can check the card against it. Items should have
  both: the copy for durability, the link for verification.
- **When there is no public source** — jay's own line, a private paste, a conversation — say so in the raw file and
  leave `--src-url` off. Silence means "no public source", not "nobody looked".
- **Why.** A card that separates what was reported from what it argues is only checkable if the reader can reach
  what was reported. Without the link, every "Verified and unverified" section is an assertion about work nobody
  else can repeat.
- **Backfill.** Items added before 2026-09-24 mostly carry only the channel and the raw copy. Re-running
  `add-tech-item.py` with the same key and `--src-url` upgrades one in place without changing its number.
  **Pass `--date` when you do.** Without it the added date is reset to today and a second `raw/` copy is written
  under today's name, orphaning the original. Ten items were reset this way on 2026-09-24 and restored with
  `--date 2026-09-23`; the orphaned raw copies were removed before they were committed.

## LLM-wiki layers — raw, index, search, bins, interview bank, closing three (jay, 2026-09-21)

The learning-greed item (Tech #1, REVISIT) asked for Karpathy's LLM-wiki layers (Tech #109) on top of this site.
jay: "make the alice Knowledge Notes system aligned with … Let the system hold the index". What exists now:

- **Raw layer — [`raw/`](raw/README.md).** An append-only copy of every source an item was written from (pastes,
  fetched article text, Gemini briefings, the morning reports). `add-tech-item.py --raw <file>` copies it to
  `raw/YYYY-MM-DD-<key>.<ext>` and links it from the kicker as `raw`; a `--raw` path that is already inside `raw/`
  (a morning report that feeds several items) is linked without copying. Never edited; a changed source is a new dated
  file. Items from before 2026-09-21 mostly have none — the page is the record, and that is stated, not hidden.
- **Index — [`index.md`](index.md) and [`index.json`](index.json), generated.** One row per item across every
  section: number, section, status, added date, type, source, bin, English and Korean title, key, raw link (the JSON
  also carries the lead, related item numbers and the key expressions). `scripts/build-index.py` rebuilds both and is
  run at the end of `add-tech-item.py`, `english-notes.py`, `reorder-by-status.py` and `roll-done-states.py`, so the
  index is never older than the last change. Do not edit the generated files.
- **Search — `python3 scripts/notes-search.py <words>`** answers "have I already learned this?" before an item is
  added (all words must match; `--any`, `--section`, `--status`, `--json`). Exit 1 with "new to the site" means go
  ahead. Run it first for every new subject; it replaces remembering.
- **Bins — `--bin deep | converse | file`** in the kicker and the index, set at capture time: *deep* moves the through
  line and gets the hours; *converse* gets one interview sentence and no more until it touches a project; *file* gets
  the card and the Key expressions and is released. Optional; items before 2026-09-21 have no bin.
- **Interview bank — [`interview-bank.md`](interview-bank.md).** `--bin converse --sentence "…"` appends one row
  (item, title, the sentence, date). Rows are never edited; a better sentence is a new row.
- **Closing three.** Each day's `docs/history/YYYY-MM-DD-dev-notes-history.md` ends with a `### Closing three` block:
  what I learned, what is still unclear, the next step (Fraza's three lines, from the learning-greed item). It is
  appended last, after the day's final entry; when a later entry is added the block moves below it. The unclear line
  is tomorrow's first candidate.
- **What did not change:** the wiki is still `docs/topics/*.html`, the schema is still this README, the log is still
  `docs/history/`. No page was regenerated for these layers; only the kickers of items added with `--bin` / `--raw`
  carry the new spans.

## English pages: English first, Korean apart (jay, 2026-09-18)

- Every `english-N.html` has two articles like the PoC pages — `#en` (why, dialogue, key expressions) and `#ko`
  (제목, 상황, 왜, 대화, 협업 기법 세 가지) — with the language switch in the hero and at the top of each article.
  jay: "separate english and korean parts as others so that I don't read the translation first." No Korean line sits
  under an English line any more. `scripts/english-notes.py` renders it from `docs/topics/english/english-N.md`; the
  source format is unchanged (`> 한국어` under each line).

## NEW lasts two business days, Korean calendar (jay, 2026-09-25: "define category New as the new items during two business day based on Korea holiday system"; supersedes the one-week rule of 2026-09-21)

- An item is **NEW** on the day it was added and through the **next business day**. Once **two or more business days**
  have passed since `added`, it rolls to **PLANNED** (grey). So something added on a Monday is NEW Monday and Tuesday
  and grey on Wednesday; added on a Friday it is NEW Friday and Monday and grey on Tuesday.
- **A business day is Mon–Fri that is not a Korean public holiday.** Weekends and 공휴일 do not count, so a long
  holiday holds the New run open. Items added on 2026-09-23 were still NEW on 09-25 because 09-24 and 09-25 were 추석.
- **The holiday table** is [`scripts/kr_holidays.py`](../../scripts/kr_holidays.py) — a hardcoded list, because every
  script here is zero-dependency and runs offline. It **refuses to guess**: asked about a year it has no table for it
  raises, and both callers then leave the item NEW and print a loud warning rather than expiring it wrongly. Lunar
  holidays (설날, 부처님오신날, 추석) and 대체공휴일 move every year, so **each year must be added by hand**, with a
  source. Currently covered: **2026 only.**
- **Two callers, and both had to change.** `reorder-by-status.py` for Tech / Theory / Invest / Life, and
  `english-notes.py` for English, which keeps its own copy because English statuses come from the `.md` files —
  `status: new` is overridden to planned at build time and the file is not rewritten. Changing one and not the other
  is the bug this rule change nearly shipped with.
- **The date it uses:** `added` on the `_nav.js` item, written by `add-tech-item.py`; for English, `added:` in the
  `.md`, or the page's git creation date.
- **Scope:** every section, plus English. LOCKED Health cards are untouched. Important, done and REVISIT never expire;
  only NEW does.
- **Effect when it was introduced:** 63 items rolled on the first run and 360 English items on the second. A week is a
  long time at this posting rate — the New run had stopped meaning "arrived recently" and started meaning "arrived".
- **To keep something NEW longer:** mark it Important, or re-run it with a newer `--date`. Nothing is deleted; a rolled
  item sits at the top of PLANNED, directly under the NEW run.

## Order by status; at most 10 Important per section (jay, 2026-09-18)

- **Every section, since 2026-09-21** (jay: "The number should be in order for all the category 'Important', New, All,
  Revisit, Yesterday, Today"): Life is now sorted by `reorder-by-status.py` like Tech, Theory and Invest, and English
  is sorted by `english-notes.py` — the shown number (1000…) is the position in status order, the file stays
  `english-N.md` and the page `english-N.html`. So each rail button shows one contiguous run of numbers in every
  category. Cost, as in Tech: an item's number moves when its status does, so cite items by key or title, not only by
  number. The Health cards keep their own 1400… numbering at the end of Life.

- In Tech and Theory the numbers follow the status: **done (Done / Yesterday done / Today done) < Important <
  New < Planned**, stable within each rank (jay: "make the important ones have lower number than new ones but higher
  than done"). `scripts/reorder-by-status.py` applies it to `_nav.js`, the rail and cards in `notes.html`, and every
  page's kicker and pager; run it after a status change that should move an item. Life is all NEW; English keeps its
  chronological numbering (2026-09-16).
- **Important is capped at 10 per section** (jay: "make the amount of important items 10 for each category"). When the
  cap was introduced the first 10 in number order stayed red and the rest (Tech 11, Theory 39) became Planned. To
  promote a new item, demote one first.

## Section numbering, goals, and the red badge (jay, 2026-09-18)

- **Numbers start per section:** Tech **1**, Theory **1001**, Invest **1501**, Life **1801**, Eng **2001**, Health **3001** (jay, 2026-09-21: "start Eng from 2001, Theory 1001, Invest 1501, Life 1801" — Eng had grown past 180 items and the earlier 501 / 801 / 901 / 1001 spacing left Life only 99 numbers before Eng. Each section now owns a block of 500 or more: Tech 1–1000, Theory 1001–1500, Invest 1501–1800, Life 1801–2000, Eng 2001–3000, Health 3001–. Health was not named in the request; it moved from 1401 so it stays last and out of Theory's block. Earlier the same day the bases were 501 / 801 / 901 / 1001 / 1401, and before that 500 / 800 / 1300 / 1000 / 1400.) One constant per section in `scripts/notes_numbering.py`; changing it and re-running `reorder-by-status.py`, `english-notes.py` and `health-cards.py` renumbers the whole site
  (jay: "make the Items from 1, Theory from 700, English 1000, Life 1300, Health 1400"). One table in
  `scripts/notes_numbering.py` (`BASE`, `display(navid, k)`, `position(navid, shown)`); `add-tech-item.py`,
  `reorder-by-status.py`, `english-notes.py` and `health-cards.py` all read it, so a number alone tells the section.
  `--slot` in `add-tech-item.py` is still the 1-based position inside the section. Keys and file names do not change
  (`english-1.md` shows as 1000; `health-1.html` as 1400).
- **Goals:** 1,000 items done is the first turning point and 2,000 the final goal (`GOALS` in the same module, mirrored
  in `_progress.js`). When the done count reaches a goal, every page shows a one-time congratulation (confetti + card, dismissed with "Thanks", remembered per browser in
  `localStorage` `milestone-1000` / `milestone-2000`). No progress chip toward the goal (jay: the numbers already tell).
- **The red badge is the "All categories" pill.** Clicking it toggles `body.rail-all` (kept in `sessionStorage`): the
  detail-page rail then lists every section for whichever mode button is on, the badge gets an inset red ring and the
  section pills go dark; clicking a section pill turns it off again (jay: "Make this button clickable and have meaning
  of all category"). The badge always reads `All · 14% · 68/472` — one fixed
  shape, only the tooltip changes (jay: "don't change it when being clicked") (jay: "make it
  clickable and make the clicking shows all the categories … I mean All to the status red area").
- **Section pills select the category** (jay: "these buttons are operational for each category and the section runs
  as category selection"). On a detail page the rail starts on the current item's section; clicking another pill
  shows that section instead (the pill lights up, the rail scrolls to it, the page does not change); clicking the lit
  pill returns to the default. On the list page the default is every section and the pill also jumps to the section in
  the main column. The mode buttons (Important · New · All / Done · Yesterday · Today) filter inside the selected
  category; the red badge's All is the only thing that widens a button to every section.

## Invest section; Foundations → Theory (jay, 2026-09-18)

- New fifth section **Invest** (`sec-invest` / `nav-sec-invest`, numbers from **800**) between Theory and Life: "how to
  invest, the historical recessions or events, and how to analyze the chart with TradingView". Tag chips:
  **Economics** (the economy and its data — every Economics-tagged item moved here from Foundations, jay: "All Economics
  items should go to Investment") and **Invest** (method, history, charts). Add with
  `add-tech-item.py --section invest --tag Economics|Invest`.
- **Foundations is now Theory** (jay: "Make the Foundations shorter with proper name"), numbers from **500**; ids
  `sec-fundamentals` / `nav-sec-fundamentals` unchanged; tags Math | Algorithms. Bases live in `scripts/notes_numbering.py`. The English section
  is labelled **Eng** (jay: "English to Eng"; `LABEL` in `english-notes.py`, ids unchanged).
- First Invest content: ten *basic and important* TradingView chart-reading items (candles, timeframes, support and
  resistance, trend structure, moving averages, volume, RSI, MACD, Fibonacci, risk on the chart), tag Invest, type
  Basics, status Important — which fills the 10-per-section Important cap, so promote a new Invest item only after
  demoting one. Drafts were written from `scratchpad/tv/INSTRUCTIONS.md` (structure = the standard item source).

## Section order: Tech · Theory · Invest · Life · Eng (jay, 2026-09-21: "change the order of Eng and Life")

- Swapped on 2026-09-21 so the numbers ascend down the rail once Life moved to 900 (1 · 500 · 800 · 900 · 1000).
  `english-notes.py` places the Eng rail group, article and pill after Life's; `reorder-by-status.py`'s NEXT map ends
  Invest → Life → Eng. Everything below this line describes the 2026-09-18 order and is kept as history.


- Life is the last section. Generators that need a "next section" marker use the end-of-list sentinels instead
  (`id="no-results"` for the rail, `<p class="src">` for the articles): `add-tech-item.py` (mindset), `reorder-by-status.py`,
  `health-cards.py`; `english-notes.py` inserts the Eng group, article, pill and nav entries *before* Life.
