import pandas as pd
from sqlalchemy import text

from db_connection import get_postgres_engine


def transform_data():
    # Connect to SQLite
    sqlite_engine = "sqlite:///db/crypto.db"

    # Read raw data
    df = pd.read_sql("SELECT * FROM coins_raw", sqlite_engine)

    print(f"Read {len(df)} rows from SQLite")

    # Keep only the columns we need
    transformed_df = df[
        [
            "id",
            "symbol",
            "name",
            "current_price",
            "market_cap",
            "total_volume",
            "price_change_percentage_24h"
        ]
    ].copy()

    # Rename columns for PostgreSQL
    transformed_df = transformed_df.rename(
        columns={
            "current_price": "price_usd",
            "market_cap": "market_cap_b",
            "total_volume": "volume_24h",
            "price_change_percentage_24h": "change_24h_pct"
        }
    )

    # Convert market cap to billions
    transformed_df["market_cap_b"] = (
        transformed_df["market_cap_b"] / 1_000_000_000
    )

    # Create trend column
    transformed_df["trend"] = transformed_df["change_24h_pct"].apply(
        lambda x: "UP" if x > 0
        else "DOWN" if x < 0
        else "FLAT"
    )

    # Add extraction timestamp
    transformed_df["extracted_at"] = pd.Timestamp.now()

    # Connect to PostgreSQL
    print("Writing transformed data to PostgreSQL...")

    postgres_engine = get_postgres_engine()

    # Create table if it doesn't exist
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS crypto_market_history (
        id TEXT,
        symbol TEXT,
        name TEXT,
        price_usd DOUBLE PRECISION,
        market_cap_b DOUBLE PRECISION,
        volume_24h DOUBLE PRECISION,
        change_24h_pct DOUBLE PRECISION,
        trend TEXT,
        extracted_at TIMESTAMP
    );
    """

    with postgres_engine.begin() as connection:
        connection.execute(text(create_table_sql))

    # Insert transformed data
    transformed_df.to_sql(
        "crypto_market_history",
        postgres_engine,
        if_exists="append",
        index=False
    )

    postgres_engine.dispose()

    print(
        f"Successfully inserted "
        f"{len(transformed_df)} rows into PostgreSQL"
    )


if __name__ == "__main__":
    transform_data()