# trackr

[Shopify Back-End Dev Intern Challenge Fall 2022](https://docs.google.com/document/d/1PoxpoaJymXmFB3iCMhGL6js-ibht7GO_DkCF2elCySU/edit)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![codecov](https://codecov.io/gh/Nyette/trackr/branch/main/graph/badge.svg?token=5QW54IJ6CB)](https://codecov.io/gh/Nyette/trackr)

## Prereqs

* [Python](https://www.python.org/)
* [Poetry](https://python-poetry.org/)
* [PostgreSQL](https://www.postgresql.org/)

## Getting Started

* Clone this repo
* Navigate to the project directory
* Activate the virtual environment: `poetry shell`
* Install dependencies: `poetry install`
* Install the git hook scripts: `pre-commit install`
* Set environment variables in `.env`:

```
MODE=("development" or "production")

SECRET_KEY=(a random, hard to guess string)

PROD_DATABASE_URI=(the connection string of your database)

DEV_DATABASE_URI=(the connection string of your database)
```

* Generate migration: `flask db migrate`
* Apply migrations: `flask db upgrade`
* Run tests: `pytest tests/`
* Start the server: `python wsgi.py`
