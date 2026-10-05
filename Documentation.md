# GPA Tracker

GPA Tracker helps students keep completed courses and grades in one place and
see how they contribute to an overall GPA. It is a CS3250 project built with
Python, Flask, SQLAlchemy, and SQLite.

This guide covers the implementation and local setup. The existing [README](README.md)
contains the course requirements, schedule, team roles, and testing section.

Students create an account, sign in, and choose a course and letter grade. The
app saves each entry under their account. The intended GPA calculation weights
each grade by the course's credits.

---

## Quick start

Use Python 3.10 or later. From the repository root:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/init_db.py
PYTHONPATH=src flask --app app run
```

Open `http://127.0.0.1:5000`. The app creates a local database at startup.
Run commands from the repository root so it can find the pages and styles.
These commands start the development version. See the [test report](docs/TEST_REPORT.md)
for current failures and remaining checks.
Package setup and Docker delivery remain unfinished.

## Documentation

|Guide|Purpose|
|---|---|
|[Architecture](docs/ARCHITECTURE.md)|What each part does and how records connect|
|[Test report](docs/TEST_REPORT.md)|Verified results and remaining checks|
