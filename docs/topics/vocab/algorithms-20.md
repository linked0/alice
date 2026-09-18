| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| scale as | (증가율이) ~형태로 커지다 · 작업량이 곱셈이 아니라 덧셈으로 늘어나는 구조적 이점을 말할 때. "scales as (languages + targets)" |
| merge (control flow) | 합류하다, 흐름이 하나로 합쳐지다 · 여러 실행 경로가 한 지점에서 만날 때. "at points where control flow merges" |
| explicit | 명시적인, 드러나 있는 · 굳이 따로 분석하지 않아도 표현 자체에 정보가 드러날 때. "def-use relationships are explicit in the representation itself" |
| derive from | ~에서 도출되다, 유도되다 · 어떤 개념이 다른 개념을 바탕으로 계산되어 나올 때. "derived from the dominance relation" |
| lower (into) | (더 낮은 단계로) 변환하다 · 상위 표현을 하위 명령어 형태로 바꿔 내릴 때. "an out-of-SSA pass lowers phi nodes into copy instructions" |
| fold away | 접혀서 사라지다, 소거되다 · 최적화 과정에서 불필요한 코드가 없어질 때. "what folds away and what survives at the IR level" |
| optimizer settings | 최적화 설정 · 컴파일러가 코드를 얼마나·어떻게 최적화할지 정하는 옵션. "a change in compiler optimization settings" |
| IR | 중간표현(Intermediate Representation) · 소스 언어와 타깃 머신 사이에 두어 최적화·코드생성 로직이 (언어+타깃) 규모로만 커지게 하는 계층. "An IR (intermediate representation) sits between the source language" |
| SSA | 정적 단일 대입 형식(Static Single Assignment) · 모든 변수가 딱 한 번만 대입되는 IR 형태, 최적화를 단순하게 만드는 핵심 전제. "SSA (static single assignment) is an IR form" |
| LLVM | LLVM · 여러 언어·타깃이 공유하는 대표적인 컴파일러 인프라 프로젝트, SSA 기반 최적화를 쓰는 대표 사례로 언급. "Modern optimization in LLVM, the Go compiler, most JITs" |
| GOSSAFUNC | GOSSAFUNC · Go 컴파일러가 특정 함수의 SSA 변환 과정을 단계별로 덤프해 보여주는 환경변수/도구. "Go's GOSSAFUNC output" |
| phi function | 파이 함수(phi function) · 여러 실행 경로가 합류하는 지점에서 어느 분기에서 왔는지에 따라 값을 선택하는 SSA 전용 구성 요소. "a phi function picks a value depending" |
| dominance frontier | 지배 프론티어(dominance frontier) · phi 함수를 어디에 배치해야 하는지 계산해주는 그래프 이론 개념, dominance relation에서 유도됨. "computed from the dominance frontier" |
<!-- acronyms 2026-09-18 -->
