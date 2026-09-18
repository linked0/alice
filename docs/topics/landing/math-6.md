## en
- **Verex: test that no derived key is truncated below a safe length.** Add a test that checks, for every place conditionId, collectionId or positionId is shortened for indexing, the resulting collision probability against 2^(b/2), not just against 2^b.
- **Devnet indexer: document the bit length and justification for any shortened key.** If the indexer builds short internal keys from these hashes for storage efficiency, keep the chosen length and its collision-resistance reasoning in one place instead of scattered across code.
- **Auditor: confirm truncated hashes shown in UI are cosmetic-only.** Review any place an identifier is shortened for display or logging (Etherscan-style) to confirm it is never reused as an actual lookup key, since that quiet reuse is the failure mode this card warns about.

## ko
- **Verex: 파생된 키가 안전 길이 아래로 잘리지 않는지 테스트한다.** conditionId, collectionId, positionId를 인덱싱용으로 줄이는 모든 곳에서, 2^b가 아니라 2^(b/2) 기준으로 충돌 확률을 확인하는 테스트를 추가한다.
- **Devnet 인덱서: 줄인 키의 비트 길이와 그 근거를 한 곳에 문서화한다.** 인덱서가 저장 효율을 위해 이 해시들로 짧은 내부 키를 만든다면, 선택한 길이와 충돌 저항 근거를 코드 곳곳이 아니라 한 곳에 적어둔다.
- **Auditor: UI에 보이는 잘린 해시가 장식용일 뿐인지 확인한다.** 화면 표시나 로깅용으로(Etherscan 스타일) 식별자를 줄인 곳을 검토해, 그것이 실제 조회 키로 재사용되지 않는지 확인한다. 그런 조용한 재사용이 이 카드가 경고하는 실패 형태다.
