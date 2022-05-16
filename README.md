# trackr

[Shopify Back-End Dev Intern Challenge Fall 2022](https://docs.google.com/document/d/1PoxpoaJymXmFB3iCMhGL6js-ibht7GO_DkCF2elCySU/edit?usp=sharing) Submission

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
FLASK_APP=trackr
FLASK_ENV=development
```

* Set configuration values in `instance/config.py`. Note that the `instance` directory should be a subdirectory of the repo:

```python
SECRET_KEY = "dev"

SQLALCHEMY_DATABASE_URI = "postgresql://microblog_7uo9_user:KPReAqyNWodBLoYCPv1mP8XnnJXsnoIf@dpg-c9qsfcehb05tgup8bf4g-a.ohio-postgres.render.com/microblog_7uo9"
```

* Apply database migrations: `flask db upgrade`
* Start the development server: `flask run --host=0.0.0.0`
