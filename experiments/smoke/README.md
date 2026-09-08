# Smoke: local run plumbing

Status: infrastructure example. No scientific hypothesis or external data.

Generate seeded synthetic Bernoulli labels and score a constant probability of
0.5. The Brier score must be 0.25 for every label. This checks the environment,
entrypoint, immutable run-directory allocation, config snapshot, and artifacts.
It does not validate a useful research method, splitting policy, or model API.

From the repository root:

```bash
uv run --locked python -m experiments.smoke.run --config experiments/smoke/config.json
```

The command prints a fresh `results/smoke/<run_id>/` directory. Inspect
`status.json` for completion, `metrics.json` for the expected Brier score, and
`manifest.json` for code/environment/config/input identity. The manifest records
`null` Git fields when no checkout is available. A dirty flag is not a source
snapshot; preserve the patch with real research runs.

Each run retains `resolved_config.json` and `synthetic_labels.json`. Repeating
the config generates identical labels in the locked environment, but a new run
ID and timestamps. Use `--output-root /tmp/research-smoke` for disposable checks.
Recovery is a fresh invocation; this example has no resume or scheduler support.
Exceptions during execution produce a failed status; a forcibly killed process
may leave `running`, which must not be interpreted as a live job.
