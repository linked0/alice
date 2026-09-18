## en
- **Verex contracts: add a checks-effects-interactions review and a reentrancy-guard to every withdraw/claim path in the ctf-exchange fork.** Add a Foundry invariant test that fails on any external call occurring before its own balance write.
- **Bridge/DeFi: audit the lock-and-mint unlock path and the from-scratch staking withdraw path the same way.** Both are the same "callback before state update" shape as the classic exploit, so the same guard and test belong there too.

## ko
- **Verex 컨트랙트: ctf-exchange 포크의 모든 withdraw/claim 경로에 checks-effects-interactions 리뷰와 리엔트런시 가드를 추가한다.** 자기 잔액 쓰기보다 먼저 일어나는 외부 호출이 있으면 실패하는 Foundry 인바리언트 테스트를 추가한다.
- **Bridge/DeFi: 락앤민트의 언락 경로와 처음부터 만든 스테이킹의 인출 경로도 같은 방식으로 감사한다.** 둘 다 고전적 익스플로잇과 같은 "상태 갱신 전 콜백" 형태이므로 같은 가드와 테스트가 거기에도 필요하다.
