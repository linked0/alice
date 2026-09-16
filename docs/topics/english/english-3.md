# 3 · Incident — Every transaction passed. The total was wrong.
title_ko: 모든 트랜잭션은 통과했다. 총량이 틀렸다.
situation: The bridge minted more jUSD than it locked, and nothing alarmed for days. The postmortem is about why nobody noticed, not who pushed the button.
situation_ko: 브리지가 잠근 것보다 많은 jUSD를 발행했고 며칠간 아무 알람도 없었다. 포스트모템의 주제는 누가 버튼을 눌렀는가가 아니라 왜 아무도 몰랐는가다.
why: The vocabulary of invariants, halts, and false positives, and the sentence that turns a dead end into a finding.
why_ko: 인베리언트, 중단, 오탐의 어휘. 그리고 막다른 길을 발견으로 바꾸는 문장.

## Dialogue
Priya: I checked every transaction in that window. All of them passed validation.
> 그 구간의 모든 트랜잭션을 확인했어요. 전부 검증을 통과했습니다.
Jay: I believe you, and that's the finding, not the dead end. Each transaction was fine. The total wasn't. We validated and never reconciled.
> 믿어요. 그리고 그게 막다른 길이 아니라 발견입니다. 개별 트랜잭션은 멀쩡했고 총량이 틀렸어요. 검증만 하고 대사는 안 했죠.
Priya: What would reconciling have looked like?
> 대사라는 게 구체적으로 뭐였을까요?
Jay: One comparison every block: locked against minted. It wouldn't have stopped the bug. It would have turned a week into a block.
> 매 블록 비교 하나요. 잠긴 양 대 발행량. 버그를 막지는 못했겠지만 일주일을 한 블록으로 바꿨을 겁니다.
Priya: And when the two numbers disagree?
> 두 숫자가 안 맞으면요?
Jay: Withdrawals stop and someone gets paged. If we won't do that, we shouldn't build the check. An alert with no action attached is decoration.
> 출금이 멈추고 누군가 호출됩니다. 그렇게 하지 않을 거면 검사를 만들지 말아야 해요. 행동이 안 붙은 경보는 장식입니다.
Priya: People will hate being woken for a false positive.
> 오탐으로 깨우면 사람들이 싫어할 텐데요.
Jay: They will, and I'd still take it. A wrong page costs a bad night. No page costs the reserves.
> 그렇겠죠. 그래도 저는 받겠습니다. 잘못된 호출은 하룻밤을 잃고, 호출이 없으면 준비금을 잃습니다.

## Techniques
1. **동의로 시작해 재정의한다.** "I believe you, and that's the finding." 상대의 결론을 부정하지 않고 그 결론의 의미를 바꾼다.
2. **검증과 대사를 구분한다.** "We validated and never reconciled." 개별 항목의 정당성과 총량의 일치는 다른 검사다. 이 한 문장이 사고의 구조를 설명한다.
3. **경보에는 행동을 묶는다.** "An alert with no action attached is decoration." 모니터링 논의를 대시보드에서 런북으로 옮기는 문장.

## Expressions
| passed validation | 검증을 통과했다 |
| that's the finding, not the dead end | 그게 막다른 길이 아니라 발견이다 |
| validate vs. reconcile | 검증하다 vs. 대사하다 |
| locked against minted | 잠긴 양 대 발행량 |
| turn a week into a block | 일주일을 한 블록으로 바꾸다 |
| someone gets paged | 누군가 호출된다 |
| an alert with no action attached | 행동이 붙지 않은 경보 |
| a false positive | 오탐 |
| I'd still take it | 그래도 받겠다 |
| costs us the reserves | 준비금을 잃게 한다 |
