X/Twitter thread pasted by jay, 2026-09-23 (Japanese original, pasted in Korean translation).

The question, quoted at the end of the paste:
  佐々木康介∞ @redsasakou · 22시간 (원문 언어 일본어)
  "왜 안 되는 거야? 누가 보안 잘 아는 사람한테 설명해 줬으면 좋겠어. EDR 같은 거 안 깔려 있어서
   방어할 수 없는 거라는 뜻?" — quoting a post by @yoppy_cyber about employees not having local
   administrator rights on their work PCs.

The answer, from a security practitioner whose handle is not in the paste:

--- PASTED CONTENT (verbatim) ---

보안에 조금 아는 편이라서 설명해드릴게요.

직원의 PC에서 "관리자 권한을 빼는 것"이 의미 불명확하게 보이는 건, 사이버 공격 방어만으로
평가하기 때문인데, 실무적인 이유는 주로 두 가지예요.

1. 기업 통제·감사 측면
EDR, MDM, 자산 관리, SASE 클라이언트는 로컬 관리자라면 원칙적으로 중지·삭제할 수 있어요. 주요
제품에는 탬퍼 프로텍션(조작 방지)이 있어서 일반적인 언인스톨은 막을 수 있지만, MDM 등록 해제,
설정 변경, 취약한 정규 드라이버를 들여와 EDR을 무효화하는 기법(BYOVD) 등은 관리자 권한이 있으면
남아요. 그러면 "전체 단말에 에이전트가 들어가 있다""도입 소프트웨어를 파악하고 있다""취약점에
패치가 적용되어 있다"라는 감사에서 증명해야 할 전제를, 에이전트의 생사 감시나 준수 기기 요구 같은
보상 통제로 별도로 보장해야 해요. 불가능한 건 아니지만, 통제 설계와 설명의 부하는 확실히
올라가요. 사용자가 자유롭게 소프트웨어를 설치할 수 있는 환경에서는 라이선스 관리도 같은 이유로
무너져요.

2. 악의적인 직원에 대한 대처
내부 부정의 데이터 유출 자체는 정규 권한 내에서 이뤄지는 경우가 많아서, 이를 막는 건 DLP나 로그
감사 역할이에요. 관리자 권한이 효과를 발휘하는 건 "증적의 완전성"이에요. 관리자 권한이 있으면,
감시 에이전트의 중지, 로컬 로그의 삭제, 단말 측 전송 제한의 해제 같은 "발자국을 지우는" 행위가
가능해져요. 사용자 권한이라면 이런 건 권한 상승을 동반하므로 EDR의 탐지 대상이 될 수 있고,
클라우드 측에 증적이 남아요. "누가 무엇을 했는지"를 나중에 증명할 수 있는 게, 징계나 법적 대응의
전제예요.

3. "요즘 공격은 멀웨어리스라서 무의미하다"는 건가요
인포스티러에 의한 인증 정보나 세션 쿠키의 도난은 사용자 권한으로 성립하고, 훔친 인증 정보로
SaaS에 직접 들어가는 공격은 단말의 관리자 권한과 무관해요. 관리자 권한의 박탈은 초기 침투를 막는
통제가 아니에요. 반면에, 단말에 들어온 후의 횡적 전개·영속화·EDR 무효화에는 관리자 권한이
필요해요. LSASS로부터의 인증 정보 획득도 BYOVD도 관리자가 전제예요. EDR이 뛰어나서 관리자 권한을
넘겨도 된다는 게 아니라, EDR이 뛰어나게 유지하기 위해 관리자 권한을 빼는 게 올바른 순서예요.
참고로 "사용자 권한으로 하는 기업일수록 관리자 비밀번호가 공통"이라는 지적은 맞아요. 그 해결책은
LAPS(로컬 관리자 비밀번호의 자동 랜덤화)이고, 모두에게 관리자 권한을 주는 게 아니에요.

4. 정말 고쳐야 할 부분
원 게시물을 진실로 본다면, 생산성을 해치는 건 권한 박탈이 아니라 "신청해서 정보분석팀이
설치해준다"는 배포 방식이에요. MDM/UEM(Intune, Jamf 등)의 승인된 카탈로그에 의한 셀프 서비스
배포와 필요 시에만의 JIT 승격으로 바꾸면, 통제와 생산성은 양립할 수 있어요. 원 게시물에서 일어나는
건 통제의 옳고 그름 문제가 아니라, 운영 설계의 구식 문제라고 생각해요.

--- END PASTED CONTENT ---

NOTES ON SOURCING (written when the card was built, 2026-09-23)

Reported: the thread above. The responder's handle is not in the paste and I did not identify
them. I did not follow the link to @yoppy_cyber's original post, so the situation being discussed
— employees without local admin, software installed on request by an information-analysis team —
is known only through this thread's description of it.

Checked against general knowledge rather than against the thread: the technical claims here are
standard and correct. Local administrator rights are the boundary that makes agent tampering,
MDM unenrollment, local log deletion and kernel-level EDR neutralisation possible; BYOVD works by
loading a signed but vulnerable legitimate driver to obtain kernel execution, which is why
user-mode tamper protection is not sufficient on its own; credential material in LSASS memory is
readable only with debug privileges that require administrator; infostealers that read
browser-stored tokens and session cookies operate fine at user level; and LAPS is the standard
answer to shared local administrator passwords. The card states the mechanisms in outline, as
reasons a control exists — it contains no operational detail for carrying any of them out.

The card's own arguments, labelled as such in the body:
 1. That the thread's real contribution is a reframing: removing admin is not an access control
    against attackers, it is an INTEGRITY control for the monitoring plane and for the evidence.
    That is why "modern attacks are malware-less" does not refute it — it answers a question the
    control was never making.
 2. That the ordering line is a dependency inversion worth keeping as a general rule: a detector
    that the monitored party can disable is not a detector. Applies well beyond endpoints.
 3. That §4 is the part most organisations get wrong: when a control is unpopular, the complaint
    is usually about the queue in front of it, not the control. Self-service catalogue plus JIT
    elevation removes the queue without removing the boundary.
 4. That the thread's strongest rhetorical move is conceding the opposing point first — insider
    exfiltration does happen within legitimate rights, and admin removal does not stop initial
    access — and then showing the control was aimed elsewhere.

Related items: an-invariant-is-a-stop-not-an-alarm (#67), consumed-authorization,
third-party-blast-radius, harness-engineering-shift-left, sec-heartbleed.
