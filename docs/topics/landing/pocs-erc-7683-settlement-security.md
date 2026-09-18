## en
- **Verex: name the settlement model before calling anything "7683 compatible."** If Verex ever uses an intent/filler model across chains, write down which of the three settlement models (optimistic, light client, bridge committee) it uses and price the filler spread from the actual capital-lockup time, not from the label.
- **Bridge/Token: run the general-call test on the relayer.** Check whether the JYVE lock-and-mint relayer's mint path exposes a general call(target, calldata) reachable through any privileged role; if it does, narrow it to a pre-registered whitelist of functions and addresses, the same mitigation that would have stopped the Term Labs pattern.
- **Auditor: add "does settlement expose a general call" as a standing yes/no check.** Apply it to every cross-chain or privileged-role contract (Bridge, Verex filler, OFA solver) before sign-off, since the answer decides whether security is a property of the code or of whoever holds the permission.

## ko
- **Verex: "7683 호환"이라 부르기 전에 정산 모델부터 지정한다.** Verex가 체인 간 인텐트/필러 모델을 쓰게 된다면 세 정산 모델(낙관적, 라이트 클라이언트, 브리지 위원회) 중 무엇을 쓰는지 적어두고, 라벨이 아니라 실제 자본 잠김 시간으로 필러 스프레드를 가격 책정한다.
- **Bridge/Token: 릴레이어에 general call 테스트를 적용한다.** JYVE lock-and-mint 릴레이어의 민팅 경로가 어떤 권한 있는 역할을 통해서든 general call(target, calldata)에 도달 가능한지 확인한다. 가능하다면 사전 등록된 함수·주소 화이트리스트로 좁힌다. Term Labs 패턴을 막았을 완화책과 같다.
- **Auditor: "정산이 general call을 노출하는가"를 상시 체크 항목으로 추가한다.** Bridge, Verex 필러, OFA 솔버 등 체인 간 또는 권한 역할이 있는 모든 컨트랙트에 승인 전 적용한다. 이 답이 보안을 코드의 속성으로 만들지, 권한 보유자의 시가로 만들지를 결정한다.
