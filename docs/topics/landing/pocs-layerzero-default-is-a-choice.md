## en
- **Bridge: write down who you trust, in the README.** If Bridge ever adds a third-party message layer, run the verifier-config query right after first deploy and paste the trust assumption into the repo, so it isn't an invisible default the way an unset DVN config is.
- **Bridge/relayer: name destination-gas underprovisioning as a failure mode.** Write the retry story for "message sent, destination execution failed silently" before the relayer ships — the send looking successful while nothing happened is exactly the trap this piece describes.
- **OFA: copy the four-way module split.** Keep matching, clearing, settlement and risk as separate boundaries in the auction design, with risk kept out of settlement specifically, independent of whether ATLAS itself is ever used.

## ko
- **Bridge: 무엇을 신뢰하는지 README에 적는다.** Bridge가 언젠가 서드파티 메시지 레이어를 쓴다면 첫 배포 직후 검증자 설정 쿼리를 돌려 신뢰 가정을 리포에 남긴다. 설정하지 않은 DVN처럼 보이지 않는 기본값으로 남기지 않는다.
- **Bridge/릴레이어: 목적지 가스 부족을 실패 모드로 명명한다.** "메시지는 보냈는데 목적지 실행이 조용히 실패"하는 케이스에 대한 재시도 전략을 릴레이어 출시 전에 적는다. 전송은 성공한 것처럼 보이는데 아무 일도 일어나지 않는 것이 이 글이 말하는 함정 그대로다.
- **OFA: 네 갈래 모듈 분리를 그대로 가져온다.** ATLAS를 실제로 쓰든 안 쓰든, 매칭·클리어링·정산·리스크를 경매 설계에서 별개의 경계로 유지하고 특히 리스크를 정산과 분리해 둔다.
