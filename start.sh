#!/bin/bash

# This script ensures the correct python environment is used to run the app.
# It uses the absolute path to the python interpreter installed in our Docker image.

/usr/local/bin/python -m uvicorn main:app --host 0.0.0.0 --port 8000