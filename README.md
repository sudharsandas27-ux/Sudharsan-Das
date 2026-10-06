# Organic Intelligence Protocol (OIP)

## Evidence-First. Fail-Closed. Source-Locked.

Organic Intelligence Protocol (OIP) is an evidence-first, fail-closed, source-locked research methodology for construct measurement, dataset qualification, analytical authorization, and evidence-bounded decision systems.

OIP is designed to maintain a strict boundary between what a source establishes and what an analytical system is permitted to claim.

The governing scientific sequence is:

Evidence → Measurement → Score → Evaluation → Claim

The governing principle is:

> No evidence, no operationalization.

When required evidence is insufficient, contradictory, unresolved, or not independently established, OIP does not fill the gap with assumptions, proxies, synthetic outcomes, silent imputation, post-hoc tuning, or AI-generated interpretations.

The process stops.

---

# Research Lineage

## v1.0.39 — Waymo Safety Claim Audit

### Scope

OIP v1.0.39 applies the evidence-first, fail-closed methodology to a public Waymo safety-claim dataset.

The audit does not determine that Waymo is safe or unsafe.

It examines whether the supplied benchmark structure and provenance satisfy the evidence requirements necessary for downstream safety evaluation.

### Verified dataset structure

- CSV3: 1,804 rows × 21 columns
- CSV4: 18,352 rows × 7 columns
- 601 analytical grains contained repeated benchmark structures
- 1,202 repeated source rows
- 888 repeated benchmark values were tested
- 314 repeated benchmark values remained untested
- 170 associated with Blincoe
- 144 associated with KA
- 85 distinct S2 cells contained untested rows

### Evidence finding

The audit identified repeated `Benchmark Crash Count` values across analytical grains.

The supplied documentary material established that:

> Benchmark Crash Count = count of crashes in the human benchmark crash data source corresponding to the Outcome.

However, the documentary evidence supplied to the audit did not establish the required rule for resolving the repeated benchmark values across the affected analytical grains.

Documentary occurrence was therefore not treated as semantic equivalence.

### Fail-closed result

C08 = FAIL_CLOSED

C09 Entry = NOT_AUTHORIZED

C09 execution = BLOCKED

Benchmark selection = NOT_AUTHORIZED

Benchmark aggregation = NOT_AUTHORIZED

Benchmark averaging = NOT_AUTHORIZED

Deduplication = NOT_AUTHORIZED

Benchmark replacement = NOT_AUTHORIZED

Semantic equivalence = NOT_AUTHORIZED

Temporal leakage audit = NOT_AUTHORIZED

Scientific authorization = FALSE

Waymo safety verdict = NOT_ISSUED

No safety claim was issued.

The audit therefore establishes an evidence boundary, not a safety verdict.

### Evidence-bounded conclusion

The supplied dataset contains 601 analytical grains with repeated Benchmark Crash Count structures. The supplied documentary corpus does not resolve the required benchmark provenance and semantic mapping for the affected repeated values.

Under the OIP fail-closed protocol, downstream safety evaluation is therefore not authorized.

---

# v1.0.38 — Tanzania KHDS 1991–1994 Panel

### Dataset

Kagera Health and Development Survey (KHDS)

Country: Tanzania

Study period: 1991–1994

Panel structure: Wave 1–Wave 4

### Verified source inventory

- Total source files: 442
- Physical DTA files: 420
- Hashed DTA files: 420
- Hash errors: 0
- Unique DTA hashes: 420
- Duplicate hash groups: 0
- Variable occurrences: 12,029
- Unique variable names: 2,980

### Evidence and authorization state

The audit maintained separate evidence and authorization states.

GFL authorization = FALSE

IDS authorization = FALSE

AML authorization = FALSE

Required documentary and semantic evidence remained unresolved where the source material did not establish sufficient construct meaning.

The audit therefore did not promote candidate variables into authorized operational constructs merely because corresponding variables existed in the dataset.

### Documented unresolved evidence

The audit recorded unresolved documentary evidence requiring further review.

Unresolved evidence count: 13

Status: PENDING_EVIDENCE

