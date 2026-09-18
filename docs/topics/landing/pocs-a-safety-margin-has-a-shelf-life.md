## en
- **Wallet: put session-key and signature verification behind one interface.** Every EIP-7702/7715 signature check in Wallet and Rabbit should be reachable from a single point, so a scheme swap is a migration with a procedure, not a scattered redeploy.
- **Devnet: date-stamp every "big enough" security parameter.** Key lengths, session-key expiry windows, and bond sizes chosen because they're "safe" should carry the date and the attack they were measured against, turning review into a scheduled event.
- **Auditor: count verification sites and check for drift, not just count them.** Where signature or nonce checks are already duplicated across Rabbit/Wallet code, flag any place one copy skips a check the others do — that's a bug to fix now, ahead of any future migration.

## ko
- **Wallet: 세션 키와 서명 검증을 하나의 인터페이스 뒤에 둔다.** Wallet과 Rabbit의 모든 EIP-7702/7715 서명 체크는 한 지점에서 도달 가능해야 한다. 그래야 스킴 교체가 흩어진 재배포가 아니라 절차가 있는 마이그레이션이 된다.
- **Devnet: "충분히 크다"는 모든 보안 파라미터에 날짜를 찍는다.** 키 길이, 세션 키 만료 기간, 본드 크기처럼 "안전하다"고 고른 값은 날짜와 그 기준이 된 공격을 함께 적어, 리뷰를 일정화된 이벤트로 만든다.
- **Auditor: 검증 지점을 세는 것을 넘어 드리프트를 점검한다.** Rabbit·Wallet 코드에서 서명·논스 체크가 이미 중복돼 있다면 한 곳만 체크를 빠뜨린 곳이 있는지 표시한다. 그건 미래 마이그레이션 이전에 지금 고쳐야 할 버그다.
