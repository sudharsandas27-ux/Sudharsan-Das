# Organic Intelligence Protocol (OIP)

OIP is an evidence-first research framework for examining whether automated decision systems can incorporate demonstrated real-world outcomes, contextual relevance and resilience rather than relying primarily on formal credentials or infrastructure-dependent signals.

## Core Evidence Chain

**Evidence → Measurement → Score → Evaluation → Claim**

> Evidence must authorize measurement. Measurement must authorize score. Score must precede evaluation. Evaluation must precede claim.

Where required evidence is not established, the process remains fail-closed.


---

# OIP v1.0.37 — Nigeria GHS-Panel Wave 5 Qualification Audit

OIP v1.0.37 applies the evidence-first, fail-closed qualification sequence to the Nigeria General Household Survey, Panel 2023–2024, Wave 5.

This release is a dataset qualification audit followed by an archival freeze. It is not an empirical validation.

## Audit Scope

The Nigeria GHS-Panel Wave 5 source package contained:

- 108 Stata data files
- 13 documentation PDFs
- 3,371 unique variable names
- Documentation and structural evidence review
- Missingness and encoding-recovery audit
- Temporal and leakage discovery audit

These quantities describe the audited source environment and diagnostic processing. They do not constitute authorization of constructs, identifiers, outcomes, scores or empirical validity.

## Final Qualification State

- GFL: `NOT AUTHORIZED`
- IDS: `NOT AUTHORIZED`
- AML: `NOT AUTHORIZED`
- Construct authorization: **NONE**
- Identifier authorization: **NONE**
- Outcome authorization: **NONE**
- Analytical cohort: **NOT CREATED**
- Score: **NOT PERFORMED**
- Empirical evaluation: **NOT PERFORMED**

### Final Qualification

`FAIL_CLOSED`

### Release Boundary

`AUDIT_ONLY / FAIL_CLOSED`

The audit preserved unresolved evidence conflicts and did not silently reconcile them.

No unsupported proxy substitution, silent imputation, synthetic outcome, random fallback or post-hoc tuning was used.

## C03 — Dataset Identity Conflict

C03 established a dataset version-identity conflict.

Local documentary evidence identifies:

`NGA_2023_GHSP-W5_v01_M / Version 01`

The mounted dataset directory identifies:

`NGA_2023_GHSP-W5_v02_M_Stata`

The local Basic Information Document is:

`Version 2`

The relationship between these references was not established and was not silently reconciled.

### C03 Final State

`CONFLICT_CONFIRMED`

`BLOCKED_FAIL_CLOSED`

`forensic_gate = PASS`

`silent_reconciliation = False`

## C12 / C12r — Missingness and Encoding Recovery

C12 initially entered a fail-closed state on five encoding-sensitive files.

A controlled retry in C12r recovered all five files using explicit encoding attempts.

### C12r Final State

`PASS_WITH_RECOVERED_FILES`

- Recovered files: 5/5
- Encoding semantic identity: `UNVERIFIED`
- Imputation: `False`
- NaN-to-zero coercion: `False`
- Synthetic values: `False`

The original C12 fail-closed state is preserved as part of the audit history.

## C13 — Temporal and Leakage Discovery

C13 produced temporal and leakage discovery flags for further evidence review.

These findings remained discovery-only.

No temporal anchor, leakage classification, predictor, construct, outcome, cohort or score was authorized from these discovery results.

## C14 — Authorization Boundary

C14 remained:

`FAIL_CLOSED`

The sole unresolved blocker was the dataset version-identity conflict established in C03.

### Authorization Boundary

- Construct authorization: `False`
- Outcome authorization: `False`
- Analytical cohort authorization: `False`
- Score authorization: `False`
- Evaluation authorization: `False`
- Validity claim authorization: `False`

## C15 — Archival Freeze

C15 verified the presence and integrity of the preceding audit artifacts and preserved the final fail-closed authorization state.

### C15 Final State

`ARCHIVAL_FREEZE_PASS_WITH_FAIL_CLOSED_STATE`

## C15 Manifest SHA-256

`651ebac98ed1d500435561ad2b91804273f45c13e4d6d6e2e4b78d219ddff776`

The C15 manifest records the frozen archival state of the Nigeria v1.0.37 qualification audit.

---

# OIP v1.0.36 — Tanzania NPS Wave 4 Qualification Audit

OIP v1.0.36 applies the frozen OIP source-definition and measurement-criteria sequence to the Tanzania National Panel Survey 2014–2015, Wave 4.

This release is a dataset qualification audit followed by an archival freeze. It is not an empirical validation.

## Audit Scope

The Tanzania NPS Wave 4 source package contained:

- 83 source artifacts
- 75 Stata files
- 8 PDFs
- 1,152 documentary pages extracted
- 1,792 unique variable names
- 7 identifier candidates
- 27,214 rows observed during identifier diagnostics

