# 2026-09-25 · alice

관련 문서: `docs/topics/README.md` (아이템 작성 규칙 — 이 날 세 절이 추가·교체됨).
별도의 태스크/설계 문서 없이 jay의 채팅 지시로 진행된 하루라, 각 항목이 그 지시를 인용한다.

### 독서 목록 다섯 개를 한 카드로 병합 (#1821)

**Cause** jay: "Can you merge the book times into one?" — Life 섹션에 한 사람의 독서 목록을 담은 카드가 다섯 개(#1826–#1830) 흩어져 있었다.
**Reasoning** 다섯을 따로 두면 비교가 불가능한데, 비교가 값어치의 전부다. 각 목록에 **명시된 선별 기준**이 붙어 있었고 그 기준들이 서로 다르다. 옮겨지는 것은 마흔다섯 개의 제목이 아니라 다섯 개의 기준이다.
**Change** `scripts/remove-item.py`를 새로 작성(이 저장소 최초의 아이템 제거 도구, dry-run 기본, raw/ 보존). 다섯을 제거하고 `the-rule-not-the-list` 한 장으로 합쳤다.
**Result** Life #1821. 다만 제거 후 점검에서 **다섯 모두 raw 파일이 없었다** — raw 레이어(2026-09-21 시작)보다 먼저 만들어진 카드들이라 상세 페이지 자체가 기록이었다. 그 사실을 병합 카드의 raw에 남겼고, 책별 세부는 이제 git 이력에만 있다.

### NEW는 한국 영업일 2일 (전 저장소 규칙 변경)

**Cause** jay: "Can you define category 'New' as the new items during two business day based on Korea holiday system".
**Reasoning** 7일 달력 기준은 연휴가 끼면 실제 체감과 어긋난다.
**Change** `scripts/kr_holidays.py` 신규(2026년 공휴일 표, 의존성 없음, 미수록 연도는 예외를 던진다). `reorder-by-status.py`와 `english-notes.py` **양쪽**을 수정.
**Result** 63개 아이템 + 영어 360개가 PLANNED로 롤오버. **두 곳에 같은 규칙이 복제돼 있던 것이 함정**이었고 — 한쪽만 고쳤다면 영어 401개가 영원히 NEW였다 — README에 그 사실을 기록했다.

### 목록 카드 다섯 장 추가 (#1822–#1827)

**Cause** jay가 붙여넣은 다섯 뭉치: 가디언 이름을 단 소설 100선, NYT 21세기 책 100선(한국 서점판), NYT 21세기 영화 100선, 일본 미디어 예술 100선 만화/애니메이션.
**Reasoning** 전부 "목록"이라는 같은 물건이고, 계열로 묶으면 서로를 검증한다.
**Change** 각각 카드로 작성. 검증에서 나온 것들:
- **가디언 목록은 가디언 것이 아니다.** 실제 목록(맥크럼, 2015)을 받아와 대조 — 영어 전용, 연대순, 톨스토이·프루스트·『빌러비드』·한강 없음. "한강이 유일한 아시아 작가"라는 주석도 **그 목록 자신의 내용으로 반박**된다(이시구로·루슈디·로이·미스트리·나이폴).
- **일본 미디어 예술 100선은 4부문 × 25편**이고, **공식 25편 = 일반 순위 상위 25편**임을 위키백과의 무순위 25편과 대조해 확인했다(양 부문 모두 정확히 일치). 따라서 26~50위는 "표는 받고 떨어진" 목록이다.
- 애니 전문가 목록 끝의 〈마운틴 헤드〉는 2025년 영어 실사 영화라 **붙여넣기 오염**으로 판단, 제외하고 그 사실을 raw에 남겼다.
**Result** Life #1822–#1827.

### 아이템 규칙 세 가지 문서화

**Cause** jay의 지시 세 건.
**Change** `docs/topics/README.md`에 추가: (1) 모든 아이템은 **원문 출처 링크**를 갖는다(`--src-url`, `add-tech-item.py`에 인자 추가), (2) **채팅에서 한 설명은 아이템 안에 들어가야 한다** — "답장을 지우고 아이템만 읽었을 때 빠진 게 있으면 아이템이 완성되지 않은 것", (3) NEW 2영업일 규칙.
**Result** 세 규칙 모두 시행 중. (1)의 백필 중 `--date` 누락으로 10개 아이템의 added가 오늘로 바뀌고 고아 raw 파일이 생긴 사고가 있었고, 되돌린 뒤 그 함정도 README에 적었다.

### Life 섹션에 태그 칩 도입

**Cause** jay: "Can you add book or something proper flag for Life items as the Theory items do like MATH, Algorithms".
**Reasoning** Theory는 칩이 있는데 Life는 없어서 47개 카드가 구분되지 않았다.
**Change** `add-tech-item.py`가 mindset 섹션에서도 `--tag`를 받도록 하고(값이 없으면 칩을 찍지 않는다), `scripts/set-life-tag.py`를 새로 작성해 기존 42개를 백필. 어휘: Book · Film · Manga · Anime · Work · Mind · Body · People.
**Result** Life 전 항목에 칩. 이어서 jay 요청으로 **Book·Film·Manga·Anime 네 개를 한 색(앰버)으로** 묶었다 — `scripts/tag-colors.py`, 칩 1,985개에 `data-tag` 속성 추가. 이 과정에서 **여섯 개 스크립트가 옛 칩 모양을 박아두고 있었고**, 그중 `reorder-by-status.py`와 `build-index.py`는 **오류 없이 잘못 동작**할 뻔했다(칩이 제목으로 새거나 인덱스에서 태그가 전부 소실). 전부 수정하고 재생성으로 검증.

### 목록 카드를 한국어 전용으로, 번호를 인접하게

**Cause** jay: "For all book items, I don't need english version" / "make place book items as near as possible … I meant book, film, anime".
**Reasoning** 번호는 상태순 정렬을 따르고 그 정렬은 안정적이므로, **자유 변수는 상태 블록 안의 순서뿐**이다.
**Change** 여섯 카드를 한국어 파일 하나로 EN/KO 양쪽에 넣고(생성기가 한국어 제목 `## 왜`·`Jayverse에서의 위치`를 받도록 수정), `scripts/move-in-status-block.py`로 NEW 블록 끝과 PLANNED 블록 앞으로 모았다.
**Result** #1821–#1828 연속 여덟. #1807(IMPORTANT)만 떨어져 있고, 그건 상태를 바꿔야 해서 jay 판단으로 남겼다.

### 왼쪽 레일이 클릭할 때마다 움직이던 문제 — 세 번 만에 원인을 맞춤

**Cause** jay: "if the item is in the window, don't blink the list by redrawing" → "it blinks yet" → "make it not scroll, for that timing".
**Reasoning / 세 단계**
1. **첫 시도(틀림)** — 로드 시 가운데 정렬에 "이미 보이면 건드리지 말 것" 가드를 넣었다. 스크롤 스파이 쪽에는 2026-08-27부터 있던 가드인데 로드 경로에만 없었다. 진짜 버그였지만 jay가 본 버그는 아니었다.
2. **두 번째(다른 진짜 버그)** — 상세 페이지의 레일 컨테이너는 **비어 있는 채로 나가고** 975개 항목을 `</body>` 근처 스크립트가 채운다. 빈 패널을 칠했다가 다시 칠하는 것. `scripts/rail-before-paint.py`로 `_nav.js`와 빌더를 `</nav>` 바로 뒤로 옮겨 페인트 전에 DOM이 존재하게 했다.
3. **세 번째(진짜 원인)** — **어떤 가시성 검사도 이길 수 없었다.** 클릭은 새 페이지를 띄우고 그 레일은 scrollTop=0에서 시작하므로, 방금 보이던 항목이 **진짜로** 화면 밖이다. 검사 대상 상태를 페이지 이동이 파괴한다.
**Change** `scripts/rail-keep-position.py` — 레일이 sessionStorage에 스크롤 위치를 저장하고 다음 페이지에서 복원한다. 가운데 정렬은 **저장된 위치가 없는 첫 진입에만** 남겼다. 위치는 섹션별로 저장하고 같은 섹션 이동에서만 넘긴다(섹션마다 보이는 목록이 다르다).
**Result** 클릭해도 패널이 전혀 움직이지 않는다. 부수 효과로 **두 생성기가 조용히 깨질 뻔한 것**을 잡았다 — 둘 다 템플릿을 `<script src="_nav.js">` 리터럴로 자르고 `__NAV_CURRENT__`를 tail에서 치환하고 있었는데, 그 문자열을 내가 옮겼으므로 이후 생성되는 모든 페이지가 **템플릿의 키를 물려받아 엉뚱한 항목을 활성 표시**했을 것이다. 첫 패치에서 여는 `<script>` 태그를 정규식이 삼킨 것도 태그 개수 대조로 잡아 되돌렸다.

### Eng #2006 보강 — reconciliation, work around, 그리고 두 개의 no

**Cause** jay의 질문 네 건(설명은 채팅이 아니라 아이템에 들어가야 한다는 규칙 적용).
**Change** `english-24.md`에 기법 4~7 추가: `work around` + 사람(장애물 취급의 뉘앙스), `reconciliation`의 회계 의미(대사·對査)와 감사에서의 무게, `even when the answer is no`의 주어가 **리더**라는 점(jay가 부하로 오해 — 내 한국어가 목적어를 빠뜨려 그렇게 읽혔다), 그리고 Fiona의 두 가지 no(협상의 no "That's a lot of unpaid consulting", 기술의 no "Don't.").
**Result** 대화 속 한국어 번역도 "정합성 검증 시스템" → "대사(對査) 시스템"으로 교정. Jay의 약속이 **이 장면에서는 아직 시험되지 않았다**는 한계도 명시했다.
