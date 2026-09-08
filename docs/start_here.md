# Starting a new project

1. Read the user's idea and available repository context. Draft
   `research_program.md`: the question, why it matters, scope, baseline, primary
   metric, split/selection plan, and smallest experiment that could change the
   next decision. Mark unknowns explicitly; ask only for choices that materially
   block progress. An unspecified paid budget permits local work only.
2. Rename the project in `pyproject.toml`, the root `README.md`, and `.env.example`.
   Rename `src/research_project/` and update its references in experiment code,
   tests, and build configuration. Populate the project brief in `AGENTS.md`
   with the research focus, high-level goal, target deliverable or venue,
   success criteria, deadline, and fixed constraints. Mark unknowns explicitly.
   Adapt its working guidelines to the project and retain the instruction to
   update this brief when the direction changes. Choose a license with the
   owner before publishing.
3. Record data access, provenance, and retention in `data/README.md`. Record
   hardware, commands, cost limits, and existing authorization in
   `infrastructure.md`. Add required dependencies with `uv add` and regenerate
   the lock when package metadata changes. Verify `bash setup_dev.sh` and
   `make check`.
4. Run `make smoke` to verify the scaffold. Copy `experiments/_template/` to a
   meaningful hypothesis directory, replace the prompts, add its config and
   entrypoint, and implement a bounded baseline. Keep the smoke example until
   the real baseline covers its plumbing or remove it and update the Makefile.
5. Validate the actual data path and metrics before scaling. Write exact launch,
   status, recovery, and summarization commands in the experiment README. Add
   cluster launchers only when a target has been established. Paid execution
   must stay within the user's recorded authorization.
6. Leave `state.md` with completed work, run/artifact locations, checks performed,
   outstanding choices, and next commands. Update the docs index when adding
   findings or decisions.
7. Finish bootstrap cleanup in the initialized project: delete
   `docs/template_design.md` and this file (`docs/start_here.md`), and remove
   the entire **Bootstrap only** section from `AGENTS.md`. Rewrite the root
   README and `docs/state.md` for the actual project; remove the starter prompt,
   template publishing advice, template verification history, and other
   one-time setup instructions. Remove their entries from `docs/README.md` and
   repair all references to removed files, including layout listings. Remove
   obsolete example code and its commands once replaced by the real baseline;
   retain reusable experiment/finding/decision templates where useful. Do not
   preserve a copy of the cleanup checklist in the project docs. Check links
   and run the project's checks after cleanup, then commit verified work when
   Git is available. This cleanup applies to initialized projects, not to
   maintenance of the reusable template repository.

Completion means another agent can read the question, reproduce the baseline,
locate its evidence, and identify the next decision without relying on chat
history. Blank templates are not evidence of completed research.
