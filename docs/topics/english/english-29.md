# 29 · Incident — Telling the CTO the dependency was ours to check
title_ko: 그 의존성은 우리가 확인할 몫이었다고 CTO에게 말하기
situation: Jay leads the settlement team at a Dublin fintech. A vendor's library shipped a bad release; the team's deploy pulled it automatically and payouts stalled for 40 minutes. The CTO, Rachel, opens the review with "so this was the vendor's fault." Jay's team did not pin the version. Saying "yes" is easy and wrong.
situation_ko: Jay는 더블린 핀테크의 정산 팀 리드. 벤더 라이브러리가 나쁜 릴리스를 냈고, 팀의 배포가 그것을 자동으로 끌어와 지급이 40분 멈췄다. CTO Rachel이 "그러니까 벤더 잘못이었군요"로 리뷰를 시작한다. Jay의 팀은 버전을 핀하지 않았다. "네"라고 하는 것은 쉽고 틀리다.
why: Owning a failure in front of an executive without either grovelling or deflecting is a lead's core skill, and non-native speakers often over-apologise. The form that works: correct the framing in one sentence, separate what was theirs from what was ours, and arrive with the fix already scheduled.
why_ko: 임원 앞에서 굽실거리지도 회피하지도 않고 실패를 소유하는 것은 리드의 핵심 기술이고, 비원어민은 과하게 사과하는 일이 많다. 되는 형식: 프레임을 한 문장으로 바로잡고, 그들 몫과 우리 몫을 나누고, 수정을 이미 일정에 올린 채로 온다.
status: planned

## Dialogue
Rachel: So this was the vendor's fault. They shipped a broken release.
> 그러니까 벤더 잘못이었군요. 망가진 릴리스를 냈으니.
Jay: They shipped a broken release, and we deployed it without anyone deciding to. Those are two different failures, and only the second one is ours to fix, so that's the one I want to spend this meeting on.
> 망가진 릴리스를 낸 건 그들이고, 누구도 결정하지 않았는데 그것을 배포한 건 우리입니다. 다른 두 실패이고, 둘째만 우리가 고칠 수 있으니 이 회의는 그것에 쓰고 싶습니다.
Rachel: Why did it deploy without a decision?
> 왜 결정 없이 배포됐죠?
Jay: Our manifest allowed any minor version, and the build didn't fail when the lockfile drifted. So a release that came out at 02:00 was in our production image by the 09:00 deploy. Nobody read it because nothing asked anyone to.
> 매니페스트가 어떤 마이너 버전이든 허용했고, 락파일이 어긋나도 빌드가 실패하지 않았습니다. 그래서 02:00에 나온 릴리스가 09:00 배포 때 프로덕션 이미지에 들어갔습니다. 아무도 읽지 않은 건 아무것도 읽으라고 요구하지 않았기 때문입니다.
Rachel: That sounds like a process gap, not an engineering one.
> 그건 엔지니어링이 아니라 프로세스 공백처럼 들리는데요.
Jay: It's both, and I own both. The process gap is that a dependency bump wasn't a reviewed change. The engineering gap is that CI let it through. As of this morning, the build fails on any lockfile mismatch, and bumps to the six packages that can move money arrive as pull requests, not as surprises. That took two hours; it should have taken two hours a year ago.
> 둘 다이고, 둘 다 제 책임입니다. 프로세스 공백은 의존성 올림이 리뷰되는 변경이 아니었다는 것. 엔지니어링 공백은 CI가 통과시켰다는 것. 오늘 아침부터 락파일 불일치에는 빌드가 실패하고, 돈을 움직일 수 있는 여섯 패키지의 올림은 놀람이 아니라 풀 리퀘스트로 옵니다. 두 시간 걸렸고, 1년 전에 두 시간 걸렸어야 했습니다.
Rachel: What do we tell the vendor?
> 벤더에게는 뭐라고 하죠?
Jay: That their release broke and we'd like a post-mortem, which is fair. But I'd rather we didn't tell them it cost us forty minutes, because it didn't. Their release cost us zero minutes. Our pipeline cost us forty.
> 릴리스가 망가졌으니 사후 분석을 원한다고요. 그건 정당합니다. 다만 우리에게 40분을 잃게 했다고는 말하지 않는 게 좋겠습니다. 그렇지 않았으니까요. 그들의 릴리스는 0분을 잃게 했고, 우리 파이프라인이 40분을 잃게 했습니다.
Rachel: All right. Put the six packages in the review, and send me the list.
> 좋아요. 여섯 패키지를 리뷰에 넣고, 목록을 보내주세요.

## Techniques
1. **프레임을 나누되 부정하지 않는다.** "They shipped a broken release, and we deployed it without anyone deciding to." 상대 문장을 그대로 인정한 뒤 두 번째 사실을 붙인다. "아니요"로 시작하면 방어로 들린다.
2. **고칠 수 있는 것에 회의를 쓴다.** "only the second one is ours to fix, so that's the one I want to spend this meeting on." 책임 소재 논쟁을 행동으로 바꾸는 한 문장.
3. **이미 고친 것으로 소유를 증명한다.** "As of this morning, the build fails… That took two hours; it should have taken two hours a year ago." 사과 대신 완료된 수정과 솔직한 자책 한 줄. 이것이 신뢰를 회복한다.






## Words
| post-mortem | /poʊstˈmɔrtɛm/ | 사후 분석 |
| drifted | /ˈdrɪftəd/ | 락파일이 어긋났다 |

## Expressions
| two different failures | 서로 다른 두 실패 |
| ours to fix | 우리가 고칠 몫 |
| without anyone deciding to | 누구도 결정하지 않은 채 |
| the lockfile drifted | 락파일이 어긋났다 |
| nothing asked anyone to | 아무것도 누구에게도 요구하지 않았다 |
| a process gap | 프로세스 공백 |
| I own both | 둘 다 제 책임입니다 |
| as of this morning | 오늘 아침부터 |
| not as surprises | 놀람이 아니라 |
| it cost us zero minutes | 우리에게 0분을 잃게 했다 |
| a post-mortem | 사후 분석 |
