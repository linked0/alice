## en
- **Dark Horse: if security-hole research or a Base App mini-app ever runs third-party or untrusted code, use "the sandbox boundary is the import list" directly.** Audit exactly which host functions are exposed.
- **OFA: if solvers are ever allowed to submit executable strategy code rather than just bids, treat that code like WASM-hosted code.** Require an explicit, minimal capability list rather than trusting the auction to vet it.
- **Auditor: record "the boundary equals the import list" as a standing methodology check.** Apply it to any future non-EVM or plugin-style execution surface Jayverse adds.

## ko
- **Dark Horse: 보안 취약점 연구나 Base App 미니앱이 서드파티 또는 신뢰할 수 없는 코드를 실행하게 되면, "샌드박스 경계는 곧 import 목록"이라는 프레임을 그대로 적용한다.** 어떤 호스트 함수가 노출되는지 정확히 감사한다.
- **OFA: 솔버가 입찰뿐 아니라 실행 가능한 전략 코드를 제출할 수 있게 된다면, 그 코드를 WASM 호스팅 코드처럼 취급한다.** 경매 결과를 신뢰하는 대신 명시적이고 최소한의 권한 목록을 요구한다.
- **Auditor: "경계는 곧 import 목록"이라는 점검을 표준 방법론 항목으로 기록한다.** Jayverse가 향후 추가할 비-EVM 또는 플러그인 방식 실행 표면에 적용한다.
