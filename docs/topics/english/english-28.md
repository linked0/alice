# 28 · Feedback — Telling a senior peer their design is wrong, in writing
title_ko: 시니어 동료의 설계가 틀렸다고 글로 말하기
situation: Jay is two months into a lead role at an Amsterdam fintech. Bram, a staff engineer on a sister team, has circulated a design that puts the ledger's idempotency keys in Redis with a 24-hour TTL. Jay knows from a production incident in Seoul that this loses duplicates after a day. The comment will be read by both teams and Bram's manager.
situation_ko: 암스테르담 핀테크 리드 두 달 차. 자매 팀의 스태프 엔지니어 Bram이 원장의 멱등성 키를 24시간 TTL의 Redis에 두는 설계를 회람했다. Jay는 서울의 프로덕션 장애에서 이것이 하루 뒤 중복을 놓친다는 것을 안다. 코멘트는 두 팀과 Bram의 매니저가 읽는다.
why: Written disagreement across teams is where non-native speakers either soften until nothing lands or sound harsh without meaning to. Dutch directness helps here, but the form still matters: state the failure concretely, give the evidence, propose the fix, and leave the decision with the author.
why_ko: 팀을 가로지르는 글로 된 반대는 비원어민이 아무것도 전달되지 않을 만큼 부드럽게 하거나 의도치 않게 거칠게 들리는 자리다. 네덜란드식 직설이 도움이 되지만 형식은 여전히 중요하다. 실패를 구체적으로 말하고, 증거를 주고, 수정을 제안하고, 결정은 저자에게 남긴다.
status: planned

## Dialogue
Jay (design doc comment): Bram, one blocking concern on section 4, the rest looks solid. A 24-hour TTL on idempotency keys means a retry after 24 hours is treated as a new payment. Retries that late are rare but real: a partner's batch job replayed a 3-day-old file at my last company and we double-paid 212 merchants before anyone noticed.
> Bram, 4절에 블로킹 우려 하나, 나머지는 견고해 보입니다. 멱등성 키에 24시간 TTL을 두면 24시간 뒤의 재시도가 새 결제로 처리됩니다. 그렇게 늦은 재시도는 드물지만 실제로 있습니다. 전 직장에서 파트너 배치 작업이 3일 된 파일을 재전송했고 누군가 알아차리기 전에 가맹점 212곳에 이중 지급했습니다.
Bram: Fair example, but unbounded keys in Redis is a memory problem. What's your proposal?
> 좋은 예지만, Redis에 무제한 키는 메모리 문제예요. 제안이 뭔가요?
Jay: Keep Redis as the fast path, but make the ledger itself the source of truth: a unique constraint on (partner_id, idempotency_key) in Postgres, kept for the retention period we already have for transactions, seven years. Redis TTL can stay at 24 hours because a miss falls through to the database, which rejects the duplicate. Cost is one index and one extra query on the cold path.
> Redis는 빠른 경로로 두되, 원장 자체를 진실의 원천으로 만듭시다. Postgres에 (partner_id, idempotency_key) 유니크 제약을 두고, 거래에 이미 있는 보존 기간 7년을 유지합니다. Redis TTL은 24시간으로 둬도 됩니다. 미스는 데이터베이스로 떨어지고 거기서 중복을 거절하니까요. 비용은 인덱스 하나와 콜드 경로의 추가 쿼리 하나입니다.
Bram: That doubles the write path latency for every payment.
> 그러면 모든 결제의 쓰기 경로 지연이 두 배가 돼요.
Jay: It adds one indexed insert that we're already doing, since the payment row is written anyway; the constraint rides on that write. I measured a similar setup at about 0.4 milliseconds extra at p99. If you'd like, I can put a benchmark in your branch by Thursday so we're arguing about a number rather than an estimate.
> 이미 하고 있는 인덱스된 삽입 하나가 추가되는 겁니다. 결제 행은 어차피 쓰이고, 제약은 그 쓰기에 올라타니까요. 비슷한 구성에서 p99 약 0.4밀리초 추가로 측정했습니다. 원하시면 목요일까지 브랜치에 벤치마크를 넣어 추정이 아니라 숫자로 논쟁하죠.
Bram: Do that. If it's under a millisecond I'll take it.
> 그렇게 하세요. 1밀리초 아래면 받겠습니다.
Jay: Deal. And to be clear, it's your design and your call. I'm flagging it because I've paid for this one already.
> 좋습니다. 그리고 분명히 하면, 당신 설계고 당신 결정입니다. 제가 이미 이 비용을 치러봤기 때문에 표시하는 겁니다.

## Techniques
1. **하나만 블로킹, 나머지는 인정.** "one blocking concern on section 4, the rest looks solid." 리뷰의 범위를 첫 문장에서 정한다. 열 개를 지적하면 하나도 고쳐지지 않는다.
2. **사례는 숫자와 함께.** "replayed a 3-day-old file… double-paid 212 merchants." 추상적 우려는 무시되고, 날짜와 숫자가 있는 사례는 의제가 된다.
3. **추정 대신 측정을 제안한다.** "a benchmark in your branch by Thursday so we're arguing about a number rather than an estimate." 논쟁을 의견에서 데이터로 옮기고, 내가 일을 맡아 상대의 방어를 낮춘다. 그리고 결정권을 돌려준다("your design and your call").



## Words
| one blocking concern | /wʌn ˈblɑkɪŋ kənˈsɝn/ | 블로킹 우려 하나(승인을 막는 문제) |
| rest looks solid | /rɛst lʊks ˈsɑləd/ | 나머지는 견고해 보인다 |
| rare but real | /rɛr bʌt ril/ | 드물지만 실제로 있는 |
| before anyone noticed | /bɪˈfɔr ˈɛniˌwʌn ˈnoʊtəst/ | 누군가 알아차리기 전에 |
| fast path | /fæst pæθ/ | 빠른 경로 / 느린 경로 |
| source of truth | /sɔrs ʌv truθ/ | 진실의 원천 |
| falls through to | /fɔlz θru tu/ | ~로 떨어진다(다음 단계로 넘어간다) |
| I'll take it | /aɪl teɪk ɪt/ | 받겠다(수락) |

## Expressions
| one blocking concern | 블로킹 우려 하나(승인을 막는 문제) |
| the rest looks solid | 나머지는 견고해 보인다 |
| rare but real | 드물지만 실제로 있는 |
| before anyone noticed | 누군가 알아차리기 전에 |
| fast path / cold path | 빠른 경로 / 느린 경로 |
| source of truth | 진실의 원천 |
| falls through to | ~로 떨어진다(다음 단계로 넘어간다) |
| rides on that write | 그 쓰기에 올라탄다(추가 비용 없이) |
| arguing about a number rather than an estimate | 추정이 아니라 숫자로 논쟁하다 |
| I'll take it | 받겠다(수락) |
| your design and your call | 당신의 설계고 당신의 결정 |
| I've paid for this one already | 이 비용은 이미 치러봤다 |
