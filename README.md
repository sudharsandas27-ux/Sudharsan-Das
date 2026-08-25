# Organic Intelligence Protocol (OIP)

OIP is a research framework designed to test whether automated decision systems should prioritize real-world outcomes and resilience, rather than relying strictly on credentials and digital records.

---

### OIP v1.0.28 — Blind Evaluation & Rank-Shift Audit (Demonstration)

This concept demonstration showcases how OIP's blind outcome evaluation shifts candidate rankings away from traditional credential bias.

#### Audit Output Summary

| Entity ID | OIP Blind Score (F1) | OIP Adjusted SIS (F2) | Credential Rank (CS Heavy) | OIP Blind Rank | Rank Shift ($\Delta R$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Entity_A** | 0.385 | 0.0783 | **1** | 3 | **-2** |
| **Entity_B** | **0.814** | **0.7350** | 3 | **1** | **+2** |
| **Entity_C** | 0.620 | 0.5650 | 2 | 2 | 0 |

* **Interactive Google Colab Notebook:** [Run Rank-Shift Audit PoC](https://colab.research.google.com/drive/1Ih0SEHQnNGshP97URTa4kFWaaY3zLuxi?usp=sharing)
* **Executable Script:** `decision_poc.py`

> **Status Notice:** This script demonstrates the specification-defined mathematical logic of the OIP framework using a synthetic dataset ($N=3$). Empirical validation ($E1$-$E3$) remains pending.
