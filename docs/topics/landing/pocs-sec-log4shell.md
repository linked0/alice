## en
- **CI: audit what every logging call actually does with untrusted input.** Rabbit, Verex, and Wallet all log request or transaction data; treat any logging library feature that can execute code or fetch a remote resource on a logged string as an attack surface, the way Log4Shell forced onto Log4j.
- **Auditor: add "what does this dependency's logging do with attacker input" as a standing check.** A dependency's convenience feature is jay's attack surface; this is a cheap line item for the Auditor row to check on every pinned OpenZeppelin or third-party submodule.
- **gitboard: track logging-library CVEs for pinned dependencies.** Since OpenZeppelin contracts are pinned as submodules and other dependencies are lockfile-frozen, gitboard is a natural place to flag a Log4Shell-class CVE the moment a frozen lockfile would otherwise hide it.

## ko
- **CI: 모든 로깅 호출이 신뢰할 수 없는 입력으로 실제로 무엇을 하는지 감사한다.** Rabbit, Verex, Wallet 모두 요청이나 트랜잭션 데이터를 로깅한다. 로깅된 문자열로 코드를 실행하거나 원격 자원을 가져올 수 있는 로깅 라이브러리 기능은, Log4Shell이 Log4j에 강제했던 것과 같은 공격면으로 취급한다.
- **Auditor: "이 의존성의 로깅이 공격자 입력으로 무엇을 하는가"를 상시 점검 항목으로 추가한다.** 의존성의 편의 기능이 곧 공격면이라는 것은, 고정된 OpenZeppelin이나 다른 서드파티 서브모듈마다 Auditor 행이 확인할 값싼 항목이다.
- **gitboard: 고정된 의존성의 로깅 라이브러리 CVE를 추적한다.** OpenZeppelin 컨트랙트는 서브모듈로 고정되고 다른 의존성은 락파일로 고정되어 있으므로, gitboard는 고정된 락파일이 오히려 숨길 수 있는 Log4Shell급 CVE를 바로 표시할 자연스러운 자리다.
