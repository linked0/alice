# 399 · Interview — A flapping node
title_ko: A flapping node — "가장 어려웠던 디버깅" 질문에 간헐적 장애를 영어로 설명하기
situation: A hiring manager abroad asks Jay the standard question — tell me about a bug that was hard to track down. Jay picks a real one from the day before: users could not buy tokens on his exchange, the server logs were clean, and the node underneath kept going up and down. He has to explain an intermittent failure in English without saying "it was weird" three times.
situation_ko: 해외 면접에서 채용 담당자가 단골 질문을 던진다. 추적하기 어려웠던 버그 이야기를 해보라. Jay는 바로 전날의 실제 사례를 고른다. 거래소에서 사용자가 토큰을 살 수 없었고, 서버 로그는 깨끗했고, 그 아래의 노드는 계속 떴다 죽었다 했다. "it was weird"를 세 번 말하지 않고 간헐적 장애를 영어로 설명해야 한다.
why: **Flap** is the word this whole story turns on. It is the standard verb for a thing that alternates between up and down — it comes from network engineering (*route flapping*, *link flapping*) and it is not slang, so it is safe in an interview. The trap is reaching for "unstable", which says the mood but not the behaviour; flapping says specifically that it recovers and fails again, which is the detail that makes an intermittent bug hard. Around it sits the vocabulary of debugging under uncertainty: **a red herring** for the clue that wastes your time, **to rule out** for eliminating a suspect, **a smoking gun** for the evidence that settles it, and **to narrow it down** for the process itself. Interviewers listen for whether you can separate a symptom from a root cause; the phrases below are how that separation sounds in English.
why_ko: 이 이야기의 축은 **flap**이다. 위아래를 오가는 상태를 가리키는 표준 동사로, 네트워크 엔지니어링(*route flapping*, *link flapping*)에서 왔고 속어가 아니라 면접에서도 안전하다. 함정은 "unstable"로 도망가는 것이다. 그건 느낌만 말할 뿐 동작을 말하지 않는다. flapping은 복구됐다가 다시 죽는다는 것까지 말해주고, 바로 그 점이 간헐적 버그를 어렵게 만든다. 그 주위에 불확실한 상황에서 디버깅할 때 쓰는 어휘가 붙는다. 시간을 낭비하게 만든 단서는 **a red herring**, 용의자를 지우는 것은 **to rule out**, 결정적 증거는 **a smoking gun**, 범위를 좁혀가는 과정은 **to narrow it down**이다. 면접관은 증상과 근본 원인을 구분할 줄 아는지를 듣는다. 아래 표현들이 그 구분을 영어로 말하는 방식이다.
status: new
added: 2026-09-22

## Dialogue
Ava: Tell me about a bug that was hard to track down.
> 추적하기 어려웠던 버그 이야기를 해주세요.
Jay: Users couldn't buy tokens on my exchange. The server logs were clean — the only warnings were a bot probing for credentials, which was a red herring.
> 제 거래소에서 사용자가 토큰을 살 수 없었습니다. 서버 로그는 깨끗했고, 유일한 경고는 크리덴셜을 뒤지는 봇이었는데 그건 헛다리였습니다.
Ava: Clean logs on a user-facing failure. How did you narrow it down?
> 사용자에게 보이는 장애인데 로그는 깨끗하다. 어떻게 범위를 좁혔나요?
Jay: The transaction was signed in the browser, so it never reached my server at all. That ruled out the backend and sent me on chain instead.
> 트랜잭션이 브라우저에서 서명돼서 서버에 아예 도달하지 않았습니다. 그래서 백엔드를 배제하고 온체인 쪽을 봤습니다.
Ava: And what did you find there?
> 거기서 뭘 찾았나요?
Jay: Two things. The app was calling a function the deployed contract didn't have — a rename that shipped in the code but never got redeployed. And the node was flapping: three failures, then it answered again, but forty blocks behind.
> 두 가지입니다. 앱이 배포된 컨트랙트에 없는 함수를 호출하고 있었어요. 이름 변경이 코드에는 반영됐는데 재배포는 안 된 거죠. 그리고 노드가 flap하고 있었습니다. 세 번 실패하고 다시 응답했는데 40블록 뒤였습니다.
Ava: Behind? That's an odd direction to move.
> 뒤라고요? 이상한 방향이네요.
Jay: That was the smoking gun. It was a forked test chain restarting from the fork point, so anything deployed onto it was wiped. The addresses we were pointing at held no code.
> 그게 결정적 증거였습니다. 포크된 테스트 체인이 포크 지점부터 다시 시작하는 거라, 그 위에 배포한 건 전부 날아갔습니다. 우리가 가리키던 주소에는 코드가 없었습니다.
Ava: So what did you change?
> 그래서 뭘 바꿨나요?
Jay: I pointed it at contracts that live in the forked state, so they survive a restart. Then I proved it before deploying — the old call reverted with no signature, the new one reverted on the allowance check. Different failure, same input.
> 포크된 상태 안에 있는 컨트랙트로 바꿨습니다. 그러면 재시작해도 살아남으니까요. 그리고 배포 전에 증명했습니다. 기존 호출은 시그니처 없이 revert했고, 새 호출은 allowance 검사에서 revert했습니다. 같은 입력, 다른 실패였죠.

