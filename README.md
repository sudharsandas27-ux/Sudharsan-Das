# Organic Intelligence Protocol (OIP)

OIP is a research framework designed to examine whether automated decision systems can incorporate demonstrated real-world outcomes, contextual relevance, and resilience rather than relying primarily on formal credentials, documentation, or infrastructure-dependent signals.

---

## OIP v1.0.28 — Blind Evaluation & Rank-Shift Audit

This section is an illustrative concept demonstration of the OIP decision-logic structure using synthetic candidate data.

### Demonstration Output

Entity ID | OIP Blind Score (F1) | OIP Adjusted SIS (F2) | Credential Rank | OIP Blind Rank | Rank Shift (ΔR)
--- | --- | --- | --- | --- | ---
Entity_A | 0.385 | 0.0783 | 1 | 3 | -2
Entity_B | 0.814 | 0.7350 | 3 | 1 | +2
Entity_C | 0.620 | 0.5650 | 2 | 2 | 0

Interactive Google Colab: "Run Rank-Shift Audit PoC"

Executable script: `decision_poc.py`

Status: Concept demonstration only. This example illustrates rank-shift behaviour under the specified OIP logic. It does not establish empirical superiority or real-world effectiveness.

---

## OIP v1.0.28 — Synthetic Simulation & Methodology Update

The v1.0.28 evaluation notebook explored the OIP scoring structure using a synthetic HR-style dataset of 54,808 generated records.

### Simulation Summary

Metric | Baseline | OIP v1.0.28 | Difference
--- | --- | --- | ---
Synthetic records | 54,808 | 54,808 | Same generated cohort
Top-10% promotion yield | 12.66% | 20.62% | +7.96 percentage points
Reported simulation test | — | — | p = 3.59e-29

### Data Provenance Clarification

A provenance review of the executable notebook showed that the 54,808-row dataset was generated synthetically using `np.random`, rather than loaded directly from an external HR benchmark dataset as initially described.

The `is_promoted` outcome was also synthetically generated within the simulation.

Therefore, the reported +7.96 percentage-point difference is classified as a synthetic decision-logic simulation, not independent empirical evidence.

Important: The synthetic outcome was generated from variables that overlap with the variables used in the OIP ranking. This creates a circular or self-reinforcing simulation structure.

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

## Current Position

OIP v1.0.32 provides a documented evidence-first audit record using real UNPS 2019/20 data.

The current result does not claim that OIP has been empirically validated.

Instead, it records what evidence was available, what evidence remained insufficient, and where the empirical validation process must continue.

The system is designed to stop before scoring when the required evidence is not established.
