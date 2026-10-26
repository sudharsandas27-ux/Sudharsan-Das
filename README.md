Organic Intelligence Protocol (OIP)

Evidence-First. Fail-Closed. Source-Locked.

The Organic Intelligence Protocol (OIP) is a research methodology for evidence-based construct measurement, dataset qualification, analytical authorization, and evidence-bounded decision systems.

OIP is designed to maintain a clear boundary between what available evidence establishes and what an analytical system is permitted to claim.

Governing sequence: Evidence → Measurement → Score → Evaluation → Claim

Governing principle: No evidence, no operationalization.

When required evidence is missing, contradictory, unresolved, or not independently established, OIP preserves that uncertainty rather than filling the gap with unsupported assumptions, proxies, synthetic outcomes, silent imputation, post-hoc tuning, or unverified AI-generated interpretations.

Current research position: Research-stage methodology. The presence of specifications, audits, and software tests does not independently establish scientific validity, causal validity, real-world safety, or production readiness.

---

Claim Discipline and Evidence Classification

OIP distinguishes four categories of evidence and claims.

1. VERIFIED FINDINGS: Findings supported by inspectable primary-source documents, specifications, or recorded outputs within a defined verification boundary.
2. REPORTED RESULTS: Findings documented in reports or posts when the underlying execution or source artifacts have not been independently reconstructed.
3. UNRESOLVED EVIDENCE: Missing provenance, contradictory values, or qualification gaps that remain unresolved under fail-closed rules.
4. CLAIMS NOT ESTABLISHED: Claims of empirical validity, predictive superiority, causal validity, commercial readiness, real-world safety, or general AI alignment effectiveness that have not been established by the available evidence.

A passing software test demonstrates conformity with the expectations encoded for that test. It does not, by itself, establish that those expectations are scientifically valid or that the software is safe in real-world use.

OIP v0.2.0 — Synthetic Reference Implementation and Baseline Verification

Author: Sudharsan Das
Project: Organic Intelligence Protocol
Status: Research-stage synthetic software verification
Scientific or production approval: NOT GRANTED

OIP v0.2.0 is a Python-based synthetic reference implementation demonstrating selected evidence-first, fail-closed authorization rules. It is not a complete implementation of the entire OIP methodology.

Initial Release

The initial v0.2.0 release documentation, dated October 20, 2026, reports 26 recorded tests passed with zero reported failures. The documented "decide(case)" function returns four explicit states:

- "APPROVED"
- "PENDING_EVIDENCE"
- "BLOCKED"
- "INVALID_INPUT"

These results describe the scope reported in the initial release documentation.

Subsequent Baseline Verification

The saved baseline-verification outputs report the following test-record structure.

Section| Planned records
Core| 14
Edge| 8
Input Validation| 5
Output Contract| 5
Immutability| 3
Configuration| 4
Precedence| 3
Exhaustive Matrix| 72
Total planned test records| 114
Supplemental Core_Reason records| 14
Total exported rows| 128

The 14 supplemental Core_Reason records are additional records, not additional unique planned tests. Therefore, 128 exported rows must not be described as 128 unique planned tests.

The recorded outputs report PASS for the listed test sections. This is a statement about the specified synthetic cases and their encoded expectations, not a claim of universal correctness.

Outstanding reconciliation: The initial release documentation reports 26 recorded tests, while the subsequent baseline-verification output reports 114 planned test records and 14 supplemental reason records. The relationship between these two scopes remains unresolved unless the underlying primary artifacts establish it. They must not be silently combined into a single test count.

Published Baseline Artifacts

The repository contains the following baseline-verification artifacts:

- "oip-v0-2-0-baseline-verification.ipynb"
- "OIP_v0.2.0_AUDIT_REPORT.json"
- "OIP_v0.2.0_AUDIT_RESULTS.csv"
- "OIP_v0.2.0_Audit_Report.pdf"

The JSON and CSV SHA-256 values recorded in the baseline audit report are:

- JSON: "a1f387bcf9a855ea9a9cc233f9697661274d871d45ce85d0347e7f564c6b17bd"
- CSV: "b4637bda0989e66fe3bf20428340f29a7f0a4269ad31a063ca7a1f2b8c576b84"

