| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| survive contact with production | 실전(프로덕션)에 부딪혀도 무너지지 않다 · 검증 결과가 실제 배포 후에도 유효한지 말할 때. "fail... at the split, not at the model" |
| announce itself | 스스로 티가 나다, 알아서 드러나다 · 문제(leak)가 눈에 띄지 않게 숨어있음을 말할 때. "It does not announce itself" |
| bake into | (계산·결과에) 녹아들다, 반영되어 굳어지다 · 테스트셋 정보가 학습 특성에 섞여 들어간 상황. "baked into the training features" |
| account for | ~을 설명하다, ~만큼을 차지하다 · 남은 차이 중 일부의 원인을 짚을 때. "that alone accounts for" |
| reach into | (시간·범위상) ~까지 걸쳐 들어가다 · 학습 라벨이 검증 구간까지 침범하는 상황. "reaches into the validation window" |
| purge | (겹치는 데이터를 검증 전에) 걸러내다 · 교차검증에서 겹치는 학습 샘플을 제거하는 절차. "purged cross-validation with an embargo" |
| embargo | (일정 기간) 사용을 유예·차단하는 구간 · 검증 이후 학습 재개 전 두는 간격. "embargo a gap" |
| chance-level | 우연 수준, 무작위와 다를 바 없는 · 처음 보는 대상에 대한 낮은 성능을 말할 때. "chance-level on new ones" |
| invite the question | (당연히) ~라는 의문을 불러일으키다 · 정직한 숫자 하나가 오히려 의심을 살 때. "invites the question" |
| the moment it goes live | 실제로 가동되는 바로 그 순간 · 배포 직후 성능이 무너지는 시점을 가리킬 때. "degrades the moment it goes live" |
| leak | (검증에 섞이면 안 될 정보가 새어 들어오는) 데이터 누수 · 예측 시점에 없어야 할 정보가 학습에 섞이는 문제를 가리킴. "A leak is any path by which information" |
| imputer | 결측치를 채워 넣는 전처리 도구(imputer) · 통계량을 분할 전에 학습해 버리면 안 되는 예시로 언급. "the imputer's median" |
| target encoder | 범주형 변수를 타깃 평균으로 인코딩하는 기법(target encoder) · 분할 전에 학습하면 누수가 되는 전처리 예시. "a target encoder's per-category averages" |
| calibration | 예측 확률이 실제 빈도와 얼마나 일치하는지 보는 지표(calibration) · 누수된 분할 위에서는 이 지표도 믿을 수 없다는 맥락. "looks well-calibrated on data it has effectively already seen" |
| label horizon | 라벨이 내다보는 미래 시점 범위(label horizon) · 검증 구간과 겹치면 누수가 발생하는 지점. "whose label horizon reaches into the validation window" |
<!-- acronyms 2026-09-18 -->
