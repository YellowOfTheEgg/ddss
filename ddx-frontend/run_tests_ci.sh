#!/usr/bin/env bash

npm run test:ci

if [ $? -eq 1 ]; then
  echo "Test failed. No need to run coverage."
  exit 1
fi

# Coverage report and badge for CI
if [[ ! -v CODECOV_TOKEN ]]; then
    echo "CODECOV_TOKEN is not set"
else
    bash <(curl -s https://codecov.io/bash)
fi