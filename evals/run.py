"""Evaluation harness skeleton.

Every project defines: a dataset in evals/datasets/, a
`score(example, prediction) -> dict` function, and writes a results JSON with
per-example scores + aggregate metrics + git SHA + model name.
The README's "Results" section is generated from these files, never written by hand.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import UTC, datetime
from pathlib import Path

RESULTS = Path(__file__).parent / "results"


def load_dataset(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def predict(example: dict) -> str:
    raise NotImplementedError("Wire the project's system here")


def score(example: dict, prediction: str) -> dict[str, float]:
    raise NotImplementedError("Define task-specific metrics here")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default="evals/datasets/dev.jsonl")
    parser.add_argument("--ci", action="store_true", help="Fail if metrics drop below thresholds")
    args = parser.parse_args()

    examples = load_dataset(Path(args.dataset))
    rows = []
    for ex in examples:
        pred = predict(ex)
        rows.append({"id": ex.get("id"), "prediction": pred, **score(ex, pred)})

    metric_keys = [k for k in rows[0] if k not in ("id", "prediction")] if rows else []
    aggregate = {k: sum(r[k] for r in rows) / len(rows) for k in metric_keys}
    sha = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True
    ).stdout.strip()
    out = {
        "timestamp": datetime.now(UTC).isoformat(),
        "git_sha": sha,
        "n": len(rows),
        "aggregate": aggregate,
        "rows": rows,
    }
    RESULTS.mkdir(exist_ok=True)
    path = RESULTS / f"{datetime.now(UTC):%Y%m%d-%H%M%S}-{sha}.json"
    path.write_text(json.dumps(out, indent=2))
    print(json.dumps(aggregate, indent=2))


if __name__ == "__main__":
    main()
