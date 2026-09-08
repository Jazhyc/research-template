import json
from pathlib import Path

import pytest

from experiments.smoke.run import run, validate_config
from research_project.runs import create_run, sha256_file

CONFIG = {"experiment": "smoke", "seed": 0, "samples": 20, "positive_probability": 0.5}


def test_run_is_repeatable_and_preserves_previous_artifacts(tmp_path):
    config_path = tmp_path / "config.json"
    config_path.write_text(json.dumps(CONFIG))
    first = run(config_path, tmp_path / "results")
    original = {p.name: p.read_bytes() for p in first.iterdir()}
    second = run(config_path, tmp_path / "results")
    assert first != second
    assert original == {p.name: p.read_bytes() for p in first.iterdir()}
    assert (first / "synthetic_labels.json").read_bytes() == (
        second / "synthetic_labels.json"
    ).read_bytes()
    manifest = json.loads((first / "manifest.json").read_text())
    assert manifest["config_sha256"] == sha256_file(first / "resolved_config.json")
    assert manifest["input"]["sha256"] == sha256_file(first / "synthetic_labels.json")
    assert json.loads((first / "status.json").read_text())["state"] == "completed"
    assert json.loads((first / "metrics.json").read_text())["brier_score"] == 0.25


@pytest.mark.parametrize(
    "change",
    [
        {"samples": 0},
        {"samples": True},
        {"seed": 1.2},
        {"positive_probability": float("nan")},
        {"positive_probability": 1.1},
        {"experiment": "../escape"},
        {"unknown_option": 1},
    ],
)
def test_invalid_config_is_rejected(change):
    with pytest.raises(ValueError):
        validate_config(CONFIG | change)


def test_run_directory_cannot_escape_output_root(tmp_path):
    with pytest.raises(ValueError):
        create_run(tmp_path / "results", "../escape", {}, tmp_path)
    assert not (tmp_path / "results").exists()


def test_failure_is_visible_and_does_not_claim_completion(tmp_path, monkeypatch):
    import experiments.smoke.run as runner

    config_path = tmp_path / "config.json"
    config_path.write_text(json.dumps(CONFIG))

    def fail(_path: Path):
        raise RuntimeError("synthetic execution failure")

    monkeypatch.setattr(runner, "sha256_file", fail)
    with pytest.raises(RuntimeError):
        run(config_path, tmp_path / "results")
    (status_path,) = (tmp_path / "results" / "smoke").glob("*/status.json")
    status = json.loads(status_path.read_text())
    assert status["state"] == "failed"
    assert status["error_type"] == "RuntimeError"
