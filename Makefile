.ONESHELL:
.DEFAULT_GOAL:=help
SHELL:=/bin/bash
PACKAGE_NAME:=auto_name_enum

.PHONY: test
test:
	uv run pytest

.PHONY: types
types:
	uv run mypy ${PACKAGE_TARGET} tests --pretty
	uv run basedpyright ${PACKAGE_TARGET} tests

.PHONY: lint
lint:
	uv run ruff check ${PACKAGE_TARGET} tests

.PHONY: qa
qa: test lint types
	@echo "All quality checks pass!"

.PHONY: format
format:
	uv run ruff format ${PACKAGE_TARGET} tests

.PHONY: clean
clean:  ## Clean up build artifacts and other junk
	@rm -rf .venv
	@uv run pyclean . --debris
	@rm -rf dist
	@rm -rf .ruff_cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -f .coverage*
	@rm -f .junit.xml

# Recipe stolen from: https://gist.github.com/prwhite/8168133?permalink_comment_id=4160123#gistcomment-4160123
.PHONY: help
help:  ## Show help message
	@awk 'BEGIN {FS = ": .*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[$$()% 0-9a-zA-Z_-]+(\\:[$$()% 0-9a-zA-Z_-]+)*:.*?##/ { gsub(/\\:/,":", $$1); printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
