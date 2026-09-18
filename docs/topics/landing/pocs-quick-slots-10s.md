## en
- **Verex: grep the settlement/CLOB path for every time-valued constant.** Pull poll intervals, confirmation counts, signature deadlines, oracle heartbeats and cache TTLs out of Verex's code and mark each as wall-clock, block-derived, or coincidentally equal — only the block-derived-but-unlabeled ones are the bug.
- **Verex: write every deadline in the unit of what it protects.** A quote or fill deadline is wall-clock (seconds); a dispute or challenge window is block-derived (confirmations) — never mix them, since a slot-time or chain change silently tightens whichever one is mistyped.
- **Devnet/Bridge: rerun the same inventory before any chain migration.** Devnet targets Sepolia today and may fork or add a second chain later; the time-constant inventory this page describes is also the list of assumptions that migration would break, so build it once now.

## ko
- **Verex: 정산/CLOB 경로의 모든 시간 상수를 grep한다.** Verex 코드에서 폴링 간격, 컨펌 수, 서명 마감, 오라클 하트비트, 캐시 TTL을 뽑아 각각 벽시계 기준인지 블록 기반인지 우연히 같은 값인지 표시한다. 라벨 없는 블록 기반 값만이 버그다.
- **Verex: 모든 마감을 그것이 보호하는 것의 단위로 적는다.** 호가·체결 마감은 벽시계(초) 기준이고, 분쟁·챌린지 윈도우는 블록 기반(컨펌 수)이다. 이 둘을 섞지 않는다. 슬롯 타임이나 체인이 바뀌면 잘못 타이핑된 쪽이 조용히 빡빡해진다.
- **Devnet/Bridge: 체인 마이그레이션 전에 같은 인벤토리를 다시 돈다.** devnet은 지금 Sepolia를 대상으로 하고 나중에 포크되거나 두 번째 체인이 추가될 수 있다. 이 글이 말하는 시간 상수 인벤토리는 그 마이그레이션이 깨뜨릴 가정 목록이기도 하니 지금 한 번 만들어 둔다.
