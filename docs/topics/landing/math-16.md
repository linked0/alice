## en
- **Verex: write the oracle-dispute payoff matrix before setting bond sizes.** Model challenger/reporter payoffs explicitly and solve for the equilibrium, instead of assuming the non-zero-sum bond-and-reward game behaves like the (roughly zero-sum) trading side.
- **OFA: check whether solver competition is actually zero-sum.** If solvers can coordinate on the price they bid in the intent auction, the mechanism has quietly become non-zero-sum, and collusion-resistance has to be designed for, not assumed away.
- **Auditor: log that an equilibrium exists separately from whether it's desirable.** Any mechanism write-up (slashing, dispute bonds) should say which equilibrium was found and note if it's a prisoner's-dilemma-shaped one, worse than the cooperative outcome.

## ko
- **Verex: 본드 크기를 정하기 전에 오라클 분쟁의 페이오프 행렬을 써본다.** 챌린저와 리포터의 페이오프를 명시적으로 모델링하고 균형을 풀어본다. 논제로섬인 본드-보상 게임이 (거의 제로섬인) 거래 쪽처럼 행동한다고 가정하지 않는다.
- **OFA: 솔버 경쟁이 정말 제로섬인지 확인한다.** 인텐트 경매에서 솔버들이 입찰가를 조율할 수 있다면 메커니즘은 조용히 논제로섬이 된 것이고, 담합 저항성은 가정이 아니라 설계 대상이어야 한다.
- **Auditor: 균형의 존재와 그것이 바람직한지는 따로 기록한다.** 슬래싱, 분쟁 본드 같은 메커니즘 문서는 어떤 균형이 나왔는지 적고, 협력적 결과보다 나쁜 죄수의 딜레마형 균형인지도 명시한다.