Semantic authorization: FALSE

No unsupported operationalization was performed.

No final OIP score was authorized.

No empirical validity claim was issued.

### Important boundary

The current verified source record does not independently establish the previously circulated claims of:

- 339 four-wave household-individual pairs
- 13 candidate outcomes → 0 approved
- "FINAL MASTER AUDIT LOCK / FAIL CLOSED EVIDENCE BOUNDED"

Those statements are therefore not presented as verified facts in this README.

---

# v1.0.37 — Nigeria GHS Panel Wave 5

OIP v1.0.37 continued the evidence-first, fail-closed qualification architecture against the Nigeria General Household Survey Panel Wave 5.

The audit maintained the separation between:

Evidence discovery

Construct authorization

Variable operationalization

Analytical cohort authorization

Outcome authorization

Score computation

Empirical evaluation

Claim authorization

The existence of candidate variables was not treated as proof of construct validity.

The pipeline preserved the fail-closed boundary where required documentary or semantic evidence was insufficient.

Public executable record:

Kaggle — OIP v1.0.37 Nigeria GHS Panel Wave 5 Qualification

https://www.kaggle.com/code/sudharsandas27/oip-v1-0-37-nigeria-ghs-panel-wave-5-qualificati

---

# v1.0.36 — Tanzania NPS Wave 4

OIP v1.0.36 continued the dataset qualification and evidence-gating lineage using the Tanzania NPS Wave 4 panel.

The audit retained the source-locked methodology and separated:

Dataset provenance

Variable identity

Construct evidence

Operationalization

Cohort authorization

Outcome evidence

Analytical authorization

The methodology did not treat computational availability as scientific authorization.

Public executable record:

Kaggle — OIP v1.0.36 Tanzania NPS Wave 4 Qualification

https://www.kaggle.com/code/sudharsandas27/oip-v1-0-36-tanzania-nps-wave-4-step-3-qualifi

---

# v1.0.35 — Evidence Reconciliation and Governance

OIP v1.0.35 extended the evidence reconciliation and governance layer of the research lineage.

The version continued the separation between:

Evidence found

Evidence sufficient

Operationalization authorized

Analytical execution authorized

Claim authorized

Unresolved evidence was retained rather than silently converted into an analytical assumption.

Unverified cryptographic values and historical artifact counts are intentionally not reproduced here until they can be independently checked against their canonical artifacts.

---

# v1.0.34 — Four-Dataset Evidence Boundary Report

OIP v1.0.34 formalized the evidence boundary across multiple longitudinal datasets.

The scientific authorization conjunction was defined as:

Source Definitions Frozen
AND
GFL Approved
AND
IDS Approved
AND
AML Approved
AND
Analytical Cohort Frozen
AND
Score Frozen
AND
Outcome Independent
AND
Outcome Estimable
AND
Leakage Audit Passed
AND
Evaluation Design Frozen

Failure of any required condition prevents downstream scientific authorization.

### BEMP boundary

The supplied BEMP notebook was an unexecuted notebook artifact.

Because the supplied copy contained no recorded execution outputs, exact runtime quantities such as final positive, negative, or unresolved outcome counts could not be independently reconstructed.

The synthesis therefore does not infer those quantities.

### Ethiopia boundary

The Ethiopia source set contained:

- 75 source files
- 68 Stata files
- 7 PDF files
- 2,550 file-variable records
- 1,625 unique variable names

The final GFL, IDS, AML, outcome, and score authorization gates were not established.

Qualification remained fail-closed.

### Core conclusion

File integrity, provenance, schema, metadata, and documentary occurrence do not by themselves establish construct validity or empirical validity.

No evidence → no operationalization.

---

# v1.0.33 — ESS4 Evidence Base

OIP v1.0.33 expanded the documentary and computational evidence-base architecture.

The version continued the separation between:

Source evidence

Construct evidence

Operationalization evidence

Outcome evidence

Evaluation evidence

Claim evidence

Candidate variables were not automatically promoted to approved analytical variables.

---

# v1.0.32 — Evidence-Gated Research Continuation

