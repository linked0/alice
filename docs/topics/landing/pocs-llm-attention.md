## en
- **Auditor/Number: budget context length instead of "just pass more."** Any LLM-based feature (a research assistant, an auditor summarizer) needs an explicit context-length budget and caching strategy documented, since attention cost grows quadratically with context.
- **Number: prefer retrieval/chunking over long-context dumps.** When building research tooling around Number's readings, chunk and retrieve relevant history rather than passing full history into one long-context call, given the O(n^2) cost this page names.

## ko
- **Auditor/Number: "그냥 더 넣기"가 아니라 컨텍스트 길이 예산을 정한다.** 리서치 어시스턴트, Auditor 요약기 같은 LLM 기반 기능은 어텐션 비용이 컨텍스트 길이에 제곱으로 커지므로 명시적인 컨텍스트 길이 예산과 캐싱 전략을 문서화해야 한다.
- **Number: 롱 컨텍스트 통째 전달 대신 검색/청킹을 쓴다.** Number 읽기 자료를 다루는 리서치 툴을 만들 때, 이 페이지가 말하는 O(n²) 비용을 감안해 전체 히스토리를 하나의 롱 컨텍스트 호출에 넣는 대신 관련 부분을 청크로 나눠 검색한다.
