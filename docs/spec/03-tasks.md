# 03 — Tasks

**Last updated:** YYYY-MM-DD

Rules: one commit per task (or small group of tasks). A milestone is closed only when its
Definition of Done is fully met. Claude Code works top to bottom and does not start a milestone
whose dependencies are open. Status: `[ ]` todo · `[~]` in progress · `[x]` done · `[-]` dropped (say why).

## H1 — <milestone name>
**Covers:** RF-01, RF-02
**Definition of Done:**
- [ ] Tests for RF-01, RF-02 pass (`make test`)
- [ ] `make evals` reports <metric> ≥ <threshold> on dev.jsonl
- [ ] Results row added to README
- [ ] ADRs for any decision taken during the milestone

**Tasks**
- [ ] H1.1 — <task> (files: `src/project/x.py`, `tests/test_x.py`)
- [ ] H1.2 — <task>
- [ ] H1.3 — <task>

## H2 — <milestone name>
**Covers:** RF-03
**Depends on:** H1
**Definition of Done:**
- [ ] ...

**Tasks**
- [ ] H2.1 — ...

## Backlog (unscheduled)
Ideas that are out of the current spec. Promoting one requires a requirements change.
