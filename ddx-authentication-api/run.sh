#!/usr/bin/env bash

# start the service
gunicorn app.main:app --reload -b 0.0.0.0:8001 --log-level info -k uvicorn.workers.UvicornWorker
