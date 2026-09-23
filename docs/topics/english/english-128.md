# 128 · Word — foul play
title_ko: foul play — 범죄 행위(살인·폭행), 반칙·부정행위
situation: Overnight, a hot wallet on the staging cluster drained to zero. In the morning incident call, Marek, the security lead, wants to know whether someone did it on purpose. Jay has looked at the logs and does not want to name a crime before ruling out a bug.
situation_ko: 밤사이 스테이징 클러스터의 핫월렛 잔액이 0이 됐다. 아침 장애 회의에서 보안 리드 Marek이 누군가 고의로 한 일인지 알고 싶어 한다. 로그를 본 Jay는 버그를 배제하기 전에 범죄라고 이름 붙이고 싶지 않다.
why: **Foul play** has two homes. In police and news language it means criminal action behind a death or a loss — "no sign of foul play" is the stock phrase when a death turns out to be natural. In sport it means cheating or a foul. In an incident, "foul play" is the careful way to say "someone did this deliberately" without saying "hack" or "theft" yet; **suspect foul play** and **rule out foul play** are the usual verbs. It is a noun only; there is no "foul-played". It is not "fair play", its opposite, and not "a foul" on its own, which is one rule violation in a game.
why_ko: **Foul play**는 두 자리에서 산다. 경찰과 뉴스 언어에서는 죽음이나 손실 뒤에 있는 범죄 행위를 뜻하며, 사망이 자연사로 밝혀질 때 "no sign of foul play"가 상투구다. 스포츠에서는 반칙이나 부정행위다. 장애 상황에서 "foul play"는 아직 "hack"이나 "theft"라고 하지 않으면서 "누가 고의로 했다"를 조심스럽게 말하는 방법이고, **suspect foul play**와 **rule out foul play**가 흔한 동사 짝이다. 명사로만 쓴다. "foul-played" 같은 동사는 없다. 반대말인 "fair play"와도 다르고, 경기의 반칙 한 번을 뜻하는 "a foul"과도 다르다.
status: new
added: 2026-09-21
source: jay's NAVER 영어단어장, second export (2026-09-21), page 3 card 13 (word): 옥스퍼드 영한사전 "foul play — 1. 명사 폭행치사; 살인 2. 명사 (특히 스포츠 경기에서) 부정행위[반칙]". The situation and dialogue are new.
source_ko: jay의 NAVER 영어단어장, 두 번째 내보내기(2026-09-21), 3페이지 13번 카드(단어): 옥스퍼드 영한사전 "foul play — 1. 명사 폭행치사; 살인 2. 명사 (특히 스포츠 경기에서) 부정행위[반칙]". 상황과 대화는 새로 썼다.
raw: 2026-09-21-english-79.txt

## Dialogue
Marek: The staging hot wallet is empty. Do we treat this as an attack?
> 스테이징 핫월렛이 비었어요. 공격으로 봐야 하나요?
Jay: Not yet. I don't want to call it foul play before we rule out a bug. The drain went to our own fee-collector address, in twelve regular transactions.
> 아직은요. 버그를 배제하기 전에 범죄 행위라고 부르고 싶지 않아요. 빠져나간 돈은 우리 수수료 수집 주소로, 12건의 규칙적인 트랜잭션으로 갔어요.
Marek: "Foul play" — that's the police phrase, isn't it?
> "foul play"는 경찰이 쓰는 말 아닌가요?
Jay: It is. "No sign of foul play" means nobody did it on purpose. Here it looks like the sweep job ran with the wrong threshold, not like theft.
> 맞아요. "No sign of foul play"는 아무도 고의로 하지 않았다는 뜻이죠. 여기선 스윕 작업이 잘못된 임계값으로 돈 것 같지, 도둑맞은 것 같지는 않아요.
Marek: And if the address weren't ours?
> 주소가 우리 게 아니었다면요?
Jay: Then I'd suspect foul play and we'd rotate every key on the cluster before lunch.
> 그럼 범죄 행위를 의심하고 점심 전에 클러스터의 키를 전부 교체했을 거예요.

## Techniques
1. **결론 단어를 쓰기 전에 배제 조건을 말한다.** "I don't want to call it foul play before we rule out a bug" — 판단을 미루는 이유가 곧 조사 순서가 된다.
2. **반대 가정으로 단어의 무게를 보여 준다.** "And if the address weren't ours?" → "Then I'd suspect foul play" — 어떤 증거가 나오면 말이 바뀌는지 짝으로 제시한다.



## Words
| foul play | /faʊl pleɪ/ | (죽음·손실 뒤의) 범죄 행위; 반칙 |
| rule out X | /rul aʊt ɛks/ | X를 배제하다 |
| suspect foul play | /səˈspɛkt faʊl pleɪ/ | 범죄 행위를 의심하다 |
| rotate a key | /ˈroʊˌteɪt ə ki/ | 키를 교체하다 |

## Expressions
| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| foul play | (죽음·손실 뒤의) 범죄 행위; 반칙 — "call it foul play", "no sign of foul play" |
| rule out X | X를 배제하다 — 조사 순서. "before we rule out a bug" |
| suspect foul play | 범죄 행위를 의심하다 — 장애·보안 회의 |
| rotate a key | 키를 교체하다 — 침해 의심 시 조치 |
