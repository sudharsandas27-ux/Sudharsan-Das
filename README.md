# Organic Intelligence Protocol (OIP)

OIP is an evidence-first research framework for examining whether automated decision systems can incorporate demonstrated real-world outcomes, contextual relevance and resilience rather than relying primarily on formal credentials or infrastructure-dependent signals.

## Core Evidence Chain

**Evidence → Measurement → Score → Evaluation → Claim**

> Evidence must authorize measurement. Measurement must authorize score. Score must precede evaluation. Evaluation must precede claim.

Where required evidence is not established, the process remains fail-closed.

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

---

# C15 — Archival Freeze

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

`946b02c745d7e37d16885da31eee8b372699378344c25be95990973d5d80faf2`

C15 is an archival control step. It introduces no new construct, score, outcome, evaluation or empirical claim.

---

# Claim Discipline

This release does not establish:

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

# Public Archival Record

Kaggle:

https://www.kaggle.com/code/sudharsandas27/oip-v1-0-36-tanzania-nps-wave-4-step-3-qualifi

---

# Citation

Sudharsan Das.  
**Organic Intelligence Protocol (OIP) v1.0.36 — Tanzania NPS Wave 4 Qualification Audit.**  
2026.
