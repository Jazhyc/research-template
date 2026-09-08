# Infrastructure and compute

## Local environment

Python 3.12; dependencies pinned in `uv.lock`. Run `bash setup_dev.sh` and
`make check`. No accelerator or API access is required for `make smoke`.
If a sandbox blocks the default uv cache, set `UV_CACHE_DIR` to a writable
location. Machine-specific paths belong in local configuration.

## Project targets

None configured. For each target, record hardware, software/driver versions,
checkout and artifact paths, setup, launch/status/cancel commands, and recovery.
Probe the hardware before freezing a performance recipe. Keep credentials in
ignored local configuration or the platform's secret store.

## Budget and authorization

No paid execution authorized by this template. Record the owner's actual
instruction, date, provider/target, run scope, spending ceiling, and stop rule
before paid work. Estimate input/output tokens or accelerator hours, retries,
storage, and expected total cost; compare with actual usage afterward.

## Monitoring and retention

Record how agent checks are scheduled, startup criteria, monitoring cadence,
failure handling, and whether checks survive the session. Infrastructure
watchdogs and agent follow-ups serve different purposes.

Before releasing a target, retrieve important outputs, verify checksums, record
their durable location, and confirm the owner's termination authorization.
An ignored local result directory is not a backup.
