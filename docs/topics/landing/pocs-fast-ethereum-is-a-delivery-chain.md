## en
- **Devnet: store a confidence label alongside every cached block state, never just a boolean.** Since every service reads chain state through Devnet's RPC, tag cached reads with head/fast-confirmed/safe/finalized rather than a plain "confirmed" flag.
- **Wallet/Bridge: replace fixed confirmation counts with an explicit policy on the Anvil⇄Sepolia bridge.** Test reorg, stale-RPC, and fallback behavior directly, and require the policy to fail closed rather than silently trust an unconfirmed deposit.
- **Verex: log which confidence tier a resolution actually read at settlement time.** A faster L1 signal changes nothing for Verex unless the resolution pipeline explicitly adopts it, so record safe-versus-finalized per market resolution.

## ko
- **Devnet: 캐시된 블록 상태마다 불리언 하나가 아니라 확신도 라벨을 함께 저장한다.** 모든 서비스가 Devnet의 RPC를 통해 체인 상태를 읽으므로, 캐시된 값에는 단순 "confirmed" 대신 head/fast-confirmed/safe/finalized를 태깅한다.
- **Wallet/Bridge: Anvil⇄Sepolia 브리지에서 고정된 확인 횟수 대신 명시적 정책을 쓴다.** 리오그, RPC 지연, 폴백 동작을 직접 테스트하고, 확인되지 않은 입금을 조용히 신뢰하지 말고 정책이 명시적으로 닫혀서 실패하게 한다.
- **Verex: 정산 시점에 실제로 어느 확신도 등급을 읽었는지 기록한다.** 더 빠른 L1 신호도 Verex의 정산 파이프라인이 명시적으로 채택하지 않으면 아무것도 바꾸지 않으므로, 마켓 정산마다 safe인지 finalized인지 기록한다.
