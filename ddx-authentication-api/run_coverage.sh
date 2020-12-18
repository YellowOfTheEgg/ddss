#!/usr/bin/env bash

# Coverage report and badge for CI
if [[ ! -v CODECOV_TOKEN ]]; then
    echo "CODECOV_TOKEN is not set"
else
    codecov
fi