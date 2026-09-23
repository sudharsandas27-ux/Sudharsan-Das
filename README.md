# Organic Intelligence Protocol (OIP)

OIP is a research framework designed to examine whether automated decision systems can incorporate demonstrated real-world outcomes, contextual relevance, and resilience rather than relying primarily on formal credentials, documentation, or infrastructure-dependent signals.

---

## OIP v1.0.28 — Blind Evaluation & Rank-Shift Audit

This section is an illustrative concept demonstration of the OIP decision-logic structure using synthetic candidate data.

### Demonstration Output

| Entity ID | OIP Blind Score (F1) | OIP Adjusted SIS (F2) | Credential Rank | OIP Blind Rank | Rank Shift (ΔR) |
|---|---:|---:|---:|---:|---:|
| Entity_A | 0.385 | 0.0783 | 1 | 3 | -2 |
| Entity_B | 0.814 | 0.7350 | 3 | 1 | +2 |
| Entity_C | 0.620 | 0.5650 | 2 | 2 | 0 |

Interactive demonstration: Run Rank-Shift Audit PoC

Executable script: `decision_poc.py`

Status: Concept demonstration only. This example illustrates rank-shift behaviour under the specified OIP logic. It does not establish empirical superiority or real-world effectiveness.

---

## OIP v1.0.28 — Synthetic Simulation & Methodology Update

The v1.0.28 evaluation notebook explored the OIP scoring structure using a synthetic HR-style dataset of 54,808 generated records.

### Simulation Summary

| Metric | Baseline | OIP v1.0.28 | Difference |
|---|---:|---:|---:|
| Synthetic records | 54,808 | 54,808 | Same generated cohort |
| Top-10% promotion yield | 12.66% | 20.62% | +7.96 percentage points |
| Reported simulation test | — | — | p = 3.59e-29 |

### Data Provenance Clarification

A provenance review of the executable notebook showed that the 54,808-row dataset was generated synthetically using `np.random`, rather than loaded directly from an external HR benchmark dataset as initially described.

The `is_promoted` outcome was also synthetically generated within the simulation.

Therefore, the reported +7.96 percentage-point difference is classified as a synthetic decision-logic simulation, not independent empirical evidence.

The synthetic outcome was generated from variables that overlap with the variables used in the OIP ranking. This creates a circular or self-reinforcing simulation structure.

The resulting lift and statistical significance do not establish causal efficacy, production superiority, or real-world validity.

---

## OIP v1.0.29 — BEMP Fail-Closed Audit

OIP v1.0.29 introduced an evidence-first empirical evaluation pipeline using the Bangladesh Environmental Mobility Panel (BEMP) as an external evaluation target.

The audit enforced:

- Documentary evidence before variable approval
- Frozen operationalization before scoring
- No unsupported proxy mappings
- No random fallback
- No silent imputation
- No "NaN → 0" conversion without explicit evidence
- Missing outcome ≠ negative outcome
- "IDS = 0" → "LIV" undefined, with no epsilon substitution
- Fail-closed execution when evidence gates were not satisfied

The BEMP evaluation did not establish empirical validation because the evidence required for construct operationalization and outcome evaluation was insufficient.

---

## OIP v1.0.30 — Normative Evidence & Claim-Discipline Framework

OIP v1.0.30 formalized the evidence hierarchy and fail-closed state transitions governing empirical evaluation.

The core principle is:

> No evidence, no operationalization.

AI-generated suggestions, keyword matches, variable names, statistical convenience, or apparent correlations are not treated as sufficient evidence for construct approval.

---

## OIP v1.0.31 — Malawi IHPS Fail-Closed Empirical Evaluation Audit

OIP v1.0.31 applied the evidence-first, fail-closed methodology to the Malawi Integrated Household Panel Survey 2010–2019.

The final computational pipeline audited 395 Stata files and examined:

- Dataset provenance and structure
- Documentary evidence
- Variable identity and coding
- Missingness
- Longitudinal identifier evidence
- GFL, IDS and AML construct candidates
- Outcome candidates
- Evidence required for empirical execution

Relevant evidence signals were identified, but the available evidence was insufficient to operationalize all required OIP constructs according to their documented definitions.

The audit therefore remained fail-closed.

### Final Audit Status

`FAIL_CLOSED_AUDIT_COMPLETE`

---

## OIP v1.0.32 — UNPS 2019/20 Evidence-First Validation Audit

OIP v1.0.32 applies the evidence-first and fail-closed methodology to the Uganda National Panel Survey 2019/20.

The purpose of this audit was to determine whether the available real data and documentary evidence were sufficient to support the required OIP constructs and an outcome suitable for empirical evaluation before any OIP score was calculated.

The audit covered:

- Data provenance
- Dataset structure
- Schema validation
- Variable metadata and coding
- Missingness
- Household and person identifiers
- Temporal structure
- Linkage evidence
- Construct evidence
- Outcome candidates
- Leakage checks
- Final authorization state

The dataset contained 109 Stata files.

All 109 files were successfully read in the corrected schema audit.

The audit identified 230 candidate outcome variables across four areas:

- Anthropometry
- Consumption
- Employment
- Illness

