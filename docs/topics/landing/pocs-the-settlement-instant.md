## en
- **Verex: replace the single-price snapshot with a sized TWAP window.** For any market resolving on price-at-an-instant, make window length and validation band explicit parameters in the resolution field (e.g. 30s/60s), and size them by pricing cost-to-manipulate against reference-venue depth first, the way Polymarket's fix does.
- **Verex/Auditor: pick push or pull per market type.** A market resolving on a price at a specific instant needs a pull-style signed report, not latest on-chain state; a market resolving on a categorical outcome needs decentralized consensus instead, and the resolution field should say which.
- **Auditor: record the halt-to-finalization gap as its own field.** Treat the interval between oracle finalization and trading halt as a named part of the audited methodology, not an implementation detail — if a position can open after the settling price is fixed, that window is the defect.

## ko
- **Verex: 단일 가격 스냅샷을 사이즈가 정해진 TWAP 윈도우로 바꾼다.** 특정 순간의 가격으로 정산하는 마켓이라면 윈도우 길이와 검증 밴드를 정산 필드에 명시적 파라미터로 넣고(예: 30초/60초), Polymarket이 한 것처럼 레퍼런스 거래소의 유동성 대비 조작 비용을 먼저 계산해 그 값을 정한다.
- **Verex/Auditor: 마켓 종류별로 푸시와 풀을 구분해 정한다.** 특정 순간의 가격으로 정산하는 마켓은 최신 온체인 상태가 아니라 풀 방식의 서명된 리포트가 필요하고, 카테고리형 결과로 정산하는 마켓은 탈중앙 합의가 필요하다. 정산 필드에 어느 쪽인지 명시한다.
- **Auditor: 정지-확정 간극을 별도 필드로 기록한다.** 오라클 확정과 거래 정지 사이의 간격을 구현 디테일이 아니라 감사 방법론의 명시된 항목으로 다룬다 — 정산 가격이 이미 정해진 뒤에도 포지션을 열 수 있다면 그 윈도우 자체가 결함이다.
