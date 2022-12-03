#!/bin/bash
black . --exclude=venv
isort . --force-single-line-imports --quiet --apply -l=250
autoflake --recursive --exclude venv --in-place --expand-star-imports --remove-all-unused-imports ./
isort . --quiet --apply