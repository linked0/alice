| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| local cache | 로컬 캐시(원본을 내 기기에 복사해 두고 거기서 읽는 것) · gadak의 전체 구조. "a local cache for Jira and Confluence" |
| round trip | 왕복(요청이 서버에 갔다 오는 한 번의 비용) · 네트워크 지연을 말할 때. "pays a round trip per query" |
| rate limit | 레이트 리밋(일정 시간 안에 허용되는 요청 수 상한) · API가 끊기는 지점. "got cut off by a rate limit mid-task" |
| pagination | 페이지네이션(결과를 여러 페이지로 쪼개 주는 방식) · 집계가 느려지는 진짜 이유. "a statement about pagination" |
| GROUP BY | 그룹 바이(기준 컬럼으로 묶어 집계하는 SQL 절) · 에픽별 집계 쿼리. "answers it as one GROUP BY" |
| median | 중앙값(값을 줄 세웠을 때 한가운데 값; 평균보다 이상치에 강함) · 벤치마크 보고 단위. "Medians, measured 2026-08-26" |
| system of record | 기록의 원본(진실로 취급되는 시스템) · 캐시가 넘보면 안 되는 자리. "claiming to be the system of record" |
| stale | 오래된·낡은(원본보다 뒤처진 상태) · 캐시의 본질적 한계. "the cache is stale by however often you sync" |
| write path / read path | 쓰기 경로 / 읽기 경로 · 캐시 설계의 핵심 구분. "The cache is a read path, not a replacement" |
| queued locally | 로컬에 쌓아 두다(나중에 보내려고 대기시키다) · 오프라인 편집 방식. "Nothing is queued locally to be flushed later" |
| reconciliation | 정합성 맞추기(어긋난 두 상태를 다시 일치시키는 일) · 오프라인 쓰기의 대표 난제. "no offline-edit reconciliation problem" |
| attributed to | ~의 이름으로 기록되다 · 감사 추적에서. "attributed to the agent's name" |
| audit trail | 감사 기록(누가 무엇을 언제 했는지 남는 흔적) · 에이전트 작업의 책임 소재. "the audit trail does not quietly credit the human" |
| empty result set | 빈 결과 집합(행이 0개인 정상 응답) · 오류와 구별해야 하는 것. "it returns an empty result set" |
| confident negative | 확신에 찬 부정(근거 없이 "없다"라고 단정하는 답) · 에이전트의 실패 방식. "for an agent it is a confident negative" |
| transferable lesson | 옮겨 쓸 수 있는 교훈(다른 맥락에도 적용되는 배움) · 사례에서 규칙을 뽑을 때. "This is the transferable lesson" |
| well formed | 제대로 만들어진(문법·어휘가 유효한) · 쿼리를 신뢰하기 전 조건. "prove the query was well formed" |
| disclosure scope | 공개 범위(밖으로 나갈 수 있는 정보의 경계) · 프라이버시 판단. "Cache scope is disclosure scope" |
| second-order effect | 2차 효과(직접 결과가 다시 낳는 결과) · 설계 변화의 파급. "the second-order effect on the agent" |
| unglamorous | 화려하지 않은·수수한 · 해법이 단순할 때 쓰는 칭찬. "The fix is unglamorous" |
