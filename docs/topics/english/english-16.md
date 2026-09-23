# 16 · EIP — The popup won't show on our chain
title_ko: 우리 체인에서는 팝업이 뜨지 않는다
situation: The ERC-7715 permission popup works on Sepolia and never appears on the devnet. Sun-woo thinks the devnet is broken. It isn't; MetaMask checks a supported-chain list.
situation_ko: ERC-7715 권한 팝업이 Sepolia에서는 되고 devnet에서는 절대 뜨지 않는다. 선우는 devnet이 고장났다고 생각한다. 아니다. MetaMask가 지원 체인 목록을 확인한다.
why: Explaining a vendor limitation as a fact to route around, and deciding where each test belongs instead of trying to make one chain do everything.
why_ko: 벤더 제한을 우회할 사실로 설명하고, 한 체인이 모든 것을 하게 하려 애쓰는 대신 각 테스트가 어디에 속하는지 정하기.

## Dialogue
Sun-woo: The 7715 popup never appears on the devnet. Same code works on Sepolia. Something's wrong with our chain.
> devnet에서 7715 팝업이 절대 안 떠요. 같은 코드가 Sepolia에서는 되고요. 우리 체인에 뭔가 문제가 있어요.
Jay: Nothing's wrong with the chain. MetaMask gates that popup on a list of chains it supports, and 313370 isn't on it. It wasn't on it as 31337 either.
> 체인에는 문제 없어요. MetaMask가 그 팝업을 지원 체인 목록으로 막고, 313370은 목록에 없어요. 31337이었을 때도 없었고요.
Sun-woo: Can we get on the list?
> 목록에 들어갈 수 있나요?
Jay: Not for a private devnet. So we stop trying to make one chain do everything. The delegation framework deploys fine on the devnet; I verified that on the fourteenth. The popup is a Sepolia test.
> 사설 devnet은 안 돼요. 그러니 한 체인이 모든 걸 하게 하려는 시도를 멈춰요. delegation 프레임워크는 devnet에 잘 배포돼요. 14일에 확인했어요. 팝업은 Sepolia 테스트예요.
Sun-woo: So the demo has two chains?
> 그럼 데모가 체인 둘이에요?
Jay: The demo has one path with two adapters. On the devnet the server builds the EIP-712 delegation and the user signs it; on Sepolia MetaMask does it in the popup. Same mandate either way.
> 데모는 어댑터 둘이 달린 경로 하나예요. devnet에서는 서버가 EIP-712 위임을 만들고 사용자가 서명하고, Sepolia에서는 MetaMask가 팝업에서 해요. 어느 쪽이든 같은 위임이죠.
Sun-woo: I'll write that in the README so nobody debugs this again.
> README에 적어서 아무도 이걸 다시 디버깅하지 않게 할게요.
Jay: Put it next to the chain-id decision. That's where someone will look.
> 체인 id 결정 옆에 두세요. 사람들이 찾아볼 곳이 거기예요.

## Techniques
1. **"고장"을 "제한"으로 재분류한다.** "Nothing's wrong with the chain. MetaMask gates that popup…" 원인의 위치를 옮기면 디버깅이 멈추고 설계가 시작된다.
2. **검증 사실을 날짜와 함께 말한다.** "I verified that on the fourteenth." 기억이 아니라 기록으로 말하면 신뢰가 다르다.
3. **문서의 위치까지 정한다.** "Put it next to the chain-id decision." 문서는 쓰는 것보다 찾는 곳에 두는 게 중요하다.






## Words
| deploys | /dɪˈplɔɪz/ | 잘 배포된다 |
| adapters | /əˈdæptɚz/ | 어댑터 둘이 달린 경로 하나 |
| nothing's | /ˈnʌθɪŋz/ | 체인에는 문제가 없다 |

## Expressions
| never appears | 절대 나타나지 않는다 |
| nothing's wrong with the chain | 체인에는 문제가 없다 |
| gates it on a list | 목록으로 제한한다 |
| can we get on the list? | 목록에 들어갈 수 있나? |
| make one chain do everything | 한 체인이 모든 걸 하게 하다 |
| deploys fine | 잘 배포된다 |
| one path with two adapters | 어댑터 둘이 달린 경로 하나 |
| same mandate either way | 어느 쪽이든 같은 위임 |
| so nobody debugs this again | 아무도 이걸 다시 디버깅하지 않게 |
| that's where someone will look | 사람들이 찾아볼 곳이 거기다 |
