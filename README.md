# Organic Intelligence Protocol (OIP)

OIP is a research framework designed to test whether automated decision systems can incorporate demonstrated real-world outcomes, contextual relevance, and resilience rather than relying primarily on formal credentials, documentation, or infrastructure-dependent signals.

---

## OIP v1.0.28 — Blind Evaluation & Rank-Shift Audit

This section is an illustrative concept demonstration of the OIP decision-logic structure using synthetic candidate data.

### Demonstration Output

| Entity ID | OIP Blind Score (F1) | OIP Adjusted SIS (F2) | Credential Rank | OIP Blind Rank | Rank Shift (ΔR) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Entity_A** | 0.385 | 0.0783 | **1** | 3 | **-2** |
| **Entity_B** | **0.814** | **0.7350** | 3 | **1** | **+2** |
| **Entity_C** | 0.620 | 0.5650 | 2 | 2 | 0 |

- **Interactive Google Colab:** [Run Rank-Shift Audit PoC](https://colab.research.google.com/drive/1Ih0SEHQnNGshP97URTa4kFWaaY3zLuxi?usp=sharing)
- **Executable script:** `decision_poc.py`

> **Status:** Concept demonstration only. This example illustrates rank-shift behaviour under the specified OIP logic. It does not establish empirical superiority or real-world effectiveness.

---

## OIP v1.0.28 — Synthetic Simulation & Methodology Update

The v1.0.28 evaluation notebook explored the OIP scoring structure using a synthetic HR-style dataset of 54,808 generated records.

### Simulation Summary

| Metric | Baseline | OIP v1.0.28 | Difference |
| :--- | :---: | :---: | :---: |
| **Synthetic records** | 54,808 | 54,808 | Same generated cohort |
| **Top-10% promotion yield** | 12.66% | 20.62% | +7.96 percentage points |
| **Reported simulation test** | — | — | p = 3.59e-29 |

### Data-Provenance Clarification

A provenance review of the executable notebook shows that the 54,808-row dataset was **generated synthetically using `np.random`**, rather than loaded directly from an external HR benchmark dataset as initially described. The `is_promoted` outcome was also synthetically generated within the simulation.

Therefore, the reported +7.96 percentage-point difference is classified as a **synthetic decision-logic simulation**, not independent empirical evidence.

> **Important:** The synthetic outcome was generated from variables that overlap with the variables used in the OIP ranking. This creates a circular/self-reinforcing simulation. The resulting lift and statistical significance therefore do not establish causal efficacy, production superiority, or real-world validity.

---

## OIP v1.0.29 — Independent Empirical Evaluation (Roadmap)

The next validation stage will use a provenance-documented external dataset and a pre-specified evaluation protocol.

### Planned Safeguards for v1.0.29

- Externally sourced and provenance-documented dataset.
- Explicit operational definitions for each OIP variable.
- Temporal separation between decision inputs and outcome measurement (leakage controls).
- Pre-frozen baseline and OIP ranking procedure.
- Independent outcome variable not generated from OIP inputs.
- Reproducible statistical analysis.

The objective is not to prove OIP in advance, but to test whether its predicted effects survive an independent evaluation.

> **Do not trust the claim. Reproduce the experiment.**
