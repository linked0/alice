# 9 · EIP — 7702 or 4337 for the wallet
title_ko: 지갑에 7702냐 4337이냐
situation: The wallet needs gasless transactions. Marek wants ERC-4337 because the bundlers exist. Jay leans EIP-7702 because the user keeps their address. Both are right about something.
situation_ko: 지갑에 가스리스 트랜잭션이 필요하다. Marek은 번들러가 이미 있으니 ERC-4337을, Jay는 사용자가 주소를 유지하니 EIP-7702를 원한다. 둘 다 무언가에 대해서는 맞다.
why: How to argue a standards choice: name what each one is actually for, then find the layer where you don't have to choose.
why_ko: 표준 선택 논쟁법. 각각이 실제로 무엇을 위한 것인지 이름 붙이고, 선택하지 않아도 되는 층을 찾는다.

## Dialogue
Marek: Go with 4337. Alchemy runs the bundler and the paymaster, and it works on Sepolia today.
> 4337로 가요. Alchemy가 번들러와 페이마스터를 운영하고 Sepolia에서 오늘 동작해요.
Jay: It does, and the user gets a new address, a smart account, that isn't the one they arrived with. 7702 lets the same EOA borrow contract code, so their address stays.
> 그렇죠. 그리고 사용자는 도착했을 때의 주소가 아닌 새 주소, 스마트 계정을 받아요. 7702는 같은 EOA가 컨트랙트 코드를 빌리게 하니 주소가 유지되죠.
Marek: But there's no 7702 bundler infrastructure on our devnet.
> 그런데 우리 devnet에는 7702 번들러 인프라가 없어요.
Jay: There's no 4337 bundler there either. Anvil is just a node. Either way the devnet needs us to run something.
> 4337 번들러도 거기엔 없어요. Anvil은 노드일 뿐이죠. 어느 쪽이든 devnet에서는 우리가 뭔가를 돌려야 해요.
Marek: So it's not really a devnet argument.
> 그러니까 devnet 논쟁은 아니네요.
Jay: No. The real question is what the user keeps. I'd design the intent layer so the account type is an adapter: 7702 where the chain supports it, 4337 where a bundler exists, same preview, same receipt.
> 아니에요. 진짜 질문은 사용자가 무엇을 유지하느냐예요. 계정 타입이 어댑터가 되게 인텐트 층을 설계하겠어요. 체인이 지원하면 7702, 번들러가 있으면 4337, 미리보기와 영수증은 같게요.
Marek: That's more work up front.
> 초반 작업이 더 많네요.
Jay: A week more, and we stop having this argument every fork. Let's write the capability matrix first and pick per chain from it.
> 일주일 더요. 그리고 포크마다 이 논쟁을 다시 하지 않게 되죠. capability matrix를 먼저 쓰고 체인별로 거기서 고릅시다.

## Techniques
1. **"맞다, 그리고"로 받는다.** "It does, and the user gets a new address" 상대의 사실을 인정한 뒤 빠진 결과를 붙인다.
2. **가짜 논점을 걷어낸다.** "So it's not really a devnet argument." 상대가 스스로 말하게 유도해 진짜 질문으로 돌아온다.
3. **선택을 어댑터로 바꾼다.** "the account type is an adapter" 양자택일을 설계 층 하나로 흡수하면 논쟁이 반복되지 않는다.



## Words
| borrow contract code | /ˈbɑˌroʊ ˈkɑnˌtrækt koʊd/ | 컨트랙트 코드를 빌리다 |
| either way | /ˈiðɚ weɪ/ | 어느 쪽이든 |

## Expressions
| go with 4337 | 4337로 가자 |
| the one they arrived with | 그들이 가지고 온 것 |
| borrow contract code | 컨트랙트 코드를 빌리다 |
| there's no … there either | 거기엔 …도 없다 |
| either way | 어느 쪽이든 |
| not really a … argument | 사실 … 논쟁이 아니다 |
| what the user keeps | 사용자가 유지하는 것 |
| same preview, same receipt | 같은 미리보기, 같은 영수증 |
| more work up front | 초반 작업이 더 많다 |
| pick per chain from it | 거기서 체인별로 고르다 |
