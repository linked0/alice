# 7 · Design — Why not just use 31337?
title_ko: 왜 그냥 31337을 쓰지 않나?
situation: The hosted devnet needs a chain id. Priya wants to keep Anvil's default so no config changes. Jay wants a dedicated id and has to argue it in terms of wallets and replay, not taste.
situation_ko: 호스팅 devnet에 체인 id가 필요하다. Priya는 설정을 바꾸지 않으려 Anvil 기본값을 유지하자고 한다. Jay는 전용 id를 원하고, 취향이 아니라 지갑과 재생 공격으로 논증해야 한다.
why: A design argument won by listing concrete failures, then conceding the one real cost so the other side does not have to find it.
why_ko: 구체적 실패를 나열해 이기는 설계 논쟁. 그리고 상대가 찾아내기 전에 진짜 비용 하나를 먼저 인정하기.

## Dialogue
Priya: Keep 31337. Every service already speaks it and nothing needs to change.
> 31337을 유지하죠. 모든 서비스가 이미 그걸 쓰고 아무것도 바꿀 필요가 없어요.
Jay: Two things break quietly. Wallets key their network list by chain id, so the local fork and the hosted devnet become one network with two RPCs. And EIP-155 replay protection is per chain id, so a signature made locally is valid on the devnet.
> 두 가지가 조용히 깨져요. 지갑은 네트워크 목록을 체인 id로 구분하니 로컬 포크와 호스팅 devnet이 RPC 둘 달린 한 네트워크가 되고, EIP-155 재생 방지는 체인 id 단위라서 로컬에서 만든 서명이 devnet에서 유효해요.
Priya: Would anyone actually replay a test signature?
> 실제로 테스트 서명을 재생할 사람이 있을까요?
Jay: Probably not on purpose. By accident, yes: same forked addresses, same nonces, one wrong RPC in an env file. That's the bug that costs an afternoon and teaches nothing.
> 의도적으로는 아마 없겠죠. 실수로는 있어요. 같은 포크 주소, 같은 nonce, env 파일의 잘못된 RPC 하나. 오후 하나를 잃고 아무것도 배우지 못하는 버그예요.
Priya: What does a new id cost us?
> 새 id는 우리에게 뭘 비용으로 요구하나요?
Jay: One entry in the rails chain list and a MetaMask add-network prompt the first time. And one thing I'll concede: MetaMask's 7715 popup won't engage on an id it doesn't know. We test that on Sepolia anyway.
> rails 체인 목록에 항목 하나와 처음 한 번의 MetaMask 네트워크 추가 프롬프트요. 그리고 하나 인정할게요. MetaMask의 7715 팝업은 모르는 id에서는 뜨지 않아요. 그건 어차피 Sepolia에서 테스트합니다.
Priya: 313370 then. It's 31337 with a zero, easy to remember.
> 그럼 313370이요. 31337에 0 하나, 기억하기 쉽네요.
Jay: And check it's unregistered on chainlist before we ship anything.
> 그리고 무엇이든 배포하기 전에 chainlist에 미등록인지 확인해요.

## Techniques
1. **"조용히 깨진다"로 시작한다.** "Two things break quietly." 지금 아무 문제 없어 보이는 이유를 미리 설명하는 프레임.
2. **가능성 질문에는 사고 경로로 답한다.** "By accident, yes: …" 확률 논쟁 대신 실수의 구체적 경로 하나를 보여준다.
3. **진짜 비용은 먼저 인정한다.** "one thing I'll concede" 상대가 찾아낼 반론을 먼저 말하면 논쟁의 신뢰가 올라간다.






## Words
| unregistered | /ənˈrɛdʒɪstɚd/ | 미등록인지 확인하라 |
| concede | /kənˈsid/ | 하나 인정하겠다 |

## Expressions
| break quietly | 조용히 깨진다 |
| key their network list by chain id | 네트워크 목록을 체인 id로 구분하다 |
| one network with two RPCs | RPC 둘 달린 한 네트워크 |
| replay protection is per chain id | 재생 방지는 체인 id 단위다 |
| by accident, yes | 실수로는, 그렇다 |
| costs an afternoon and teaches nothing | 오후를 잃고 아무것도 가르치지 않는다 |
| what does it cost us? | 우리에게 어떤 비용인가? |
| one thing I'll concede | 하나 인정하겠다 |
| won't engage on an id it doesn't know | 모르는 id에서는 작동하지 않는다 |
| check it's unregistered | 미등록인지 확인하라 |
