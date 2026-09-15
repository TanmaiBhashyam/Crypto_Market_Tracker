import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


load_dotenv()


def get_postgres_engine():

    database_url = URL.create(
        drivername="postgresql+psycopg",
        username=os.environ["DATABASE_USER"],
        password=os.environ["DATABASE_PASSWORD"],
        host=os.environ["DATABASE_HOST"],
        port=int(os.environ.get("DATABASE_PORT") or "5432"),
        database=os.environ["DATABASE_NAME"],
    )

    engine = create_engine(database_url)

    return engine