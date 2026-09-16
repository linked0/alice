# 20 · Design — One fact, one home
title_ko: 사실 하나, 집 하나
situation: The devnet's RPC URL is written in six places across four repos, and two of them disagree. Marek proposes a shared config package; Priya thinks that's overkill for a URL.
situation_ko: devnet의 RPC URL이 네 레포의 여섯 곳에 적혀 있고 그중 둘이 서로 다르다. Marek은 공유 설정 패키지를 제안하고, Priya는 URL 하나에 과하다고 본다.
why: The argument for a single source of truth, made with the cost of the current state rather than the elegance of the proposed one.
why_ko: 단일 진실 원천을 위한 논증. 제안의 우아함이 아니라 현재 상태의 비용으로 설득한다.

## Dialogue
Marek: The devnet URL is in six places and two are wrong. Let's put chains in rails and import from there.
> devnet URL이 여섯 곳에 있고 둘은 틀렸어요. 체인 정보를 rails에 두고 거기서 import합시다.
Priya: It's a URL. A package for a URL is overkill.
> URL 하나잖아요. URL 하나에 패키지는 과해요.
Jay: It's a URL, a chain id, a WebSocket endpoint, an explorer, and the block time, times three chains. That's fifteen facts, and today they have six homes each.
> URL 하나에 체인 id, WebSocket 엔드포인트, 익스플로러, 블록 시간, 그것이 체인 셋. 사실 열다섯 개인데 지금은 각각 집이 여섯이에요.
Priya: Most of them never change.
> 대부분 바뀌지 않아요.
Jay: The devnet address changed twice this week. And the cost isn't editing six files; it's the day we edit five and debug the sixth.
> devnet 주소는 이번 주에 두 번 바뀌었어요. 비용은 파일 여섯을 고치는 게 아니라, 다섯을 고치고 여섯 번째를 디버깅하는 날이에요.
Priya: Fine, but rabbit deploys from source. It can't depend on a local path.
> 알겠어요. 그런데 rabbit은 소스에서 배포해요. 로컬 경로에 의존할 수 없어요.
Jay: Good catch. Then rabbit copies the file and says in the header that rails is canonical. One home for the fact, and the copies know they're copies.
> 잘 잡았어요. 그럼 rabbit은 파일을 복사하고 헤더에 rails가 정본이라고 적어요. 사실의 집은 하나, 복사본은 자기가 복사본임을 알게요.
Marek: I'll add a check that diffs the copy against rails in CI.
> CI에서 복사본과 rails를 diff하는 검사를 추가할게요.
Jay: Then it's a cache with a freshness check, which is the only kind of copy I trust.
> 그러면 신선도 검사가 있는 캐시고, 제가 믿는 유일한 종류의 복사본이에요.

## Techniques
1. **크기를 다시 센다.** "That's fifteen facts, and today they have six homes each." "URL 하나"라는 프레임을 숫자로 교정한다.
2. **비용을 편집이 아니라 디버깅으로 말한다.** "the day we edit five and debug the sixth" 중복의 진짜 비용은 작업량이 아니라 불일치다.
3. **반론을 설계에 흡수한다.** "Good catch. Then rabbit copies the file and says… rails is canonical." 배포 제약을 인정하고 원칙을 지키는 형태를 찾는다.

## Expressions
| six places and two are wrong | 여섯 곳, 그중 둘은 틀림 |
| overkill | 과한 것 |
| fifteen facts with six homes each | 각각 집이 여섯인 사실 열다섯 |
| most of them never change | 대부분 바뀌지 않는다 |
| edit five and debug the sixth | 다섯을 고치고 여섯 번째를 디버깅하다 |
| deploys from source | 소스에서 배포한다 |
| good catch | 잘 잡았다 |
| canonical | 정본인 |
| the copies know they're copies | 복사본이 자기가 복사본임을 안다 |
| a cache with a freshness check | 신선도 검사가 있는 캐시 |
