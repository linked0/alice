## en
- **Devnet: keep a status column next to every fork date it tracks.** Since Devnet forks Sepolia, log whether an upstream fork date is confirmed by named client teams, deferred, or just circulating, so a devnet sync never gets scheduled off an invented mainnet date.
- **Bridge: verify dependency claims at the EIP text, not the summary.** Before assuming an L1 change the relayer depends on requires two EIPs together, check whether that dependency is stated in the EIPs themselves or just inferred by whoever summarized them.
- **gitboard: link the primary source behind any "next target" note.** When gitboard records "Devnet next syncs to fork X," attach the client-team minutes it was confirmed in, so a stale assumption is traceable later instead of silently repeated.

## ko
- **Devnet: 추적하는 모든 포크 날짜 옆에 상태 칸을 둔다.** Devnet은 Sepolia를 포크하므로, 상류 포크 날짜가 이름 있는 클라이언트 팀들이 확정한 것인지, 보류된 것인지, 그냥 떠도는 것인지 기록한다. devnet 동기화가 날조된 메인넷 날짜에 맞춰 잡히지 않도록 한다.
- **Bridge: 의존성 주장은 EIP 원문에서 확인하고 요약에서 확인하지 않는다.** 릴레이어가 의존하는 L1 변화가 두 EIP를 함께 필요로 한다고 가정하기 전에, 그 의존성이 EIP 본문에 명시되어 있는지 아니면 요약한 사람의 추론인지 확인한다.
- **gitboard: "다음 목표" 메모 옆에 1차 출처를 링크한다.** gitboard에 "Devnet 다음 동기화는 포크 X"라고 적을 때는 그것이 확정된 클라이언트 팀 회의록을 함께 붙인다. 낡은 가정이 말없이 반복되지 않고 나중에 추적 가능하도록 한다.
