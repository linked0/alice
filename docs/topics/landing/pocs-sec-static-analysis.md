## en
- **CI: run Slither as a required check on every contracts PR across Verex, Token, Wallet and DeFi.** Track its true-positive rate over time so a run of noisy findings gets triaged as "read the finding," not "disable the tool."
- **Auditor: record which static-analysis findings were triaged as false positives, and why.** The methodology (what was checked, by which rule) should include the judgment calls made on top of Slither/Semgrep output, not just the raw tool report.

## ko
- **CI: Verex, Token, Wallet, DeFi 전체의 모든 컨트랙트 PR에 Slither를 필수 체크로 돌린다.** 참양성률을 시간에 따라 추적해서, 잡음 섞인 결과가 나오면 "도구를 끈다"가 아니라 "결과를 읽는다"로 대응하게 한다.
- **Auditor: 어떤 정적 분석 결과를 오탐으로 판단했는지, 왜 그런지 기록한다.** 방법론(무엇을 어떤 규칙으로 확인했는지)에는 Slither·Semgrep 원시 출력뿐 아니라 그 위에서 내린 판단도 포함되어야 한다.
