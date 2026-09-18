| Expression | 뜻 · 쓰이는 자리 |
|---|---|
| stall | 멈추다, 정체되다 · 스레드나 프로세스가 진행을 멈춘 상태. "even if some thread stalls" |
| bounded (number of steps) | 상한이 정해진, 유한하게 제한된 · 무한정이 아니라 정해진 한도 안에서 끝남을 보장할 때. "within a bounded number of steps" |
| underneath (it) | (모르는 사이에) 그 아래에서, 밑에서 · 겉으로는 안 변한 것 같지만 실제로는 바뀐 상태를 가리킬 때. "the data structure's actual state has changed underneath it" |
| batch up | 모아서 한꺼번에 처리하다 · 개별적으로 처리하지 않고 묶어서 나중에 처리할 때. "batches up freeing nodes from epochs" |
| surface (in production) | (문제가) 겉으로 드러나다, 표면화되다 · 숨어 있던 버그가 실제 서비스에서 터질 때. "only surface in production" |
| walk straight into (a trap) | 함정에 그대로 걸려들다 · 조심하지 않으면 뻔히 빠지는 문제를 경고할 때. "can walk you straight into this trap" |
| use-after-free | 해제 후 사용 오류 · 이미 반환된 메모리를 계속 참조해서 생기는 버그를 가리키는 표준 용어. "you get use-after-free and data corruption" |
| ABA | ABA 문제 · 값이 A→B→A로 바뀌었다가 되돌아왔을 때 CAS가 "변화 없음"으로 착각해 그 사이의 실제 상태 변화를 놓치는 동시성 버그. "that's where the ABA problem comes from" |
| CAS | 비교 후 교체(Compare-And-Swap) · 락 없이 원자적으로 값을 읽고 비교해 바꾸는 하드웨어 연산, 대부분의 lock-free 알고리즘의 기반. "an atomic read-modify-write like CAS" |
| Treiber stack | 트라이버 스택 · CAS만으로 구현하는 대표적인 lock-free 스택 자료구조, ABA 문제를 실습으로 겪어보는 표준 예제. "Implement a Treiber stack with CAS" |
<!-- acronyms 2026-09-18 -->
