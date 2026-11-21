# OIP Final Candidate Verification Report

## Scope

This package records research-stage verification of:
- HK009 candidate engine
- UC004 hashing-policy candidate

## Execution ledger

Total recorded executions: 108
PASS: 105
FAIL: 2
Expected policy rejections: 1

Reconciliation:
108 = 105 + 2 + 1

Historical harness errors are retained separately and are not counted
as candidate-engine failures.

Historical expectation mismatches remain recorded.
Tiny-value Score/SIS mismatches were independently rechecked against
direct arithmetic and passed the recheck.

## Verification coverage

- HK009 targeted tests and formula boundary/precedence tests
- Score and SIS weight verification
- Missing/invalid input precedence
- IDS boundary checks
- LIV IDS=0 undefined behaviour
- Stability boundary behaviour
- UC004 approved input policy
- Nested data structures
- Large-input hashing
- Independent hash comparisons
- Depth-100 structure hashing
- Final HK009 smoke regression

## Final integrity check

HK009 SHA-256:
bb2b7e7e73da48faab9e4512a7cded597827d62d5c7a577d1b0879120457b6d8

UC004 SHA-256:
4ca011513d537c059702fedd07602fbdfc833ee3f03db3eada5fa534e5ef0371

Final integrity check: PASS (2/2 files)

## Limitations

- Research-stage candidate verification only.
- No empirical validation.
- No scientific validation.
- No real-world measurement authorization.
- No production release approval.
- No engine lock.
- Cross-runtime canonical serialization remains unresolved.
- Historical source/report reconciliation blockers remain open.


## Supplemental source-level boundary probe (not part of the 108-execution ledger)

During preparation of the accompanying candidate verification report, the two included source files were inspected and an additional probe was run using the native Python integer `10**400`.

Observed results:
- HK009 `validate_numeric(10**400)` returned `INVALID_INPUT`; `calculate_score(10**400, 1, 1)` also returned `INVALID_INPUT`.
- UC004 `validate_hash_input(10**400)` raised `OverflowError` (`int too large to convert to float`). The `hash_same_runtime` call raises the same error because validation occurs before the serialization exception handler.

The approved numeric-input policy accepts native Python integers and floats and does not specify a maximum integer magnitude. Python integers are arbitrary-precision and finite. On that reading, this behaviour is an implementation gap. If a magnitude limit is intended, it requires an explicit owner-approved specification.

This supplemental probe is not included in the 108 recorded executions and does not change the ledger totals. Neither candidate source file was modified. Keep this issue open for a separately versioned candidate revision and targeted re-testing.
