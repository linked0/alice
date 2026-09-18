## en
- **Auditor: treat any Jayverse agent that reads a user-supplied image (portal screenshots, support flows) as a prompt-injection surface.** Extend the same allowlist/scoping discipline applied to text tool calls to image inputs.
- **Number: if Number ever parses scanned documents or chart images for readings, run the injection PoC first.** Verify a malicious image can't smuggle instructions into the extracted data before trusting the pipeline.

## ko
- **Auditor: 사용자가 제공한 이미지(포털 스크린샷, 지원 플로우)를 읽는 모든 Jayverse 에이전트를 프롬프트 인젝션 표면으로 취급한다.** 텍스트 도구 호출에 적용하는 것과 같은 허용목록/범위 제한 원칙을 이미지 입력에도 확장한다.
- **Number: Number가 스캔 문서나 차트 이미지를 파싱해 읽기를 만든다면 인젝션 PoC를 먼저 돌린다.** 파이프라인을 신뢰하기 전에 악의적 이미지가 추출 데이터에 지시문을 몰래 넣을 수 없는지 검증한다.
