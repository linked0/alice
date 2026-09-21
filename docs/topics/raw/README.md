# Raw layer — sources as they arrived, never edited

The first of Karpathy's three layers (raw → wiki → schema; Tech #109, applied in the learning-greed item of
2026-09-19): a copy of every source a Knowledge Notes item was written from, kept so the source can be
**reopened instead of re-remembered**. The wiki is `docs/topics/*.html`; the schema is
[`../README.md`](../README.md); the log is `docs/history/`; the index is [`../index.md`](../index.md).

Rules (jay, 2026-09-21: "make the alice Knowledge Notes system aligned with … Let the system hold the index"):

- **Append-only.** A file here is written once and never edited, reformatted or "cleaned". If a source
  changes, add a new dated copy. `add-tech-item.py --raw <file>` copies without overwriting.
- **Name:** `YYYY-MM-DD-<item key>.<ext>` for a source behind one item; `YYYY-MM-DD-gemini-youtube*.md`
  for a Gemini briefing (one briefing feeds several items); `YYYY-MM-DD-alice-tech-report.md` for the
  morning blockchain report (the date is the report's own date, one day before it is read).
- **What belongs here:** pasted briefings, fetched article text (as plain text, tags stripped), Gemini
  files, the morning reports. The item page's kicker links to it as `raw`, and `index.json` carries the path.
- **What never belongs here:** the Health rules, anything from `~/Documents/Private`, passwords, keys,
  or any file jay did not mean to publish. The repo is public documentation.
- **Not every item has a raw file.** Items written from a chat paste before 2026-09-21 have none; the
  transcript is gone and the item is the record. That is stated, not hidden.

| File | Feeds |
|---|---|
| `2026-09-14…20-alice-tech-report.md` | Tech items with source `file` on those days (the exact report per item was not logged before 2026-09-21, so the pages do not link them) |
| `2026-09-18-gemini-youtube*.md` | Tech #60–#63 of that day (now renumbered), Life harris-you-did-not-author-your-last-thought, eat-the-same-dish-twice-tokyo — see `../gemini-checked.md` |
| `2026-09-21-gemini-youtube.md` | Invest 820, Tech moe / rag / embeddings items, Life 1331–1332 |
| `2026-09-20-galaxy-brain-resistance-principles-with-teeth.txt` | Tech galaxy-brain item (Vitalik, tags stripped, 4,790 words) |
| `2026-09-21-ethlabs-week13-quick-slots-blobs-aa-migration.txt` | Tech Ethlabs week 13 item (X Article via the public tweet API) |
| `2026-09-21-alice-tech-report.md` | Tech staking-queue item (`--raw` pointing at a file already in `raw/` links it without copying) |
| `2026-09-21-english-38.txt` | Eng #38 connecting-vs-transfer (조선일보 윤희영 칼럼 발췌, jay가 채팅에 붙여넣음; URL 미수집) |
| `2026-09-21-english-39.txt` | Eng #39–#78 (NAVER 영어단어장 첫 내보내기, 카드 20장 = 항목 40개) |
| `2026-09-21-english-79.txt` | Eng #79–#182 (NAVER 영어단어장 둘째 내보내기, 2~4쪽 + 마지막 카드; 반복 카드는 원래 항목에 합침) |
| `2026-09-21-english-183.txt` | Eng #183–#397 (NAVER 영어단어장 셋째 내보내기, 전체 뷰 228장, 메모 없음 → 카드 한 장 = 항목 한 개) |
