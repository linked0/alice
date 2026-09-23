# 18 · 1:1 — The PR is wrong and the person is fine
title_ko: PR은 틀렸고 사람은 괜찮다
situation: Sun-woo's first big PR reimplements a helper that already exists in rails, and does it worse. Jay has to get the PR redone without teaching Sun-woo to stop taking initiative.
situation_ko: 선우의 첫 큰 PR이 rails에 이미 있는 헬퍼를 다시, 더 나쁘게 구현했다. Jay는 선우가 주도성을 잃지 않게 하면서 PR을 다시 하게 해야 한다.
why: Feedback English for juniors: judge the work, protect the instinct, and give one concrete habit instead of a general lecture.
why_ko: 주니어를 위한 피드백 영어. 결과물을 판단하고, 본능은 보호하고, 일반적인 훈계 대신 구체적인 습관 하나를 준다.

## Dialogue
Jay: Before the code: the instinct to build the helper yourself instead of waiting for someone was right. Keep that.
> 코드 얘기 전에요. 누굴 기다리는 대신 헬퍼를 직접 만들려 한 본능은 맞았어요. 그건 유지해요.
Sun-woo: But?
> 그런데요?
Jay: But it exists. rails has formatUnits with the same signature, and it handles the eighteen-decimals edge case yours misses. So the PR should shrink to an import.
> 그런데 이미 있어요. rails에 같은 시그니처의 formatUnits가 있고, 당신 것이 놓친 18자리 소수 엣지 케이스를 처리해요. 그러니 PR은 import 하나로 줄어들어야 해요.
Sun-woo: I didn't know rails had it. I searched the repo.
> rails에 있는 줄 몰랐어요. 레포를 검색했는데요.
Jay: This repo, right? The habit I'd add is one more search, in rails, before writing anything that feels generic. Five minutes, every time. That's the whole lesson.
> 이 레포죠? 제가 추가하고 싶은 습관은, 범용적으로 느껴지는 걸 쓰기 전에 rails에서 한 번 더 검색하는 거예요. 매번 5분. 그게 교훈의 전부예요.
Sun-woo: Should I close the PR?
> PR을 닫을까요?
Jay: Rewrite it. The test you wrote is good and rails doesn't have one for that case. Keep the test, swap the implementation, and the PR becomes a contribution to rails instead of a duplicate.
> 다시 쓰세요. 당신이 쓴 테스트는 좋고 rails에는 그 케이스의 테스트가 없어요. 테스트는 두고 구현을 바꾸면, PR이 중복이 아니라 rails에 대한 기여가 돼요.
Sun-woo: That's a better PR than the one I opened.
> 제가 연 것보다 나은 PR이네요.
Jay: It usually is, the second time.
> 대개 두 번째가 그래요.

## Techniques
1. **본능과 결과를 갈라 말한다.** "the instinct… was right. Keep that." 주도성을 먼저 보호하면 뒤의 교정이 위축을 낳지 않는다.
2. **훈계 대신 습관 하나.** "one more search, in rails… Five minutes, every time. That's the whole lesson." 교훈을 한 문장으로 제한하면 실제로 남는다.
3. **살릴 것을 찾는다.** "Keep the test, swap the implementation." 전면 부정 대신 PR 안의 좋은 부분을 지목해 다시 쓸 동력을 준다.



## Words
| before the code | /bɪˈfɔr ðə koʊd/ | 코드 얘기 전에 |
| instinct was right | /ˈɪnstɪŋkt wɑz raɪt/ | 본능은 맞았다 |
| keep that | /kip ðæt/ | 그건 유지하라 |
| habit I'd add | /ˈhæbət aɪd æd/ | 내가 추가하고 싶은 습관 |

## Expressions
| before the code | 코드 얘기 전에 |
| the instinct was right | 본능은 맞았다 |
| keep that | 그건 유지하라 |
| shrink to an import | import 하나로 줄어들다 |
| the habit I'd add | 내가 추가하고 싶은 습관 |
| anything that feels generic | 범용적으로 느껴지는 무엇이든 |
| that's the whole lesson | 그게 교훈의 전부다 |
| keep the test, swap the implementation | 테스트는 두고 구현을 바꿔라 |
| a contribution instead of a duplicate | 중복이 아닌 기여 |
| it usually is, the second time | 대개 두 번째가 그렇다 |
