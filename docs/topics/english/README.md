# English (formerly Dev English) — the language section of Knowledge Notes

One markdown file per conversation, `english-N.md`, rendered by `scripts/english-notes.py` into
the section on `docs/notes.html`, the nav data in `docs/topics/_nav.js`, and one detail page
`docs/topics/english-N.html`. Run the script after adding or editing a file; it is idempotent.

## Rules (jay, 2026-09-16)

- **Grows without a cap** (was "grows to 100" until 2026-09-21, when the word book took Eng past 180). Numbering is chronological and append-only: the newest conversation is `N+1`.
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
- **`pin: true`** (선택, jay 2026-09-21: "Make it first") — 같은 status 묶음 안에서 맨 앞에 둔다. 없으면 묶음은 파일 번호순이라 새로 추가한 항목이 항상 뒤에 붙는다. status 사이의 순서(REVISIT < done < IMPORTANT < NEW < PLANNED)는 바꾸지 않으므로, new 항목이 done 항목을 앞지를 수는 없다.
- **바깥 글에서 온 항목의 저작권 (jay, 2026-09-21).** 저작권이 있는 기사(이코노미스트 등)는 본문을 저장소에 옮기지 않는다. 항목에는 제목과 정확한 출처, 내가 쓴 요약, 기사의 수치, 짧은 인용, 표현·어휘만 담고 raw 파일은 만들지 않으며 `source:`에 그 사실을 적는다. 저장소가 공개라서 암호화해 두어도 결국 공개 배포다.
- **Status** is set in the file header (`status: planned | done | recent | important | new`);
  default `planned`. Mark `done` when jay says so.
- **Source, when the conversation came from an outside text (jay, 2026-09-21).** Three optional header
  keys: `source:` / `source_ko:` — the full citation (author, title, publication, date; say plainly what
  was taken from it and what was written on top) — and `raw:` — the filename of an append-only copy of
  the source under [`../raw/`](../raw/README.md). The script renders a `raw` link in the kicker and a
  Source / 출처 block at the end of both articles. Omit all three when the conversation is written from
  scratch or from the day's own discussion. Never invent a URL that was not captured.

## File format

```
# N · Tag — Title
title_ko: 한국어 제목
situation: one or two sentences, English
situation_ko: 같은 내용, 한국어
why: why this conversation is worth learning
why_ko: 한국어
status: planned
source: 저자, "제목", 매체, 날짜 — 무엇을 가져왔고 무엇을 새로 썼는지 (선택)
source_ko: 같은 내용, 한국어 (선택)
added: YYYY-MM-DD — 추가한 날 (선택; 없으면 이 .md 파일이 git에 들어간 날을 쓴다. 키커와 _nav.js에 표시, 2026-09-21)
status: new — 오늘 쓴 대화는 new (jay, 2026-09-21: "should be shown with Eng and New buttons selected"); added 로부터 7일이 지나면 파일은 그대로 두고 planned 로 표시된다
raw: YYYY-MM-DD-english-N.txt (선택; docs/topics/raw/ 안의 원본 사본)

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

## NAVER 단어장 카드는 항목 두 개다 (jay, 2026-09-21)

- jay의 NAVER 영어단어장 카드 한 장에는 **단어**(사전 표제어)와 **메모의 문장**(드라마 자막 한 줄을 분석한 노트)이 있고,
  둘은 서로 무관하다. 카드 한 장 = **Eng 항목 두 개**: 태그 `Word`(단어)와 `Line`(문장), 카드 순서대로 번호를 잇는다.
  카드 20장 = 항목 40개. jay: "20장의 카드가 단어와 메모에 무관한 문장 항목이 있어 … 이제부터 두개를 분리해서 생각해
  … Eng 카테고리에 40개를 추가하라는 얘기였음." 한 항목에 표로 모으는 것이 아니다. 각 항목은 짧은 대화(4~6줄), 기법
  1~2개, 표현 2~4줄이고 `source:`에 카드 번호와 단어/문장을 적으며 `raw:`는 내보낸 전문 하나를 함께 가리킨다. 메모가 앞
  카드의 문장을 반복하면 그 메모가 든 둘째 표현을 쓴다. 본보기: Eng #39~#78 (2026-09-21).
- **합치기 (jay, 2026-09-21: "if there are already the same item you can ignore or merge it to the original one").** 둘째 내보내기(#79~#182)에서 정한 규칙:
  - 카드의 단어나 메모가 이미 항목으로 있으면 새 항목을 만들지 않고, 원래 항목의 `source:`에 "둘째 내보내기에도 반복됨"을 한 줄 덧붙인다 (#41, #54, #67~#71, #73, #74, #77, #78).
  - 사전만 다른 같은 표제어(manslaughter / voluntary manslaughter, mess with ×3, condescend to ×2, snuff / snuff out)는 Word 항목 하나로 합치고 `source:`에 카드를 모두 적는다.
  - 한 카드의 단어가 다른 카드의 문장에 그대로 들어 있으면(infatuated) 그 Line 항목으로 합친다.
  - 메모가 문장이 아니라 용어 한 줄이면(footgun, on-ramp) 그 용어를 `Word` 태그 항목으로 만들고 `source:`에 "memo"라고 적는다; 메모가 앞 카드의 문장을 다시 풀이하면 그 메모의 자기 예문을 쓴다(generic you → "You never know what might happen."); 메모에 영어 문장이 없으면(betaxolol의 KBS 기사 메모) Line 항목은 없고 `source:`에 그렇게 적는다.
- **메모 없는 카드는 항목 하나다 (jay, 2026-09-21, 셋째 내보내기 = 전체 뷰 228장).** 단어장의 `전체` 뷰에는 암기메모가 없는 카드가 대부분이다. 표제어와 뜻만 있거나 예문과 번역만 있으므로 **카드 한 장 = 항목 한 개**이고, 표제어·구·숙어면 `Word`, 완결된 문장이면 `Line`이다. 메모가 없어 쓸 재료가 적으므로 이 항목들은 영어 200~330단어로 #39~#182보다 짧게 쓴다. 사전만 다른 같은 표제어나 같은 숙어의 두 예문은 위 합치기 규칙대로 한 항목으로 묶는다. 본보기: Eng #183~#397 (228장 → 215개; parlay into·condescend·whittle down·deed 네 장은 이미 항목이라 원래 항목에 표시만 했다).

