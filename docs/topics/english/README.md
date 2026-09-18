# English (formerly Dev English) — the language section of Knowledge Notes

One markdown file per conversation, `english-N.md`, rendered by `scripts/english-notes.py` into
the section on `docs/notes.html`, the nav data in `docs/topics/_nav.js`, and one detail page
`docs/topics/english-N.html`. Run the script after adding or editing a file; it is idempotent.

## Rules (jay, 2026-09-16)

- **Grows to 100.** Numbering is chronological and append-only: the newest conversation is `N+1`.
  No reordering by status, unlike the Blockchain section.
- **One per day (jay, 2026-09-18; was one per tech item until then).** The first item added on a KST day
  brings one conversation with it; further items that day do not. It does not have to relate to the
  item. Material from the day's own discussions is fair game.
  does not have to relate to the item. Material from the day's own discussions is fair game.
- **From #21 on: getting a job abroad.** Conversations a developer and team lead needs to be hired
  and to lead in English — interviews (system design, behavioural, take-home debrief), salary and
  offer negotiation, first weeks on a foreign team, running standups and one-on-ones, giving and
  receiving feedback, disagreeing with a manager, presenting to stakeholders. Critical and
  concrete: real stakes, real numbers, the sentence that wins or loses the moment.
- **Status** is set in the file header (`status: planned | done | recent | important | new`);
  default `planned`. Mark `done` when jay says so.

## File format

```
# N · Tag — Title
title_ko: 한국어 제목
situation: one or two sentences, English
situation_ko: 같은 내용, 한국어
why: why this conversation is worth learning
why_ko: 한국어
status: planned

## Dialogue
Speaker: English line
> 한국어 번역 (바로 아래 줄)

## Techniques
1. **기술 이름.** 설명 — 영어 문장을 인용해서 (Korean)

## Expressions
| english expression | 뜻 · 쓰이는 자리 |
```

Tags so far: Review, Design, Incident, EIP, BD, Ops, Planning, 1:1. Add new ones freely
(Interview, Negotiation, Onboarding, Standup, Stakeholders …).
