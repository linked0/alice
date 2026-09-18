## en
- **Devnet/Rabbit: write the ownership contract before any native-crypto FFI call.** If a service ever calls a native library (secp256k1, BLS, a precompile wrapper) via cgo or a Node native addon, decide who allocates and who frees before wiring it in — the boundary the practical connection already flags for node stability.
- **Wallet: catch panics at any native-signer boundary.** If the simulate-before-sign flow ever talks to a hardware or native signing library through FFI, catch panics at that boundary and convert them to an error code rather than letting them cross into the TypeScript runtime.
- **CI: flag new native-library dependencies in review.** Add a check (even a PR-template note) for any new FFI/native dependency, since these bugs are boundary contract violations that ordinary unit tests won't catch.

## ko
- **Devnet/Rabbit: 네이티브 암호화 FFI 호출 전에 소유권 계약을 적는다.** cgo나 Node 네이티브 애드온으로 secp256k1, BLS, 프리컴파일 래퍼 같은 네이티브 라이브러리를 호출한다면, 연결하기 전에 누가 할당하고 누가 해제하는지 정한다. 이는 Practical Connection이 이미 노드 안정성 문제로 짚은 경계다.
- **Wallet: 네이티브 서명 경계에서 패닉을 잡는다.** simulate-before-sign 흐름이 FFI로 하드웨어나 네이티브 서명 라이브러리와 통신한다면, 그 경계에서 패닉을 잡아 에러 코드로 변환하고 TypeScript 런타임으로 넘어가지 않게 한다.
- **CI: 새 네이티브 라이브러리 의존성을 리뷰에서 표시한다.** 새로운 FFI/네이티브 의존성이 생기면 (PR 템플릿 메모라도) 체크를 추가한다. 이런 버그는 경계 계약 위반이라 일반 단위 테스트로는 잡히지 않는다.
