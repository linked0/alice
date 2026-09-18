## en
- **Wallet: compute the actual entropy of any seed or passkey material it generates.** Beyond trusting "128-bit" or "12-word" labels, Wallet should verify the real entropy in bits of whatever randomness source it uses, since overestimating entropy is exactly the failure mode this page warns about.
- **Verex: treat LMSR parameter choice as an entropy-maximization problem.** The market maker's cost function is already log-sum-exp; use the maximum-entropy view to justify parameter defaults rather than picking them by trial and error.
- **Devnet: audit whatever randomness source seeds test accounts or session keys.** A devnet's convenience randomness is a common place for weak entropy to hide; measure it in bits before assuming it is fine because it is "only a testnet."

## ko
- **Wallet: 자신이 생성하는 시드나 패스키 자료의 실제 엔트로피를 계산한다.** "128비트"나 "12단어" 라벨을 그냥 믿는 대신, Wallet이 쓰는 무작위성 소스의 실제 비트 엔트로피를 검증한다. 엔트로피를 과대평가하는 것이 이 글이 경고하는 바로 그 실패 양상이기 때문이다.
- **Verex: LMSR 파라미터 선택을 엔트로피 최대화 문제로 다룬다.** 마켓 메이커의 비용 함수는 이미 log-sum-exp 형태이므로, 시행착오 대신 최대 엔트로피 관점을 파라미터 기본값 근거로 쓴다.
- **Devnet: 테스트 계정이나 세션 키를 시드하는 무작위성 소스를 감사한다.** 데브넷의 편의용 무작위성은 약한 엔트로피가 흔히 숨는 곳이다. "테스트넷이니까 괜찮다"고 가정하기 전에 비트 단위로 측정한다.
