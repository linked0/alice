# Knowledge Notes (formerly Tech Notes, renamed 2026-09-18) — how items are added

`docs/notes.html` is hand-maintained HTML with four sections: **Tech** (formerly "Blockchain & Tech"),
**Foundations** (renamed from Fundamentals 2026-09-18; ids `sec-fundamentals` / `--section fundamentals` unchanged), **Life**, **English** (formerly "Dev English"). `docs/topics/_nav.js` is the source of truth for numbering and
status; `docs/topics/_progress.js` paints the rail badges from it. Each item has a detail page in
`docs/topics/`.

## Anything jay mentions is a candidate item (jay, 2026-09-18)

- When jay mentions or pastes an item, a note, an article, a talk, or a number in conversation, treat it
  as an item for Knowledge Notes without waiting for the words "add this item": pick the section
  (Tech, Foundations, Life), draft it, and say so in the reply. jay still decides whether it
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
  Foundations items use the same script with `--section fundamentals --tag Math|Algorithms|Economics`;
  they append at the end of the section (numbering there is curriculum order, not done-first) and get
  the same date and source tag (jay, 2026-09-18, first item #193).
  does the whole insert (nav data, card with date, detail page, renumbering, pager, counters).
  Re-run with the same key to replace an item in place.

- Done items first. The newest report takes the first not-done slot; items after it shift by one.
  Detail pages' `#N` kicker and prev/next pager are rebuilt after every insert.
- Dot colors: `#22c55e` DONE, `#38bdf8` RECENTLY DONE, `#ef4444` IMPORTANT, `#64748b` PLANNED,
  `#eab308` NEW. Mark done only when jay says so.
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

- Every Tech, Foundations and Life detail page ends with a **Key expressions** table (Korean
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

- Every Tech, Foundations and Life page closes its body with **Where it lands in Jayverse** (Korean:
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
- Their text is not in the repo: the plaintext lives outside it at `~/Documents/Private/life-health-rules.md`
  (one `## Health N — title` heading per item, `### en` / `### ko` blocks), and
  `HEALTH_PASS='…' node scripts/health-encrypt.mjs <that file>` writes only ciphertext (AES-256-GCM, PBKDF2-SHA256
  600k) to `docs/topics/_health.js` and then runs `scripts/health-cards.py`, which rewrites the cards and rail links
  in `notes.html` between `<!-- health-nav -->` / `<!-- health-cards -->` markers and regenerates the `health-N.html`
  pages. The password is never written to a file; `add-tech-item.py` leaves these cards alone (no key in `_nav.js`,
  numbers are not renumbered).

## TODAY DONE / YESTERDAY DONE — the two fresh done states (jay, 2026-09-18)

- When an item is marked done it becomes **TODAY DONE** (midnight blue, `#191970`) and stays so until the first item
  of the *next* day is marked done; then it becomes **YESTERDAY DONE** (sky blue, `#38bdf8`; jay, 2026-09-18:
  "add the other day done status of which name tells everything") for one more done-day, and then plain **DONE**
  (green; Foundations blue). jay renamed the states from "lately done" / "done the other day" to **Today done** /
  **Yesterday done** ("아예 change …"); "yesterday" means the previous day on which something was done, which is not
  always the calendar yesterday. "The other day" means the previous day on which something was done, not necessarily
  yesterday. A day starts at
  **06:00 KST** (jay: "done from the 6 a.m. today before the new day's first one is done"). This replaces the old
  RECENTLY DONE (sky blue), which never rolled over.
- Mechanics: `add-tech-item.py --status recent` (alias `today`; `--done-at` to override the time) stamps `done`
  (ISO, +09:00) on the `_nav.js` item; English items take `status: recent` + `done: <ISO +09:00>` in
  `docs/topics/english/english-N.md`, which `english-notes.py` carries into `_nav.js`. Both scripts then run
  `scripts/roll-done-states.py`, which buckets every stamped item by `(done − 6h).date()`, keeps the newest bucket as
  TODAY DONE and the one before it as YESTERDAY DONE, relabels the rest DONE, syncs every rail dot in `notes.html`
  with `_nav.js`, and collapses duplicate rail entries. The roll script is safe to run alone.
- Rail buttons in two rows — **Important · New · All** / **Done · Yesterday · Today** (a `.tier-break` span forces the
  break; list page, every detail page, template `rtd-shell.mjs`): Done = plain DONE only, i.e. finished before yesterday (jay, 2026-09-18: "Add done button also" … "Done before
  Yesterday"), Today = TODAY DONE only, Yesterday = YESTERDAY DONE only, **Important = IMPORTANT only** (jay,
  2026-09-18: "make the important button only shows important"; the 2026-09-08/09 rule that Important also showed new
  and recently done items is retired). Each button shows exactly one state, inside the selected category (see the pills rule below). The state labels changed everywhere, including the page template `scripts/rtd-shell.mjs`.

## English pages: English first, Korean apart (jay, 2026-09-18)

- Every `english-N.html` has two articles like the PoC pages — `#en` (why, dialogue, key expressions) and `#ko`
  (제목, 상황, 왜, 대화, 협업 기법 세 가지) — with the language switch in the hero and at the top of each article.
  jay: "separate english and korean parts as others so that I don't read the translation first." No Korean line sits
  under an English line any more. `scripts/english-notes.py` renders it from `docs/topics/english/english-N.md`; the
  source format is unchanged (`> 한국어` under each line).

## Order by status; at most 10 Important per section (jay, 2026-09-18)

- In Tech and Foundations the numbers follow the status: **done (Done / Yesterday done / Today done) < Important <
  New < Planned**, stable within each rank (jay: "make the important ones have lower number than new ones but higher
  than done"). `scripts/reorder-by-status.py` applies it to `_nav.js`, the rail and cards in `notes.html`, and every
  page's kicker and pager; run it after a status change that should move an item. Life is all NEW; English keeps its
  chronological numbering (2026-09-16).
- **Important is capped at 10 per section** (jay: "make the amount of important items 10 for each category"). When the
  cap was introduced the first 10 in number order stayed red and the rest (Tech 11, Foundations 39) became Planned. To
  promote a new item, demote one first.

## Section numbering, goals, and the red badge (jay, 2026-09-18)

- **Numbers start per section:** Tech **1**, Foundations **700**, English **1000**, Life **1300**, Health **1400**
  (jay: "make the Items from 1, Foundations from 700, English 1000, Life 1300, Health 1400"). One table in
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
