# 11 · Ops — The key leaked. What else does it open?
title_ko: 키가 유출됐다. 그 키가 또 무엇을 여나?
situation: An Alchemy key was committed to a public branch for twenty minutes. Priya rotated it. Jay wants to know the blast radius before calling it done.
situation_ko: Alchemy 키가 공개 브랜치에 20분 동안 커밋됐다. Priya가 교체했다. Jay는 끝났다고 하기 전에 피해 범위를 알고 싶다.
why: Security incidents in English are a sequence of scope questions. This one also shows how to praise the fast fix and still ask for the slow one.
why_ko: 보안 사고 영어는 범위 질문의 연쇄다. 빠른 수정을 칭찬하면서도 느린 수정을 요구하는 법.

## Dialogue
Priya: The key was live for about twenty minutes. I've rotated it and the new one is in Secret Manager.
> 키가 약 20분 노출됐어요. 교체했고 새 키는 Secret Manager에 있습니다.
Jay: Good, that's the right first move. Now the second question: what did that key open?
> 좋아요, 올바른 첫 조치예요. 이제 두 번째 질문. 그 키가 무엇을 열었죠?
Priya: The devnet's fork upstream. Node API on Sepolia.
> devnet의 포크 업스트림이요. Sepolia의 Node API.
Jay: Only that? Same app as the bundler or the webhooks?
> 그것만요? 번들러나 웹훅과 같은 앱이에요?
Priya: Separate app. The AA path has its own key.
> 별도 앱이에요. AA 경로는 자체 키가 있어요.
Jay: Then the blast radius is one read-only quota for twenty minutes. Check the dashboard for a usage spike and we can close it. That split just paid for itself.
> 그럼 피해 범위는 20분간 읽기 전용 쿼터 하나네요. 대시보드에서 사용량 급증을 확인하고 닫죠. 그 분리가 방금 값을 했어요.
Priya: Should we add a pre-commit hook for secrets?
> 시크릿용 pre-commit 훅을 추가할까요?
Jay: Yes, and a scan of the history too. Twenty minutes is the window we noticed. I want to know it's the only one.
> 네, 그리고 히스토리 스캔도요. 20분은 우리가 알아챈 창이에요. 그게 유일한 창인지 알고 싶어요.

## Techniques
1. **첫 조치를 명시적으로 인정한다.** "that's the right first move" 다음 질문이 비난으로 들리지 않게 하는 한 문장.
2. **범위 질문을 순서대로 던진다.** "what did that key open? Only that? Same app as…?" 사고 대응은 짧은 질문의 연쇄다.
3. **알아챈 것과 실제를 구분한다.** "Twenty minutes is the window we noticed." 관측된 창과 진짜 창이 다를 수 있음을 짚어 후속 조치를 정당화한다.



## Words
| rotate a key | /ˈroʊˌteɪt ə ki/ | 키를 교체하다 |
| right first move | /raɪt fɝst muv/ | 올바른 첫 조치 |
| blast radius | /blæst ˈreɪdiəs/ | 피해 범위 |
| usage spike | /ˈjusədʒ spaɪk/ | 사용량 급증 |
| window we noticed | /ˈwɪndoʊ wi ˈnoʊtəst/ | 우리가 알아챈 창 |

## Expressions
| the key was live for | 키가 …동안 유효했다 |
| rotate a key | 키를 교체하다 |
| the right first move | 올바른 첫 조치 |
| what did that key open? | 그 키가 무엇을 열었나? |
| blast radius | 피해 범위 |
| a usage spike | 사용량 급증 |
| that split just paid for itself | 그 분리가 방금 값을 했다 |
| a pre-commit hook for secrets | 시크릿 검사용 pre-commit 훅 |
| the window we noticed | 우리가 알아챈 창 |
| I want to know it's the only one | 그게 유일한 것인지 알고 싶다 |
