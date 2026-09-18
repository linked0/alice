## en
- **CI: extend the pin-by-SHA discipline already used for OpenZeppelin submodules to any model or dataset a service loads.** Wherever Jayverse ever pulls a Hugging Face repo, add revision (commit SHA), licence and trust_remote_code fields to whatever manifest CI already checks with frozen lockfiles, instead of trusting a floating branch.
- **Number: record the same five-field lockfile for any model behind a distributed reading.** Repo id, resolved SHA, licence at that revision, whether trust_remote_code is required, and the tokenizer's own repo and SHA — before a reading ships, not after someone asks what produced it.
- **gitboard: add a dependency-drift check, not a one-time pin.** Periodically re-resolve any pinned model/dataset refs and diff them on gitboard, the same way the card's thirty-day re-resolve turns "nothing changed" into a measured fact instead of an assumption.

## ko
- **CI: OpenZeppelin 서브모듈에 쓰는 SHA 고정 원칙을 모델·데이터셋에도 그대로 적용한다.** Jayverse의 어떤 서비스든 Hugging Face 레포를 가져온다면, CI가 이미 프로즌 락파일로 점검하는 매니페스트에 revision(커밋 SHA), 라이선스, trust_remote_code 필드를 추가하고 흐르는 브랜치를 신뢰하지 않는다.
- **Number: 배포되는 읽기 뒤의 모델마다 같은 다섯 필드 락파일을 기록한다.** repo id, 확정된 SHA, 그 리비전의 라이선스, trust_remote_code 필요 여부, 토크나이저 자체의 repo와 SHA를 읽기가 나가기 전에 적어둔다. 누가 무엇이 이걸 만들었냐고 묻고 나서가 아니라.
- **gitboard: 일회성 고정이 아니라 드리프트 체크를 추가한다.** 고정해둔 모델·데이터셋 참조를 주기적으로 재해석해 gitboard에서 diff한다. 이 카드의 30일 재해석이 "아무것도 안 바뀌었다"를 가정이 아니라 측정된 사실로 만드는 것과 같은 방식이다.
