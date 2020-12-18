#! /usr/bin/env bash
if [[ $INTEGRATION_TESTS = "True"  ]]; then
    echo "Integration tests activated"
    python init_tests.py
else
   echo "Integration tests disabled"
fi

python -m pytest --cov-report term-missing --cov=app
