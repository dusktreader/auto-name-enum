.ONESHELL:
.DEFAULT_GOAL:=help
SHELL:=/bin/bash
PACKAGE_NAME:=auto_name_enum

.PHONY: install
install:
	poetry install

.PHONY: test
test: install
	poetry run pytest

.PHONY: lint
lint: install
	poetry run black --check ${PACKAGE_NAME} tests
	poetry run isort --check ${PACKAGE_NAME} tests
	poetry run pflake8 ${PACKAGE_NAME} tests

.PHONY: mypy
mypy: install
	poetry run mypy ${PACKAGE_NAME} --pretty

.PHONY: qa
qa: test lint mypy
	echo "All quality checks pass!"

.PHONY: format
format: install
	poetry run black ${PACKAGE_NAME} tests
	poetry run isort ${PACKAGE_NAME} tests

.PHONY: clean
clean:
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info
