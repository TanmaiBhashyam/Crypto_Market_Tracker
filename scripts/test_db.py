from db_connection import get_postgres_engine

def test_connection():

    engine = get_postgres_engine()

    with engine.connect() as connection:
        print("Successfully connected to PostgreSQL!")


if __name__ == "__main__":
    test_connection()