## en
- **Verex: test stationarity before forecasting any price series.** Run an ADF test and difference the CLOB price or resolution-source history before fitting anything ARIMA-style, since a naive trend forecast on a non-stationary series manufactures false confidence.
- **Number: log the stationarity check as part of a reading's methodology.** Any Number reading built on ARIMA-style forecasting should record its stationarity test and differencing order alongside the reading, tying into the "reading as a licensed, versioned object" rule.
- **DeFi: check staking-APY series for stationarity before modeling them.** The liquid-staking study build should not fit a predictive model on raw APY history without first testing and differencing it.

## ko
- **Verex: 어떤 가격 시계열도 예측 전에 정상성부터 검정한다.** ARIMA류 모델을 적합하기 전에 CLOB 가격이나 정산 소스 히스토리에 ADF 검정과 차분을 적용한다. 비정상 시계열에 대한 단순 추세 예측은 근거 없는 확신을 만들어낼 뿐이다.
- **Number: 정상성 검정을 읽기의 방법론에 기록한다.** ARIMA류 예측에 기반한 Number 읽기는 정상성 검정 결과와 차분 차수를 읽기와 함께 남겨야 한다. 이는 "라이선스되고 버전 관리되는 객체로서의 읽기" 규칙과 이어진다.
- **DeFi: 스테이킹 APY 시계열도 모델링 전에 정상성을 확인한다.** 유동성 스테이킹 스터디 빌드는 원시 APY 히스토리에 검정과 차분 없이 예측 모델을 바로 적합해서는 안 된다.
