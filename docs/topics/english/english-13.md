# 13 · Review — The Dockerfile copies the whole repo
title_ko: Dockerfile이 레포 전체를 복사한다
situation: Marek's new Dockerfile does COPY . . in the final stage and there is no .dockerignore. The image works. It also contains .env and the git history.
situation_ko: Marek의 새 Dockerfile이 마지막 스테이지에서 COPY . .을 하고 .dockerignore가 없다. 이미지는 동작한다. .env와 git 히스토리도 들어 있다.
why: A security review comment that stays specific: name what is in the image, not what could go wrong in general.
why_ko: 구체적으로 머무는 보안 리뷰 코멘트. 일반적으로 무엇이 잘못될 수 있는지가 아니라 이미지에 실제로 무엇이 들어 있는지를 말한다.

## Dialogue
Jay: The image builds and runs, so this isn't about function. I pulled it and listed the layers. There's a .env in there, and a .git folder.
> 이미지가 빌드되고 돌아가니 기능 문제는 아니에요. 이미지를 받아서 레이어를 봤는데 .env와 .git 폴더가 들어 있어요.
Marek: The .env only has local values.
> .env는 로컬 값만 있어요.
Jay: Today. The Dockerfile doesn't know that, and the next person's .env will have a real key. The fix is two lines: a .dockerignore, and COPY --from=build of the exact output paths instead of the whole stage.
> 오늘은요. Dockerfile은 그걸 모르고, 다음 사람의 .env에는 진짜 키가 있을 거예요. 수정은 두 줄이에요. .dockerignore 하나, 그리고 스테이지 전체 대신 정확한 출력 경로만 COPY --from=build.
Marek: Copying the whole build stage was easier.
> 빌드 스테이지 전체를 복사하는 게 더 쉬웠어요.
Jay: It was, and it's how source ends up in production images. Copy dist and package.json, nothing else. If the image needs something else, you'll find out at startup, which is the right time.
> 그랬죠. 그리고 그게 소스가 프로덕션 이미지에 들어가는 경로예요. dist와 package.json만 복사하고 나머지는 빼요. 이미지에 다른 게 필요하면 시작할 때 알게 되고, 그게 맞는 시점이에요.
Marek: Want me to add a size check too?
> 크기 검사도 추가할까요?
Jay: Nice to have. The .dockerignore is the blocker; the rest is polish.
> 있으면 좋고요. .dockerignore가 블로커고 나머지는 다듬기예요.

## Techniques
1. **증거를 먼저 보여준다.** "I pulled it and listed the layers." 추정이 아니라 관찰로 시작하면 반박의 여지가 사라진다.
2. **"오늘은"으로 시간을 확장한다.** "Today. The Dockerfile doesn't know that." 지금은 괜찮다는 반론에 미래의 사용자를 끌어온다.
3. **블로커와 다듬기를 구분한다.** "The .dockerignore is the blocker; the rest is polish." 상대가 무엇을 먼저 해야 하는지 분명해진다.



## Words
| list the layers | /lɪst ðə ˈleɪɚz/ | 레이어를 나열하다 |
| exact output paths | /ɪɡˈzækt ˈaʊtˌpʊt pæðz/ | 정확한 출력 경로 |
| nothing else | /ˈnʌθɪŋ ɛls/ | 그 외에는 아무것도 |
| nice to have | /naɪs tu hæv/ | 있으면 좋은 것 |
| blocker vs. polish | /ˈblɑkɚ ˈvɝsəz ˈpɑlɪʃ/ | 블로커 vs. 다듬기 |

## Expressions
| this isn't about function | 기능 문제가 아니다 |
| list the layers | 레이어를 나열하다 |
| the next person's .env | 다음 사람의 .env |
| the fix is two lines | 수정은 두 줄이다 |
| the exact output paths | 정확한 출력 경로 |
| how source ends up in production images | 소스가 프로덕션 이미지에 들어가는 경로 |
| nothing else | 그 외에는 아무것도 |
| the right time to find out | 알게 되기에 맞는 시점 |
| nice to have | 있으면 좋은 것 |
| the blocker vs. polish | 블로커 vs. 다듬기 |
