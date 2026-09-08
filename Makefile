.PHONY: setup check smoke

setup:
	bash setup_dev.sh

check:
	uv run --locked ruff check .
	uv run --locked ruff format --check .
	uv run --locked pytest

smoke:
	uv run --locked python -m experiments.smoke.run --config experiments/smoke/config.json
