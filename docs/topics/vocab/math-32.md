| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| scale back down | (원래 규모로) 다시 축소하다 · 곱셈 후 늘어난 소수부 비트를 되돌려 줄이는 과정. "must be scaled back down by dividing by 2^n" |
| the single biggest risk | 가장 큰 단일 위험 요소 · 중간 오버플로가 최대 위험임을 강조할 때. "makes intermediate overflow the single biggest risk" |
| carry (an intermediate result) | (계산 중간값을) 담아 처리하다 · 512비트 중간 결과를 유지하는 mulDiv 로직. "carries a 512-bit intermediate result" |
| truncate | (하위 비트를) 잘라내다, 버리다 · 나눗셈 과정에서 정밀도가 손실되는 이유. "division inevitably truncates low-order bits" |
| favor X over Y | Y보다 X에 유리하게 처리하다 · 반올림 방향이 프로토콜보다 사용자에게 유리하지 않게 한다는 원칙. "doesn't favor the user over the protocol" |
| leak (balance) | (자금·잔고가) 의도치 않게 새어나가다 · 반올림 실수가 프로토콜 잔고 유출로 이어지는 상황. "the protocol's balance can leak" |
| Q64.96 | 정수부 64비트, 소수부 96비트의 고정소수점 표기(Qm.n notation) · Uniswap v3가 가격의 제곱근을 저장하는 포맷. "Q64.96 puts 96 bits in the fractional part" |
| Uniswap v3 | 대표적인 탈중앙 거래소(DEX) 프로토콜 · Q64.96 포맷으로 가격의 제곱근을 저장하는 주체. "the format Uniswap v3 uses to store the square root" |
| LMSR | 로그 시장 스코어링 규칙(Logarithmic Market Scoring Rule) · 예측시장 가격 결정에 쓰이는 메커니즘, 고정소수점 근사가 필요한 지점. "LMSR price calculation and settlement amounts both need fixed-point approximations" |
| mulDiv | 곱한 뒤 나누되 512비트 중간값을 유지해 오버플로를 막는 함수 패턴(mulDiv) · 정밀도 손실과 오버플로를 동시에 방지하는 구현 방식. "implementations need mulDiv-style logic that carries a 512-bit intermediate result" |
<!-- acronyms 2026-09-18 -->
