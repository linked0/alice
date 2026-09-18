## en
- **Wallet: implement simulate → explain → sign → monitor as the actual pipeline, not a slogan.** Wrap every write jayverse-wallet sends through viem's simulateContract, decode the result, and show the plain-language outcome before the signature prompt — since it's an embedded wallet, the app owns the entire consent moment.
- **Wallet: build the error-selector registry now, not after the first undecodable revert.** Combine Jayverse's own ABIs with a 4byte-style directory and an explicit "unknown reason" fallback, so decoded failures don't silently collapse from "insufficient allowance, need 50 more" to "something reverted."
- **gitboard: publish the false-promise rate as a standing metric.** Track the share of transactions that passed simulation but failed on-chain, per contract, as the SLO that measures whether the explain step is honest.

## ko
- **Wallet: simulate → explain → sign → monitor를 구호가 아니라 실제 파이프라인으로 구현한다.** jayverse-wallet이 보내는 모든 쓰기 트랜잭션을 viem의 simulateContract로 감싸고, 결과를 디코딩해 서명 요청 전에 평이한 말로 보여준다. 임베디드 지갑이므로 앱이 동의의 순간 전체를 책임진다.
- **Wallet: 디코딩 불가능한 revert를 처음 만나기 전에 에러 셀렉터 레지스트리를 미리 만든다.** Jayverse 자체 ABI와 4byte 스타일 디렉터리, 그리고 명시적인 "알 수 없는 이유" 폴백을 결합한다. 그래야 디코딩된 실패가 "허용량 50 부족" 같은 구체적 정보에서 "뭔가 revert됨"으로 조용히 퇴화하지 않는다.
- **gitboard: false-promise rate를 상시 지표로 공개한다.** 시뮬레이션은 통과했지만 온체인에서 실패한 트랜잭션의 비율을 컨트랙트별로 추적해, explain 단계가 정직한지 측정하는 SLO로 삼는다.
