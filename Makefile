.DEFAULT_GOAL := help

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

setup: ## Install deps and hooks
	uv sync --all-extras && uv run pre-commit install

lint: ## Ruff + mypy
	uv run ruff check . && uv run ruff format --check . && uv run mypy src

test: ## Unit tests (no LLM calls)
	uv run pytest -m "not llm" -q

test-llm: ## Tests that hit real LLM APIs
	RUN_LLM_TESTS=1 uv run pytest -m llm -q

evals: ## Run the evaluation suite and write results to evals/results/
	uv run python -m evals.run

demo: ## Launch the demo UI
	uv run python -m project.demo

clean: ## Remove caches
	find . -name "__pycache__" -type d -exec rm -rf {} + ; rm -rf .pytest_cache .mypy_cache .ruff_cache