The PDF records these reference values. A matching SHA-256 hash supports byte-level identity checking against the relevant reference value. A hash does not independently establish scientific correctness, security, or validity of the implementation.

Public Records

Original v0.2.0 Kaggle notebook:

https://www.kaggle.com/code/sudharsandas27/oip-authorization-protocol-v0-2-0

Baseline verification Kaggle notebook:

https://www.kaggle.com/code/sudharsandas27/oip-v0-2-0-baseline-verification

GitHub repository:

https://github.com/sudharsandas27-ux/Sudharsan-Das

Zenodo record reported for v0.2.0:

https://doi.org/10.5281/zenodo.23494314

The availability and contents of each public record should be checked at its destination.

Verification Boundary

The v0.2.0 baseline verification is a synthetic software-testing exercise. It does not establish:

- Empirical validity of the OIP methodology
- Predictive or causal validity
- Real-world medical, financial, infrastructure, or other safety
- Independent security certification
- Production readiness
- General AI alignment effectiveness
- Compliance of every historical OIP version with the current implementation

The defensible conclusion is limited to the recorded outcomes for the specified test cases. Broader claims require separate evidence and independent validation.

---

Research Lineage: v1.0.26–v1.0.39

This section summarizes the reported research lineage and its principal evidence boundaries. Each version must be interpreted according to its own primary artifacts. A summary does not replace the underlying audit report, notebook, specification, or source data.

v1.0.39 — Waymo Safety Claim Audit

The reported audit identified 601 repeated analytical grains corresponding to 1,202 rows with conflicting benchmark values at the same analytical grain.

The supplied source corpus did not establish an authorized rule for resolving those conflicting benchmark values.

- C08: "FAIL_CLOSED"
- C09 downstream evaluation: "NOT_AUTHORIZED"
- Road-safety verdict: "NOT_ISSUED"

The audit did not authorize benchmark selection, deduplication, aggregation, or a road-safety conclusion.

v1.0.38 — Tanzania KHDS

The reported audit covered 442 source files, including 420 physical DTA files. The reported 339 four-wave pairs were identified as structural overlap candidates, not as an authorized final analytical cohort.

No construct approval should be inferred from identifying candidate pairs.

v1.0.37 — Nigeria GHS Panel Wave 5

The reported audit preserved the dataset identity conflict between Version 01 and Version 2. The conflict was not silently reconciled, and recovered encodings remained subject to their documented verification boundaries.

A candidate version does not independently establish canonical dataset identity.

v1.0.36 — Tanzania NPS Wave 4

The reported audit covered 83 artifacts. Qualification was not established, and the audit remained fail-closed and audit-only.

v1.0.35 — Evidence Reconciliation and Archival Freeze

The reported archival freeze preserved upstream artifacts and unresolved conflicts. A frozen hash supports artifact identity checking but does not independently establish the scientific correctness of the underlying claims.

v1.0.34 — Four-Dataset Evidence Boundary Report

The synthesis documented conditions governing scientific authorization and evidence boundaries across multiple dataset audits.

Scientific authorization requires all applicable conditions to be established. A partial pass or unresolved prerequisite does not authorize downstream scientific claims.

The supplied BEMP notebook was reported as an unexecuted code artifact. Runtime outcome counts should not be presented as independently reconstructed execution results without supporting execution evidence.

v1.0.33 — Ethiopia ESS4

The reported audit covered 75 files, including 68 DTA files and 7 PDF files. Qualification remained blocked where required conditions were not established.

v1.0.32 — Uganda UNPS

The reported evidence audit identified candidate outcomes. Candidate variables or outcomes were not thereby approved as valid constructs or authorized analytical outcomes.

v1.0.31 — Malawi IHPS

The reported audit covered 395 Stata files. The variable "hh_b06_1" was approved for an identifier role in the documented audit, while row-level linkage remained "NOT_ESTABLISHED".

The audit result does not establish empirical validity of the wider OIP methodology.

v1.0.30 — Normative Protocol

The normative protocol established an evidence hierarchy and emphasized that AI-generated suggestions are candidates for investigation, not authoritative evidence.

