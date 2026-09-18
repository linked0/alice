## en
- **Wallet: guard modular inverse in any custom signature-recovery code.** Session-key and mandate verification (EIP-7702/7715) runs over secp256k1's prime field; make sure custom code checks gcd(a,n)=1 rather than assuming a library always guards the non-invertible case.
- **Verex: CRT-style splitting is the next lever if order-matching math needs big numbers.** Beyond LMSR's mulDiv precision, note Chinese Remainder splitting as the tool if big-integer arithmetic ever becomes a gas bottleneck in matching or settlement.
- **DeFi: verify gcd(a,n)=1 before reusing a prime-field exponent trick.** If the liquid-staking study needs a custom modular exponent for rebasing or index math, confirm the chosen modulus actually satisfies the condition Euler's theorem requires, don't just borrow the RSA-shaped formula.

## ko
- **Wallet: 커스텀 서명 복구 코드에서 모듈러 역원을 반드시 확인한다.** 세션 키와 mandate 검증(EIP-7702/7715)은 secp256k1의 소수체 위에서 돌아간다. 라이브러리가 항상 역원 없는 경우를 막아준다고 가정하지 말고, 커스텀 코드가 gcd(a,n)=1을 직접 확인하게 한다.
- **Verex: 주문 매칭에 큰 수가 필요해지면 CRT 분할이 다음 카드다.** LMSR의 mulDiv 정밀도를 넘어, 매칭이나 정산에서 큰 정수 연산이 가스 병목이 되면 중국인의 나머지 정리 분할을 도구로 기록해둔다.
- **DeFi: 소수체 지수 트릭을 재사용하기 전 gcd(a,n)=1을 확인한다.** 리베이싱이나 인덱스 계산에 커스텀 모듈러 지수가 필요하다면, RSA 형태 공식을 그냥 빌려오지 말고 선택한 모듈러스가 오일러 정리가 요구하는 조건을 실제로 만족하는지 확인한다.
