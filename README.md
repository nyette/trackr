# trackr

Shopify Back-End Dev Intern Challenge Fall 2022 Submission

[![Run on Repl.it](https://repl.it/badge/github/Nyette/trackr)](https://repl.it/github/Nyette/trackr)

## Prereqs

* [Python 3.8+](https://www.python.org/)
* [Poetry](https://python-poetry.org/)
* [PostgreSQL 14](https://www.postgresql.org/)

## Getting Started

* Clone this repo
* Navigate to the project directory
* Activate the virtual environment: `poetry shell`
* Install dependencies: `poetry install`
* Set environment variables in `.env`:

```
MODE=production

SECRET_KEY=(a random, hard to guess string)

DATABASE_URI=(the connection string of your database)
```

* Apply database migrations: `flask db upgrade`
* Start the server: `python wsgi.py`
