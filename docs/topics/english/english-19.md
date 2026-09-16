# 19 · Ops — Who can reach that port?
title_ko: 그 포트에 누가 닿을 수 있나?
situation: Priya wants to test the wallet on her phone against Jay's local Anvil and suggests opening port 8545 on the office router. Jay has a tailnet.
situation_ko: Priya가 Jay의 로컬 Anvil에 대고 폰에서 지갑을 테스트하고 싶어 사무실 라우터의 8545 포트를 열자고 한다. Jay에게는 tailnet이 있다.
why: Network-exposure English: the one question to ask before opening anything, and how to offer the safer path without a security lecture.
why_ko: 네트워크 노출 영어. 무엇이든 열기 전에 물을 질문 하나, 그리고 보안 훈계 없이 더 안전한 길을 제시하는 법.

## Dialogue
Priya: Can we open 8545 on the router so I can hit your Anvil from my phone?
> 제 폰에서 당신의 Anvil에 접근할 수 있게 라우터의 8545를 열 수 있을까요?
Jay: Before we open anything: who can reach that port afterwards?
> 무엇이든 열기 전에요. 그 다음엔 누가 그 포트에 닿을 수 있죠?
Priya: Anyone on the internet, I suppose. It's just a test chain.
> 인터넷의 누구나요, 아마. 그냥 테스트 체인인데요.
Jay: A test chain with anvil_setBalance and no auth. Someone finds it, mints themselves a million test ETH, and we spend a morning confused. Not a disaster, just a waste.
> anvil_setBalance가 있고 인증이 없는 테스트 체인이죠. 누가 발견해서 테스트 ETH 백만 개를 자기에게 찍고, 우리는 아침 내내 혼란스러워하는 거예요. 재난은 아니고 낭비죠.
Priya: So what instead?
> 그럼 대신 뭘요?
Jay: Tailscale. Your phone joins the tailnet, Anvil listens on all interfaces, and the RPC is http://100.111.162.0:8545 for you and nobody else. I need to restart Anvil with --host 0.0.0.0 for that.
> Tailscale이요. 당신 폰이 tailnet에 들어오고, Anvil이 모든 인터페이스에서 듣고, RPC는 당신에게만 http://100.111.162.0:8545예요. 그러려면 Anvil을 --host 0.0.0.0으로 재시작해야 해요.
Priya: Does restarting lose the state?
> 재시작하면 상태가 사라지나요?
Jay: No, it's on a state file. Only the listener changes. I'll do it after the current test finishes, not during.
> 아니요, state 파일에 있어요. 리스너만 바뀌어요. 지금 테스트가 끝난 뒤에 할 거예요, 도중이 아니라.

## Techniques
1. **행동 전 질문 하나.** "who can reach that port afterwards?" 모든 노출 결정에 앞서는 한 문장. 거절이 아니라 질문이라 대화가 열린다.
2. **피해를 정확한 크기로 말한다.** "Not a disaster, just a waste." 과장하면 신뢰를 잃고, 축소하면 무시된다. 크기를 맞춘다.
3. **대안을 실행 절차와 함께 준다.** "I need to restart Anvil with --host 0.0.0.0" 원칙만 말하지 않고 다음 행동을 명시한다.

## Expressions
| hit your Anvil from my phone | 내 폰에서 당신의 Anvil에 접근하다 |
| before we open anything | 무엇이든 열기 전에 |
| who can reach that port? | 누가 그 포트에 닿을 수 있나? |
| no auth | 인증 없음 |
| mint themselves a million | 자기에게 백만을 찍다 |
| not a disaster, just a waste | 재난은 아니고 낭비다 |
| listens on all interfaces | 모든 인터페이스에서 수신한다 |
| for you and nobody else | 당신에게만 |
| only the listener changes | 리스너만 바뀐다 |
| after it finishes, not during | 끝난 뒤에, 도중이 아니라 |
