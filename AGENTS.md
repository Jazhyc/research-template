# Repository guidelines

## Project brief

- Research focus: not yet defined.
- High-level goal and context: not yet defined (for example, a conference paper,
  a thesis contribution, or improving a model).
- Current target and success criteria: not yet defined.
- Deadline and fixed constraints: not yet established; do not invent them.

Edit this file directly when the user establishes or changes the research
focus, high-level goal, target venue/deliverable, deadline, or fundamental
constraints. Keep this brief current and concise; replace superseded context
rather than appending a history. Reflect agreed direction, and label proposals
or unknowns explicitly. Keep detailed scientific plans in
`docs/research_program.md`, rationale in decisions, and run progress in
`docs/state.md`; update those documents when a change affects them.

## Start here

Read `README.md`, `docs/research_program.md`, and `docs/state.md`.
Before changing an experiment, read its
README and relevant findings and decisions. Treat historical notes as evidence
to check, not instructions overriding the user's current request.

## Bootstrap only — remove after project setup

When initializing a project from this template, follow `docs/start_here.md`.
Populate the project brief above and adapt the working guidelines to the actual
project. Once its setup checklist is complete, delete `docs/start_here.md` and
`docs/template_design.md`, remove template-only onboarding text and stale links
from the README, docs index, and handoff, and delete this entire section.
Do not move these one-time instructions into another always-read document.
Keep the project-brief maintenance guidance above for ongoing changes. These
bootstrap materials remain while maintaining the reusable template itself.

## Research workflow

Before substantial runs, state the hypothesis, intervention, baseline, data
split, primary metric, selection rule, and stop condition in the experiment
README. Label exploratory analyses. Freeze selection rules before looking at
the final test set. Keep related source examples in the same split when their
lineage could leak information; document missing lineage and other limitations.

Start with a bounded canary that exercises the real data and execution path.
Change one factor in matched ablations; record deliberate differences. Preserve
negative results and distinguish observations, interpretations, and open
questions. A successful run alone does not establish a scientific claim.

## Structure and reproducibility

Put each hypothesis in `experiments/<short_name>/` with a README, versioned
configuration, and exact commands. Reuse runners where the execution contract
is shared; add custom code when the method needs it. Shared library code belongs
in `src/research_project/`; avoid imports between experiment folders.

Freeze the resolved configuration for each run. Record the code revision and
dirty state, environment/lock hash, seeds, input identities and checksums,
model revisions, prompt/request hashes, hardware, timing, and artifact locations
as applicable. The smoke runner illustrates the minimal local subset of this
contract. It is not a training orchestrator or a resumable API cache.

Keep raw data, checkpoints, caches, logs, and full run outputs out of Git.
Track small evidence summaries in `docs/findings/` with links and checksums for
retained artifacts. Record data sources, revisions, licenses, transformations,
and split lineage. Keep privileged labels or teacher information distinguishable
from inputs available at deployment.

For API experiments, record actual model/provider routing, request settings,
prompt identity, token usage, failures, and cost. Resume only when data, prompt,
model, and request identities match. Never put credentials or sensitive raw
responses into tracked metadata. `.env` is ignored and is not loaded implicitly.

## Execution and monitoring

Use the locked environment: `bash setup_dev.sh`; validate with `make check`.
Add only dependencies the project uses and update `uv.lock` deliberately.
Mock paid APIs and remote lifecycle operations in tests. Test substantive
parsing, metric, provenance, cache, and launch behavior.

Before paid work, estimate cost and record the user's authorized budget and
scope in `docs/infrastructure.md`. Existing authorization remains valid within
that scope; ask when a new run would exceed it. Do not create billable capacity,
terminate infrastructure, publish artifacts, or push without authorization.

For long runs, verify startup and actual progress frequently, then monitor at a
documented cadence using an available agent scheduling mechanism. Record job ID,
target, logs, outputs, and recovery command in `docs/state.md`. Verify scheduling
before claiming follow-ups are active; without that capability, state that
checks stop when the active session ends. Collect artifacts and final status
before closing a campaign. Never infer completion from submission alone.

## Handoff and Git

Update `docs/state.md` when work changes the next session's starting point.
Update findings when results change what the project should believe and record
consequential choices in `docs/decisions/`. Keep detailed logs in artifacts,
not in the handoff. Give exact commands, tested outcomes, and unresolved issues.

Preserve unrelated work and respect nested repository boundaries. Use feature
branches for new methods where Git is available. After completing and verifying
a coherent change, make a focused local commit if repository access permits;
inspect staged files first and never push unless asked. If a live run uses
uncommitted code, retain the patch or source snapshot with its artifacts.