## Techniques
1. **증상과 근본 원인을 문장 단위로 갈라놓는다.** "Users couldn't buy tokens"는 증상이고, "a rename that shipped in the code but never got redeployed"는 원인이다. 면접관이 듣고 싶은 건 이 둘을 섞지 않는 능력이다. 중간에 "That ruled out the backend"처럼 배제 과정을 한 줄 넣으면, 운이 좋아서가 아니라 좁혀가서 찾았다는 인상이 된다.
2. **결정적 증거를 한 문장으로 세우고 그 다음에 해석한다.** "Behind?"라는 되물음에 곧바로 "That was the smoking gun."으로 받고, 그 뒤에 이유를 붙인다. 영어 면접에서는 결론을 먼저 놓고 근거를 뒤에 대는 순서가 훨씬 잘 들린다. 한국어 습관대로 근거를 길게 쌓고 마지막에 결론을 두면 듣는 쪽이 요점을 놓친다.
3. **검증을 "다른 실패"로 표현한다.** "Different failure, same input."은 차등 테스트(differential test)를 여섯 단어로 요약한다. 고쳤다고 주장하는 대신 어떻게 확인했는지를 말하면 신뢰도가 크게 올라간다.

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| to flap | (서버·링크가) 떴다 죽었다를 반복하다 — 네트워크 용어, 속어 아님. "The node was flapping." |
| flapping / a flapping node | 간헐적으로 오르내리는 상태 — route flapping, link flapping에서 왔다 |
| intermittent | 간헐적인 — 재현이 잘 안 되는 장애를 가리키는 표준 형용사 |
| to track down | (원인을) 추적해 찾아내다 — find보다 과정이 있다는 뉘앙스 |
| to narrow it down | 범위를 좁히다 — 디버깅 과정 자체를 가리키는 말 |
| to rule out | (가능성을) 배제하다 — "That ruled out the backend." |
| a red herring | 헛다리, 주의를 딴 데로 돌리는 단서 — 원뜻은 훈제 청어 |
| a smoking gun | 결정적 증거 — 논쟁을 끝내는 증거 하나 |
| a root cause | 근본 원인 — symptom(증상)과 반드시 짝으로 쓴다 |
| to reproduce a bug | 버그를 재현하다 — 면접에서 거의 반드시 나오는 동사 |
| stale | (설정·캐시가) 오래돼 현실과 어긋난 — "the addresses were stale" |
| to point at | (설정이) ~을 가리키다 — "We were pointing at the wrong contract." |
| to silently fall back | 조용히 대체값으로 넘어가다 — 에러 없이 틀리는, 가장 위험한 실패 방식 |
| to wipe state | 상태를 날리다 — 재시작 때 데이터가 사라지는 것 |
| to survive a restart | 재시작해도 남아 있다 — 내구성을 말하는 짧은 표현 |
| to ship | (코드를) 내보내다, 배포하다 — "a rename that shipped in the code" |
| by accident, not by design | 의도한 게 아니라 우연히 — 잘 돌아가지만 설계는 아닐 때 |
| a differential test | 차등 테스트 — 하나만 바꿔 두 실행을 비교하는 검증 |
