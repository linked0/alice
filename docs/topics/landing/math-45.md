## en
- **Wallet/Rabbit: reject signatures whose scalar isn't reduced mod the curve order or that use non-canonical (high-s) form.** Add this check at the simulate-before-sign step for both regular ECDSA and any session-key/mandate signature.
- **Auditor: add "signature malleability / small-subgroup check" as a standing methodology item.** Apply it to every contract verifying ECDSA/EIP-712 signatures across Rabbit, Verex and Bridge, not just once at launch.
- **Bridge: audit the lock-and-mint relayer's signature verification for the same group-order reduction.** Bridge relayers using multisig or threshold signatures are a common target for exactly this bug class.

## ko
- **Wallet/Rabbit: 곡선 위수(order)로 축소되지 않았거나 정규형(비-high-s)이 아닌 서명 스칼라는 거부한다.** 일반 ECDSA뿐 아니라 세션 키/명령 서명에도 simulate-before-sign 단계에서 이 검사를 추가한다.
- **Auditor: "서명 malleability / 소부분군 점검"을 상시 방법론 항목으로 추가한다.** Rabbit, Verex, Bridge 전반에서 ECDSA/EIP-712 서명을 검증하는 모든 컨트랙트에 적용하고, 출시 시점 한 번으로 끝내지 않는다.
- **Bridge: lock-and-mint 릴레이어의 서명 검증도 같은 그룹 위수 축소 기준으로 감사한다.** 멀티시그나 threshold 서명을 쓰는 브리지 릴레이어는 정확히 이 버그 클래스의 흔한 표적이다.
