#!/bin/bash

# Format code with Black
black .

# Sort imports with isort
isort .

# Run Pylint for code quality check
pylint src tests
