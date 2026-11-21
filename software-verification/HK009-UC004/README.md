OIP HK009–UC004 Candidate Verification

Organic Intelligence Protocol (OIP)
Research-Stage Software Verification

Overview

This directory contains the candidate software verification package for the OIP HK009 candidate engine and UC004 hashing-policy candidate.

This work records software-level testing, input validation, formula behaviour, hashing checks, and candidate file integrity verification.

Verification Summary

- Total recorded test executions: 108
- PASS: 105
- Historical expectation mismatches: 2
- Expected policy rejections: 1
- Final candidate integrity check: PASS (2/2 files)

The two historical numerical expectation mismatches were independently rechecked against direct arithmetic and passed the recheck. The original mismatch records remain preserved.

Candidate Components

- HK009 candidate engine
- UC004 hashing-policy candidate

Evidence Package

The candidate package includes Python source files, test ledger, structured results, verification report, SHA-256 checksums, README, and changelog.

Limitations and Status

- Candidate engine approval: NOT GRANTED
- Measurement authorization: NOT GRANTED
- Scientific validation: NOT ESTABLISHED
- Production authorization: NOT AUTHORIZED
- Cross-runtime canonical serialization: OPEN

Software verification does not independently establish empirical validity, scientific validity, real-world safety, or production readiness.

OIP remains a research-stage methodology.
