## en
- **Number: if Number ever adds search or an assistant over research notes, build the eval around retrieval precision, not answer fluency.** This PoC's point is that the bottleneck is upstream of the model, so measure the retrieve step directly.
- **Auditor: wherever a service uses RAG (a Number assistant, a persona chat in Rabbit), track retrieval quality as its own metric, separate from answer quality,** so a wrong-passage failure isn't mistaken for a model failure.

## ko
- **Number: Number에 연구 노트 검색이나 어시스턴트를 추가하게 되면, 답변 유창성이 아니라 검색 정밀도를 중심으로 평가를 만든다.** 이 PoC의 요점은 병목이 모델 이전 단계에 있다는 것이므로 retrieve 단계를 직접 측정한다.
- **Auditor: RAG를 쓰는 어떤 서비스든(Number 어시스턴트, Rabbit의 페르소나 채팅) 검색 품질을 답변 품질과 별개의 지표로 추적한다.** 잘못된 문서를 가져온 실패를 모델 실패로 오인하지 않게 한다.