OIP v1.0.32 continued the transition from methodological specification toward reproducible dataset qualification.

The fail-closed architecture remained central.

Evidence gaps were treated as explicit states rather than hidden assumptions.

---

# v1.0.31 — Malawi IHPS Fail-Closed Empirical Evaluation Audit

OIP v1.0.31 applied the evidence-first methodology to the Malawi Integrated Household Panel Survey.

Dataset:

Malawi IHPS 2010–2019

Verified source files:

395 Stata files

The audit established a reproducible computational audit pipeline and examined documentary and computational evidence gates separately.

The audit did not:

- substitute unsupported proxy constructs
- convert missing values to zero
- apply unsupported imputation
- select variables after observing desired analytical behaviour
- create a synthetic outcome
- treat missing outcomes as negative outcomes
- treat identifier overlap as proof of longitudinal linkage
- create a score merely because the mathematical formula was computable

The audit remained fail-closed when required evidence was insufficient.

### What v1.0.31 did not establish

The audit did not establish:

- predictive validity
- causal validity
- universal validity
- superiority over other methods
- commercial validation
- field effectiveness
- production readiness
- hardware validation
- general AI alignment effectiveness

No empirical validation claim was made.

---

# v1.0.30 — Construct Measurement and Dataset Qualification Protocol

OIP v1.0.30 established the formal evidence hierarchy and claim-discipline framework.

The methodology is:

Evidence-First

Fail-Closed

Source-Locked

Pre-Specified

### Evidence hierarchy

The framework distinguishes evidence concerning:

- source definitions
- dataset codebooks
- questionnaires
- raw data and provenance
- variable identity
- coding
- routing
- missingness
- semantic alignment
- directionality
- operationalization
- analytical cohort
- score definition
- outcome estimability
- independent evaluation
- uncertainty
- evidence-bounded claim

### AI role

AI-generated suggestions are candidate hypotheses only.

AI does not authorize:

- variables
- construct definitions
- field meaning
- transformations
- missingness rules
- outcome definitions
- empirical validity

### Non-negotiable rules

Variable existence ≠ construct validity

Keyword similarity ≠ semantic alignment

Coding ≠ construct validity

Outcome availability ≠ outcome estimability

Score computability ≠ validation

Fail-closed ≠ proof

No silent missing-to-zero

No unsupported proxy

No synthetic outcome

No post-hoc tuning

No universal or causal claim from dataset-specific evidence

### Leakage definition

Leakage is treated as:

Mechanical ∨ Temporal ∨ Semantic

---

# v1.0.29 — BEMP Fail-Closed Audit

OIP v1.0.29 introduced the canonical fail-closed audit engine and pre-registration architecture.

The version formalized:

- frozen weights
- dataset provenance
- schema audit
- missingness preservation
- temporal separation
- leakage audit
- operationalization registry
- manifest locking
- evidence-state transitions
- analytical authorization

The supplied BEMP notebook in the later v1.0.34 synthesis was identified as an unexecuted artifact.

Therefore, exact runtime outcome counts are not asserted in this public lineage.

The methodological rule remains:

No unsupported evidence → no operationalization → no authorized score → no empirical claim.

---

# v1.0.28 — Historical Simulation and Decision-Logic Demonstration

OIP v1.0.28 belongs to the historical development of the methodology.

It is treated in the later OIP lineage as a synthetic simulation and decision-logic demonstration rather than independent empirical validation.

Historical numerical outputs from this stage are therefore not presented as evidence of empirical validity.

---

# v1.0.27 — Mathematical Provenance and Completion Register

OIP v1.0.27 documented mathematical provenance, calibration parameters, boundary conditions, and completion status.

The version recorded the provenance of earlier mathematical formulations rather than establishing new empirical validity.

The documented framework included formulas involving:

Score

SIS

LIV

and the broader OIP architecture.

The IDS boundary condition was retained:

IDS = 0 → LIV = UNDEFINED

No synthetic outcome was authorized to resolve missing empirical evidence.

---

# v1.0.26 — Initial OIP Architecture

