# CLAUDE.md — conventions for this repository

This repo is one project in a 10-project AI engineering portfolio. Every project follows the same
structure and the same standard: **the technique is here because the problem demands it, and every
claim in the README is backed by a number in `evals/results/`.**

## Project (fill in on day 1)

- **Problem:** CHANGE ME — one paragraph, in plain words, what this system does and for whom.
- **Why this technique and not the obvious alternative:** CHANGE ME.
- **Primary metric:** CHANGE ME (name, direction, current baseline).
- **Non-goals:** CHANGE ME.

## Spec-driven workflow (non-negotiable)

The spec lives in `docs/spec/`: `01-requirements.md` → `02-design.md` → `03-tasks.md`, plus
decision records in `docs/adr/`. Traceability rule: **no code change without a task, no task
without a requirement, no requirement without acceptance criteria.**

1. At session start read `CLAUDE.md`, the three spec files, and open ADRs. Summarise the current
   milestone and its Definition of Done before doing anything.
2. Work only on tasks in `03-tasks.md`, in order. Mark them `[~]` when starting, `[x]` when done.
3. For each task: propose the plan (files, functions, tests) and wait for confirmation. Then
   implement, run `make lint test`, and for eval-affecting tasks `make evals`.
4. If the implementation reveals that the spec is wrong or incomplete: stop, explain, propose the
   spec change and (if it is a decision) an ADR. Do not silently deviate.
5. A milestone is closed only when every item of its Definition of Done is checked, with numbers.
6. Never edit `01-requirements.md` on your own initiative; that is the human's document.

## Working agreement

- Keep `README.md`, `03-tasks.md`, and ADRs current as you work.
- Small, reviewable commits. Conventional Commits (`feat:`, `fix:`, `eval:`, `docs:`).
- Never commit secrets, datasets larger than 5 MB, or model weights. Use `.env`, HF Hub, or DVC.
- Never change the eval dataset or scoring function in the same commit as a model/prompt change.
- Prefer boring, explicit code over clever abstractions. Type hints everywhere. Pydantic at boundaries.

## Layout

```
src/project/      application code (rename the package per project)
  settings.py     all config from env — no hardcoded keys or model names
  llm.py          the ONLY place that calls an LLM; every call is traced in Langfuse
evals/            harness (run.py), datasets (jsonl), results (json, auto-generated)
tests/            unit tests; mark real-API tests with @pytest.mark.llm
notebooks/        didactic material: one notebook per concept, runnable top to bottom
scripts/          one-off data prep / training launchers
docs/spec/        01-requirements, 02-design, 03-tasks — the contract for this project
docs/adr/         decision records: context, decision, alternatives, consequences
```

## Commands

`make setup` · `make lint` · `make test` · `make test-llm` · `make evals` · `make demo`

Run `make lint test` before proposing a commit. CI runs the same.

## Evals are the product

- Every feature or prompt change must be accompanied by `make evals` output and a line in the
  README results table (metric, before, after, git sha).
- Datasets live in `evals/datasets/*.jsonl` with fields `id`, `input`, `expected`, plus task-specific keys.
- Scoring is deterministic where possible. LLM-as-judge only when there is no verifiable answer,
  and then calibrated against at least 30 human-labelled examples.
- Log cost and latency per run alongside quality metrics.

## README contract

Sections, in order: **Problem · Why this technique · Architecture · Results (table, generated) ·
How to run · What I learned / what didn't work · Next steps.** Keep it under two screens.

## When in doubt

Ask. Do not invent data, metrics, or citations. If something cannot be measured yet, say so in
the README rather than leaving the claim out or making it up.
