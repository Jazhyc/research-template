# Hypothesis name

Status: proposed. Owner/date: TODO.

## Question

Falsifiable hypothesis and the decision this experiment will inform.

## Design

- Intervention and matched baseline:
- Controlled factors and intentional differences:
- Data sources, revisions, transformations, and input checksums:
- Unit of analysis, split/group lineage, and leakage checks:
- Primary metric/direction, uncertainty, and subgroup guardrails:
- Development selection rule and untouched final evaluation:
- Seeds/replicates, resource estimate, and authorized budget:
- Promotion and stop conditions:

## Execution

Add a versioned config and executable entrypoint, reusing shared runners where
possible. Record exact commands from the repository root for preparation,
bounded canary, full run, status inspection, recovery, and summarization.
Specify expected outputs and failure criteria. Validate actual model/API
behavior before scaling; mock external calls in automated tests.

## Results

Run IDs, immutable configs, artifact locations, and link to a finding. Include
negative outcomes. Record deviations from the planned design before interpreting
results. Unexecuted commands and planned runs must remain labeled as such.
