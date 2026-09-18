## en
- **Rabbit: use LoRA for a consistent agent voice, not for current facts.** If Rabbit's agent needs a stable persona or support tone, that's LoRA's job; anything needing current market state or positions stays on RAG or a direct tool call.
- **Personas: keep a persona's voice separate from its factual claims.** Treat any Personas-NFT chat behavior as the style-not-facts case this PoC tests, and source market facts from Verex's live data, never from fine-tuned weights.

## ko
- **Rabbit: 일관된 에이전트 말투에는 LoRA를 쓴다, 현재 사실에는 쓰지 않는다.** Rabbit의 에이전트가 안정적인 페르소나나 지원 톤이 필요하다면 그것은 LoRA의 일이다. 현재 시장 상태나 포지션이 필요한 것은 RAG나 직접 도구 호출에 남긴다.
- **Personas: 페르소나의 말투와 사실 주장을 분리해둔다.** Personas NFT의 챗 동작은 이 PoC가 시험하는 '스타일이지 사실이 아닌' 경우로 다루고, 시장 사실은 파인튜닝된 가중치가 아니라 Verex의 실시간 데이터에서 가져온다.
