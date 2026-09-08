"""Minimal local run records. No remote execution or resume semantics."""

import hashlib
import json
import platform
import re
import subprocess
from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4


def timestamp() -> str:
    return datetime.now(UTC).isoformat()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: object) -> None:
    """Publish a JSON document atomically; each run has a single writer."""
    payload = json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n"
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


def git_identity(root: Path) -> dict:
    try:
        revision = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        status = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return {"revision": None, "dirty": None}
    return {"revision": revision, "dirty": bool(status)}


def create_run(
    output_root: Path, experiment: str, config: dict, project_root: Path
) -> Path:
    """Create a unique run and record its configuration and local provenance."""
    if not re.fullmatch(r"[a-z][a-z0-9_]*", experiment):
        raise ValueError("experiment must be a lowercase identifier")
    # Validate serialization before creating the output directory.
    json.dumps(config, allow_nan=False)
    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%S") + "-" + uuid4().hex[:12]
    output = output_root / experiment / run_id
    output.mkdir(parents=True, exist_ok=False)
    write_json(output / "resolved_config.json", config)
    lock = project_root / "uv.lock"
    write_json(
        output / "manifest.json",
        {
            "schema_version": 1,
            "experiment": experiment,
            "run_id": run_id,
            "created_at": timestamp(),
            "git": git_identity(project_root),
            "python": platform.python_version(),
            "platform": platform.platform(),
            "config_sha256": sha256_file(output / "resolved_config.json"),
            "lock_sha256": sha256_file(lock) if lock.exists() else None,
        },
    )
    write_json(
        output / "status.json",
        {
            "state": "running",
            "updated_at": timestamp(),
        },
    )
    return output
