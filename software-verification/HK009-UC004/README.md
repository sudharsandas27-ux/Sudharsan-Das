# OIP HK009 / UC004 Candidate Evidence Package

Research-stage software verification package.

Contents:
1. oip_hk009_candidate_engine.py
2. oip_uc004_hash_candidate.py
3. FINAL_VERIFICATION_REPORT.md
4. TEST_LEDGER.csv
5. TEST_RESULTS.json
6. SHA256SUMS.txt
7. README.md
8. CHANGELOG.md

Scope:
- Candidate software verification only.
- No empirical or scientific validation established.
- No production approval or engine lock.
- No measurement authorization.

UC004 cross-runtime canonical serialization remains OPEN.

Supplemental source-level review: a `10**400` native integer is currently not handled consistently by the candidates. HK009 returns `INVALID_INPUT`; UC004 raises `OverflowError`. This probe is outside the 108-execution ledger and is recorded as an open implementation gap in `FINAL_VERIFICATION_REPORT.md`. Candidate source files remain unchanged.
