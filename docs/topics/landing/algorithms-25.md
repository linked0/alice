## en
- **Verex: audit the CLOB matching loop for stack-machine overhead.** Check for stack-too-deep errors and excess DUP/SWAP specifically in the hot matching and settlement path, since that's where this tradeoff turns into real gas cost.
- **CI: add a gas-regression check on matching/settlement functions.** Track compiled bytecode gas for those specific functions across commits, not just overall contract size.
- **DeFi: minimize intermediate values in jayverse-defi's own math.** For the from-scratch liquid-staking algorithms, prefer fewer live locals to reduce stack pressure, informed by this stack-vs-register model.

## ko
- **Verex: CLOB 매칭 루프에서 스택 머신 오버헤드를 점검한다.** 이 트레이드오프가 실제 가스 비용으로 나타나는 지점인 매칭·정산 핫 패스에서 특히 stack-too-deep 오류와 과도한 DUP/SWAP을 확인한다.
- **CI: 매칭·정산 함수에 가스 회귀 체크를 추가한다.** 전체 컨트랙트 크기가 아니라 이 특정 함수들의 컴파일된 바이트코드 가스를 커밋마다 추적한다.
- **DeFi: jayverse-defi 자체 수식에서 중간값을 최소화한다.** 처음부터 만든 리퀴드 스테이킹 알고리즘에서, 이 스택 대 레지스터 모델을 참고해 살아있는 로컬 변수 수를 줄여 스택 압력을 낮춘다.
