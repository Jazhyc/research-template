# Research template

An experiment-centric starting point for research with AI agents, adapted from
[Gleipnir](https://github.com/Jazhyc/gleipnir). Each hypothesis has an executable
experiment; shared code lives in `src/`; findings and decisions outlive sessions
in `docs/`. Start small and add model, dataset, and compute dependencies when the
research question requires them.

## Start a project

Give a future agent this instruction:

> Read AGENTS.md and docs/start_here.md. Adapt this template to the following
> research idea: [idea]. Inspect what is already here, establish the research
> question and evaluation plan, and implement the smallest useful baseline.
> My available data, compute, and budget are: [constraints]. Record assumptions
> and leave reproducible commands and an updated handoff.

The agent's setup checklist is in [docs/start_here.md](docs/start_here.md).
The [adaptation notes](docs/template_design.md) explain which Gleipnir practices
this template preserves and which belong to individual projects.

During initialization, the agent fills in `AGENTS.md` with the research focus,
high-level goal, target deliverable or venue, deadline, and success criteria.
It keeps that brief current as the project evolves. Once setup is complete,
it removes the bootstrap documents and instructions and rewrites this README
for the project; reusable research templates remain available.

## Run the scaffold

Requires Python 3.12 and `uv`. From the repository root:

```bash
bash setup_dev.sh
make check
make smoke
```

The smoke example uses synthetic data, runs on CPU, and makes no network or paid
API calls. Each invocation creates a fresh directory under `results/smoke/` with
a frozen configuration, provenance manifest, metrics, and completion status.
Dependency installation requires package-index access on first setup.

## Layout

```text
AGENTS.md                 Working agreement and agent reading order
docs/start_here.md        New-project initialization checklist
docs/research_program.md  Question, scope, hypotheses, and evaluation plan
docs/state.md             Current state and next actions for the next session
docs/{research,findings,decisions,writeups}/
                          Literature, evidence, choices, and reader-facing prose
experiments/<hypothesis>/ README, config, and experiment-specific code
src/research_project/     Reusable Python code (rename for a new project)
tests/                    Focused, offline correctness checks
scripts/                  Operational and figure-generation entrypoints
cluster/                  Optional compute setup and launcher conventions
figures/                  Curated figures with regeneration commands
data/, results/, logs/    Ignored artifacts; tracked directory guides only
```

`experiments/_template/` is a copyable experiment brief. `experiments/smoke/` is
an executable plumbing example, not a research baseline. No model framework,
cloud provider, experiment tracker, or notebook platform is required.

To publish this directory as a GitHub template, initialize and commit it in a
writable Git checkout, create your remote, push, and enable **Template repository**
in the repository settings. Choose the project's license before publication.
