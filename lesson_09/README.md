# Lesson 09: SQLAlchemy + PostgreSQL

Three independent pytest tests for the `teacher` table of Skypro's local
`skypro_sql` PostgreSQL database: insert, update and delete.

## Requirements

- PostgreSQL running on localhost:5432
- Database `skypro_sql`, user `qa_user`
- Original Skypro SQL tables created and populated
- Python packages: `pytest`, `SQLAlchemy`, `psycopg2-binary`, `flake8`

## Local setup (PowerShell)

Install dependencies:

```powershell
python -m pip install sqlalchemy psycopg2-binary pytest flake8
```

Provide **your own** local password for the `qa_user` database account in
this terminal session. The password is never saved in source files:

```powershell
$env:SKYPRO_DB_PASSWORD = Read-Host "Пароль PostgreSQL qa_user"
```

Run the checks from the repository root:

```powershell
python -m flake8 lesson_09
python -m pytest lesson_09 -v
```

## Isolation and cleanup

Each test inserts a teacher with a newly generated ID and email, performs its
assertions, and then the `db` fixture executes `transaction.rollback()` via
SQLAlchemy, even if the test fails. This removes test changes and leaves the
original records unchanged. A rollback also safely handles the delete test,
which checks deletion inside the transaction before it is rolled back.

**No passwords, tokens or connection strings containing secrets belong in Git.**
