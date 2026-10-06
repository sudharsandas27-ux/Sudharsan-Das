# Organic Intelligence Protocol (OIP)

## Evidence-First | Fail-Closed | Source-Locked | Claim-Disciplined

The Organic Intelligence Protocol (OIP) is an evidence-first research methodology designed to determine whether a decision or intelligence construct can be operationalized without introducing unsupported assumptions into the analytical process.

The governing principle is simple:

> **No evidence, no operationalization.**

OIP separates what is observed from what is inferred.

A variable can exist without establishing construct validity.  
A documented outcome can exist without establishing outcome estimability.  
A computable score is not automatically an empirical validation.  
And when required evidence is insufficient, the protocol stops rather than filling the gap with assumptions.

---

## Core Evidence Chain

OIP follows a source-locked sequence:

**Evidence → Measurement → Score → Evaluation → Claim**

Each stage depends on the evidence established by the previous stage.

If the required evidence is not established, downstream execution is not authorized.

This produces explicit states such as:

- `APPROVED`
- `PENDING_EVIDENCE`
- `BLOCKED`
- `FAIL_CLOSED`
- `NOT_AUTHORIZED`
- `NOT_ESTABLISHED`
- `NOT_PERFORMED`
- `NOT_CLAIMED`

The purpose is to make uncertainty visible rather than hide it behind a numerical result.

---

# Research Lineage

## OIP v1.0.39 — Waymo Safety Claim Audit

### Dataset / Source

Waymo Safety Impact Data Hub published data and associated documentary sources.

The audit examined the benchmark structure used in the published safety analysis, with particular attention to benchmark provenance within the analytical grain:

**State + County + S2 Cell + Outcome**

### Key Structural Finding

The audit identified:

- **601 repeated analytical grains**
- **1,202 repeated rows**
- **888 previously tested rows**
- **314 previously untested rows**
- **170 Blincoe rows**
- **144 KA rows**

All 1,202 target rows contained a `Benchmark Crash Count` value.

The source data structures were also independently inspected:

- CSV3: **1,804 rows × 21 columns**
- CSV4: **18,352 rows × 7 columns**

### Evidence Resolution

The available Release Notes and Data Dictionary established the benchmark and outcome definitions and documented relevant release history.

However, the available documentary evidence did not establish a row-level rule sufficient to determine:

- which repeated benchmark value is authoritative;
- whether one value supersedes another;
- whether the values represent separate benchmark versions;
- whether aggregation is authorized;
- whether averaging is authorized;
- whether deduplication is authorized;
- whether replacement is authorized;
- whether the repeated values are semantically equivalent.

Under the fail-closed protocol, the ambiguity was preserved rather than resolved through an unsupported analytical assumption.

### Final Audit State

```text
C08 FINAL STATUS        = FAIL_CLOSED
C09 ENTRY AUTHORIZED    = False
C09 STATUS              = NOT_AUTHORIZED

Benchmark selection     = NOT_AUTHORIZED
Aggregation             = NOT_AUTHORIZED
Averaging               = NOT_AUTHORIZED
Deduplication           = NOT_AUTHORIZED
Replacement             = NOT_AUTHORIZED
Semantic equivalence    = NOT_AUTHORIZED

Temporal audit          = NOT_AUTHORIZED
Leakage audit           = NOT_AUTHORIZED
Scientific authorization = False

Waymo safety verdict    = NOT_ISSUED
