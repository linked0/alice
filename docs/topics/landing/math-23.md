## en
- **Number: publish the PCA-on-price-matrix routine as a licensed reading.** Arrange multiple markets' price series as a matrix, extract the top components, and publish the loadings as a Number indicator under the tokenized-index shape (data, licence, expiry in one token) already used elsewhere on Number.
- **Verex: use variance-explained ratio as a market-health check.** A single component with unexpectedly high loading where markets should be independent is worth flagging for review — correlated or manipulated-looking price movement, not just noise.
- **Auditor: require centering to be logged explicitly.** Forgetting to center the data before SVD is the most common pitfall; any PCA-based check should record that step so an uncentered result isn't mistaken for a real signal.

## ko
- **Number: 가격 행렬 PCA 루틴을 라이선스된 읽기로 공개한다.** 여러 마켓의 가격 시계열을 행렬로 배열하고 상위 성분을 추출한 뒤, Number의 다른 곳에서 이미 쓰는 토큰화 지수 형태(데이터·라이선스·만기를 토큰 하나에)로 로딩값을 Number 지표로 공개한다.
- **Verex: 설명된 분산 비율을 마켓 건전성 체크로 쓴다.** 마켓들이 독립적이어야 할 곳에서 예상외로 높은 로딩을 가진 단일 성분이 나타나면 검토 대상으로 표시할 가치가 있다 — 노이즈가 아니라 상관되거나 조작된 것처럼 보이는 가격 움직임이다.
- **Auditor: 센터링(평균 제거)을 명시적으로 기록하도록 요구한다.** SVD 전에 데이터를 센터링하지 않는 것이 가장 흔한 함정이다. PCA 기반 체크는 이 단계를 기록해서 센터링되지 않은 결과가 진짜 신호로 오인되지 않게 해야 한다.