These quantities describe the audited source environment and diagnostic processing. They do not constitute authorization of constructs, identifiers, outcomes, scores or empirical validity.

## Final Qualification State

- GFL: `PENDING_EVIDENCE`
- IDS: `PENDING_EVIDENCE`
- AML: `PENDING_EVIDENCE`
- Construct authorization: **NONE**
- Identifier authorization: **NONE**
- Outcome authorization: **NONE**
- Analytical cohort: **NOT CREATED**
- Score: **NOT PERFORMED**
- Empirical evaluation: **NOT PERFORMED**

### Final Qualification

`FAIL_CLOSED_QUALIFICATION_NOT_ESTABLISHED`

### Release Boundary

`AUDIT_ONLY / FAIL_CLOSED`

No unsupported proxy substitution, silent imputation, synthetic outcome, random fallback or post-hoc tuning was used.

## C15 — Archival Freeze

C15 completed the archival integrity check for C01–C14.

- Expected C01–C14: 14
- Found C01–C14: 14
- Missing cells: 0
- JSON read errors: 0
- Artifacts hashed: 28
- Upstream integrity check: `PASS`
- C15 status: `ARCHIVAL_FREEZE_PASS`

The C14 `UNRESOLVED` label is preserved in the original artifact. C15 records `PENDING_EVIDENCE` for frozen-vocabulary archival comparison.

## C15 Manifest SHA-256

`946b02c745d7e37d16885da31eee8b372699378344c25be95099073d5d80faf2`

C15 is an archival control step. It introduces no new construct, score, outcome, evaluation or empirical claim.

---

# Claim Discipline

These releases do not establish:

- Empirical validity
- Predictive validity
- Causal validity
- Universal validity
- Superiority of OIP
- Universal unmeasurability of the documented constructs

Unresolved evidence remains unresolved.

> No evidence, no operationalization.

---

# Dataset Audit Lineage

**v1.0.29 — BEMP**  
Fail-closed audit. The supplied notebook preserves the audit logic, but its executed final runtime state is not independently reconstructible from the supplied source set.

**v1.0.31 — Malawi IHPS**  
Fail-closed audit with unresolved artifact and identifier evidence conflicts preserved in the archival record.

**v1.0.32 — Uganda UNPS 2019/20**  
109 Stata files audited. Required construct and outcome evidence was not sufficient for downstream authorization.

**v1.0.33 — Ethiopia ESS4**  
75 source artifacts audited. Final state remained `FAIL_CLOSED_QUALIFICATION_NOT_ESTABLISHED`.

**v1.0.34 — Four-Dataset Synthesis**  
Descriptive evidence-boundary synthesis. Not a fifth dataset audit and not an empirical validation.

**v1.0.35 — Evidence Reconciliation & Archival Freeze**  
Reconciliation and archival freeze of the documented evidence boundaries of the preceding dataset-level audit lineage.

**v1.0.36 — Tanzania NPS Wave 4**  
Dataset qualification audit conducted under the frozen source-definition and measurement-criteria sequence, followed by archival freeze.

**v1.0.37 — Nigeria GHS-Panel Wave 5**  
Dataset qualification audit conducted on 108 Stata files and 13 documentation PDFs. Final state remained `FAIL_CLOSED`. Dataset version-identity conflict was preserved rather than silently reconciled. Archival freeze completed.

---

# Historical Framework Record

## v1.0.28

The v1.0.28 lineage contains a historical evaluation record.

The current archival record does not treat v1.0.28 as independent current empirical validation. Its provenance and historical classification relationship remains subject to reconciliation.

## v1.0.27

v1.0.27 documents mathematical provenance and specification-level formulas.

## v1.0.26

v1.0.26 contains the initial framework and multiple formula presentations. The later normative protocol requires explicit version locking rather than silently selecting between conflicting formulations.


---

# Public Archival Records

## OIP v1.0.37 — Nigeria GHS-Panel Wave 5

Kaggle:

https://www.kaggle.com/code/sudharsandas27/oip-v1-0-37-nigeria-ghs-panel-wave-5-qualificati

## OIP v1.0.36 — Tanzania NPS Wave 4

Kaggle:

https://www.kaggle.com/code/sudharsandas27/oip-v1-0-36-tanzania-nps-wave-4-step-3-qualifi

---

# Citation

Sudharsan Das.  
**Organic Intelligence Protocol (OIP) v1.0.37 — Nigeria GHS-Panel Wave 5 Qualification Audit.**  
2026.

Sudharsan Das.  
**Organic Intelligence Protocol (OIP) v1.0.36 — Tanzania NPS Wave 4 Qualification Audit.**  
2026.


---

# Governing Principle

Evidence comes before measurement.  
Measurement comes before scoring.  
Scoring comes before evaluation.  
Evaluation comes before claims.

> No evidence, no operationalization.
