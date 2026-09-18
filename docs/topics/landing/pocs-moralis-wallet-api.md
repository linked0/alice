## en
- **Wallet: default to a hosted indexing API for portfolio/net-worth display, not a self-built indexer.** Use Moralis or an equivalent for balance and net-worth first, and only build a custom indexer once a concrete gap forces it.
- **Devnet: confirm the chosen indexing API actually supports Anvil devnet (chainId 313370) before depending on it.** If it doesn't, that unsupported-chain gap is exactly the case that justifies building the custom indexer instead.

## ko
- **Wallet: 포트폴리오·순자산 표시는 직접 만든 인덱서가 아니라 호스팅 인덱싱 API를 기본값으로 삼는다.** 잔액과 순자산은 먼저 Moralis나 동급 API로 처리하고, 구체적인 공백이 강제할 때만 커스텀 인덱서를 만든다.
- **Devnet: 선택한 인덱싱 API가 Anvil devnet(체인ID 313370)을 실제로 지원하는지 의존하기 전에 확인한다.** 지원하지 않는다면, 그 미지원 체인이라는 공백이 바로 커스텀 인덱서를 만들어야 하는 근거다.