OIP v1.0.26 established the initial architecture of the Organic Intelligence Protocol.

The architecture included:

HDAI Layer

CGW Layer

Arbitration Layer

Core conceptual pillars included:

GFL — Grounded Feedback Loop

II — Infrastructure Independence

AML — Adaptive Moral Logic

with:

II = 1 − IDS

The early specification already contained multiple formula presentations, including summary and later review-oriented forms.

v1.0.27 subsequently documented the mathematical provenance and completion state of these formulations.

The initial architecture also introduced the Living Intelligence Node framework and the associated valuation formulation.

---

# Scientific Claim Boundary

OIP does not equate a computational result with a scientific claim.

The following distinctions are mandatory:

Data availability ≠ evidence sufficiency

Evidence occurrence ≠ semantic authorization

Variable existence ≠ construct validity

Construct computability ≠ construct validity

Score computability ≠ empirical validation

Outcome availability ≠ outcome estimability

Dataset qualification ≠ predictive validity

Predictive association ≠ causal validity

Fail-closed execution ≠ proof of the underlying hypothesis

A blocked audit is not a failed scientific hypothesis.

A blocked audit means the available evidence did not satisfy the predefined authorization conditions required for the next analytical stage.

---

# Why Fail-Closed

A conventional analytical workflow may continue by selecting a proxy, imputing missing information, choosing an interpretation, or optimizing a variable after observing the data.

OIP deliberately prevents these actions when they are not pre-authorized by evidence.

The result may be:

APPROVED

PENDING_EVIDENCE

BLOCKED

NOT_ESTABLISHED

NOT_CREATED

NOT_PERFORMED

NOT_AUTHORIZED

NOT_CLAIMED

These states are not failures of the methodology.

They are part of the methodology.

The objective is to make uncertainty visible rather than conceal it behind numerical output.

---

# Reproducibility

OIP research records are designed around:

- source locking
- provenance recording
- file inventory
- schema inspection
- documentary evidence
- semantic evidence
- explicit authorization states
- frozen analytical boundaries
- deterministic audit outputs
- cryptographic manifests where verified
- public executable notebooks where available

Every downstream claim must remain bounded by the evidence actually established by the audit.

---

# Current Research State

The OIP research lineage has progressed from conceptual architecture toward increasingly strict evidence qualification and fail-closed auditing across multiple longitudinal datasets and a public safety-claim dataset.

The current methodology does not claim universal intelligence measurement, predictive superiority, causal validity, commercial validation, production readiness, or general AI alignment effectiveness.

The current research objective is narrower:

To establish a reproducible evidence boundary between source material, construct measurement, analytical authorization, evaluation, and scientific claim.

---

# Governing Principle

> Evidence → Measurement → Score → Evaluation → Claim

And:

> No evidence, no operationalization.

When the evidence chain breaks, the claim chain stops.

---

# Public Research Records

### OIP v1.0.39
Kaggle:
https://www.kaggle.com/code/sudharsandas27/oip-v1-0-39-waymo-safety-claim-audit-fail-close

### OIP v1.0.37
Kaggle:
https://www.kaggle.com/code/sudharsandas27/oip-v1-0-37-nigeria-ghs-panel-wave-5-qualificati

### OIP v1.0.36
Kaggle:
https://www.kaggle.com/code/sudharsandas27/oip-v1-0-36-tanzania-nps-wave-4-step-3-qualifi

Earlier public records and versioned specifications form the historical OIP research lineage.

---

# Author

Sudharsan Das

Lead Architect

Organic Intelligence Protocol (OIP)

Tripura, India

---

# Research Position

OIP is a research-stage methodology.

It is not presented as a proven universal intelligence system.

It is not presented as a commercially validated product.

It is not presented as proof of safety, superiority, causality, or general AI alignment.

Its central contribution is methodological:

Make the evidence boundary explicit.

Do not manufacture certainty.

Do not operationalize what the evidence does not authorize.

Do not convert a computable result into a scientific claim without the required evidence.

> If the evidence is insufficient, the correct output is not a better guess.
>
> The correct output is a controlled stop.