Core rules include:

- Variable existence does not establish construct validity.
- Fail-closed behavior does not prove scientific validity.
- Missing values must not be silently converted to zero without source-supported justification.
- Dataset identity, operationalization, and authorization must remain evidence-bounded.

v1.0.29 — Canonical Fail-Closed Audit Engine

The audit framework formalized frozen weights, required variables, temporal separation, provenance requirements, and the principle that unresolved prerequisites prevent downstream authorization.

v1.0.28 — Synthetic Simulation Baseline

The reported benchmark results were subsequently reclassified as a synthetic simulation baseline rather than empirical validation. They must not be presented as proof of real-world predictive performance.

v1.0.27 — Mathematical Provenance Addendum

The addendum documented mathematical provenance and boundary conditions. In particular:

"IDS = 0 → LIV = UNDEFINED"

No epsilon floor should be introduced unless explicitly authorized by the governing specification.

v1.0.26 — Foundational Architecture

The foundational specification introduced the OIP architecture, including the HDAI, CGW, and arbitration layers, together with its documented formulas and core methodological concepts.

Historical formulas and definitions must be interpreted according to the relevant version and its controlling source documents. A summary must not silently replace one version's definition with another.

---

Research Position and Limitations

OIP is a research-stage methodology intended to make evidence boundaries, authorization conditions, and unresolved uncertainties explicit.

The work described in this repository includes specifications, dataset qualification audits, evidence reconciliation, synthetic software testing, and research-stage implementation artifacts. These activities have different evidentiary scopes and must not be treated as interchangeable.

- A source audit is not automatically a scientific validation.
- A successful software test is not automatically a real-world safety assessment.
- A hash match establishes byte-level consistency with a reference value, not the truth of a claim.
- Candidate variables are not automatically valid constructs.
- Structural overlap is not automatically an authorized cohort.
- An unresolved conflict must remain unresolved until adequate evidence supports a resolution.

The central methodological commitment is straightforward:

When evidence is insufficient, the correct output is not an unsupported guess. The correct output is to preserve uncertainty and stop the unauthorized inference.

Author

Sudharsan Das
Lead Architect, Organic Intelligence Protocol
Tripura, India

License

Refer to the repository's license file for the applicable licensing terms.
---

OIP v1.0.40 — Consolidated Master Technical Reference

Author: Sudharsan Das
Role: Independent Systems Researcher | Architect of the Organic Intelligence Protocol (OIP)
Location: Tripura, India
Release Date: 26 October 2026
Status: Research-stage technical reference

Overview

OIP v1.0.40 consolidates the documented methodology, mathematical notation, evidence hierarchy, dataset audit lineage, software verification records, and claim limitations associated with the Organic Intelligence Protocol (OIP).

The document emphasizes an evidence-first, fail-closed approach to research and analytical authorization.

Core Principles

- Evidence must authorize measurement.
- Measurement must authorize scoring.
- Scoring must precede evaluation.
- Evaluation must precede scientific claims.
- Missing, contradictory, or insufficient evidence must not be silently replaced with assumptions.
- Unresolved findings must remain explicitly unresolved.

Research Materials

The consolidated technical reference is available in the repository as:

"Sudharsan_Das_OIP_v1.0.40_Master.pdf"

Zenodo research record for the OIP v0.2.0 synthetic reference implementation:

https://zenodo.org/records/23635920

Scope and Limitations

OIP remains a research-stage methodology. This document does not establish independent empirical validation, predictive or causal validity, production readiness, commercial validation, or certification as a real-world AI security system.

The v0.2.0 synthetic software reference implementation is distinct from the broader v1.0.x methodology and dataset-audit lineage.

Historical audit results, unresolved source conflicts, and unverified counts must be interpreted according to the qualifications documented in the technical reference.

Evidence and Claim Discipline

This project follows an evidence-first and fail-closed research approach. Claims should remain limited to what the available source artifacts and documented verification procedures support.

Corrections and future developments should be recorded through explicit, versioned updates.

---

Organic Intelligence Protocol (OIP)
Evidence first. Fail closed. Claims bounded by evidence.
