## en
- **Devnet/Wallet: audit every length-prefixed parsing path for a bounds check.** Review RPC clients, the bridge relayer, and any custom binary decoding for an explicit bounds check on attacker-controlled length fields; Heartbleed's entire bug was one missing check.
- **CI: flag unsafe/C-dependency additions for this exact risk class.** Add a CI checklist item so any new C/C++ or unsafe dependency introduced into the otherwise TypeScript/Solidity stack gets reviewed for missing-bounds-check risk before it's pinned as a submodule.

## ko
- **Devnet/Wallet: 길이 접두 파싱 경로마다 경계 검사를 점검한다.** RPC 클라이언트, 브리지 릴레이어, 그 외 커스텀 바이너리 디코딩에서 공격자가 제어하는 길이 필드에 명시적 경계 검사가 있는지 확인한다. Heartbleed 버그 전체가 이 검사 하나의 누락이었다.
- **CI: 이 위험 클래스에 대해 unsafe/C 의존성 추가를 표시한다.** TypeScript/Solidity 중심 스택에 새로운 C/C++이나 unsafe 의존성이 들어올 때마다, 서브모듈로 고정되기 전에 경계 검사 누락 위험을 리뷰하는 CI 체크리스트 항목을 추가한다.
