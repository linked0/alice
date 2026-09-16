# Tech Notes — how items are added

`docs/notes.html` is hand-maintained HTML with three sections: **Blockchain & Tech**,
**Fundamentals**, **Dev English**. `docs/topics/_nav.js` is the source of truth for numbering and
status; `docs/topics/_progress.js` paints the rail badges from it. Each item has a detail page in
`docs/topics/`.

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

## Blockchain & Tech conventions

- **Tooling:** `python3 scripts/add-tech-item.py --key <key> --slot <N> --en en.md --ko ko.md [--status new] [--date]`
  does the whole insert (nav data, card with date, detail page, renumbering, pager, counters).
  Re-run with the same key to replace an item in place.

- Done items first. The newest report takes the first not-done slot; items after it shift by one.
  Detail pages' `#N` kicker and prev/next pager are rebuilt after every insert.
- Dot colors: `#22c55e` DONE, `#38bdf8` RECENTLY DONE, `#ef4444` IMPORTANT, `#64748b` PLANNED,
  `#eab308` NEW. Mark done only when jay says so.
- **Added date (jay, 2026-09-16, from #54 on):** the KST date the item was added appears on the
  card head (`<span class="topic-date">YYYY-MM-DD</span>`, right-aligned after the title) and in
  the detail page kicker after the type (`#N · PoC · YYYY-MM-DD`). Older items carry no date.
- Every item: English and Korean copy text as JSON on the card and the page; page body generated
  from the copy text so they cannot diverge; a "Verified and unverified" closing section with
  sources.
- Counters agree in three places: rail pill, section meta, `_nav.js` jump. On a new KST day,
  append the previous day's closing totals to `progress` in `_nav.js` before changing counts.

## Dev English

One conversation per new tech item; rules and format in [english/README.md](english/README.md).
