# 180 · Line — Push back the audit log. Nobody's asked for it yet.
title_ko: Push back the audit log. Nobody's asked for it yet. — 감사 로그는 뒤로 미뤄. 아직 아무도 요청하지 않았어
situation: Sprint planning. Mina wants to build audit-log tables now because a compliance-minded customer will ask eventually. Jay defers the work, corrects a misheard verb, and names the trigger that would bring the task back so the deferral is a decision, not a loss.
situation_ko: 스프린트 계획. Mina는 언젠가 컴플라이언스를 따지는 고객이 요청할 테니 지금 감사 로그 테이블을 만들고 싶어 한다. Jay는 작업을 미루고, 잘못 들은 동사를 바로잡고, 그 작업을 다시 불러올 트리거를 정해서 연기가 손실이 아닌 결정이 되게 한다.
why: **Push back** means postpone: push back the deadline, push back the audit log. Plain **push** points the other way in dev English, meaning proceed, deploy, publish (git push, push to production), so "Push the audit log" tells someone to ship it. **Nobody's asked for it yet** is the reason: speculative compliance work waits for a real trigger, an external audit, a client pilot, SOC 2 prep, and you name that trigger when you defer. Meeting form: "Let's push back the audit log — no one's asking for it yet."
why_ko: **Push back**은 미루다는 뜻이다. push back the deadline, push back the audit log. 그냥 **push**는 개발 영어에서 반대 방향, 즉 진행·배포·게시다(git push, push to production). 그래서 "Push the audit log"는 출시하라는 말이 된다. **Nobody's asked for it yet**이 이유다. 추측에 기반한 컴플라이언스 작업은 외부 감사, 고객 파일럿, SOC 2 준비 같은 실제 트리거를 기다리고, 미룰 때 그 트리거를 정해 둔다. 회의체는 "Let's push back the audit log — no one's asking for it yet."이다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, second export (2026-09-21), page 4 card 20 (sentence): Original "Push the audit log. Nobody's asked for it yet." / Corrected "Push back the audit log. Nobody's asked for it yet." / Korean "감사 로그 일정을 뒤로 미루세요. 아직 아무도 요청하지 않았으니까요." / Team Meeting Version "Let's push back the audit log—no one's asking for it yet." Language note: push alone = proceed/deploy; push back = postpone. The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 두 번째 내보내기(2026-09-21), 4페이지 20번 카드(문장): 원문 "Push the audit log. Nobody's asked for it yet." / 수정 "Push back the audit log. Nobody's asked for it yet." / 한국어 "감사 로그 일정을 뒤로 미루세요. 아직 아무도 요청하지 않았으니까요." / 팀 회의 버전 "Let's push back the audit log—no one's asking for it yet." 언어 노트: push 단독 = 진행·배포, push back = 미루다. 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-79.txt

## Dialogue
Mina: I want to start the audit-log tables this sprint. A compliance customer will ask for them eventually.
> 이번 스프린트에 감사 로그 테이블을 시작하고 싶어요. 컴플라이언스 고객이 언젠가는 요청할 거예요.
Jay: Push back the audit log. Nobody's asked for it yet, and the schema will churn before anyone does.
> 감사 로그는 뒤로 미뤄요. 아직 아무도 요청하지 않았고, 누가 요청하기 전에 스키마가 계속 바뀔 거예요.
Mina: Push it? You mean ship it?
> push요? 출시하라는 뜻이에요?
Jay: No — push it back. Defer it. "Push" on its own sounds like git push.
> 아니요, push back, 미루라고요. "push"만 쓰면 git push처럼 들려요.
Mina: Okay. What brings it back onto the board?
> 알겠어요. 그럼 뭐가 있으면 다시 보드에 올라와요?
Jay: A named trigger: a client pilot, an external audit, or SOC 2 prep. Until then, CloudTrail and the database change log cover us.
> 정해진 트리거요. 고객 파일럿, 외부 감사, 아니면 SOC 2 준비. 그때까지는 CloudTrail과 DB 변경 로그로 충분해요.

## Techniques
1. **미룰 때는 이유와 복귀 조건을 같이 말한다.** "Nobody's asked for it yet" + "A named trigger: a client pilot, an external audit, or SOC 2 prep" — 연기가 방치가 아니라 결정이 된다.
2. **잘못 들린 동사는 바로 그 자리에서 고친다.** "No — push it back. Defer it." — 동의어 하나를 덧붙이면 오해가 끝난다.

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| push back X | X를 뒤로 미루다 — 일정·작업 연기. "Push back the audit log." |
| push (to production) | 배포·진행하다 — push 단독은 미루다가 아니다 |
| nobody's asked for it yet | 아직 아무도 요청하지 않았다 — 추측성 작업을 미루는 근거 |
| a named trigger | 정해진 트리거 — 미룬 작업이 돌아오는 조건 |
