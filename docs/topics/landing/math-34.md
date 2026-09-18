## en
- **Verex: test the LMSR cost function's convexity whenever b or the outcome set changes.** Numerically verify the Hessian stays PSD as a guard, so an accidental non-convex variant never reaches the quote centers.
- **Verex: decide whether the CLOB layer enforces the same convexity guarantee.** No-crossed-quotes-create-arbitrage is a design invariant that follows from convexity, so encode it as a check rather than assuming it holds.
- **Auditor: publish the convexity check as a documented invariant.** "LMSR's cost function is convex, verified by [test]" belongs in the methodology file — arbitrage-freeness is only checkable by users if the check itself is published.

## ko
- **Verex: b나 결과 집합이 바뀔 때마다 LMSR 비용함수의 볼록성을 테스트한다.** 헤시안이 PSD로 유지되는지 수치로 검증하는 가드를 둬서, 우연히 비볼록한 변형이 퀘이트 센터에 도달하지 않게 한다.
- **Verex: CLOB 레이어가 같은 볼록성 보장을 지키는지 결정한다.** 교차 호가가 차익거래를 만들지 않는다는 것은 볼록성에서 나오는 설계 불변식이므로, 그것을 가정하지 말고 체크로 인코딩한다.
- **Auditor: 볼록성 검사를 문서화된 불변식으로 공개한다.** 'LMSR의 비용함수는 볼록하며 [테스트]로 검증됨'을 방법론 파일에 넣는다 — 차익거래 없음은 그 검사 자체가 공개되어야만 사용자가 확인할 수 있다.
