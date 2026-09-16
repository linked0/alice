# 15 · Incident — The address was right yesterday
title_ko: 그 주소는 어제는 맞았다
situation: The exchange front end shows "contract not found." The devnet was reset overnight and reseeded; every Jayverse address changed. The front end had them hardcoded.
situation_ko: 거래소 프론트에 "컨트랙트를 찾을 수 없음"이 뜬다. devnet이 밤새 리셋되고 재시드되어 모든 Jayverse 주소가 바뀌었다. 프론트는 주소를 하드코딩했다.
why: A stale-config incident and the sentence that ends the category: the source of truth is on chain, and everything else is a cache.
why_ko: 오래된 설정 사고, 그리고 그 범주를 끝내는 문장. 진실의 원천은 체인 위에 있고 나머지는 전부 캐시다.

## Dialogue
Priya: Exchange says "contract not found" for the pool. Nothing changed on our side.
> 거래소가 풀에 대해 "컨트랙트를 찾을 수 없음"이라고 해요. 우리 쪽은 아무것도 안 바꿨어요.
Jay: The devnet reset at two a.m. and the seed ran again. Every address moved. Where does the front end get the pool address?
> devnet이 새벽 2시에 리셋되고 시드가 다시 돌았어요. 주소가 전부 바뀌었죠. 프론트는 풀 주소를 어디서 가져와요?
Priya: An env variable, set at deploy.
> 배포 때 설정하는 env 변수요.
Jay: Then it was right yesterday and wrong today, and it'll be wrong again after every reset. Read it from the Registry at startup. The Registry address is the only one that survives a reset.
> 그럼 어제는 맞고 오늘은 틀리고, 리셋마다 다시 틀릴 거예요. 시작할 때 Registry에서 읽어요. 리셋을 견디는 주소는 Registry 하나뿐이에요.
Priya: What if the Registry call fails?
> Registry 호출이 실패하면요?
Jay: Then show "chain not ready" instead of a wrong address. A visible failure beats a confident wrong number.
> 그럼 틀린 주소 대신 "체인 준비 안 됨"을 보여줘요. 보이는 실패가 자신감 있는 틀린 숫자보다 나아요.
Priya: Should the env var stay as a fallback?
> env 변수는 폴백으로 남길까요?
Jay: No. A fallback that is usually stale is a trap. One source, and it's the chain.
> 아니요. 대개 오래된 폴백은 함정이에요. 원천은 하나, 체인이에요.

## Techniques
1. **원인을 질문으로 도출한다.** "Where does the front end get the pool address?" 답을 알아도 질문하면 상대가 구조를 스스로 본다.
2. **재발 조건을 명시한다.** "it'll be wrong again after every reset" 이번 사고를 범주로 확장하는 한 문장.
3. **보이는 실패를 선택한다.** "A visible failure beats a confident wrong number." 폴백 논쟁을 끝내는 원칙.

## Expressions
| nothing changed on our side | 우리 쪽은 아무것도 바꾸지 않았다 |
| every address moved | 주소가 전부 바뀌었다 |
| set at deploy | 배포 때 설정되는 |
| right yesterday and wrong today | 어제는 맞고 오늘은 틀리다 |
| survives a reset | 리셋을 견딘다 |
| chain not ready | 체인 준비 안 됨 |
| a visible failure | 보이는 실패 |
| a confident wrong number | 자신감 있는 틀린 숫자 |
| usually stale | 대개 오래된 |
| one source, and it's the chain | 원천은 하나, 체인이다 |
