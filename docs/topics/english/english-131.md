# 131 · Word — footgun
title_ko: footgun — 자충수, 자기 발등을 찍게 만드는 API나 패턴 (개발자 은어)
situation: Yusuf opens a PR that adds a config flag which silently disables retries for the whole service when it is left unset. Jay reviews it and wants to name the problem in one word before explaining why the default should be the safe one.
situation_ko: Yusuf가 설정 플래그 하나를 추가하는 PR을 올렸는데, 그 플래그를 비워 두면 서비스 전체의 재시도가 조용히 꺼진다. Jay는 리뷰에서 왜 기본값이 안전한 쪽이어야 하는지 설명하기 전에 그 문제를 한 단어로 짚고 싶다.
why: A **footgun** is a feature, API, or pattern that makes it easy to shoot yourself in the foot: it works, but the obvious way to use it hurts you later. It is developer slang, fine in code review, Slack, and design docs, and it is not an insult to the author; it describes the design, not the person. It is not a bug (the code does what it says) and not a security hole; a footgun is a trap that the design leaves for the next user. In Korean it is closest to 자충수 or "자기 발등 찍는 API".
why_ko: **footgun**은 자기 발등을 쏘기 쉽게 만드는 기능·API·패턴이다. 동작은 하지만 가장 뻔한 사용법이 나중에 나를 다치게 한다. 개발자 은어라 코드 리뷰, Slack, 설계 문서에서는 무난하고, 작성자에 대한 모욕이 아니라 설계에 대한 평가다. 버그(코드가 말한 대로 하지 않음)도, 보안 구멍도 아니다. footgun은 설계가 다음 사용자에게 남겨 둔 함정이다. 한국어로는 자충수, "자기 발등 찍는 API"에 가깝다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, second export (2026-09-21), page 3 card 14 (memo): term note "footgun — 자충수·자기 발등 찍는 API/패턴 (개발자 은어)"; the card's word "unhinged" is Eng #130. The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 두 번째 내보내기(2026-09-21), 3페이지 14번 카드(메모): 용어 메모 "footgun — 자충수·자기 발등 찍는 API/패턴 (개발자 은어)"; 이 카드의 단어 "unhinged"는 Eng #130. 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-79.txt

## Dialogue
Yusuf: The flag is optional. If you don't set it, retries are just off. Simpler that way.
> 그 플래그는 선택 사항이에요. 안 정하면 재시도가 그냥 꺼져요. 그게 더 단순하죠.
Jay: That's a footgun, though. Nobody reads the config docs before an incident, so the first person who forgets the flag ships a service with no retries and finds out at 3 a.m.
> 그런데 그건 footgun이에요. 장애 나기 전에 설정 문서를 읽는 사람은 없으니까, 플래그를 깜빡한 첫 번째 사람이 재시도 없는 서비스를 배포하고 새벽 3시에 알게 되죠.
Yusuf: Footgun?
> footgun이요?
Jay: A design that makes it easy to shoot yourself in the foot. The code isn't wrong; the default is the trap. Flip it: retries on by default, and an explicit flag to turn them off.
> 자기 발등을 쏘기 쉽게 만드는 설계요. 코드가 틀린 게 아니라 기본값이 함정이에요. 뒤집죠. 기본은 재시도 켜짐, 끄려면 명시적으로 플래그를 주는 걸로요.
Yusuf: Fair. Safe by default, opt out on purpose.
> 그러네요. 기본은 안전하게, 끄는 건 의도적으로.
Jay: Exactly. Remove the footgun and the flag is fine.
> 맞아요. footgun만 없애면 플래그 자체는 괜찮아요.

## Techniques
1. **설계의 함정은 한 단어로 이름 붙이고, 사람이 아니라 기본값을 문제 삼는다.** "That's a footgun" 뒤에 "The code isn't wrong; the default is the trap."을 붙이면 작성자를 공격하지 않으면서 왜 위험한지 분명해진다.
2. **은어를 쓰면 상대가 되물을 때 한 문장 정의를 준비해 둔다.** "A design that makes it easy to shoot yourself in the foot." — 정의 뒤에 바로 대안("Flip it: retries on by default")을 붙여 리뷰를 닫는다.





## Words
| opt | /ɑpt/ | (기본에서) 빠지기로 선택하다 |
| default | /dɪˈfɔlt/ | 기본값이 안전한 쪽 |

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| footgun | 자기 발등 찍게 만드는 API·패턴, 자충수 — 코드 리뷰·설계 문서의 개발자 은어. "That's a footgun, though." |
| shoot yourself in the foot | 자기 발등을 찍다 — footgun의 어원이 되는 관용구. "makes it easy to shoot yourself in the foot" |
| safe by default | 기본값이 안전한 쪽 — 설정·API 설계 원칙. "Safe by default, opt out on purpose." |
| opt out | (기본에서) 빠지기로 선택하다 — 명시적으로 꺼야 하는 옵션을 말할 때 |
