# 01 — Requirements

**Status:** draft | approved
**Last updated:** YYYY-MM-DD

## 1. Problem
What the system does, for whom, and why the obvious approach is insufficient. One paragraph.

## 2. Users and context
Who uses it, how, under what constraints (data availability, latency, cost, hardware).

## 3. Functional requirements
Each requirement is numbered, testable, and has acceptance criteria in Given / When / Then form.

### RF-01 — <short title>
Given <precondition>,
when <action>,
then <observable, measurable outcome>.

### RF-02 — <short title>
...

## 4. Non-functional requirements
| ID | Requirement | Target | How measured |
|----|-------------|--------|--------------|
| NF-01 | Latency p95 per query | < X s | `make evals` logs |
| NF-02 | Cost per 100 queries | < X € | Langfuse usage |
| NF-03 | Reproducibility | fixed seeds, pinned deps | CI green on fresh clone |

## 5. Success metric
- **Primary:** <metric>, target ≥ <value>, measured on `evals/datasets/test.jsonl` (n = <N>).
- **Secondary:** <metric>, <metric>.
- **Baseline to beat:** <the obvious alternative and its number>.

## 6. Out of scope
Explicit list of what this project will NOT do, so scope creep is a spec change, not a drift.

## 7. Open questions
Anything unresolved. Each item must be closed (with an ADR if it is a decision) before the milestone that depends on it starts.
