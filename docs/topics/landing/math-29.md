## en
- **Verex: calibrate the market maker's liquidity parameter with a learning rate bounded by 1/L, not by trial and error.** Confirm the chosen cost function (LMSR or otherwise) is actually convex before blaming the optimizer for a failure to converge.
- **DeFi: when liquid-staking or rebalancing parameter calibration zig-zags, diagnose conditioning before redesigning.** Add momentum or preconditioning first, and only conclude the objective is non-convex after checking that.
- **Auditor: log which failure mode a calibration hit — divergence, slow convergence, or zig-zag.** Each points to a different fix (learning rate too high, too low, or poor conditioning), and the write-up should name which one, not just "it didn't converge."

## ko
- **Verex: 마켓 메이커의 유동성 파라미터는 시행착오가 아니라 1/L로 바운드된 학습률로 캘리브레이션한다.** 옵티마이저가 수렴하지 못한다고 탓하기 전에 선택한 비용 함수(LMSR이든 다른 것이든)가 실제로 볼록한지 먼저 확인한다.
- **DeFi: 유동성 스테이킹이나 리밸런싱 파라미터 캘리브레이션이 지그재그를 그리면 재설계 전에 컨디셔닝부터 진단한다.** 모멘텀이나 프리컨디셔닝을 먼저 넣어보고, 그래도 안 될 때만 목적함수가 비볼록이라고 결론짓는다.
- **Auditor: 캘리브레이션이 어떤 실패 모드를 겪었는지(발산, 느린 수렴, 지그재그) 기록한다.** 각각 다른 수정(학습률이 너무 크다, 너무 작다, 컨디셔닝이 나쁘다)을 가리키므로, 그냥 "수렴 안 함"이 아니라 어느 것인지 문서에 명시한다.
