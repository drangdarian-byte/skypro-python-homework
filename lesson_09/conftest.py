"""Database connection and isolated transaction fixtures for lesson 9."""

import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


@pytest.fixture(scope="session")
def engine():
    password = os.getenv("SKYPRO_DB_PASSWORD")
    if not password:
        pytest.fail(
            "Set SKYPRO_DB_PASSWORD for local PostgreSQL before running tests."
        )

    url = URL.create(
        "postgresql+psycopg2",
        username="qa_user",
        password=password,
        host="localhost",
        port=5432,
        database="skypro_sql",
    )
    database_engine = create_engine(url, pool_pre_ping=True)
    try:
        yield database_engine
    finally:
        database_engine.dispose()


@pytest.fixture
def db(engine):
    """Always roll back this test's changes, even after assertion errors."""
    with engine.connect() as connection:
        transaction = connection.begin()
        try:
            yield connection
        finally:
            transaction.rollback()
