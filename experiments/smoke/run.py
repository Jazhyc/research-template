"""Verify local run plumbing with a constant predictor on synthetic labels."""

import argparse
import json
import math
import random
import time
from pathlib import Path

from research_project.runs import create_run, sha256_file, timestamp, write_json

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def validate_config(config: dict) -> None:
    expected = {"experiment", "seed", "samples", "positive_probability"}
    if not isinstance(config, dict) or set(config) != expected:
        raise ValueError(f"config must contain exactly {sorted(expected)}")
    if config["experiment"] != "smoke":
        raise ValueError("this runner only implements the smoke experiment")
    if type(config["seed"]) is not int:
        raise ValueError("seed must be an integer")
    if type(config["samples"]) is not int or config["samples"] <= 0:
        raise ValueError("samples must be a positive integer")
    probability = config["positive_probability"]
    if (
        type(probability) not in (int, float)
        or not math.isfinite(probability)
        or not 0 <= probability <= 1
    ):
        raise ValueError("positive_probability must be finite and between 0 and 1")


def run(config_path: Path, output_root: Path) -> Path:
    config = json.loads(config_path.read_text(encoding="utf-8"))
    validate_config(config)
    output = create_run(output_root, config["experiment"], config, PROJECT_ROOT)
    start = time.monotonic()
    try:
        # Execute from the frozen record, not a mutable authoring file.
        frozen = json.loads((output / "resolved_config.json").read_text())
        rng = random.Random(frozen["seed"])
        probability = frozen["positive_probability"]
        labels = [int(rng.random() < probability) for _ in range(frozen["samples"])]
        write_json(output / "synthetic_labels.json", labels)
        prediction = 0.5
        write_json(
            output / "metrics.json",
            {
                "samples": len(labels),
                "positive_rate": sum(labels) / len(labels),
                "brier_score": sum((prediction - y) ** 2 for y in labels) / len(labels),
                "interpretation": "Synthetic plumbing check; not research evidence.",
            },
        )
        manifest_path = output / "manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["input"] = {
            "kind": "synthetic_bernoulli",
            "sha256": sha256_file(output / "synthetic_labels.json"),
        }
        manifest["runner_sha256"] = sha256_file(Path(__file__))
        write_json(manifest_path, manifest)
    except BaseException as error:
        # Record the type only; arbitrary exception messages can contain inputs.
        write_json(
            output / "status.json",
            {
                "state": "failed",
                "error_type": type(error).__name__,
                "updated_at": timestamp(),
                "elapsed_seconds": time.monotonic() - start,
            },
        )
        raise
    write_json(
        output / "status.json",
        {
            "state": "completed",
            "updated_at": timestamp(),
            "elapsed_seconds": time.monotonic() - start,
        },
    )
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, default=PROJECT_ROOT / "results")
    args = parser.parse_args()
    print(run(args.config, args.output_root))


if __name__ == "__main__":
    main()
