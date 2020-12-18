#!/usr/bin/env bash

python -m pytest --cov-report term-missing --cov=app

# Coverage report and badge for CI
if [[ ! -v CODECOV_TOKEN ]]; then
    echo "CODECOV_TOKEN is not set"
else
    codecov
fi