#! /usr/bin/env bash
if [[ $INTEGRATION_TESTS = "True"  ]]; then
    echo "Integration tests activated"
else
   echo "Integration tests disabled"
fi

echo "There are not tests to be executed"
