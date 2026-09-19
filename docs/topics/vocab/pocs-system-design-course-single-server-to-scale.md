| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| ACID | Atomicity, Consistency, Isolation, Durability(원자성·일관성·고립성·지속성) · 관계형 DB가 보장하는 트랜잭션 속성, 결제·뱅킹의 필수 조건. "ACID matters: payments, banking, structured e-commerce" |
| RDBMS | Relational Database Management System(관계형 데이터베이스 관리 시스템) · 테이블과 조인 기반 DB, Postgres·MySQL이 대표. "RDBMS (Postgres, MySQL) — tables, joins" |
| NoSQL | Not only SQL(SQL만이 아닌, 비관계형 DB 총칭) · 문서·와이드컬럼·키값·그래프 계열을 묶는 말. "SQL/NoSQL injection defense via parameterized queries or an ORM" |
| SPOF | Single Point of Failure(단일 장애점) · 그 하나가 죽으면 전체가 죽는 컴포넌트, 스케일업의 고질적 리스크. "hits a ceiling and stays a single point of failure" |
| REST | Representational State Transfer(자원을 명사·HTTP 동사로 다루는 API 스타일) · 가장 흔한 공개 API 스타일. "REST names resources as plural nouns" |
| CRUD | Create, Read, Update, Delete(생성·조회·수정·삭제) · 리소스 API의 기본 동작 네 가지. "resource CRUD, cacheable, simple clients" |
| gRPC | gRPC Remote Procedure Call(구글이 만든 RPC 프레임워크) · Protocol Buffers + HTTP/2, 내부 마이크로서비스 표준. "gRPC serializes with Protocol Buffers over HTTP/2" |
| TCP | Transmission Control Protocol(전송 제어 프로토콜) · 순서 보장·재전송이 있는 연결형 전송, 결제·인증에 필수. "TCP's handshake, ordering guarantee and retransmission" |
| UDP | User Datagram Protocol(사용자 데이터그램 프로토콜) · 핸드셰이크·재전송 없는 비연결형, 지연이 유실보다 나쁠 때. "UDP skips both and is used where a late packet is worse than a lost one" |
| AMQP | Advanced Message Queuing Protocol(고급 메시지 큐잉 프로토콜) · 비동기 큐·브로커 표준. "AMQP is for asynchronous queues and brokers" |
| JWT | JSON Web Token(JSON 웹 토큰) · 서명된 클레임, DB 조회 없이 서명만 검증하는 무상태 인증. "JWTs are signed claims: the server verifies a signature instead of querying a database" |
| OAuth 2.0 / OIDC / SSO | Open Authorization / OpenID Connect / Single Sign-On(위임 인가 프레임워크 / 그 위의 신원 계층 / 통합 로그인) · 비밀번호 없이 제한된 토큰을 제3자에 위임하는 한 가족. "OAuth 2.0 itself is not authentication: it is an authorization framework for delegating a limited, revocable token" |
| RBAC / ABAC / ACL | Role-Based / Attribute-Based Access Control, Access Control List(역할 기반·속성 기반 접근 제어, 접근 제어 목록) · 인가(무엇을 할 수 있는가)의 세 표준 모델. "RBAC (roles map to permission sets), ABAC (rules over attributes), and ACL (per-resource, per-user, the Google Drive model)" |
| CORS | Cross-Origin Resource Sharing(교차 출처 리소스 공유) · 어느 출처가 API를 호출할 수 있는지 제한. "rate limiting per endpoint, per user/IP, and globally; CORS" |
| WAF | Web Application Firewall(웹 애플리케이션 방화벽) · 엣지에서 악성 요청을 거르는 계층. "a WAF; a VPN or private network" |
| VPN | Virtual Private Network(가상 사설망) · 관리자 대시보드·백엔드 전용 API를 사설망 안에만 두는 방식. "a VPN or private network for admin dashboards and backend-only APIs" |
| CSRF | Cross-Site Request Forgery(사이트 간 요청 위조) · 로그인된 사용자를 속여 원치 않는 요청을 보내게 하는 공격, 토큰으로 방어. "CSRF tokens; and XSS defense via input sanitization" |
| XSS | Cross-Site Scripting(사이트 간 스크립팅) · 악성 스크립트를 삽입하는 공격, 입력 sanitize와 HTTP-only 쿠키로 방어. "a longer-lived refresh token kept in an HTTP-only cookie to block XSS theft" |
| hash ring (consistent hashing) | 해시 링(노드와 키를 원형 해시 공간에 배치하는 구조) · 노드 증감 시 재매핑을 최소화하는 이유. "it maps both nodes and keys onto a hash ring so that adding or removing a node only remaps the keys next to it" |
| over-fetching / under-fetching | 과다 조회 / 과소 조회(필요보다 많이 또는 적게 데이터를 받는 문제) · GraphQL이 REST 대신 등장한 이유. "over- or under-fetching" |
