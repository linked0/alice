## en
- **gitboard: audit every dashboard query for string-concatenated input.** Any query built from user or service input must use parameterized queries, never string-joined data.
- **Number: apply the same parameterized-query rule to its data access layer.** Even though Number is admin-only, add it as a standing test for research and reading lookups.
- **Auditor: generalize "never build a command by string-joining untrusted data" beyond SQL.** Apply it to any off-chain service constructing shell commands, RPC calls or queries from external input.

## ko
- **gitboard: 문자열 연결로 만든 쿼리를 모든 대시보드에서 감사한다.** 사용자나 서비스 입력으로 만들어지는 모든 쿼리는 문자열 결합이 아니라 파라미터화된 쿼리를 써야 한다.
- **Number: 데이터 접근 계층에도 같은 파라미터화 쿼리 규칙을 적용한다.** Number가 관리자 전용이더라도, 연구·읽기 조회에 상시 테스트로 추가한다.
- **Auditor: "신뢰할 수 없는 데이터를 문자열로 이어붙여 명령을 만들지 않는다"를 SQL 너머로 일반화한다.** 셸 명령, RPC 호출, 쿼리를 외부 입력으로 구성하는 모든 오프체인 서비스에 적용한다.
