# 4 · EIP — Does Quick Slots make finality faster?
title_ko: Quick Slots가 최종성을 빠르게 하나?
situation: Sun-woo read the EIP-8198 thread and wants to tell the team "Ethereum is getting fast finality." Jay has to correct the claim without killing the enthusiasm.
situation_ko: 선우가 EIP-8198 스레드를 읽고 팀에 "Ethereum이 빠른 최종성을 얻는다"고 말하려 한다. Jay는 열의를 꺾지 않으면서 주장을 바로잡아야 한다.
why: How to correct a technical overstatement: separate what scales from what changes structure, and give the person a better sentence to say.
why_ko: 기술적 과장을 바로잡는 법. 비례해서 줄어드는 것과 구조가 바뀌는 것을 구분하고, 상대에게 더 나은 문장을 건넨다.

## Dialogue
Sun-woo: Quick Slots means fast finality, right? Ten-second slots, so everything finalizes faster.
> Quick Slots면 최종성이 빨라지는 거죠? 10초 슬롯이니까 전부 더 빨리 확정되고요.
Jay: Faster, yes. Fast, no. The epoch stays thirty-two slots and finality is still two epochs, so twelve point eight minutes becomes ten point seven.
> 더 빨라지긴 해요. 빠르진 않고요. 에포크는 32슬롯 그대로고 최종성은 여전히 2에포크라서, 12.8분이 10.7분이 됩니다.
Sun-woo: That's barely a change.
> 거의 차이가 없네요.
Jay: For finality, it isn't one. What the EIP buys is inclusion latency: how long until your transaction is in a block, how stale a DEX price gets. That scales with the slot directly.
> 최종성에는 변화가 아니죠. EIP가 사는 건 포함 지연이에요. 트랜잭션이 블록에 들어가기까지, DEX 가격이 얼마나 오래되는지. 그건 슬롯에 직접 비례합니다.
Sun-woo: So what should I say instead?
> 그럼 대신 뭐라고 말하죠?
Jay: "Blocks land faster, finality stays a different project." Fast finality comes from three-slot finality and the lean consensus work, and the EF's fourth prerequisite is that 8198 must not get in their way.
> "블록은 더 빨리 들어오고, 최종성은 별개의 프로젝트다." 빠른 최종성은 3슬롯 최종성과 lean 합의 작업에서 오고, EF의 네 번째 전제 조건이 8198이 그걸 방해하면 안 된다는 거예요.
Sun-woo: Got it. Two tracks, not one.
> 알겠어요. 하나가 아니라 두 트랙이네요.
Jay: Exactly. And if anyone asks what changes for us: our bridge waits for finalized, so nothing. The user-visible win is the bet confirming sooner.
> 정확해요. 우리에게 뭐가 바뀌냐고 누가 물으면, 브리지는 finalized를 기다리니 아무것도요. 사용자가 보는 이득은 베팅이 더 빨리 확인되는 거죠.

## Techniques
1. **정도와 종류를 갈라 답한다.** "Faster, yes. Fast, no." 비교급과 원급을 나누는 네 단어가 과장을 정확히 잘라낸다.
2. **틀린 문장 대신 맞는 문장을 준다.** "So what should I say instead?" 에 답을 준비해 두면 교정이 거절이 아니라 도움이 된다.
3. **우리에게의 결과로 닫는다.** "if anyone asks what changes for us" 기술 논의를 팀의 행동 하나로 끝내면 대화가 남는다.



## Words
| barely a change | /ˈbɛrli ə tʃeɪndʒ/ | 거의 변화가 없다 |
| inclusion latency | /ˌɪnˈkluʒən ˈleɪtənsi/ | 포함 지연 |
| different project | /ˈdɪfɚənt ˈprɑdʒɛkt/ | 별개의 프로젝트 |

## Expressions
| Faster, yes. Fast, no. | 더 빠르긴 하다. 빠르진 않다. |
| the epoch stays thirty-two slots | 에포크는 32슬롯 그대로다 |
| barely a change | 거의 변화가 없다 |
| inclusion latency | 포함 지연 |
| scales with the slot directly | 슬롯에 직접 비례한다 |
| what should I say instead? | 대신 뭐라고 말해야 하나? |
| a different project | 별개의 프로젝트 |
| must not get in their way | 그들을 방해하면 안 된다 |
| two tracks, not one | 하나가 아닌 두 트랙 |
| the user-visible win | 사용자가 보는 이득 |
