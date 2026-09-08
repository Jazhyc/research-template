# What this template takes from Gleipnir

Reviewed [Jazhyc/gleipnir](https://github.com/Jazhyc/gleipnir/tree/ffa47b2d9ebb4e490a61f1993d9e4050329cce2d)
at commit `ffa47b2d9ebb4e490a61f1993d9e4050329cce2d` on 2026-09-08.
The source was inspected; its training stack was not installed or executed.

| Source practice | Template adaptation |
| --- | --- |
| `AGENTS.md` defines scientific and operational expectations | Portable working agreement with explicit reading order and handoff |
| `experiments/<hypothesis>/` separates hypotheses from shared `src/gleipnir/` code | Copyable experiment brief and a neutral `src/research_project/` package |
| `docs/research_program.md`, findings, and decisions retain research context | Research program, short current-state file, and reusable note templates |
| `docs/decisions/config_driven_systems_screens.md` freezes resolved configs and shares runners | Small JSON-based CPU example with frozen config, hashes, status, and fresh output directories |
| Experiment READMEs predeclare baselines and promotion rules | Hypothesis, selection, stop, canary, and interpretation prompts |
| `figures/README.md` gives exact regeneration commands | Figure registry with input identity and finding links |
| Locked Python environment and ignored artifact trees | Python 3.12, uv lock, offline checks, and local artifact guides |
| Explicit compute monitoring and artifact collection | Portable compute record without inherited accounts or targets |

Gleipnir's model families, teacher prompts, metrics, kernels, provider routing,
GPU recipes, Slurm partition, scratch paths, deployment tools, and historical
findings are project-specific. They are not defaults here. Hydra, model-serving
engines, training frameworks, cloud clients, and experiment trackers can be
added when a concrete experiment justifies them.

The new startup checklist and `docs/state.md` make the next session's starting
point explicit. The smoke runner intentionally has no resume or remote-launch
machinery: those contracts depend on the actual workload. It records local
provenance but does not promise reproducibility across arbitrary hardware.
