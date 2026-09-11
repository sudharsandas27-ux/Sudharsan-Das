Organic Intelligence Protocol (OIP)

OIP is a research framework designed to examine whether automated decision systems can incorporate demonstrated real-world outcomes, contextual relevance, and resilience rather than relying primarily on formal credentials, documentation, or infrastructure-dependent signals.

---

OIP v1.0.28 — Blind Evaluation & Rank-Shift Audit

This section is an illustrative concept demonstration of the OIP decision-logic structure using synthetic candidate data.

Demonstration Output

Entity ID| OIP Blind Score (F1)| OIP Adjusted SIS (F2)| Credential Rank| OIP Blind Rank| Rank Shift (ΔR)
Entity_A| 0.385| 0.0783| 1| 3| -2
Entity_B| 0.814| 0.7350| 3| 1| +2
Entity_C| 0.620| 0.5650| 2| 2| 0

- Interactive Google Colab: "Run Rank-Shift Audit PoC" (https://colab.research.google.com/drive/1Ih0SEHQnNGshP97URTa4kFWaaY3zLuxi?usp=sharing)
- Executable script: "decision_poc.py"

«Status: Concept demonstration only. This example illustrates rank-shift behaviour under the specified OIP logic. It does not establish empirical superiority or real-world effectiveness.»

---

OIP v1.0.28 — Synthetic Simulation & Methodology Update

The v1.0.28 evaluation notebook explored the OIP scoring structure using a synthetic HR-style dataset of 54,808 generated records.

Simulation Summary

Metric| Baseline| OIP v1.0.28| Difference
Synthetic records| 54,808| 54,808| Same generated cohort
Top-10% promotion yield| 12.66%| 20.62%| +7.96 percentage points
Reported simulation test| —| —| p = 3.59e-29

Data-Provenance Clarification

A provenance review of the executable notebook showed that the 54,808-row dataset was generated synthetically using "np.random", rather than loaded directly from an external HR benchmark dataset as initially described. The "is_promoted" outcome was also synthetically generated within the simulation.

Therefore, the reported +7.96 percentage-point difference is classified as a synthetic decision-logic simulation, not independent empirical evidence.

«Important: The synthetic outcome was generated from variables that overlap with the variables used in the OIP ranking. This creates a circular or self-reinforcing simulation structure. The resulting lift and statistical significance do not establish causal efficacy, production superiority, or real-world validity.»

---

OIP v1.0.29 — BEMP Fail-Closed Audit

OIP v1.0.29 introduced an evidence-first empirical evaluation pipeline using the Bangladesh Environmental Mobility Panel (BEMP) as an external evaluation target.

The audit enforced:

- Documentary evidence before variable approval.
- Frozen operationalization before scoring.
- No unsupported proxy mappings.
- No random fallback.
- No silent imputation.
- No "NaN → 0" conversion without explicit evidence.
- Missing outcome ≠ negative outcome.
- "IDS = 0" → "LIV" undefined, with no epsilon substitution.
- Fail-closed execution when evidence gates were not satisfied.

The BEMP evaluation did not establish empirical validation because the evidence required for construct operationalization and outcome evaluation was insufficient.

---

OIP v1.0.30 — Normative Evidence & Claim-Discipline Framework

OIP v1.0.30 formalized the evidence hierarchy and fail-closed state transitions governing empirical evaluation.

The core principle is:

«No evidence, no operationalization.»

AI-generated suggestions, keyword matches, variable names, statistical convenience, or apparent correlations are not treated as sufficient evidence for construct approval.

---

OIP v1.0.31 — Malawi IHPS Fail-Closed Empirical Evaluation Audit

OIP v1.0.31 applied the evidence-first, fail-closed methodology to the Malawi Integrated Household Panel Survey (IHPS) 2010–2019.

The final computational pipeline successfully audited 395 Stata files and examined:

- Dataset provenance and structure.
- Documentary evidence.
- Variable identity and coding.
- Missingness.
- Longitudinal identifier evidence.
- GFL, IDS and AML construct candidates.
- Outcome candidates.
- Evidence required for empirical execution.

Relevant evidence signals were identified, but the available evidence was insufficient to operationalize all required OIP constructs according to their documented definitions.

The audit therefore remained fail-closed.

Final Audit Status

FAIL_CLOSED_AUDIT_COMPLETE
EMPIRICAL_VALIDATION_NOT_ESTABLISHED
ANALYTICAL_COHORT_NOT_CREATED
SCORES_NOT_PERFORMED

"hh_b06_1" was approved for longitudinal identifier use based on documentary evidence, but row-level longitudinal linkage was not established.

GFL, IDS and AML remained "PENDING_EVIDENCE".

No unsupported construct mappings, premature scoring, or empirical validation claims were introduced.

Public Kaggle Notebook

Full OIP v1.0.31 audit notebook:

https://www.kaggle.com/code/sudharsandas27/oip-v1-0-31-fail-closed-empirical-audit

«Important: The Kaggle notebook above is the primary public record for the complete v1.0.31 computational audit. The GitHub repository provides the research lineage, code, documentation and reproducibility materials.»

---

Claim Discipline

The OIP evaluation history intentionally distinguishes between:

- Concept demonstration
- Synthetic simulation
- Fail-closed audit
- Empirical validation

Completion of a fail-closed audit does not establish predictive validity, causal validity, universal validity, superiority, commercial validation, field effectiveness, or hardware validation.

The v1.0.31 result therefore should be interpreted as:

«The required evidence gates for empirical execution were not satisfied, so the evaluation pipeline stopped without unsupported operationalization or scoring.»

---

Reproducibility Principle

«Do not trust the claim. Reproduce the experiment.»
