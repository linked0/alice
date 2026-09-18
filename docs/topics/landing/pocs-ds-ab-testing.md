## en
- **Rabbit/Verex: fix the test horizon before running any web-app A/B test.** Use a fixed sample size or an explicit sequential design — no stopping early because a metric looks good, since peeking silently inflates the false-positive rate.
- **gitboard: note which design backed each reported experiment win.** Fixed-horizon vs sequential, since a peeked result changes the true false-positive rate behind any number gitboard displays.

## ko
- **Rabbit/Verex: 웹앱 A/B 테스트를 시작하기 전에 테스트 기간을 고정한다.** 고정 표본 크기나 명시적 순차 설계를 쓰고, 지표가 좋아 보인다고 일찍 멈추지 않는다. 피킹은 오탐률을 조용히 부풀리기 때문이다.
- **gitboard: 보고된 실험 승리마다 어떤 설계였는지 기록한다.** 고정 기간인지 순차 설계인지를, gitboard가 보여주는 숫자 뒤의 실제 오탐률이 피킹 여부로 달라지기 때문에 남긴다.