### Final Evidence State

`GFL = NOT_APPROVED`

`IDS = NOT_APPROVED`

`AML = NOT_APPROVED`

`OUTCOME = NOT_APPROVED`

`SCORE_AUTHORIZATION = NOT_AUTHORIZED`

`EMPIRICAL_VALIDATION = NOT_READY`

`FAIL_CLOSED = TRUE`

The required evidence was not sufficient to approve the OIP constructs and outcome for empirical execution.

No OIP score was calculated.

No empirical validation claim was made.

No synthetic outcome was created to fill the evidence gap.

Unsupported assumptions were not used to force operationalization.

The result is therefore recorded as a fail-closed evidence state rather than as a successful empirical validation.

### Current Status

`EVIDENCE AUDIT COMPLETE`

`EMPIRICAL VALIDATION NOT READY`

The next phase will focus on deeper documentary and real-data cross-checks using the UNPS data.

---

## OIP v1.0.33 — ESS4 Canonical Audit

OIP v1.0.33 applies the evidence-first, fail-closed audit methodology to the Ethiopia Socioeconomic Survey 2018–2019 (ESS4).

The audit examined whether the available dataset structure and documentary evidence were sufficient to support authorized operationalization of the required OIP constructs and an outcome suitable for downstream empirical evaluation.

The audit covered:

- Dataset provenance and source integrity
- Variable metadata and value-label evidence
- Identifier candidate discovery
- Structural uniqueness and co-occurrence checks
- Documentary questionnaire and metadata evidence
- Construct evidence routing
- GFL, IDS and AML evidence states
- Outcome evidence
- Operationalization authorization
- Qualification and release gates
- Final audit manifest verification

The audit preserved the distinction between structural observations, documentary evidence, construct authorization and empirical validation.

Structural uniqueness was not treated as semantic identifier authorization.

Literal documentary search hits were not treated as semantic construct verification.

Candidate evidence was not automatically treated as construct approval.

### Final Qualification State

`PROVENANCE_INTEGRITY = ESTABLISHED`

`TEMPORAL_VALIDITY = NOT_ESTABLISHED`

`CONSTRUCT_MEASUREMENT_EVIDENCE = NOT_ESTABLISHED`

`OUTCOME_INDEPENDENCE = NOT_ESTABLISHED`

`NO_SYNTHETIC_OUTCOME_CONSTRUCTION = NOT_ESTABLISHED`

`LEAKAGE_CONTROL = NOT_ESTABLISHED`

### Final Release State

`FAIL_CLOSED_QUALIFICATION_NOT_ESTABLISHED`

`RELEASE_AS_FAIL_CLOSED_AUDIT_ONLY`

The audit therefore did not proceed to unsupported construct scoring or empirical validation.

Note: The `NO_SYNTHETIC_OUTCOME_CONSTRUCTION` gate remained `NOT_ESTABLISHED` because the upstream construct authorization gate closed before outcome construction was reached. This does not indicate that a synthetic outcome was created.

The result should be interpreted as an evidence boundary for the audited ESS4 data and documentation, not as proof that the OIP constructs are universally unmeasurable across secondary datasets.

### Audit Artifact

Executable audit notebook:

`coip-v1-0-33-ess4-canonical-audit-2.ipynb`

The corresponding public computational audit record is available through the project repository and associated public notebook record.

---

## Evidence-First Principle

Across the OIP evaluation work, the methodology follows a simple rule:

> Evidence must come before operationalization.

A variable is not treated as valid evidence only because its name appears relevant, it has statistical variation, or it appears correlated with another variable.

The required evidence must come from the underlying data, documentation, measurement definitions, temporal structure and observable relationships.

When the required evidence is not established, the system remains fail-closed.

---

## Scope and Claim Discipline

The OIP evaluation work distinguishes between:

- Concept demonstrations
- Synthetic simulations
- Evidence audits
- Empirical validation

Synthetic demonstrations are not treated as real-world evidence.

Evidence identified during an audit is not automatically treated as construct validation.

A successful audit of data structure does not by itself establish OIP effectiveness.

Empirical claims require sufficient documented evidence, valid operationalization, appropriate outcomes and independent evaluation.

---

## Current Research Direction

The OIP research line currently includes four dataset-level audits:

- v1.0.29 — Bangladesh Environmental Mobility Panel (BEMP)
- v1.0.31 — Malawi Integrated Household Panel Survey (IHPS)
- v1.0.32 — Uganda National Panel Survey (UNPS)
- v1.0.33 — Ethiopia Socioeconomic Survey (ESS4)

Across these audits, the required evidence for authorized construct operationalization was not established and the pipelines remained fail-closed.

The next stage, v1.0.34, will document the descriptive pattern across these audits and define the resulting evidence boundary without claiming universal unmeasurability of the documented constructs across secondary datasets.

---

## Current Position

OIP v1.0.33 provides a documented evidence-first audit record using real ESS4 2018–2019 data and associated documentary sources.

The current result does not claim that OIP has been empirically validated.

Instead, it records what evidence was available, what evidence remained insufficient, and where the empirical validation process must continue.

The system is designed to stop before scoring when the required evidence is not established.
