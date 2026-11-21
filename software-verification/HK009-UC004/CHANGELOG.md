# Changelog

## Candidate verification package

- HK009 candidate included.
- UC004 hashing-policy candidate included.
- Final test ledger reconciled.
- Large-input tests recorded.
- Nested-structure tests recorded.
- Independent hash verification recorded.
- Depth-100 hash verification recorded.
- Final HK009 smoke regression recorded.
- Candidate SHA-256 integrity check passed (2/2).

Original engines remain unchanged.

This package does not authorize production release, engine lock,
measurement, or scientific validation.


## Supplemental source review

- Recorded an unbounded-integer boundary issue using `10**400`.
- HK009 maps the integer to INVALID_INPUT; UC004 propagates OverflowError.
- The probe is outside the 108-execution ledger; ledger totals are unchanged.
- Candidate engine source files were not modified.
- The issue remains open for a separately versioned candidate revision.
