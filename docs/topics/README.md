# Knowledge Notes (formerly Tech Notes, renamed 2026-09-18) — how items are added

`docs/notes.html` is hand-maintained HTML with four sections: **Tech** (formerly "Blockchain & Tech"),
**Fundamentals**, **Mindset**, **English** (formerly "Dev English"). `docs/topics/_nav.js` is the source of truth for numbering and
status; `docs/topics/_progress.js` paints the rail badges from it. Each item has a detail page in
`docs/topics/`.

## Anything jay mentions is a candidate item (jay, 2026-09-18)

- When jay mentions or pastes an item, a note, an article, a talk, or a number in conversation, treat it
  as an item for Knowledge Notes without waiting for the words "add this item": pick the section
  (Tech, Fundamentals, Mindset), draft it, and say so in the reply. jay still decides whether it
  stays; the default is to add, not to ask. Questions clearly marked "just asking" are the
  exception: answer them, and offer the item in one line.

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
  Fundamentals items use the same script with `--section fundamentals --tag Math|Algorithms|Economics`;
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
  file. Content jay pastes that is itself a candidate from that day's alice-tech file is tagged
  `file` (its subject came from the file; the paste is how it was pointed at). Card: `<span class="topic-src">`; kicker: `#N · PoC · YYYY-MM-DD · chat`. Pass `--source`.
- Every item: English and Korean copy text as JSON on the card and the page; page body generated
  from the copy text so they cannot diverge; a "Verified and unverified" closing section with
  sources.
- Counters agree in three places: rail pill, section meta, `_nav.js` jump. On a new KST day,
  append the previous day's closing totals to `progress` in `_nav.js` before changing counts.

## Mindset (jay, 2026-09-18)

- The third knowledge section: ways of thinking and psychological insight for doing good work and
  living well with it — talks, interviews, essays, books, distilled. Not tooling, not news; the
  test is whether the item still applies when the tools change.
- Added with the same script: `--section mindset --type Talk` (or Essay / Book / Interview).
  Numbering is chronological and append-only, like Dev English. Same date and source tag, same
  EN + KO copy text, same "Why / How it works / Where it lands in Jayverse" body.
- Sits before Dev English in the page so `scripts/english-notes.py`, which re-appends its own
  section last, keeps working unchanged. English conversations follow the once-a-day rule, not one per Mindset item.

## English (Dev English)

One conversation per day (jay, 2026-09-18; until then it was one per new item): the first item request of a KST day also adds one English conversation, later items that day do not. Rules and format in [english/README.md](english/README.md).

## Key expressions on every detail page (jay, 2026-09-18)

- Every Tech, Fundamentals and Mindset detail page ends with a **Key expressions** table (Korean
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
  (domain terms, idioms, collocations, phrasal verbs, prepositions); skip bare proper nouns and words
  that are the same in Korean transliteration.
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
