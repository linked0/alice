## en
- **Bridge/Token: name whose compromise mints infinitely.** For the JYVE Anvil⇄Sepolia lock-and-mint bridge, write down explicitly which party's key or role can mint without bound, and choose an xERC20-style per-bridge rate limit rather than leaving mint authority open-ended.
- **Bridge/Token: compute the real loss cap, not the nominal limit.** Use limit plus refill-rate times detection latency, with an honest detect-and-pause time that includes nights and weekends, when sizing any rate limit on the bridge.
- **Auditor: verify mint authority on-chain, not from docs.** Add "whose compromise mints infinitely" as a standing checklist item for JYVE and any Verex settlement asset, checked against the deployed configuration.

## ko
- **Bridge/Token: 누구의 침해가 무한 민팅으로 이어지는지 지정한다.** JYVE Anvil⇄Sepolia lock-and-mint 브리지에서 어떤 키나 역할이 무제한으로 민팅할 수 있는지 명시하고, 민팅 권한을 열어두는 대신 xERC20 방식의 브리지별 레이트 리밋을 선택한다.
- **Bridge/Token: 명목 한도가 아니라 실제 손실 상한을 계산한다.** 한도 더하기 리필 속도 곱하기 탐지 지연으로 계산하되, 야간·주말을 포함한 정직한 탐지-일시정지 시간을 브리지 레이트 리밋 설계에 사용한다.
- **Auditor: 민팅 권한을 문서가 아니라 온체인에서 검증한다.** "누구의 침해가 무한 민팅인가"를 JYVE와 모든 Verex 정산 자산에 대한 상시 체크 항목으로 추가하고 배포된 설정 값으로 확인한다.
