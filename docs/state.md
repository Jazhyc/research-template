# Current state

Stage: template scaffold; no research project or paid runs configured.

## Starting point

- Read `start_here.md` and replace the research-program prompts.
- A CPU smoke experiment demonstrates config snapshots and run provenance.
- No dataset, model, cloud account, or compute allocation has been selected.

## Active runs

None. When launching, record job ID, target, code/config identity, log/output
paths, monitoring mechanism and cadence, and recovery command here.

## Next actions

1. Define the research question and smallest credible baseline.
2. Establish data provenance, evaluation, and resource constraints.
3. Implement and verify the first project-specific experiment.

## Handoff format

Replace this guidance with the last verified state: date, relevant commits,
completed work, exact checks and outcomes, retained evidence, blockers, and next
commands. Keep this file short; link findings and decisions for the details.

## Scaffold verification (2026-09-08)

`bash setup_dev.sh`, `make check` (lint, formatting, 10 tests), and `make smoke`
passed with Python 3.12.11. The smoke metric was the expected Brier score of
0.25; local documentation links and shell syntax were checked. This session
used `UV_CACHE_DIR=/tmp/research-template-uv-cache` because the default cache
was read-only. The workspace's `.git` was an empty read-only directory, so no
commit or remote publication was possible here. Recheck these facts in the new
checkout and replace this template-specific handoff with project progress.
