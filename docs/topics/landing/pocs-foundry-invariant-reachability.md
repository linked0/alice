## en
- **DeFi: upgrade jayverse-defi's fuzz test from single-sequence to a full handler campaign.** Build a handler over deposit/wrap/unwrap/requestWithdraw/claim/addRewards/slash across several actors, with ghost sums for the withdrawal queue and the invariant `pool balance == totalPooledETH + pendingWithdrawalETH`.
- **CI: require call/revert distribution reporting on every invariant run, not just pass/fail.** A green campaign where withdraw never once succeeds should fail CI review even if no assertion broke, since the distribution is half the test.
- **Auditor: log reachability metrics as part of what was checked.** When auditing a contract's invariant tests, the methodology write-up should state the call/revert distribution and ghost-variable accounting used, not only that the assertions held.

## ko
- **DeFi: jayverse-defi의 퍼징 테스트를 단일 시퀀스에서 완전한 핸들러 캠페인으로 올린다.** 여러 액터에 걸쳐 deposit/wrap/unwrap/requestWithdraw/claim/addRewards/slash를 아우르는 핸들러를 만들고, 출금 큐용 고스트 합계와 `pool balance == totalPooledETH + pendingWithdrawalETH` 불변량을 둔다.
- **CI: 모든 invariant 실행에 대해 pass/fail뿐 아니라 call/revert 분포 리포트를 요구한다.** withdraw가 단 한 번도 성공하지 못한 녹색 캠페인은 어떤 assertion도 깨지지 않았더라도 CI 리뷰에서 걸러야 한다. 분포가 테스트의 절반이다.
- **Auditor: 도달성 지표를 점검 항목에 명시적으로 기록한다.** 컨트랙트의 invariant 테스트를 감사할 때 방법론 문서에 사용된 call/revert 분포와 고스트 변수 회계를 적어야 한다. assertion이 통과했다는 것만으로는 부족하다.
