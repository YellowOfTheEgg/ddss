#!/usr/bin/env bash

#start the service
uvicorn app.main:app --reload --port 8002 --host 0.0.0.0
