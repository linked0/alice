## en
- **Verex/contracts: add a CI grep check for `unchecked` blocks that requires an explicit comment justifying safety.** Solidity 0.8's default checks don't cover intentional unchecked math, and that's exactly where this PoC's wrap lives.
- **Devnet: add the overflow-wrap PoC (unchecked vs SafeMath vs native 0.8 checks) as a regression test in the contracts test suite,** so the fix is demonstrated in CI rather than assumed from the compiler version alone.

## ko
- **Verex/contracts: `unchecked` 블록에 대해 안전성을 정당화하는 명시적 주석을 요구하는 CI grep 체크를 추가한다.** Solidity 0.8의 기본 체크는 의도적인 unchecked 연산을 커버하지 않으며, 이 PoC의 wrap이 바로 거기서 일어난다.
- **Devnet: overflow-wrap PoC(unchecked 대 SafeMath 대 네이티브 0.8 체크)를 컨트랙트 테스트 스위트의 회귀 테스트로 추가한다.** 컴파일러 버전만으로 가정하지 않고 CI에서 고침이 실증되게 한다.
