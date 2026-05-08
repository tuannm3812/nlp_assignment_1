#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = gender-equality-nlp
PYTHON_VERSION = 3.11
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python dependencies
.PHONY: requirements
requirements:
	$(PYTHON_INTERPRETER) -m pip install -U pip
	$(PYTHON_INTERPRETER) -m pip install -e ".[dev]"

## Delete all compiled Python files and cache
.PHONY: clean
clean:
	$(PYTHON_INTERPRETER) -c "from pathlib import Path; import shutil; [p.unlink() for p in Path('.').rglob('*.py[co]')]; [shutil.rmtree(p, ignore_errors=True) for p in Path('.').rglob('__pycache__')]; [shutil.rmtree(p, ignore_errors=True) for p in ['build', 'dist', '.eggs', '.pytest_cache', '.ruff_cache', '.mypy_cache'] if Path(p).exists()]"

## Lint using ruff (use `make format` to do formatting)
.PHONY: lint
lint:
	ruff check .

## Format source code with ruff
.PHONY: format
format:
	ruff check --fix .
	ruff format .

## Run tests with pytest
.PHONY: test
test:
	pytest -v --cov=gender_equality_nlp

## Type check with mypy
.PHONY: typecheck
typecheck:
	mypy gender_equality_nlp --strict

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################

## Make dataset
.PHONY: data
data: requirements
	$(PYTHON_INTERPRETER) -m gender_equality_nlp.dataset

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)
