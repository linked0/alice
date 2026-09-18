## en
- **Verex: build the ruling table as real schema — (jurisdiction, ruling, date, ground cited, product property implicated) — not a country-code field.** Feed it into an eligibility policy at signup and market-access time, so a new state ruling is a row, not a redesign.
- **Verex: make the eligibility check read that table at runtime instead of hardcoding a country list.** Legal owns the rows, product owns the property column, and every production restriction can name the ruling behind it.
- **Rabbit: point the portal's and Chains menu's access checks at the same eligibility table Verex maintains.** A jurisdiction decision made once should not be re-encoded separately by the wallet/portal layer.

## ko
- **Verex: 국가 코드 필드가 아니라 (관할권, 판결, 날짜, 근거, 영향받는 상품 속성)이라는 실제 스키마로 판결 테이블을 만든다.** 가입과 마켓 접근 시점의 적격성 정책에 이를 입력값으로 써서, 새 주(州) 판결이 재설계가 아니라 행 하나가 되게 한다.
- **Verex: 국가 목록을 하드코딩하는 대신 적격성 체크가 런타임에 이 테이블을 읽게 한다.** 법무팀이 행과 출처를 관리하고, 프로덕트가 속성 열을 관리하며, 운영 중인 모든 제한은 근거가 된 판결을 지목할 수 있다.
- **Rabbit: 포털과 Chains 메뉴의 접근 체크가 Verex가 관리하는 같은 적격성 테이블을 참조하게 한다.** 한 번 내린 관할권 판단을 지갑/포털 계층이 따로 다시 인코딩하지 않는다.
