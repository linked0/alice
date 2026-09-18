# 30 · Interview — Explain your architecture to someone who won't read the diagram
title_ko: 다이어그램을 읽지 않을 사람에게 아키텍처 설명하기
situation: Final interview for a team lead role at a London payments company. The last interviewer is the COO, Priya, not an engineer. She asks Jay to explain the settlement system he built, and she will judge whether he can talk to the board. Jay has three minutes and no whiteboard.
situation_ko: 런던 결제 회사 팀 리드 최종 면접. 마지막 면접관은 엔지니어가 아닌 COO Priya. Jay가 만든 정산 시스템을 설명하라고 하고, 이사회와 대화할 수 있는지를 판단한다. Jay에게는 3분과 화이트보드 없음.
why: Team leads are hired for the conversations engineers cannot have. The test is whether you can drop every noun the listener does not own and keep every consequence they care about, and whether you stop when the question is answered.
why_ko: 팀 리드는 엔지니어가 할 수 없는 대화 때문에 채용된다. 시험은 듣는 사람이 모르는 명사를 모두 버리고 그들이 신경 쓰는 결과를 모두 남길 수 있는지, 질문에 답했으면 멈추는지다.
status: planned

## Dialogue
Priya: Tell me about the settlement system you built. Assume I don't know what a blockchain is, because I mostly don't.
> 만드신 정산 시스템에 대해 말해 보세요. 제가 블록체인이 뭔지 모른다고 가정하세요. 대체로 모르니까요.
Jay: Three sentences, then you steer. When a customer wins on our platform, money has to move from the people who lost to the person who won, and it has to be right the first time because we cannot take it back. I built the part that does that: it checks that the money we owe never exceeds the money we hold, and if that check ever fails, it stops everything and pages a human rather than paying anyone. In two years it stopped four times, and all four were bugs we would otherwise have paid out.
> 세 문장 하고, 그다음은 원하는 방향으로 이끄세요. 고객이 우리 플랫폼에서 이기면 진 사람들에게서 이긴 사람으로 돈이 움직여야 하고, 되돌릴 수 없으니 처음부터 맞아야 합니다. 저는 그 부분을 만들었습니다. 우리가 갚아야 할 돈이 보유한 돈을 절대 넘지 않는지 확인하고, 그 확인이 실패하면 누구에게도 지급하지 않고 모든 것을 멈추고 사람을 호출합니다. 2년 동안 네 번 멈췄고, 넷 모두 아니었다면 지급했을 버그였습니다.
Priya: Stopping everything sounds expensive.
> 모든 것을 멈추는 건 비싸게 들리네요.
Jay: It is, for about an hour each time. Paying out on a bug is expensive forever. We chose the hour. If the business ever decided the other way, the system can be set to keep going and flag instead, but I'd want that written down as a decision, not drifted into.
> 매번 한 시간쯤은요. 버그에 지급하는 건 영원히 비쌉니다. 우리는 한 시간을 택했습니다. 사업이 반대로 결정한다면 시스템은 멈추는 대신 계속 가면서 표시하도록 설정할 수 있지만, 그건 흘러가다 되는 것이 아니라 결정으로 적혀야 합니다.
Priya: What would you tell the board it costs to run?
> 이사회에 운영 비용이 얼마라고 말하겠어요?
Jay: Two engineers and roughly the price of a mid-range car per year in infrastructure. The number that matters more is the one it protects: last year it moved about 400 million pounds with zero incorrect payouts. I'd put those two numbers on one slide and nothing else.
> 엔지니어 둘과 인프라로 연간 중형차 한 대 값 정도요. 더 중요한 숫자는 그것이 보호하는 숫자입니다. 지난해 약 4억 파운드를 잘못된 지급 0건으로 옮겼습니다. 그 두 숫자를 슬라이드 하나에 넣고 다른 건 넣지 않겠습니다.
Priya: You didn't use the word blockchain once.
> 블록체인이라는 단어를 한 번도 안 쓰셨네요.
Jay: You asked me not to, and it turns out I didn't need it. That's usually a good sign about the system.
> 쓰지 말라고 하셨고, 필요 없었던 것으로 드러났네요. 보통 시스템에 대해 좋은 신호입니다.

## Techniques
1. **길이를 먼저 약속하고 지킨다.** "Three sentences, then you steer." 비기술 청자가 가장 두려워하는 것은 끝나지 않는 설명이다. 길이를 선언하면 처음 세 문장에 집중해 준다.
2. **명사 대신 결과.** "checks that the money we owe never exceeds the money we hold… stops everything and pages a human." 불변식·서킷브레이커·온콜 같은 단어 없이 같은 내용. 청자가 소유한 단어만 쓴다.
3. **비용 질문에는 보호하는 숫자를 붙인다.** "Two engineers and… the number that matters more is the one it protects." 비용은 항상 그것이 막는 손실 옆에 놓아야 읽힌다. 그리고 "one slide and nothing else"로 이사회 커뮤니케이션 감각을 보여준다.

## Expressions
| assume I don't know | 제가 모른다고 가정하세요 |
| then you steer | 그다음은 당신이 방향을 잡으세요 |
| right the first time | 처음부터 맞게 |
| we cannot take it back | 되돌릴 수 없다 |
| pages a human | 사람을 호출하다(온콜 알림) |
| we chose the hour | 우리는 그 한 시간을 택했다 |
| drifted into | 결정 없이 흘러가 도달한 |
| roughly the price of a mid-range car | 대략 중형차 한 대 값 |
| the number it protects | 그것이 보호하는 숫자 |
| one slide and nothing else | 슬라이드 하나, 다른 건 없음 |
| it turns out | 드러난 바로는 |
