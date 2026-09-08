# Optional compute integration

Add launchers only after a target is selected. Document resources, environment,
working directory, log paths, signal handling, and exact status/cancel commands
in `docs/infrastructure.md`. Pass the frozen run config to jobs. Keep account,
partition, GPU type, and scratch paths configurable; do not inherit Gleipnir's
hardware settings. No scheduler jobs or cloud resources are created by setup.
