#!/bin/bash

# delete __pycache__ folders
find . -type d -name "__pycache__" -exec rm -r {} +

# run linters
black main.py app/**
isort main.py app/** --profile black
flake8
