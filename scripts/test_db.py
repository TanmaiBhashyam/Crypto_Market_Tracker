from db_connection import get_postgres_engine


def test_connection():
    print("Testing PostgreSQL connection...")

    engine = get_postgres_engine()

    try:
        with engine.connect() as connection:
            result = connection.exec_driver_sql("SELECT 1")
            print("PostgreSQL connection successful!")
            print("Database response:", result.scalar())

    finally:
        engine.dispose()


if __name__ == "__main__":
    test_connection()