import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


load_dotenv()


def get_postgres_engine():
    required_variables = [
        "DATABASE_HOST",
        "DATABASE_PORT",
        "DATABASE_NAME",
        "DATABASE_USER",
        "DATABASE_PASSWORD",
    ]

    missing_variables = [
        variable
        for variable in required_variables
        if not os.getenv(variable)
    ]

    if missing_variables:
        raise RuntimeError(
            "Missing database environment variables: "
            + ", ".join(missing_variables)
        )

    database_url = URL.create(
        drivername="postgresql+psycopg",
        username=os.environ["DATABASE_USER"],
        password=os.environ["DATABASE_PASSWORD"],
        host=os.environ["DATABASE_HOST"],
        port=int(os.environ.get("DATABASE_PORT") or "5432"),
        database=os.environ["DATABASE_NAME"],
    )

    engine = create_engine(
        database_url,
        pool_pre_ping=True,
    )

    return engine