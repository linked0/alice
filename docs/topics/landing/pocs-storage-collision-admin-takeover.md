## en
- **Rabbit: run a pairwise storage-layout check on mandate/session-key modules.** Any pluggable module that executes inside the account's storage context needs a peer-set slot-collision check before a second module type ships, not just a per-module review.
- **Bridge: write the admin-change invariant into CI.** "The admin address only changes inside an admin-change transaction" is a one-line assertion that catches this exact bug class in the relayer and lock-and-mint contracts — add it now, not after an adapter is added.
- **gitboard/CI: point storage-layout tooling at peer sets, not just upgrades.** Existing layout-diff tooling compares version N to N+1 of one contract; repoint it, or add a pass, that compares every module sharing one host's storage against every other module.

## ko
- **Rabbit: 매니데이트/세션 키 모듈에 페어와이즈 스토리지 레이아웃 검사를 돌린다.** 계정의 스토리지 컨텍스트 안에서 실행되는 플러거블 모듈은 개별 모듈 리뷰만으로는 부족하고, 두 번째 모듈 타입을 추가하기 전에 피어 집합 단위의 슬롯 충돌 검사가 필요하다.
- **Bridge: 관리자 변경 불변식을 CI에 넣는다.** "관리자 주소는 관리자 변경 트랜잭션 안에서만 바뀐다"는 한 줄짜리 어서션이 이 버그 클래스를 정확히 잡아낸다. 릴레이어와 락앤민트 컨트랙트에 어댑터를 추가하기 전에 지금 넣는다.
- **gitboard/CI: 레이아웃 도구를 업그레이드가 아니라 피어 집합에 겨냥한다.** 기존 레이아웃 diff 도구는 한 컨트랙트의 버전 N과 N+1을 비교하는 데 맞춰져 있다. 하나의 호스트 스토리지를 공유하는 모든 모듈을 서로 비교하도록 재조준하거나 별도 패스를 추가한다.
