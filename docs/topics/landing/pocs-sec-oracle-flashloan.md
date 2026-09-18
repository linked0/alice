## en
- **Verex: never resolve or liquidate off a raw spot AMM read.** Require a TWAP or an external feed with a minimum window for any market or collateral value; treat a spot read as a UI number only, never a settlement input.
- **Auditor: add "can this value move within one transaction via flash loan" as a standing check.** Apply it to every price-dependent function across Verex and DeFi, and record which feed or TWAP defends each one.

## ko
- **Verex: 원시 spot AMM 값으로 정산하거나 청산하지 않는다.** 마켓이나 담보 가치에는 최소 윈도우를 가진 TWAP나 외부 피드를 요구하고, spot 값은 UI 표시용일 뿐 정산 입력으로 쓰지 않는다.
- **Auditor: "이 값이 플래시론으로 한 트랜잭션 안에서 움직일 수 있는가"를 상시 점검 항목으로 추가한다.** Verex와 DeFi 전반의 가격 의존 함수마다 적용하고, 각각을 어떤 피드나 TWAP이 방어하는지 기록한다.
