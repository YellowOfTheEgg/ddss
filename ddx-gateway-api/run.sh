#!/usr/bin/env bash

# start the service
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
